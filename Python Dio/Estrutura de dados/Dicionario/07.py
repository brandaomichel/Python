contatos = {"michel@gmail.com": {"nome": "Michel", "telefone": "3333-2221"}}

#print(contatos["chave"])

print(contatos.get("chave"))

print(contatos.get("chave", {}))

print(contatos.get("michel@gmail.com"), {})