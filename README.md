## app.py
#
app = Flask(__name__) → starts app.

app.secret_key → secures session data.

Three lists: easy_questions, medium_questions, hard_questions.

Connects difficulty → (questions, points).

/ → Start page: save player name, level, score, lifelines in session.  /quiz → Shows current question:

If hint → show clue,
If skip → next question,
If 50:50 → keep 1 correct + 1 wrong,
If answer → check within 15 sec, give points, go to next question.

/result → Show final score, calculate rank, save score in file.

/leaderboard → Read file, show top 5 scores.

app.run(debug=True) → starts the server.
```python

from flask import Flask, render_template, request, redirect, url_for, session
import random, os, time

app = Flask(__name__)
app.secret_key = "supersecretkey"

easy_questions = [
    {"question": "Which of these is a programmer’s real best friend?",
     "options": ["A) Keyboard", "B) Mouse", "C) Internet", "D) Undo (Ctrl+Z)"],
     "answer": "C", "hint": "You Google everything here"
     },
     {
        "question": "If your code runs without errors on the first try, what should you do?",
        "options": ["A) Celebrate immediately ", "B) can't believe for a while", "C) Call it a miracle ", "D) Quit coding, it will never happen again "],
        "answer": "B",
        "hint": "It feels too good to be true…"
    },
    {
        "question": "What’s the fastest WiFi in the office?",
        "options": [ "A) The one next to the boss’ room", "B) The one you’re not connected to", "C) Hotspot from someone’s phone",
        "D) Imaginary free WiFi"],
        "answer": "B",
       "hint": "Other WiFi always feels faster."
    }

]

medium_questions = [
    {"question": "What happens if you say 'Just one last bug fix'?",
     "options": ["A) It really ends", "B) 5 new bugs appear", "C) Code crashes completely", "D) You never sleep again"],
     "answer": "B", "hint": "Bugs multiply like rabbits"
     },
    {
        "question": "What is the secret weapon of every programmer?",
        "options": ["A) Strong logic", "B) Stack Overflow", "C) Coffee ", "D) Ctrl + C, Ctrl + V"],
        "answer": "D",
        "hint": "Copy… paste… success!"
    },
    {
    "question": "What is a programmer’s favorite place to relax?",
    "options": ["A) The cloud","B) The stack",  "C) GitHub beach","D) Sleep mode"],
    "answer": "D",
    "hint": "Even CPUs need some Zzz."
    }
]

hard_questions = [
    {"question": "What is the fastest disappearing thing in the world?",
     "options": ["A) Ice cube in summer", "B) Your salary", "C) Soap bubble", "D) Free pizza at a party"],
     "answer": "B", "hint": "You wait for payday but…"
    },
    {
        "question": "If your code doesn’t work at 2 AM, what should you do?",
        "options": ["A) Sleep and try tomorrow ", "B) Keep fixing until sunrise", "C) Blame WiFi", "D) Order pizza and continue"],
        "answer": "A",
        "hint": "Brain needs rest, not more bugs!"
    },
    {
    "question": "Why do programmers hate nature?",
    "options": ["A) Too many bugs","B) No WiFi","C) Trees don’t have USB ports","D) Sun causes glare on screens"],
    "answer": "A",
    "hint": "Nature = bugs, bugs = overtime."
    }
]

levels = {
    "easy": (easy_questions, 1),
    "medium": (medium_questions, 2),
    "hard": (hard_questions, 3)
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        level = request.form["level"]

        questions, points = levels[level]
        random.shuffle(questions)

        session["player"] = name
        session["level"] = level
        session["score"] = 0
        session["q_index"] = 0
        session["points"] = points
        session["questions"] = questions
        session["lifelines"] = {"hint": True, "skip": True, "fifty": True}
        session["start_time"] = time.time()

        return redirect(url_for("quiz"))

    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "player" not in session:
        return redirect(url_for("index"))

    q_index = session["q_index"]
    questions = session["questions"]

    if q_index >= len(questions):
        return redirect(url_for("result"))

    question = questions[q_index]
    lifelines = session["lifelines"]

    if request.method == "POST":
        action = request.form.get("action")

        if action == "hint" and lifelines["hint"]:
            lifelines["hint"] = False
            session["hint"] = question["hint"]
        elif action == "skip" and lifelines["skip"]:
            lifelines["skip"] = False
            session["q_index"] += 1
            return redirect(url_for("quiz"))
        elif action == "fifty" and lifelines["fifty"]:
            lifelines["fifty"] = False
            correct = question["answer"]
            wrongs = [opt[0] for opt in question["options"] if opt[0] != correct]
            keep = random.choice(wrongs)
            session["fifty_options"] = [opt for opt in question["options"] if opt[0] in (correct, keep)]
        elif action.startswith("answer"):
            answer = action.split(":")[1]
            elapsed = time.time() - session["start_time"]
            if elapsed <= 15:  
                if answer == question["answer"]:
                    session["score"] += session["points"]

            session["start_time"] = time.time()
            session["q_index"] += 1
            session.pop("hint", None)
            session.pop("fifty_options", None)
            return redirect(url_for("quiz"))

    return render_template("quiz.html",
                           question=question,
                           q_index=q_index + 1,
                           total=len(questions),
                           lifelines=lifelines,
                           hint=session.get("hint"),
                           fifty=session.get("fifty_options"),
                           name=session["player"])


@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(session.get("questions", [])) * session.get("points", 1)

    percent = (score / total) * 100 if total else 0
    if percent < 30:
        rank = "Sleepy Coder"
    elif percent < 60:
        rank = "Debugging Intern"
    elif percent < 90:
        rank = "Code Ninja"
    else:
        rank = "Master of Bugs"

    filename = "leaderboard.txt"
    with open(filename, "a") as f:
        f.write(f"{session['player']} - {score}\n")

    return render_template("result.html", name=session["player"],
                           score=score, total=total, rank=rank)


@app.route("/leaderboard")
def leaderboard():
    scores = []
    filename = "leaderboard.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                try:
                    nm, scr = line.strip().split(" - ")
                    scores.append((nm, int(scr)))
                except:
                    pass
    scores.sort(key=lambda x: x[1], reverse=True)
    return render_template("leaderboard.html", scores=scores[:5])


if __name__ == "__main__":
    app.run(debug=True)
```

