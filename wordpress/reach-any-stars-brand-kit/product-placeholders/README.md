# Product placeholder tiles

Interim imagery for the 6 sample WooCommerce products, until real photos exist.

- **`product-art/`** — CURRENT product images (2026-06-30): per-product **line drawings**
  (phone stand, key, tealight, pendant lamp, planter, desk organizer) on the warm tiles.
  Authored as SVG, rendered to PNG with `qlmanage -t -s 1000 -o . file.svg`. Generator:
  `product-art/make_product_art.py`. These are the featured images on the live site.
- **`make_placeholders.py` + the loose `*.png`** — the earlier "material swatch" tiles
  (warm gradient + centered mark). Superseded as product images, but the same gradient
  recipe still feeds the hero (see the theme's `assets/images/hero/`).

Swap in real photos later by setting a new featured image per product (file must be
readable from inside Studio's WASM filesystem — see below).

## Re-importing into a fresh Studio DB

The product↔image link lives in the (gitignored) site DB, so it is lost on a DB rebuild.
To restore, copy the PNGs somewhere under the live site (e.g.
`wp-content/uploads/_seed/`) so Studio's WASM wp-cli can read them — host `/tmp` paths are
NOT visible to WASM; the site root maps to `/wordpress/`. Then, per product:

```
wp media import "/wordpress/wp-content/uploads/_seed/atlas-phone-stand.png" \
  --post_id=16 --featured_image --title="Atlas Phone Stand"
```

Product IDs (Studio seed, 2026-06-30): 16 Atlas Phone Stand · 15 Comet Keychain ·
12 Luna Tealight Holder · 14 Nova Pendant Lamp Shade · 11 Orion Faceted Planter ·
13 Vega Desk Organizer. Verify with `wp post list --post_type=product --fields=ID,post_title`.
