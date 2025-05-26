import datetime

data_completa = datetime.datetime.now()

data = data_completa.date()
hora = data_completa.time()
print(data_completa)
print(data)
print(hora)

data_completa = datetime.datetime.now()

data = data_completa.date()
hora = data_completa.time()

print(f"Dia: {data_completa.day}")
print(f"Mes: {data_completa.month}")
print(f"Ano: {data_completa.year}")
print(f"Hora: {data_completa.hour}")
print(f"Minuto: {data_completa.minute}")
print(f"Segundo: {data_completa.second}")

data = datetime.date(2000, 9, 30)
print(data)
print(type(data))

hora = datetime.time(10, 20, 2)
print(hora)

completa = datetime.datetime(2001, 10, 9, 10, 20, 3)
print(completa)

atual = datetime.datetime.now()
current_time = atual.strftime("%y/%m/%d - %H:%M:%S %A - %B" )
print(current_time)

