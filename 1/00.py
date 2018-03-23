word = "stressed"

word2 = list(word)
#print(word2)

num = len(word2)
for i in range(num):
    print(word2[num - i - 1], end = "")
