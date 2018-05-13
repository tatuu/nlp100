import os
from collections import Counter

name = os.path.dirname(os.path.abspath(__name__))

joined_path = os.path.join(name, './2/hightemp.txt')

path = os.path.normpath(joined_path)

txt = open(path, encoding="utf-8_sig")
lines = txt.readlines()

txt.close()

c1 = []

for i in lines:
    temp = []
    temp = i.split()
    c1.append(temp[0])

mycounter = Counter(c1)

for j in mycounter.most_common():
    print(j)
