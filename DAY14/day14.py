# level 2
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 
'Norway', 'Iceland'] 
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1 3
# uppercased=list(map(str.upper,countries))
# print(uppercased)

# 2
# squared=list(map(lambda x: x**2,numbers))
# print(squared)

# 4
# land_countries=list(filter(lambda country : 'land' in country.lower(),countries))
# print(land_countries)

# 5
# six_char=list(filter(lambda country:len(country)==6,countries))
# print(six_char)

# 6
# six_char=list(filter(lambda country:len(country)>=6,countries))
# print(six_char)

# 7
# e_countries = list(filter(lambda country: country.startswith('E'),countries))
# print(e_countries)

# 8
# from functools import reduce
# result=reduce(
#     lambda a,b:a+b,
#     filter(lambda x:x%2==0,
#            map(lambda x: x**2,numbers))
# )
# print (result)

# 9
# def get_string_list(lst):
#     return list(filter(lambda x: isinstance(x,str),lst))
# mixed_list=[1,2,'hello','python']
# print(get_string_list(mixed_list))

# 10
# from functools import reduce
# total=reduce(lambda a,b : a+b,numbers)
# print(total)

# 11
# from functools import reduce
# sentence=reduce(lambda a,b: a+","+b,
#                 countries[:-1])
# print(sentence)

# 12
# def categories(pattern):
#     return list(filter(lambda country: pattern.lower()in country.lower(),countries))
# print(categories("la"))

# 13
# def country_start(countries):
#     result={}
#     for country in countries:
#         first_letter = country[0].upper()
#         result[first_letter]=result.get(first_letter,0)+1
#     return result
    
# print(country_start(countries))

# 14
# def get_first_ten(countries):
#     return countries[:10]
# print(get_first_ten(countries))

# 15
# def get_last_ten_countries(countries):
#     return countries[-10:]
# print(get_last_ten_countries(countries))

# level 3
# 1

