# level 1

# 1
# age=int(input("enter your age :"))
# if age>18:
#     print("you are old enough to drive")
# else:
#     print("wait until you are 18")

# 2
# myage=int(input("enter my age :"))
# yourage=int(input("enter your age :"))
# diff=myage-yourage
# diff1=yourage-myage
# if myage>yourage:
#     print("i am ",diff , "years older than you")
# else:
#    print("you are" ,diff1, "older than me")

# 3
# a=int(input("enter num a:"))
# b=int(input("enter num b:"))
# if a>b:
#     print(("a is greater than b"))
# else:
#     print("b is greater than a")

# level 2

# 1
# score=int(input("enter score :"))
# if score >=90:
#     print('A')
# elif 89 >=score>=70:
#     print('B')
# elif 69>=score>=60:
#     print('C')
# elif 59>=score>=50:
#     print('D')
# else:
#     print('F')

# 2
# month = input("Enter the month: ")
# if month in ("September", "October", "November"):
#     print("autumn")
# elif month in ("December", "January", "February"):
#     print("winter")
# elif month in ("March", "April", "May"):
#     print("spring")
# elif month in ("June", "July", "August"):
#     print("summer")
# else:
#     season = "Invalid month"

# 3
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input("Enter a fruit: ")

# if fruit in fruits:
#     print("That fruit already exists in the list")
# else:
#     fruits.append(fruit)
#     print("Updated list:", fruits)

# level 3

# 1
person={
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finaland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

if 'skills' in person:
    skills=person['skills']
    mid_skill=skills[len(skills)//2]
    print(mid_skill)

    if 'skills' in person:
        print("python is there ?",'Python' in person['skills'])

        if(person['skills']=={'Javascript','React'}):
            print("front end developer")
        else:
            print("backend developer")
                








