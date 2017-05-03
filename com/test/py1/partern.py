import re

patter = re.compile(r'hello')
match1 = patter.match('hello word')
print(patter)

if match1:
    print(match1.groups())
else:
    print('匹配失败')