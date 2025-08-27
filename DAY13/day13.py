# 1
# number=[-6,-7,-5,-4,0,1,2,3,4]
# negative_zero_no=[i for i in number if i<=0]
# print(negative_zero_no)

# 2
# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# flattend_list=[i for row in list_of_lists for i in row]
# print(flattend_list)

# 3
# lst=[(x,1,x**1,x**2,x**3,x**4)for x in range(11)]
# for itm in lst:
#  print(itm)

# 4
# countries = [[('Finland', 'Helsinki')], 
#              [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output=[]

# for item in countries:
#     country, capital =item[0]
#     output.append([country.upper(),        
#                    country[:3].upper(),    
#                    capital.upper()])      
# print(output)

# 5
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')],
#               [('Norway', 'Oslo')]]
# result = [{'country': country.upper(), 'city': city.upper()} 
#           for [(country, city)] in countries]
# print(result)

# 6
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], 
#          [('Donald', 'Trump')], [('Bill', 'Gates')]]

# result = [first + " " + last for [(first, last)] in names]

# print(result)

# 7
# slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
# intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1
# print("Slope:", slope(2, 4, 6, 8))
# print("Intercept:", intercept(2, 4, 6, 8))

