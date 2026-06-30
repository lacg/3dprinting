#!/usr/bin/env python3
"""Generate cohesive on-brand product placeholder tiles for Reach Any Stars.
Each tile: a soft warm diagonal gradient (a different brand tone per product,
like a 3D-print material swatch) + gentle vignette + the brand mark centered."""
import os
from PIL import Image, ImageDraw

THEME = "/Volumes/20260401-WDBlack-SN850X-2TB/Work/Gigs/ras/3dprinting/wordpress/reach-any-stars-brand-kit/reach-any-stars"
MARK = os.path.join(THEME, "assets/images/logo-mark-graphite.png")
OUT = "/private/tmp/claude-501/-Volumes-20260401-WDBlack-SN850X-2TB-Work-Gigs-ras-3dprinting/3dc43956-c48b-40b3-a7e5-55f847b90c4c/scratchpad/products"
os.makedirs(OUT, exist_ok=True)
S = 1200

def hx(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# (product_id, filename, top-left tone, bottom-right tone) — warm, cohesive, varied
TILES = [
    (16, "atlas-phone-stand",   "#ECE3D3", "#D8C9AE"),  # warm sand
    (15, "comet-keychain",      "#F4F1EA", "#E4DCCB"),  # paper
    (12, "luna-tealight",       "#F1ECE2", "#E0D8C8"),  # warm light
    (14, "nova-pendant",        "#F2EAD9", "#E6D9BE"),  # pale gold
    (11, "orion-planter",       "#E7E0D2", "#CFC4B0"),  # greige
    (13, "vega-organizer",      "#E4E3DD", "#C9C7BD"),  # cool stone
]

def diagonal_gradient(a, b, size):
    # small diagonal mask resized up, then composite two solids through it
    n = 96
    m = Image.new("L", (n, n))
    px = m.load()
    for y in range(n):
        for x in range(n):
            px[x, y] = int(255 * (x + y) / (2 * (n - 1)))
    mask = m.resize((size, size), Image.BICUBIC)
    return Image.composite(Image.new("RGB", (size, size), b),
                           Image.new("RGB", (size, size), a), mask)

def vignette(size, strength=0.10):
    # radial mask: bright center -> darker edges
    n = 128
    m = Image.new("L", (n, n), 0)
    d = ImageDraw.Draw(m)
    cx = cy = n / 2
    maxd = (cx ** 2 + cy ** 2) ** 0.5
    px = m.load()
    for y in range(n):
        for x in range(n):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 / maxd
            px[x, y] = int(255 * min(1.0, dist) * strength)
    return m.resize((size, size), Image.BICUBIC)

mark_src = Image.open(MARK).convert("RGBA")
mw = int(S * 0.34)
mh = int(mw * mark_src.height / mark_src.width)
mark = mark_src.resize((mw, mh), Image.LANCZOS)
# soften the mark slightly so it reads as a brand motif, not a loud logo
r, g, b, a = mark.split()
a = a.point(lambda v: int(v * 0.88))
mark = Image.merge("RGBA", (r, g, b, a))

for pid, name, c1, c2 in TILES:
    img = diagonal_gradient(hx(c1), hx(c2), S).convert("RGB")
    # gentle vignette for depth
    dark = Image.eval(img, lambda v: int(v * 0.90))
    img = Image.composite(dark, img, vignette(S))
    # subtle halo ring behind the mark
    ov = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    rr = int(S * 0.30)
    d.ellipse([S//2 - rr, S//2 - rr, S//2 + rr, S//2 + rr], outline=(32, 32, 32, 26), width=3)
    img = Image.alpha_composite(img.convert("RGBA"), ov)
    # mark centered, optically nudged up a hair
    img.alpha_composite(mark, (S//2 - mw//2, int(S//2 - mh//2 - S*0.01)))
    path = os.path.join(OUT, f"{name}.png")
    img.convert("RGB").save(path, "PNG", optimize=True)
    print(pid, path)
print("done")
