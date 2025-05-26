from datetime import datetime, timedelta

data1 = datetime(2020, 10, 20)
data2 = datetime(2020, 11, 20)
diferenca_data = data2 - data1
print(diferenca_data)

data_atual = datetime.now()
data_futura1 = data_atual + timedelta(weeks=4)
data_futura2 = data_atual + timedelta(days=30)
data_futura3 = data_atual + timedelta(hours=12)
data_futura4 = data_atual + timedelta(minutes=60)
print(f"Data atual: {data_atual}")
print(f"Mais 4 semanas: {data_futura1}")
print(f"Mais 30 dias {data_futura2}")
print(f"Mais 12 horas {data_futura3}")
print(data_futura4)

data_2000 = datetime(2000, 1, 1, 0, 0, 0)
data_agora = datetime.now()
diferenca = data_agora - data_2000

print(f"Desde o ano 2000 {diferenca.days} dias")
print(f"Desde o ano 2000 {diferenca.seconds} segundos")
print(f"Desde o ano 2000 {diferenca.microseconds} microseguindos")

anos = int(diferenca.days/365)
meses = anos * 12
print(f"Desde o ano 2000 {anos} anos")
print(f"Desde o ano 2000 {meses} meses")

data_text = input("Digite a data no formato DD/MM/AAAA")
datatime = datetime.strptime(data_text, "%d/%m/%Y")
print(datatime)