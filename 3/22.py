import json
import os
import re

f = open('./3/jawiki-country.json', 'r',  encoding='utf-8_sig')
temp = {i : json.loads(line) for i , line in enumerate(f)}
for j in temp:
    if temp[j]['title'] == 'イギリス':
        article = temp[j]['text']
        break

art_list = article.split('\n')
art_len = len(art_list)
# for i in range(art_len):
#     if 'Category' in art_list[i]:
#         tmp1 = art_list[i].split(':')
#         tmp2 = tmp1[1].split(']')
#         if '|' in tmp2[0]:
#             tmp3 = tmp2[0].split('|')
#             print(tmp3[0])
#         else:
#             print(tmp2[0])

pattern = re.compile(r'''
    ^
    .*
    \[\[Category:
    (
    .*?
    )
    (?:
    \|.*
    )?
    \]\]
    .*
    $
    ''', re.MULTILINE + re.VERBOSE)

result = pattern.findall(article)

for i in result:
    print(i)
