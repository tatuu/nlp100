#from Ngram import ngram

def mozi(word, num):
    w = list(word)
    w_len = len(w)

    tmp_array = []
    for i in range(w_len - num + 1):
        tmp_word = ""
        for j in range(num):
            tmp_word += w[i + j]
        tmp_array.append(tmp_word)

    return tmp_array

def wa(array1, array2):
    array1_len = len(array1)
    array2_len = len(array2)

    tmp = []

    for i in range(array1_len):
        if array1[i] not in tmp:
            tmp.append(array1[i])

    for i in range(array2_len):
        if array2[i] not in tmp:
            tmp.append(array2[i])

    return tmp

def seki(array1, array2):
    array1_len = len(array1)
    array2_len = len(array2)

    tmp = []

    for i in range(array1_len):
        for j in range(array2_len):
            if array1[i] == array2[j] and array1[i] not in tmp:
                tmp.append(array1[i])

    return tmp

def sa(array1, array2):
    array1_len = len(array1)
    array2_len = len(array2)

    tmp = []

    for i in range(array1_len):
        for j in range(array2_len):
            if array1[i] not in tmp and not array1[i] == array2[j]:
                boolean = True
            else:
                boolean = False
                break
        if boolean == True:
            tmp.append(array1[i])



    return tmp


word1 = "paraparaparadise"
word2 = "paragraph"

tmp1 = mozi(word1, 2)
tmp2 = mozi(word2, 2)
print(tmp1)
print(tmp2)
print("-----------------------------------------------------------")

tmp3 = wa(tmp1, tmp2)
print("和集合")
print(tmp3)

tmp4 = seki(tmp1, tmp2)
print("積集合")
print(tmp4)

tmp5 = sa(tmp1, tmp2)
print("差集合")
print(tmp5)

print("se" in tmp1)
print("se" in tmp2)
