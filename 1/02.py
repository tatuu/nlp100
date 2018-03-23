word1 = "パトカー"
word2 = "タクシー"

w1 = list(word1)
w2 = list(word2)

num = len(word1)
word3 = ""
for i in range(num):
    word3 += w1[i]
    word3 += w2[i]

print(word3)
