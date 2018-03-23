#from Ngram import ngram
import random

def typo(word):
    tmp = word.split(" ")
    tmp_len = len(tmp)

    num1 = []
    array_tmp1 = []

    for i in range(1, tmp_len - 1):
        if len(tmp[i]) > 4:
            num1.append(i)
            array_tmp1.append(tmp[i])

    random.shuffle(array_tmp1)

    array_tmp2 = []
    j = 0

    for i in range(0, tmp_len):
        if i in num1:
            array_tmp2.append(array_tmp1[j])
            j += 1
        else:
            array_tmp2.append(tmp[i])

    return array_tmp2



w = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."


print(typo(w))
