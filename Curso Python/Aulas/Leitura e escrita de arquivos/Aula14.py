import yaml

with open('C:/Users/Michel/OneDrive/Documentos/GitPython/Python/Curso Python/Aulas/Leitura e escrita de arquivos/config.yaml') as file:
    data = yaml.load(file, Loader=yaml.full_load)

    print(data['database']['name'])