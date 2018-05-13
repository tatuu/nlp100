import json
import os

f = open('./3/jawiki-country.json', 'r',  encoding='utf-8_sig')
temp = {i : json.loads(line) for i , line in enumerate(f)}
for j in temp:
    if temp[j]['title'] == 'イギリス':
        print(temp[j]['text'])
        break
