# level 1

# 1
# import random
# import string
# def random_userid():
#   return ''.join(random.choices(string.ascii_letters + string.digits ,k=6))
# print(random_userid())

# 2
# import random
# import string
# def user_id_gen_by_user(a,b):
#      return ''.join(random.choices(string.ascii_letters + string.digits ,k=6))
# a=input("enter a :")
# b=input("enter b :")

# print(user_id_gen_by_user(a,b))

# 3
# import random

# def rgb_color_gen():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return f"rgb({r},{g},{b})"

# print(rgb_color_gen())

# level 2

# 1
# import random
# def list_of_hexa_color(n):
#     colors =[]
#     for _ in range(n):
#             color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
#             colors.append(color)
#     return colors

# print(list_of_hexa_color(5))

# 2
# import random
# def list_of_rgb_colors(n):
#     colors=[]
#     for _ in range(n):
#         r=random.randint(0,255)
#         g=random.randint(0,255)
#         b=random.randint(0,255)
#         colors.append(f"rgb({r},{g},{b})")
#     return colors

# print(list_of_rgb_colors(3))

# 3
# import random
# def generate_colors(color_type, n):
#     colors = []
#     if color_type == 'hexa':
#         for _ in range(n):
#             color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
#             colors.append(color)
#     elif color_type == 'rgb':
#         for _ in range(n):
#             r = random.randint(0, 255)
#             g = random.randint(0, 255)
#             b = random.randint(0, 255)
#             colors.append(f"rgb({r},{g},{b})")
#     return colors
# print(generate_colors('hexa', 3))    
# print(generate_colors('rgb', 1))  

# level 3

# 1
# import random
 
# def shuffle_list(lst):
#     random.shuffle(lst)
#     return lst
# print(shuffle_list([5,6,4,7,8]))

# 2
# import random
# def unique_random_no():
#     return random.sample(range(10),7)
# print(unique_random_no())










