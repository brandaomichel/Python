from datetime import datetime

data_txt = input("Informe a data de nascimento em formato dia/mes/ano")
data_nascimento = datetime.strptime(data_txt, '%d/%m/%Y')
data_agora = datetime.now()
dife_datas = data_agora - data_nascimento
print(dife_datas)