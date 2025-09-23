import os
from PIL import Image

# ========================
# VARIÁVEIS DE CONFIGURAÇÃO
# ========================
# PASTA_IMAGENS = "gif_imagens"   # pasta onde estão as imagens originais
# PASTA_SAIDA = "gif_redimensionadas"  # pasta de saída para imagens redimensionadas
# NOVA_ALTURA = 100               # altura desejada em píxeis
# ========================

PASTA_IMAGENS = input("Pasta a redimensionar: ")
PASTA_SAIDA = input("Nome da pasta de saida: ")
NOVA_ALTURA = int(input("Altura das imagens: "))

def redimensionar_imagens():
    # Criar pasta de saída se não existir
    os.makedirs(PASTA_SAIDA, exist_ok=True)

    # Lista de ficheiros da pasta
    ficheiros = os.listdir(PASTA_IMAGENS)
    imagens = [f for f in ficheiros if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not imagens:
        print("Nenhuma imagem encontrada na pasta.")
        return

    for nome in imagens:
        caminho_original = os.path.join(PASTA_IMAGENS, nome)
        caminho_saida = os.path.join(PASTA_SAIDA, nome)

        with Image.open(caminho_original) as img:
            # calcular nova largura mantendo proporção
            largura_original, altura_original = img.size
            nova_largura = int((NOVA_ALTURA / altura_original) * largura_original)

            # redimensionar
            img_redimensionada = img.resize((nova_largura, NOVA_ALTURA), Image.LANCZOS)

            # guardar na pasta de saída
            img_redimensionada.save(caminho_saida)

            print(f"{nome} redimensionada para {nova_largura}x{NOVA_ALTURA}")

    print(f"\nTodas as imagens foram redimensionadas e guardadas em '{PASTA_SAIDA}'.")

if __name__ == "__main__":
    redimensionar_imagens()
