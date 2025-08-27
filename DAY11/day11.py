# level 1

# 1
# def add_two_numbers(num1 , num2):
#     total=num1 + num2
#     print("sum of two no is",total)
#     return total
# add_two_numbers(2,7)

# 2
# def area_of_circle(r):
#     pi=3.14
#     area= pi * r**2
#     print("area of circle is ",area)
# area_of_circle(7.6)

# 3
# def add_all_nums(*args):
#     total = 0              
#     for i in args:         
#         total += i        
#     return total            
# print(add_all_nums(3, 7, 5, 6))   

# 4
# def convert_cel_fah(c ):
#     conv=(c * 9/5)+32
#     print("conversion from c ",c," to f is ",conv)
# convert_cel_fah(5)

# 5
# def check_season(month):
#     month = month.lower()

#     if month in ["september", "october", "november"]:
#         print("its autumn")
#     elif month in ["december", "january", "february"]:
#         return "Winter"
#     elif month in ["march", "april", "may"]:
#         return "Spring"
#     elif month in ["june", "july", "august"]:
#         return "Summer"
#     else:
#         print("none")

# print(check_season("May"))

# 6
# def func_slope(x1,y1,x2,y2):
#     if x2==x1:
#         return "sloe is undefined"
#     slope = (y1-y2)/(x1-x2)
#     print("the slope is ",slope)

# func_slope(3,5,1,51)

# 7
# def quadratice_eq(a ,x ,b,c):
#     quadratic=(a*x**2) + (b*x) + c
#     print("quadratic equation is :" , quadratic)
# quadratice_eq(2,4,5,8)

# 8
# def print_list(my_list):
#     for item in my_list:
#         print("the list is :",item)
# fruits=["apple","grapes","mango"]
# print_list(fruits)

# 9
# def reversed_list(arr):
#     reversed_arr=[]
#     for i in range(len(arr)-1,-1,-1):
#         reversed_arr.append(arr[i])
#         print(reversed_arr)
# num=[3,7,2,5]
# print(reversed_list(num))

# 10
# def capitalize_list_item(my_list):
#     capitalized_list=[]
#     for i in my_list:
#         capitalized_list.append(i.capitalize())
#     return capitalized_list
# fruits=["kiwi","apple"]
# print(capitalize_list_item(fruits))

# 11
# def add_item(my_list , item):
#      my_list.append(item)
#      print(my_list)

# food_staff=['potato','tomato','milk']
# print(add_item(food_staff,'meat'))

# 12
# def remove_item(my_list,item):
#     my_list.remove(item)
#     print(my_list)

# foodstaff=['apple','milk','meat']
# print(remove_item(foodstaff,'meat'))

# 13
# def sum_of_numbers(num):
#     sum =0
#     for i in range(1,num+1):
#         sum +=i
#     print("sum is :" ,sum)
# sum_of_numbers(4)

# 14 15
# def sum_of_odd_even(num):
#     even=0
#     odd=0
#     for i in range(1,num+1):
#         if i%2==0:
#          even+=i
#         else:
#           odd+=i
#     print("even sum is ",even)
#     print('odd sum is ',odd)
# sum_of_odd_even(5)

# level 2

# 1
# def evens_and_odds(n):
#     evens = 0
#     odds = 0
#     for i in range(n + 1):  
#         if i % 2 == 0:
#             evens += 1
#         else:
#             odds += 1
#     print("The number of odds are", odds)
#     print("The number of evens are", evens)

# evens_and_odds(10)

# 1
# def factorial(n):
#     ans = 1
#     for  i in range(1 , n +1):
#      ans*=i
#      print("factorial is ",ans)
# factorial(6)

# 2
# def is_empty(num):
#     if not num:
#         return True
#     else:
#         return False
    
# print(is_empty([]))
    
# 3
# def calculate_mean(data):
#     return sum(data) / len(data)

# def calculate_median(data):
#     sorted_data = sorted(data)
#     n = len(sorted_data)
#     mid = n // 2
#     if n % 2 == 0:
#         return (sorted_data[mid - 1] + sorted_data[mid]) / 2
#     else:
#         return sorted_data[mid]
    
# from collections import Counter
# def calculate_mode(data):
#     counts = Counter(data)
#     max_count = max(counts.values())
#     modes = []
    
#     for k, v in counts.items():
#         if v == max_count:
#             modes.append(k)
    
#     if len(modes) == 1:
#         return modes[0]   
#     else:
#         return modes  
 
# import math
# def calculate_std(data):
#     return math.sqrt(calculate_variance(data))

# def calculate_variance(data):
#     mean = calculate_mean(data)
#     return sum((x - mean) ** 2 for x in data) / len(data)

# def calculate_range(data):
#     return max(data) - min(data)

# num=[4,7,6,2,4]
# print("mode :" ,calculate_mode(num))
# print("range :" ,calculate_range(num))
# print("varaince :" , calculate_variance(num))
# print("mean :" , calculate_mean(num))

# level 3

# 1
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):   
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(7))   
# print(is_prime(10))  

# 2
# def all_unique(lst):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] == lst[j]:
#                 return False
#     return True
# print(all_unique([1, 2, 2, 3]))  

# 3
# def same_data(list):
#     first_type=type(list[0])
#     for i in list:
#         if type(i)!=first_type:
#             print("not same type")
#         else:
#             print("same type ")

# print(same_data([3,6,1]))
# print(same_data(["thw","gdg",4]))

# 4
# def is_valid_variable(var):
#     if len(var) == 0:
#         print("not a python variable")    
#     if var[0].isdigit():
#         print("not a python variable")
#     for ch in var:
#         if not (ch.isalnum() or ch == "_"):
#             print("not python variable")
#         else:
#             print("yahh its python variable")
# print(is_valid_variable("9mnhj"))

# 5
def most_spoken_languages(countries, top_n=10):
    lang_count = {}

    for country in countries:
        for lang in country["languages"]:
            if lang in lang_count:
                lang_count[lang] += 1
            else:
                lang_count[lang] = 1

    langs_list = []
    for lang in lang_count:
        langs_list.append([lang, lang_count[lang]])

    for i in range(len(langs_list)):
        for j in range(i + 1, len(langs_list)):
            if langs_list[j][1] > langs_list[i][1]:
                langs_list[i], langs_list[j] = langs_list[j], langs_list[i]

    return langs_list[:top_n]







  




    

