import json

def lerDados():
    arq = open('bancoDeDados.json', 'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)

def salvarDados(motos) -> list:
    arq = open('bancoDeDados.json', 'w+', encoding='utf-8')
    data = json.dumps(motos, indent=4)
    arq.write(data)
    arq.close