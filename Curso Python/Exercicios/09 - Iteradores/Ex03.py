class Tabuada():
    def __init__(self, num):
        self.num = num
    def __iter__(self):
        self.atual = 0
        return self
    
    def __next__(self):
        self.atual += 1
        if self.atual == 11:
            raise StopIteration

        return self.atual * self.num

tabuada = Tabuada(5)

for i in tabuada:
    print(i)