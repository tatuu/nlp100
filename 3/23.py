import json
import os

f = open('./3/jawiki-country.json', 'r',  encoding='utf-8_sig')
temp = {i : json.loads(line) for i , line in enumerate(f)}
for j in temp:
    if temp[j]['title'] == 'イギリス':
        article = temp[j]['text']
        break

art_list = article.split('\n')
art_len = len(art_list)
for i in range(art_len):
    if 'Category' in art_list[i]:
        print(art_list[i])
