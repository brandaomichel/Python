e_inteiro = isinstance(5, (int, float, str))
print(e_inteiro)

class Base:
    def __init__(self):
        pass

class Herdeiro(Base):
    def __init__(self):
        pass

classe = Herdeiro()
e_base = isinstance(classe, Base)

print(e_base)