## index.html
#
Player enters their name , 
Player selects level (easy, medium, hard) ,
Then presses Start Quiz 🚀 → sends data to Flask (app.py).

Uses Bootstrap 5 (for design & responsiveness) ,
Adds custom CSS for colors, background, and buttons.

Centered card (div.card) with rounded corners & shadow.

Card Content -
Title: 🎮 Quiz Game.
Form (method = POST → data sent to Flask):

Input box → "Enter your name",
Dropdown → "Choose difficulty level",
Button → "Start Quiz 🚀".


```html
 <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz Game - Start</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #1c3934 0%, #828698 100%);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: 'Segoe UI', sans-serif;
    }
    .card {
      border-radius: 20px;
      box-shadow: 0px 10px 25px rgba(247, 245, 245, 0.2);
    }
    .btn-custom {
      background: #5c5663;
      background: linear-gradient(135deg, #564766 0%, #5b384c 100%);
      color: white;
      border: none;
      border-radius: 12px;
      padding: 10px 20px;
    }
    .btn-custom:hover {
      opacity: 0.9;
    }
  </style>
</head>
<body>
  <div class="card p-5 text-center" style="width: 400px;">
    <h1 class="mb-4">🎮 Quiz Game</h1>
    <form method="post">
      <div class="mb-3">
        <input type="text" name="name" class="form-control" placeholder="Enter your name" required>
      </div>
      <div class="mb-3">
        <select name="level" class="form-select">
          <option value="easy">Easy</option>
          <option value="medium">Medium</option>
          <option value="hard">Hard</option>
        </select>
      </div>
      <button type="submit" class="btn-custom w-100">Start Quiz 🚀</button>
    </form>
  </div>
</body>
</html>
```
## learderboard.html
#
Score List-
Uses Jinja2 loop ({% for name, score in scores %}) to display player name + score.

loop.index → automatically shows ranking (1, 2, 3 …).

If no scores → shows “No scores yet”.

Button-
A Bootstrap button → "Play Again" → links to index route.

