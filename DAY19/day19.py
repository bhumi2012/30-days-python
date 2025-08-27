# level 1

# 1
# def count_lines_words(filename):
#     with open(filename ,"r",encoding="utf-8") as f:
#         text=f.read()
#     num_lines=len(text.splitlines())
#     num_words=len(text.split())
#     return num_lines,num_words
# print("obama speech :",count_lines_words("./obama_speech.txt"))
# print("Michelle Obama speech:", count_lines_words("./michelle_obama_speech.txt"))
# print("Donald Trump speech:", count_lines_words("./donal_speech.txt"))
# print("Melina Trump speech:", count_lines_words("./melina_trump_speech.txt"))

# 2
# import json
# from collections import Counter

# def most_spokn_lang(filename, top_n):
#     with open(filename, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     languages = []
#     for country in data:
#         languages.extend(country.get("languages", []))


#     lang_counter = Counter(languages)

    
#     most_comm = [(count, lang) for lang, count in lang_counter.most_common(top_n)]
#     return most_comm
# print(most_spokn_lang(filename="./countries_data.json", top_n=10))

# 3
# import json
# def most_populated_countries(filename,top_n):
#     with open(filename,"r",encoding="utf-8")as f:
#         data=json.load(f)

#         sorted_countries = sorted(data, key=lambda x: x.get("population", 0), reverse=True)

#         result = [{"country": c["name"], "population": c["population"]} for c in sorted_countries[:top_n]]
#     return result
# print(most_populated_countries(filename="./countries_data.json", top_n=10))

# level 2
# 4
# import re
# def incoming_email(filename):
#     with open(filename,"r",encoding="utf-8")as f:
#         text=f.read()
#         emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
#         return emails
    
# emails=incoming_email("./email_exchnge.txt")
# print("total email found :",emails)
# print(emails[:10])

# 5
# import re
# from collections import Counter

# def find_most_common_words(filename, top_n):
#     with open(filename, "r", encoding="utf-8") as f:
#         text = f.read().lower()
#     words = re.findall(r"\w+", text)
#     counter = Counter(words)
#     most_common = [(count, word) for word, count in counter.most_common(top_n)]
#     return most_common
# print(find_most_common_words("sample.txt", 10))
# print(find_most_common_words("sample.txt", 5))


