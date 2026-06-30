#!/usr/bin/env python3
"""Per-product line-art tiles: each product's warm gradient + a simple line
illustration of the item. Rendered to PNG via qlmanage, then set as featured
images. Honest sketch placeholders until real photos exist."""
import os
OUT = "/private/tmp/claude-501/-Volumes-20260401-WDBlack-SN850X-2TB-Work-Gigs-ras-3dprinting/3dc43956-c48b-40b3-a7e5-55f847b90c4c/scratchpad/art"
os.makedirs(OUT, exist_ok=True)

BG = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<radialGradient id="glow" cx="0.42" cy="0.34" r="0.62"><stop offset="0" stop-color="#FBF6EC" stop-opacity="0.7"/><stop offset="1" stop-color="#FBF6EC" stop-opacity="0"/></radialGradient>
</defs>
<rect width="1200" height="1200" fill="url(#bg)"/>
<rect width="1200" height="1200" fill="url(#glow)"/>
<g fill="none" stroke="#2B2722" stroke-width="16" stroke-linecap="round" stroke-linejoin="round">
{art}
</g>
</svg>'''

# (slug, product_id, c1, c2, art)
P = [
 ("atlas-phone-stand", 16, "#ECE3D3", "#D8C9AE", '''
   <path d="M452 768 H748"/>
   <path d="M520 768 L616 470"/>
   <g transform="rotate(18 600 600)"><rect x="500" y="406" width="208" height="372" rx="26"/><line x1="604" y1="724" x2="604" y2="724"/></g>'''),
 ("comet-keychain", 15, "#F4F1EA", "#E4DCCB", '''
   <circle cx="600" cy="404" r="104"/>
   <circle cx="600" cy="404" r="40"/>
   <line x1="600" y1="508" x2="600" y2="792"/>
   <path d="M600 700 h60"/>
   <path d="M600 754 h46 v42"/>'''),
 ("luna-tealight", 12, "#F1ECE2", "#E0D8C8", '''
   <path d="M512 606 L536 776 H664 L688 606"/>
   <path d="M494 606 H706"/>
   <path d="M600 606 C 552 560 556 500 600 462 C 644 500 648 560 600 606 Z"/>'''),
 ("nova-pendant", 14, "#F2EAD9", "#E6D9BE", '''
   <line x1="600" y1="330" x2="600" y2="452"/>
   <path d="M548 452 L470 672 H730 L652 452 Z"/>
   <path d="M470 672 H730"/>
   <path d="M558 672 Q600 730 642 672"/>'''),
 ("orion-planter", 11, "#E7E0D2", "#CFC4B0", '''
   <path d="M500 600 L534 776 H666 L700 600"/>
   <path d="M482 600 H718"/>
   <path d="M600 600 V776"/>
   <path d="M600 600 C 554 552 540 478 572 432"/>
   <path d="M600 600 C 646 552 660 478 628 432"/>
   <path d="M600 600 V448"/>'''),
 ("vega-desk-organizer", 13, "#E4E3DD", "#C9C7BD", '''
   <path d="M452 650 H748 L708 780 H492 Z"/>
   <path d="M600 650 V780"/>
   <line x1="528" y1="650" x2="512" y2="498"/>
   <line x1="566" y1="650" x2="584" y2="476"/>'''),
]

for slug, pid, c1, c2, art in P:
    open(os.path.join(OUT, f"{slug}.svg"), "w").write(BG.format(c1=c1, c2=c2, art=art))
    print(slug, pid)
print("done")
