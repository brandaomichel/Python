def calcular_total(nums):
    
    return sum(nums)

def retorna_ant_suc(num):
    ant = num - 1
    suc = num + 1

    return ant, suc

print(calcular_total([10, 20, 30]))
print(retorna_ant_suc(10))