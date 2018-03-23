word ="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

w = word.split(" ")

num = len(w)
#print(num)
n_array = [1,5,6,7,8,9,15,16,19]
w_dic = {}
for i in range(num):
    if i in n_array:
        tmp = w[i][:2]
        w_dic[tmp] = i
    else:
        tmp = w[i][:1]
        w_dic[tmp] = i


print(w_dic)
