def retira_palvar(texto, palavras):
    for palavra in palavras:
        texto = texto.replace(palavra, "*")
    return texto

texto_user = "nao pode falar a palvra droga ou monstro no chat"
palvra_proi = ["droga", 'monstro']
print(retira_palvar(texto_user, palvra_proi))