After finishing quiz, Flask writes score in leaderboard.txt , 
When you visit /leaderboard, Flask reads scores → passes to this page ,
Page displays top 5 in a neat list.
```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Leaderboard</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-5 bg-light">
  <div class="container">
    <h1>🏆 Leaderboard (Top 5)</h1>
    <ul class="list-group">
      {% for name, score in scores %}
        <li class="list-group-item d-flex justify-content-between">
          <span>{{ loop.index }}. {{ name }}</span>
          <span>{{ score }}</span>
        </li>
      {% else %}
        <li class="list-group-item">No scores yet</li>
      {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}" class="btn btn-primary mt-3">Play Again</a>
  </div>
</body>
</html>
```
## quiz.html
#
Adds JavaScript countdown:
Starts from 15 sec.
Updates timer every second.
If time runs out → auto-submits form (moves to next).

Shows:
Q{{ q_index }} / {{ total }} → current question number out of total .
Question text → {{ question["question"] }} . 
Timer (⏳ 15 sec).

Buttons for:
Hint (shows clue).
Skip (move to next).
50:50 (reduce options).
Buttons disappear once used.
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script>
    // Simple timer (15 sec)
    let timeLeft = 15;
    function countdown() {
      if (timeLeft <= 0) {
        document.getElementById("timer").innerHTML = " Time's up!";
        document.getElementById("quizForm").submit();
      } else {
        document.getElementById("timer").innerHTML = "⏳ " + timeLeft + " sec left";
      }
      timeLeft -= 1;
      setTimeout(countdown, 1000);
    }
    window.onload = countdown;
  </script>
</head>
<body style="background-color: rgb(223, 225, 229);">
  <div class="container">
    <h2>Q{{ q_index }} / {{ total }}</h2>
    <p>{{ question["question"] }}</p>
    <div id="timer" class="text-danger fw-bold"></div>

    <form method="post" id="quizForm">
      {% if fifty %}
        {% for opt in fifty %}
          <button name="action" value="answer:{{ opt[0] }}" class="btn btn-basic w-100 my-2">{{ opt }}</button>
        {% endfor %}
      {% else %}
        {% for opt in question["options"] %}
          <button name="action" value="answer:{{ opt[0] }}" class="btn btn-light w-100 my-2">{{ opt }}</button>
        {% endfor %}
      {% endif %}

      <hr>
      <p><strong>Lifelines:</strong></p>
      {% if lifelines["hint"] %}<button name="action" value="hint" class="btn btn-warning">Hint</button>{% endif %}
      {% if lifelines["skip"] %}<button name="action" value="skip" class="btn btn-info">Skip</button>{% endif %}
      {% if lifelines["fifty"] %}<button name="action" value="fifty" class="btn btn-dark">50:50</button>{% endif %}
    </form>

    {% if hint %}
      <div class="alert alert-secondary mt-3">💡 Hint: {{ hint }}</div>
    {% endif %}
  </div>
</body>
</html>
```
## result.html
#
After finishing all questions, Flask sends data (name, score, rank) to this page.
Page shows results clearly.
Player can click Play Again → restart the quiz.

Player details:
Name → {{ name }}.

Score → {{ score }}/{{ total }}.

Rank → {{ rank }} (calculated in app.py).
```html
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz Result</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #1c3934 0%, #828698 100%);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: 'Segoe UI', sans-serif;
    }
    .result-card {
      background: white;
      border-radius: 20px;
      padding: 40px;
      text-align: center;
      box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
    }
    .btn-play {
      background: #11998e;
      background: linear-gradient(135deg, #564766 0%, #5b384c 100%);
      color: white;
      border: none;
      border-radius: 12px;
      padding: 12px 24px;
      margin-top: 20px;
    }
    .btn-play:hover {
      opacity: 0.9;
    }
  </style>
</head>
<body>
  <div class="result-card">
    <h1>🎉 Quiz Over! 🎉</h1>
    <h3>{{ name }}, your score: <b>{{ score }}/{{ total }}</b></h3>
    <p class="mt-3">Your Rank: <strong>{{ rank }}</strong></p>
    <a href="{{ url_for('index') }}" class="btn-play">Play Again</a>
  </div>
</body>
</html>
```



