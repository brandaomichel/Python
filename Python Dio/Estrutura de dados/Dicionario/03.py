contatos = {
    "michel@gmail.com": {"nome": "Michel", "telefone": "3333-2221"},
    "juliana@gmail.com": {"nome": "Juiana", "telefone": "3333-3333"},
    "paulo@gmail.com": {"nome": "Paulo", "telefone": "3333-4444"},
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "3333-2244421"}
}

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)
