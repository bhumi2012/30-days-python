# 1
# import requests
# import re
# from collections import Counter

# romeo_juliet='http://www.gutenberg.org/files/1112/1112.txt'
# response = requests.get(romeo_juliet)
# text=response.text.lower()
# words=re.findall(r'\w',text)

# counter=Counter(words)
# top10=counter.most_common(10)
# print("Top 10 most frequent words in Romeo & Juliet:")
# print(top10)

# 2
# import statistics as stats
# import requests
# cats_api = 'https://api.thecatapi.com/v1/breeds'
# response = requests.get(cats_api).json()
# weights = []
# lifespans = []
# countries = []

# for cat in response:
#     w = cat["weight"]["metric"].split(" - ")
#     weights.append((float(w[0]) + float(w[1])) / 2)  # average
#     ls = cat["life_span"].split(" - ")
#     lifespans.append((float(ls[0]) + float(ls[1])) / 2)
#     countries.append(cat.get("origin", "Unknown"))

# print("Cats' Weight (kg):")
# print("Min:", min(weights))
# print("Max:", max(weights))
# print("Mean:", stats.mean(weights))
# print("Median:", stats.median(weights))
# print("Std Dev:", stats.stdev(weights))
# print("\nCats' Lifespan (years):")
# print("Min:", min(lifespans))
# print("Max:", max(lifespans))
# print("Mean:", stats.mean(lifespans))
# print("Median:", stats.median(lifespans))
# print("Std Dev:", stats.stdev(lifespans))

# # Frequency
# from collections import Counter
# country_counts = Counter(countries)
# print("\nCat Breeds by Country:")
# print(country_counts.most_common(10))

# 3
# countries_api = 'https://restcountries.com/v3.1/all'
# response = requests.get(countries_api).json()

# largest_countries = sorted(response, key=lambda x: x.get("area", 0), reverse=True)[:10]
# print("\n10 Largest Countries (by area):")
# for c in largest_countries:
#     print(c["name"]["common"], c["area"])

# languages = []
# for country in response:
#     langs = country.get("languages", {})
#     languages.extend(list(langs.values()))

# lang_counts = Counter(languages).most_common(10)
# print("\n10 Most Spoken Languages:")
# print(lang_counts)

# total_languages = len(set(languages))
# print("\nTotal number of languages:", total_languages)

# 4
# import requests
# from bs4 import BeautifulSoup

# uci_url = "https://archive.ics.uci.edu/ml/datasets.php"
# response = requests.get(uci_url)

# soup = BeautifulSoup(response.text, "html.parser")

# datasets = [a.text for a in soup.find_all('a') if "datasets" in str(a.get('href'))]

# print("Some datasets from UCI Repository:")
# print(datasets[:20])   
