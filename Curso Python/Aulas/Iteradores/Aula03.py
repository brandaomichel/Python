def ancora():
    yield 1
    yield 2
    yield 3

for item in ancora():
    print(item)

print(10 in ancora())

func = ancora()
print(next(func))

def meu_range(nume):
    local_num = 0 
    while local_num < nume:
        yield local_num
        local_num += 1

for i in meu_range(10):
    print(i)