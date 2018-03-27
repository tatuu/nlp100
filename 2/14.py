import os
import sys

name = os.path.dirname(os.path.abspath(__name__))

joined_path = os.path.join(name, 'hightemp.txt')

path = os.path.normpath(joined_path)

txt = open(path, encoding="utf-8_sig")
lines = txt.readlines()

txt.close()

args = sys.argv
num = int(args[1])

for i in range(num):
    print(lines[i])
