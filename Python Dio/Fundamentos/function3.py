def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro Salvo com Sucesso: {marca}/{modelo}/{ano}/{placa}')

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
print()
salvar_carro(marca="Fiat", modelo="Punto", ano=2012, placa="ABC-1235")
print()
salvar_carro(**{"marca": "Fiat", "modelo": "Argo", "ano": 2020, "placa": "ASD-3211"})
print()