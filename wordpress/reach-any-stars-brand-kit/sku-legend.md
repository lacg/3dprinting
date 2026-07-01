# Reach Any Stars — SKU legend

The single source of truth for how product SKUs are coded. Every SKU decodes with
this file; the future print-queue automation reads the same segments.

## Format

```
RAS-<PRODUCT>-<SIZE>-<COLOUR>-<FINISH>
```

- Hyphen-delimited → parsed by splitting on `-`, **not** by character position, so
  segments can be any length (no padding, no capacity ceiling).
- Example: `RAS-PLANTR-010-PURPLE-SILK` = Reach Any Stars · Planter · 10 cm · Purple · Silk.

### Segments

| Segment | Rule | Examples |
|---|---|---|
| `RAS` | Fixed brand prefix (Reach Any Stars). Always present. | `RAS` |
| `PRODUCT` | 6-letter product code (see table). | `PLANTR` |
| `SIZE` | Primary dimension in **cm**, zero-padded to 3 digits (sorts correctly). | `008`, `010`, `030` |
| `COLOUR` | Readable colour word (any length). | `PURPLE`, `BLACK`, `CORAL` |
| `FINISH` | Readable finish word (any length). | `SILK`, `MATTE`, `SATIN` |

**Colour + Finish = one real spool.** We stock specific filaments ("Purple Silk",
"Black Matte"), so in WooCommerce this is **Size × Filament** (Filament = the spools we
carry), never a colour × finish cross-product.

## Product codes (6 letters)

| Product | Code |
|---|---|
| Atlas Phone Stand | `PHONST` |
| Comet Keychain | `KEYCHN` |
| Luna Tealight Holder | `TEALGT` |
| Nova Pendant Lamp Shade | `PENDNT` |
| Orion Faceted Planter | `PLANTR` |
| Vega Desk Organizer | `ORGNZR` |

## Finish words

`MATTE` · `SATIN` · `SILK` (shiny) · `GLOSS` · `METAL` (metallic) · `TRANS` (translucent) · `BASIC` (standard PLA)

## Colour words (extend as spools are added)

`BLACK` · `WHITE` · `GREY` · `RED` · `ORANGE` · `YELLOW` · `GREEN` · `BLUE` · `NAVY` ·
`PURPLE` · `PINK` · `BROWN` · `BEIGE` · `GOLD` · `SILVER` · `BRONZE` · `CORAL` · `CREAM` · `NATURAL`

> Add new colours/finishes here first, then use them in SKUs — keeps codes consistent.

## The spools we actually stock

_(fill in as filaments are purchased — this is the real inventory the shop offers)_

| Spool (WooCommerce option) | Colour | Finish |
|---|---|---|
| _e.g._ Purple Silk | `PURPLE` | `SILK` |
| _e.g._ Black Matte | `BLACK` | `MATTE` |
