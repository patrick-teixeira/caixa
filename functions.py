import json



def add_manga(nome, autor, genero, editora, volume, preco):
    manga_data =   {nome: {
        "autor":  autor,
        "genero": genero,
        "editora": editora,
        "volumes": int(volume),
        "preco":  float(preco)
    }}
    with open('dados.json','r+') as file:
        file_data = json.load(file)
        for i in range(len(file_data['mangas'])):
            if nome in file_data['mangas'][i]:
                return
        file_data["mangas"].append(manga_data)
        file.seek(0)    
        json.dump(file_data, file, indent = 4)

def mangas_estoque():
    mangas = []
    with open('dados.json', 'r') as file:
        data = json.load(file)
        for i in range (len(data['mangas'])):
            mangas.append(list(data['mangas'][i].keys())[0])
        return mangas


def pesquisar(manga):
    mangas = []
    with open('dados.json', 'r') as file:
        data = json.load(file)
        for i in range (len(data['mangas'])):
            mangas.append(list(data['mangas'][i].keys())[0])
    if manga.lower() in mangas: return True

def quant_volumes(manga):
    mangas = []
    with open('dados.json', 'r') as file:
        data = json.load(file)
        for i in range (len(data['mangas'])):
            mangas.append(list(data['mangas'][i].keys())[0])
    if manga in mangas:
        return data['mangas'][mangas.index(manga)][manga]['volumes']

def valor_manga(manga):
    mangas = []
    with open('dados.json', 'r') as file:
        data = json.load(file)
        for i in range (len(data['mangas'])):
            mangas.append(list(data['mangas'][i].keys())[0])
    if manga in mangas:
        return data['mangas'][mangas.index(manga)][manga]['valor']
    
