#!/usr/bin/env python3
"""Hero background tiles: pure warm gradients + a soft off-centre light glow and
vignette. NO logo/shape, so cropping into the wide hero never looks 'cut'.
Landscape (1600x1000) so object-fit:cover crops minimally. Cross-fades as
shifting warm light behind the headline."""
import os
from PIL import Image, ImageDraw

OUT = "/Volumes/20260401-WDBlack-SN850X-2TB/Work/Gigs/ras/3dprinting/wordpress/reach-any-stars-brand-kit/reach-any-stars/assets/images/hero"
os.makedirs(OUT, exist_ok=True)
W, H = 1600, 1000

def hx(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# (filename, tone A, tone B, glow x%, glow y%) — warm, cohesive, varied light
TILES = [
    ("hero-1", "#ECE3D3", "#D6C6A9", 0.32, 0.28),
    ("hero-2", "#F2ECE0", "#E0D6C2", 0.66, 0.30),
    ("hero-3", "#EFE7D8", "#DCCDB2", 0.50, 0.22),
    ("hero-4", "#F2EAD7", "#E4D6B8", 0.28, 0.34),
    ("hero-5", "#E9E1D1", "#CFC2A8", 0.70, 0.26),
    ("hero-6", "#EDE6D6", "#DBCDB1", 0.46, 0.32),
]

def diagonal(a, b):
    n = 96
    m = Image.new("L", (n, n)); px = m.load()
    for y in range(n):
        for x in range(n):
            px[x, y] = int(255 * (x + y) / (2 * (n - 1)))
    mask = m.resize((W, H), Image.BICUBIC)
    return Image.composite(Image.new("RGB", (W, H), b), Image.new("RGB", (W, H), a), mask)

def radial_mask(cx, cy, spread):
    n = 160
    m = Image.new("L", (n, n), 0); px = m.load()
    cxp, cyp = cx * n, cy * n
    maxd = (n ** 2 + n ** 2) ** 0.5
    for y in range(n):
        for x in range(n):
            d = ((x - cxp) ** 2 + (y - cyp) ** 2) ** 0.5 / maxd
            v = max(0.0, 1.0 - d / spread)
            px[x, y] = int(255 * v * v)
    return m.resize((W, H), Image.BICUBIC)

def vignette():
    n = 160
    m = Image.new("L", (n, n), 0); px = m.load()
    cx = cy = n / 2; maxd = (cx ** 2 + cy ** 2) ** 0.5
    for y in range(n):
        for x in range(n):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 / maxd
            px[x, y] = int(255 * min(1.0, d) * 0.12)
    return m.resize((W, H), Image.BICUBIC)

vg = vignette()
for name, c1, c2, gx, gy in TILES:
    img = diagonal(hx(c1), hx(c2)).convert("RGB")
    # soft warm light glow
    glow = Image.new("RGB", (W, H), hx("#FBF6EC"))
    img = Image.composite(glow, img, radial_mask(gx, gy, 0.55))
    # gentle vignette for depth
    dark = Image.eval(img, lambda v: int(v * 0.90))
    img = Image.composite(dark, img, vg)
    img.save(os.path.join(OUT, f"{name}.png"), "PNG", optimize=True)
    print(name)
print("done")
