def deixa_maiusculo(func):
    def inner_fun(str1, str2):
        return func(str1, str2).upper()
    return inner_fun

@deixa_maiusculo
def concat_string(str1, str2):
    return str1 + str2

strrr = concat_string('michel', 'michel')
#print(strrr)

def deixa_mai(func):
    def iinner_fuc(texto):
        return func(texto).upper()
    
    return iinner_fuc

def insert_parentese(func):
    def inner_func(texto):
        return '(' + func(texto) + ')'
    
    return inner_func

@deixa_mai
@insert_parentese
def formata_string(texto):
    return texto

print(formata_string("This text to be formatted"))