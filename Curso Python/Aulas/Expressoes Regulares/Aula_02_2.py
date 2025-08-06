import re

text = 'ABCDefgHI123'

#[]
info1 = re.findall('[Ae3]', text)
info2 = re.findall('[A-Z]', text)
info3 = re.findall('[a-z]', text)
info4 = re.findall('[0-9]', text)
info5 = re.findall('[A-Za-z]', text)

print(info1)
print(info2)
print(info3)
print(info4)
print(info5)