import pandas as pd
import numpy as np

# nums=[1,2,3,4,5]
# s=pd.Series(nums)
# print(s)

# nums = [1, 2, 3, 4, 5] 
# s = pd.Series(nums, index=[1, 2, 3, 4, 5]) 
# print(s) 

# dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'} 
# s = pd.Series(dct) 
# print(s)

# data = [ 
#     ['Asabeneh', 'Finland', 'Helsink'],  
#     ['David', 'UK', 'London'], 
#     ['John', 'Sweden', 'Stockholm'] 
# ] 
# df = pd.DataFrame(data, columns=['Names','Country','City']) 
# print(df)

# data = [ 
# {"Name": "Asabeneh", 
# "Country":"Finland","City":"Helsinki"}, 
# {"Name": "David", "Country":"UK","City":"London"}, 
# {"Name": "John", "Country":"Sweden","City":"Stockholm"}] 
# df = pd.DataFrame(data) 
# print(df)

# 1

df = pd.read_csv("hacker_news.csv")

# 2
# print("First 5 rows:")
# print(df.head())

# 3
# print("\nLast 5 rows:")
# print(df.tail())

# 4
# print("\nTitle column:")
# print(df['title'])

# 5
# print("Rows and Columns:", df.shape)

# python_titles = df[df['title'].str.contains("python")]
# print("\nTitles containing 'Python':")
# print(python_titles['title'])

# js_titles = df[df['title'].str.contains("javascript")]
# print("\nTitles containing 'js':")
# print(js_titles['title'])