# level 1

# 1
# list=[""]
# print(list)

# 2
# list=["bhumi","modi","phone","abc","charger","oh"]
# print(list)

# 3
# list=["bhumi","modi","phone","abc","charger","oh"]
# print(len(list))

# 4
# lt=["bhumi","modi","phone","abc","charger","oh"]
# print(lt[0])
# print(len(lt)//2)
# print(lt[-1])

# 5
# mixed_data_type=["bhumi",19,5.5,"single","dumas"]
# print(mixed_data_type)

# 6
# it_company=["facebook","google","microsoft","apple","IBM"]
# print(it_company)

# 7 8 9
# it_company=["facebook","google","microsoft","apple","IBM"]
# print(it_company)
# print(len(it_company))
# print(it_company[0])
# print(len(it_company)//2)

# 10
# it_company=["facebook","google","microsoft","apple","IBM"]
# it_company[2]="ios"
# print(it_company)

# 11 12 13 
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "Amazon"]
# it_companies.append("IT")
# print("After adding a company:", it_companies)
# it_companies.insert(3,"IT")
# print("after inserting :",it_companies)
# it_companies["Apple"].upper()
# print(it_companies)

# 14
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "Amazon"]
# joined = '#;  '.join(it_companies)
# print(joined)

# 15
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "Amazon"]
# does_exist='Apple' in it_companies
# print(does_exist)

# 16 17
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "Amazon"]
# it_companies.sort()
# print(it_companies)
# it_companies.sort(reverse=True)
# print(it_companies)

# 18
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "Amazon"]
# print(it_companies[:3])

# 19
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "Amazon"]
# print(it_companies[-3:])

# 20 21 22 23

# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# middle_one = it_companies[len(it_companies)//2 : len(it_companies)//2 + 1]
# middle_two = it_companies[len(it_companies)//2 - 1 : len(it_companies)//2 + 1] 
# print("Middle:", middle_one)  #

# it_companies.pop(0)
# print("After removing first:", it_companies)

# del it_companies[len(it_companies)//2 : len(it_companies)//2 + 1]  
# print("After removing middle:", it_companies)

# it_companies.pop(-1)
# print("After removing last:", it_companies)


# 24 25 26 27

# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# it_companies.clear()
# print("After removing all companies:", it_companies)

# del it_companies

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node', 'Express', 'MongoDB']
# joined_list = front_end + back_end
# print("Joined list:", joined_list)

# full_stack = joined_list[:]  
# full_stack.append("python")
# print( full_stack)


# level 2
# ages=[19,22,19,24,20,25,26,24,25,24]
# 1
# ages.sort()
# print(ages)

# print(min(ages))
# print(max(ages))

# min=min(ages)
# max=max(ages)
# ages +=[min , max]
# print(ages)

# ages.sort()
# mid=len(ages)//2
# median=(ages[mid] + ages[~mid]) / 2
# print(median)

# avg = sum(ages)/len(ages)
# print(avg)

# ranges=max-min
# print(ranges)

# compare_min = abs(min- avg)
# compare_max = abs(max- avg)
# print("abs(min - average):", compare_min)
# print("abs(max - average):", compare_max)

# 1 2 3

# countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# mid = len(countries) // 2
# middle_countries = countries[mid:mid+1]
# print("Middle country(ies):", middle_countries)

# first_half = countries[:(len(countries)+1)//2]
# second_half = countries[(len(countries)+1)//2:]
# print("First half:", first_half)
# print("Second half:", second_half)

# first, second, third, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# print("First country:", first)
# print("Second country:", second)
# print("Third country:", third)
# print("Scandic countries:", scandic)






