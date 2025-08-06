import re 

texto = '001234510'

info = re.findall('1', texto)

print(info)

info2 = re.split('1', texto)

print(info2)

info3 = re.sub('1', '%', texto)

print(info3)