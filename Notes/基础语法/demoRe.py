# -*- codeing = utf-8 -*-
# @Time : 2020/8/23 5:36 下午

import re
# ------正则表达式：字符串模式

# ---re.compile
'''
# 此处的AA是正则表达式 用来验证其他字符串
pat = re.compile("^AA")
# 此处的search("")字符串的内容是用来被校验的
m = pat.search("AAsds")
print(m)
'''

# ----没有模式对象

# -----re.search
'''
# 参数一是正则规则，参数2是字符串，匹配第一次就返回值 后面不在匹配
sel = re.search('^a', 'avvv')
print(sel)
'''

# ----re.findall
'''
# 查找全局，匹配所有a规则，并且添加到列表中
print(re.findall('a', 'sadasdaas'))
'''

# ----sub
# 参数一，被替换对象 参数二，替换后对象 参数三，需要替换的字符串
print(re.sub('a', 'A', 'asdasd'))

# 建议在正则表达式中，被比较的字符串前面加上r ,不用担心转义字符的问题
a = r"\aabd-\'"
