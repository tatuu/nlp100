import os

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
    if temp[0] + "\n" not in c1:
        c1.append(temp[0] + "\n")

for j in c1:
    print(j, end="")
