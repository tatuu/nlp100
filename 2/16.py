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
lines_len = len(lines)

sliced_lines = list(zip(*[iter(lines)]*num))
sliced_num = len(sliced_lines)
#print(len(sliced_lines))

for i in range(sliced_num):
    file_name = "child_" + str(i) + ".txt"
    j_path = os.path.join(name, file_name)

    tmp_path = os.path.normpath(j_path)

    tmp_txt = open(tmp_path, 'w', encoding="utf-8_sig")
    tmp_txt.writelines(sliced_lines[i])
    tmp_txt.close()
