import os

def listar_fotos(pasta):
    extensoes_fotos = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.jiff']
    fotos = []
    
    
    for arquivo in os.listdir(pasta):
        
        if any(arquivo.lower().endswith(ext) for ext in extensoes_fotos):
            fotos.append(arquivo)
    
    return fotos

caminho_pasta = 'C:/Users//Desktop/Internet Explorer/Foto e Imagens/Imagens'

fotos_encontradas = listar_fotos(caminho_pasta)

for foto in fotos_encontradas:
    print(foto)
