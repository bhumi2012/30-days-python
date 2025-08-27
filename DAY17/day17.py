# 1
# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 
#          'Estonia','Russia']
# *nordic_countries, es , ru = names
# print("nordic countries :",nordic_countries)
# print("estonia :",es)
# print("russia :",ru)


# eg
# try:
#     name=input('enter name :')
#     print(f'you are {name}')
# except TypeError:
#     print("type error occured")
# except ValueError:
#     print('value error occured')

# unpacking list
# def sum_of_five(a,b,c,d,e):
#     return a+b+c+d+e
# lst=[2,4,3,1,6]
# print(sum_of_five(*lst))

# unpacking dictionary
# def unpacking_dict(name ,country ,city,age):
#      return f'{name} lives in {country}, {city} , she is {age}'
# dct={"name":"bhumi","country":"india","city":"surat","age":20}
# print(unpacking_dict(**dct))

# packing list
# def sum_all(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s
# print(sum_all(1,5,4))

# packing dictionary
# def packing_info(**kwargs):
#     for keys in kwargs:
#         print(f"{keys}={kwargs[keys]}")
#     return kwargs
# print(packing_info(name="Asabeneh", 
#       country="Finland", city="Helsinki", age=250))