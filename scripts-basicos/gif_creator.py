import os
from PIL import Image

# ========================
# VARIÁVEIS DE CONFIGURAÇÃO
# ========================

#PASTA_IMAGENS = "gif_imagens"   # pasta onde estão as imagens
#NOME_GIF = "resultado.gif"      # nome do ficheiro GIF de saída
#DURACAO_FRAME = 500             # duração de cada frame em ms


PASTA_IMAGENS = input("nome da pasta de imagens: ")   
NOME_GIF = input("nome do file gif de output: ")
NOME_GIF = NOME_GIF+'.gif'
DURACAO_FRAME = int(input("tempo de duracao_frames: "))
# ========================

def criar_gif():
    # Lista de ficheiros na pasta
    ficheiros = sorted(os.listdir(PASTA_IMAGENS))
    
    # Filtrar apenas imagens suportadas
    imagens = [f for f in ficheiros if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not imagens:
        print("Nenhuma imagem encontrada na pasta.")
        return
    
    # Abrir todas as imagens
    frames = [Image.open(os.path.join(PASTA_IMAGENS, img)) for img in imagens]
    
    # Criar o GIF
    frames[0].save(
        NOME_GIF,
        save_all=True,
        append_images=frames[1:],
        duration=DURACAO_FRAME,
        loop=0
    )
    
    print(f"GIF criado com sucesso: {NOME_GIF}")

if __name__ == "__main__":
    criar_gif()
