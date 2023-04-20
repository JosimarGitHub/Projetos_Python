import json

with open("/home/dev_net/My_Projects/LAB_AUTOMACAO.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


print(dados) 