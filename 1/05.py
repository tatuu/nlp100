#from Ngram import ngram

def mozi(word, num):
    w = list(word)
    w_len = len(w)

    for i in range(w_len - num + 1):
        for j in range(num):
            print(w[i + j], end = "")
        print("")

def tango(word, num):
    w = word.split(" ")
    w_len = len(w)

    for i in range(w_len - num + 1):
        for j in range(num):
            print(w[i + j] + " ", end = "")
        print("")

word = "I am an NLPer"

mozi(word, 2)
print("----------------------------")
tango(word, 2)
