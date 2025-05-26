texto = 'testanto capitalize'
print(texto.capitalize())

texto2 = "tesSsofPoK pythoi"
print(texto2.upper())
print(texto2.lower())
print(texto2.swapcase())

text03 = "python is the best"
print(text03.title())

texto4 = '1234567'
print(texto4.center(9))
print(texto4.center(14))
print(texto4.center(20, '-'))

texto4 = "1234567"
print(texto4.rjust(9))
print(texto4.ljust(9))

texto = "12121212"
print(texto.count("121"))
print(texto.startswith("12"))
print(texto.endswith("12"))

texto = "me encontra 20 10 5"
pos = texto.find("10")
print(pos)

texx = "Ol@ eu sou  @ ful@n@"
novo = texx.replace("@", 'a')
print(novo)

textt = '10, 20, 30'
print(textt.split(","))

texto = "Ola, bom dia\n este e um curso de python\n bem vindo"
print(texto.splitlines())

print("abcdE3".isalpha())
print("abcdE3".isalnum())
print("abc,dE3".isalnum())
print("123.1".isdecimal())