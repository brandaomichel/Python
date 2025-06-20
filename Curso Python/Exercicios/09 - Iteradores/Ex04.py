class Fatorial:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __iter__(self):
        self.atual = self.x
        return self
    
    @staticmethod
    def calcula_fatorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        
        return result
    
    def __next__(self):
        if self.atual == self.y + 1:
            raise StopIteration
        
        result =  Fatorial.calcula_fatorial(self.atual)
        self.atual += 1 
        return result

for i in Fatorial(1, 10):
    print(i)