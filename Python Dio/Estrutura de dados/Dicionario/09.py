contatos = {"michel@gmail.com": {"nome": "Michel", "telefone": "3333-2221"}}

contatos.setdefault("nome", "AAAA")
print(contatos)

contatos.setdefault("idade", 29)
print(contatos)