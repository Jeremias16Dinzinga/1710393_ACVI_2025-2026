#!/usr/bin/env python3
"""
imagens2txt_pixels.py — Lê uma imagem (JPG/PNG/BMP) e exporta todos os píxeis para um ficheiro .txt
"""

from pathlib import Path
from PIL import Image

def main():
    print("=== Exportar todos os píxeis da imagem para TXT ===\n")
    formato = input("Indique o formato (jpg, png, bmp): ").strip().lower()
    entrada = input("Indique o caminho da imagem: ").strip()
    saida = input("Indique o nome do ficheiro .txt de saída: ").strip()

    fp = Path(entrada)
    if not fp.exists():
        print("❌ Ficheiro não encontrado.")
        return

    try:
        with Image.open(fp) as img:
            largura, altura = img.size
            modo = img.mode
            img = img.convert("RGB")  # forçar para RGB para uniformizar

            linhas = []
            linhas.append(f"# Ficheiro: {fp.name}")
            linhas.append(f"# Dimensões: {largura}x{altura}")
            linhas.append(f"# Modo original: {modo}")
            linhas.append("# Dados dos píxeis (linha por linha)\n")

            # Guardar cada linha da imagem
            for y in range(altura):
                linha_pix = []
                for x in range(largura):
                    r, g, b = img.getpixel((x, y))
                    linha_pix.append(f"({r},{g},{b})")
                # Junta todos os píxeis da linha separados por espaço
                linhas.append(" ".join(linha_pix))

        Path(saida).write_text("\n".join(linhas), encoding="utf-8")
        print(f"✅ Relatório completo gravado em {saida}")

    except Exception as e:
        print("❌ Erro ao processar a imagem:", e)

if __name__ == "__main__":
    main()
