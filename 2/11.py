import os

name = os.path.dirname(os.path.abspath(__name__))

joined_path = os.path.join(name, './nlp100/2/hightemp.txt')

path = os.path.normpath(joined_path)

txt = open(path, encoding="utf-8_sig")
lines = txt.readlines()

txt.close()

for i in lines:
    i.replace(" ", " ")

print(lines)

f = open('text.txt', 'w')
f.writelines(lines)
f.close()
