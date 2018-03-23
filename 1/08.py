#from Ngram import ngram

def cipher(word):
    if word.islower():
        tmp = 219 - ord(word)
        return chr(tmp)
    else:
        return word

def decode(word):
    tmp = 219 - ord(word) 
    return chr(tmp)

w1 = "t"
w2 = "テ"
print(cipher(w1))
print(cipher(w2))

print(decode(cipher(w1)))
