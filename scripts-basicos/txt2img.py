#!/usr/bin/env python3
import sys, re, argparse
from pathlib import Path
from typing import List, Tuple, Optional
import numpy as np
from PIL import Image

NUMERIC_TUPLE_RE = re.compile(r'\(\s*\d+\s*(?:,\s*\d+\s*){0,4}\)')

def parse_txt_image(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Keep lines, but we will extract only *numeric* tuples to avoid things like "(linha por linha)"
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    out_name_meta = None
    dims_meta = None
    mode_meta = None

    # Parse simple metadata from lines that start with '#'
    for ln in lines[:20]:
        if ln.lstrip().startswith('#'):
            body = ln.lstrip('#').strip()
            lb = body.lower()
            if lb.startswith('ficheiro:'):
                out_name_meta = body.split(':',1)[1].strip()
            elif lb.startswith('dimensões:') or lb.startswith('dimensoes:'):
                dims_txt = body.split(':',1)[1].strip()
                m = re.match(r'(\d+)\s*[xX]\s*(\d+)', dims_txt)
                if m:
                    dims_meta = (int(m.group(1)), int(m.group(2)))
            elif lb.startswith('modo original:') or lb.startswith('modo:'):
                mode_meta = body.split(':',1)[1].strip().upper()

    # Extract only numeric tuples per line
    pixel_rows: List[List[Tuple[int, ...]]] = []
    for ln in lines:
        # Skip pure comment lines
        if ln.startswith('#'):
            continue
        tuples = []
        for grp in NUMERIC_TUPLE_RE.findall(ln):
            nums = re.findall(r'\d+', grp)
            vals = tuple(int(n) for n in nums)
            tuples.append(vals)
        if tuples:
            pixel_rows.append(tuples)

    if not pixel_rows:
        raise ValueError("Não foram encontrados tuplos numéricos de píxeis, ex.: (12,34,56).")

    # Infer dimensions or normalize to metadata
    H = len(pixel_rows)
    W = max(len(r) for r in pixel_rows)
    if dims_meta:
        Wm,Hm = dims_meta
        W,H = Wm,Hm
        norm_rows = []
        for row in pixel_rows[:H]:
            if len(row) < W:
                pad = row[-1] if row else (0,0,0)
                row = row + [pad]*(W-len(row))
            else:
                row = row[:W]
            norm_rows.append(row)
        while len(norm_rows) < H:
            norm_rows.append(norm_rows[-1])
        pixel_rows = norm_rows
    else:
        pixel_rows = [row + [row[-1]]*(W-len(row)) if len(row)<W else row for row in pixel_rows]

    # Infer/normalize mode
    if mode_meta is None:
        n = len(pixel_rows[0][0])
        mode_meta = {1:'L', 3:'RGB', 4:'RGBA'}.get(n, 'RGB')
    if mode_meta in ('GREY','GRAY','GREYSCALE','GRAYSCALE','LUMINANCE'):
        mode_meta = 'L'
    if mode_meta not in ('L','RGB','RGBA','CMYK'):
        mode_meta = 'RGB'
    return out_name_meta, (W,H), mode_meta, pixel_rows

def rows_to_image(dims, mode, rows):
    W,H = dims
    n_channels = len(rows[0][0])
    arr = np.zeros((H, W, n_channels), dtype=np.uint8)
    for y in range(H):
        for x in range(W):
            pix = rows[y][x]
            for c in range(n_channels):
                v = int(pix[c])
                if v < 0: v = 0
                if v > 255: v = 255
                arr[y,x,c] = v
    if mode=='L':
        if arr.shape[2]==1:
            return Image.fromarray(arr[:,:,0], 'L')
        else:
            return Image.fromarray(arr.squeeze(), 'L')
    elif mode=='CMYK':
        return Image.fromarray(arr, 'CMYK').convert('RGB')
    else:
        if arr.shape[2]==3:
            img = Image.fromarray(arr, 'RGB')
        elif arr.shape[2]==4:
            img = Image.fromarray(arr, 'RGBA')
        else:
            img = Image.fromarray(arr)
        return img.convert(mode)

def save_image(img, suggested_name: Optional[str] = None):
    if suggested_name:
        out_name = suggested_name
    else:
        out_name = "image.png"
    ext = Path(out_name).suffix.lower()
    if ext not in ('.png','.jpg','.jpeg','.bmp'):
        ext = '.png'
        out_name = str(Path(out_name).with_suffix('.png'))
    out_path = Path(out_name).name
    if ext in ('.jpg','.jpeg','.bmp') and img.mode in ('RGBA','LA'):
        img = img.convert('RGB')
    img.save(out_path)
    return out_path

def main():
    ap = argparse.ArgumentParser(description="Converte TXT de píxeis em imagem (BMP/JPG/PNG). Ignora texto como '(linha por linha)'.")
    ap.add_argument("input_txt", help="Caminho do ficheiro TXT")
    ap.add_argument("-o","--output", help="Forçar caminho de saída (opcional)")
    args = ap.parse_args()
    in_path = Path(args.input_txt)
    if not in_path.exists():
        # Ajuda rápida para erro comum no Windows ao omitir a extensão
        if not in_path.suffix and in_path.with_suffix(".txt").exists():
            in_path = in_path.with_suffix(".txt")
        else:
            raise FileNotFoundError(f"Ficheiro não encontrado: {in_path}")
    fname, dims, mode, rows = parse_txt_image(in_path)
    img = rows_to_image(dims, mode, rows)
    out_path = args.output if args.output else fname
    path = save_image(img, out_path)
    print(f"Imagem criada: {path}")
    print(f"Dimensões: {dims[0]}x{dims[1]} | Modo: {img.mode}")
if __name__ == "__main__":
    from PIL import Image
    main()
