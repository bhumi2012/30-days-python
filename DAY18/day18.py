import re
from collections import Counter
# level 1
# 1
# paragraph = """I love teaching. If you do not love teaching 
# what else can you love. I love Python if you do not love 
# something which can give you all the capabilities to develop 
# an application what else can you love."""

# words=re.findall(r'\w+',paragraph.lower())
# print(words)

# word_count=Counter(words)
# print(word_count)

# most_common=word_count.most_common(1)
# print(most_common)

# 2
# text = """The position of some particles on the
#  horizontal x-axis are -12, -4, -3 and -1 in 
# the negative direction, 0 at origin, 4 and 8 in 
# the positive direction."""

# points=re.findall(r'-?\d+',text)
# print(points)

# points=list(map(int,points))
# sortedpoints =sorted(points)
# print(sortedpoints)

# distance=sortedpoints[-1] - sortedpoints[0]
# print("distance is :",distance)

# level 2
# 1
# def valid_var(name):
#     pattern = r'^[a-zA-Z_]w*$'
#     return bool(re.match(pattern , name))

# print(valid_var('first-name'))
# print(valid_var('firstname'))

# level 3
# 1
# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve 
# %tea@ching%;. There $is nothing; &as& mo@re rewarding as 
# educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching 
# m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s 
# mo@tivate yo@u to be a tea@cher!?'''

# def cleaning_text(sentence):
#     return re.sub(r'[^a-zA-Z0-9\s]',' ',sentence)

# def most_freq(sentence,n=3):
#  words=re.findall(r'\b\w+\b', sentence.lower())
#  return Counter(words).most_common(n)

# cleaned=cleaning_text(sentence)
# print(cleaned)
# print(most_freq(cleaned,3))