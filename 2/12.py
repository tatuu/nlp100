import os

name = os.path.dirname(os.path.abspath(__name__))

joined_path = os.path.join(name, './2/hightemp.txt')

path = os.path.normpath(joined_path)

txt = open(path, encoding="utf-8_sig")
lines = txt.readlines()

txt.close()

c1 = []
c2 = []


for i in lines:
    temp = []
    temp = i.split("\t")
    c1.append(temp[0] + "\n")
    c2.append(temp[1] + "\n")

joined_path1 = os.path.join(name, './2/col1.txt')

path1 = os.path.normpath(joined_path1)
f1 = open(path1, 'w', encoding="utf-8_sig")
f1.writelines(c1)
f1.close()

joined_path2 = os.path.join(name, './2/col2.txt')

path2 = os.path.normpath(joined_path2)
f2 = open(path2, 'w', encoding="utf-8_sig")
f2.writelines(c2)
f2.close()
