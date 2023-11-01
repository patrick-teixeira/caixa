import json

def add_autor(autor, obra):
    with open('dados.json','r+') as file:
        file_data = json.load(file)
        if autor in file_data['autores']:
            if obra not in file_data["autores"][autor]:
                print('a')
                file_data["autores"][autor].append(obra)
                file.seek(0)
                json.dump(file_data, file, indent = 4)
                return
        else:
            file_data["autores"][autor] = [obra]
            file.seek(0)
            json.dump(file_data, file, indent = 4)
            print(file_data['autores'])


def add_editora(editora, obra):
    with open('dados.json','r+') as file:
        file_data = json.load(file)
        if editora in file_data['editoras']:
            if obra not in file_data["editoras"][editora]:
                print('a')
                file_data["editoras"][editora].append(obra)
                file.seek(0)
                json.dump(file_data, file, indent = 4)
                return
        else:
            file_data["editoras"][editora] = [obra]
            file.seek(0)
            json.dump(file_data, file, indent = 4)

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

def ler_autor():
    with open('dados.json', 'r') as file:
        data = json.load(file)
        autores = list(data['autores'].keys())
        for autor in autores:
            print(autor)

def mangas_estoque():
    mangas = []
    with open('dados.json', 'r') as file:
        data = json.load(file)
        for i in range (len(data['mangas'])):
            mangas.append(list(data['mangas'][i].keys())[0])
        return mangas

def ler_editoras():
    with open('dados.json', 'r') as file:
        data = json.load(file)
        editoras = list(data['editoras'].keys())
        for i in range (len(editoras)):
            print(editoras[i])

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
    
if __name__ == '__main__':
    pass