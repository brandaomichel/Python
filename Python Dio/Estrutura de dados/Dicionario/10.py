contatos = {
    "michel@gmail.com": {"nome": "Michel", "telefone": "3333-2221"},
    "juliana@gmail.com": {"nome": "Juiana", "telefone": "3333-3333"},
    "paulo@gmail.com": {"nome": "Paulo", "telefone": "3333-4444"},
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "3333-2244421"}
}

resultado = "michel@gmail.com" in contatos
print(resultado)

resultado = "sd@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["michel@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["michel@gmail.com"]
print(resultado)