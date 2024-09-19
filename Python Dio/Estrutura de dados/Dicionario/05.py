contatos = {
    "michel@gmail.com": {"nome": "Michel", "telefone": "3333-2221"}}

copia = contatos.copy()

copia["michel@gmail.com"] = {"nome": 'asd'}
print(copia["michel@gmail.com"])