# Reach Any Stars — Brand Kit

Everything to skin your WordPress + WooCommerce store in the brand: the `reach-any-stars`
**standalone block theme** (Full Site Editing) — color tokens, Manrope typography, spacing,
element + WooCommerce styles, header/footer parts and block templates — plus the logo PNGs
and a full favicon set. Built to be handed to Claude Code on your computer.

```
reach-any-stars-brand-kit/
├── reach-any-stars/            ← the block theme. ZIP THIS FOLDER to upload to WordPress.
│   ├── style.css               ← theme header (no Template line — standalone, not a child)
│   ├── functions.php           ← block-theme + WooCommerce supports
│   ├── theme.json              ← all brand tokens live here (single source of truth)
│   ├── templates/              ← front-page, index, page, single, archive, search, 404
│   ├── parts/                  ← header.html, footer.html
│   └── assets/
│       ├── fonts/Manrope[wght].woff2     (self-hosted variable font, 200–800)
│       └── images/             (logo PNGs the theme/header can use)
├── brand-assets/
│   ├── logos/                  (full-res transparent PNGs — mark, lockup, stacked, light+dark)
│   ├── favicons/               (.ico, PNG sizes, apple-touch, maskable, manifest, head snippet)
│   └── fonts/                  (Manrope woff2 + ttf + static Medium/SemiBold)
└── README.md
```

---

## The Manrope decision (locked)

**Typeface: Manrope**, used for everything — wordmark, headings, and body. One family, no pairing.

- **Why it fits.** Manrope is geometric in construction but warm in its curves — the same
  "geometric bones, organic skin" idea as the delta. The name reads like it *grew from* the
  mark rather than getting bolted on beneath it. That continuity is the whole reason it won
  over the other candidates.
- **License:** Open Font License — free for commercial use, including on physical products,
  and free to self-host. No Google Fonts call, no GDPR footnote, faster load.
- **Wordmark spec:** Title Case, one line, **weight 500 (Medium)**, tracking **~0.015em**.
  (All-caps was tried and rejected — it flattened every candidate font into the same shape.)
- **Web weights:** the shipped `Manrope[wght].woff2` is the variable font covering 200–800,
  so body (400), headings (600), and the 500 wordmark all come from one 53 KB file.

Type scale and weights are already wired into `theme.json`: body 400 / headings 600 with a
slight negative tracking (−0.012em) so large headings stay tight and architectural; H1 at 700.

---

## Color tokens

Defined once in `theme.json`, available in every block's color picker and in CSS as
`var(--wp--preset--color--SLUG)`. Color comes from product photography — the UI chrome stays
quiet and neutral. No gold, no brass.

| Token              | Hex       | Role                                   |
|--------------------|-----------|----------------------------------------|
| `ras-paper`        | `#F4F2EE` | Page background (light)                |
| `ras-surface`      | `#FBFAF7` | Cards / raised surfaces                |
| `ras-ink`          | `#2B2722` | Primary text / dark logo               |
| `ras-muted`        | `#6E665C` | Secondary text                         |
| `ras-line`         | `#DED8CC` | Hairlines / borders                    |
| `ras-graphite`     | `#202020` | Futuristic charcoal — dark sections    |
| `ras-warm-charcoal`| `#241F1B` | Woody base — alt dark / button hover   |
| `ras-aluminum`     | `#BFBFB6` | Futuristic mark / metallic neutral     |
| `ras-greige`       | `#C4B9A6` | Woody mark / warm accent               |
| `ras-light`        | `#EDEAE4` | Text/logo on dark backgrounds          |

---

## Install the theme

This is a **standalone block theme** — there is no parent to install. WooCommerce should be
active for the shop/product/cart templates to render.

1. **Zip the `reach-any-stars` folder** (the folder itself, so the zip contains
   `reach-any-stars/style.css`, not loose files).
2. In WordPress: **Appearance → Themes → Add New → Upload Theme**, choose the zip, install,
   then **Activate**.
3. Open **Appearance → Editor** — header/footer parts and all templates (front page, shop,
   single product, cart, etc.) are editable as blocks. **Styles** shows the Reach Any Stars
   palette and Manrope as defaults. Manrope's `@font-face` is generated automatically from
   `theme.json`; nothing to enqueue by hand.

> Building locally first (LocalWP / WordPress Studio): install + activate this theme and
> WooCommerce, then carry the theme across in your site export when you go live.

---

## Favicons

Easiest path in WordPress: **Settings → General → Site Icon** (or the Customizer / Site Editor),
upload `brand-assets/favicons/icon-512.png`, and WordPress generates the tab and Apple icons.

Manual / full control: upload the contents of `brand-assets/favicons/` to your **site root** and
paste `head-snippet.html` into `<head>`. The icon is the bare delta in **aluminum on charcoal**,
chosen for contrast in a browser tab.

Files: `favicon.ico` (16/32/48) · `icon-16/32/48/180/192/512.png` · `apple-touch-icon.png` ·
`icon-maskable-512.png` · `site.webmanifest`.

---

## Logo usage

Two forms, two colorways. Transparent backgrounds.

- **`logo-mark-*`** — bare delta. Header on small screens, app/social avatar, anywhere the brand
  is already established.
- **`logo-lockup-*`** — delta over the **Reach Any Stars** wordmark. The first impression: header,
  packaging, listing banners — anywhere a stranger meets the brand cold.
- **`logo-stacked-graphite`** — three-line alt for narrow / vertical spaces.

Pick the colorway by background: **`-graphite`** on light (paper/white), **`-light`** on dark
(charcoal). For your WooCommerce header, set `logo-lockup-graphite.png` as the site logo in the
Site Editor header block, and swap to `-light` if you put the header on a charcoal bar.

---

## Handing to Claude Code

Point Claude Code at this folder and it has everything it needs: the tokens are declarative in
`theme.json`, so asking it to "add a charcoal newsletter section using the brand tokens" or
"build a product card pattern on `ras-surface` with a `ras-line` border" resolves to real values
with no guessing. Keep custom CSS in `style.css`.
