import os
import commands

name = os.path.dirname(os.path.abspath(__name__))

joined_path1 = os.path.join(name, './nlp100/2/col1.txt')

path1 = os.path.normpath(joined_path1)
f1 = open(path1, encoding="utf-8_sig")
line1 = f1.readlines()
f1.close()

joined_path2 = os.path.join(name, './nlp100/2/col2.txt')

path2 = os.path.normpath(joined_path2)
f2 = open(path2, encoding="utf-8_sig")
line2 = f2.readlines()
f2.close()

num = len(line1)
for i in range(num):
    line1[i] = line1[i].strip()

temp = []

for i in range(num):
    temp.append(line1[i] + "\t" + line2[i])

print(temp)

joined_path3 = os.path.join(name, './nlp100/2/col3.txt')

path3 = os.path.normpath(joined_path3)
f3 = open(path3, 'w', encoding="utf-8_sig")
f3.writelines(temp)
f3.close()

check = commands.getoutput("comfirm_13.sh")
