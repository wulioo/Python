# -*- coding:UTF-8 -*-
import re

f = open("/Users/dev/Downloads/backend.log", "r")
f1 = open("/Users/dev/Downloads/bbbb.log", 'a+')
content = f.read()
result = content.split('--#015', re.S)
str1 = "array"
red = re.findall('[a-zA-Z]{3}  [0-9](.*?)--#015', content, re.S)

for lines in red:
    res = re.sub('[a-zA-Z]{3}  [0-9] [0-9]{2}:[0-9]{2}:[0-9]{2} hb-bss distribute.bss', '', lines)
    reb = re.findall('array([.\s\S]*?)#015', res)
    for lineb in reb:
        res = res.replace(lineb, lineb.replace('\n', ''))
    insert = re.findall('distribute.bss\s(.*?)GET', lines)
    for ins in insert:
        # print(ins)
        i = ins
        for line in res.split('\n'):
            str2 = i+line
            print(str2, file=f1)


f.close()
