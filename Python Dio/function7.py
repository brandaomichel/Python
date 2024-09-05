def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Punto", 2015, "MAP-1234", marca="Fiat", motor="1.6", combustivel="Flex")