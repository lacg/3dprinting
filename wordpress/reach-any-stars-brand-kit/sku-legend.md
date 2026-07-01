# Reach Any Stars — SKU legend

The single source of truth for how product SKUs are coded. Every SKU decodes with
this file; the future print-queue automation reads the same segments.

## Format

```
RAS-<TYPE>-<MODEL>-<SIZE>-<COLOUR>-<FINISH>
```

- Hyphen-delimited → parsed by splitting on `-`, **not** by character position, so
  segments can be any length (no padding, no capacity ceiling).
- Example: `RAS-PLANTR-ORION-010-PURPLE-SILK` = Reach Any Stars · Planter · Orion · 10 cm · Purple · Silk.

### Segments

| Segment | Rule | Examples |
|---|---|---|
| `RAS` | Fixed brand prefix (Reach Any Stars). Always present. | `RAS` |
| `TYPE` | 6-letter item-type code (see table). Type-first groups a family together when sorted. | `PLANTR` |
| `MODEL` | Product model name — unique per product, on-brand (star/constellation). | `ORION`, `LUNA` |
| `SIZE` | Primary dimension in **cm**, zero-padded to 3 digits (sorts correctly). | `008`, `010`, `030` |
| `COLOUR` | Readable colour word (any length). | `PURPLE`, `BLACK`, `CORAL` |
| `FINISH` | Readable finish word (any length). | `SILK`, `MATTE`, `SATIN` |

**Colour + Finish = one real spool.** We stock specific filaments ("Purple Silk",
"Black Matte"), so in WooCommerce this is **Size × Filament** (Filament = the spools we
carry), never a colour × finish cross-product.

## Product codes (TYPE + MODEL)

Item-type code (6 letters) + model name (unique per product, star/constellation).

| Product | Type | Model |
|---|---|---|
| Atlas Phone Stand | `PHONST` | `ATLAS` |
| Comet Keychain | `KEYCHN` | `COMET` |
| Luna Tealight Holder | `TEALGT` | `LUNA` |
| Nova Pendant Lamp Shade | `PENDNT` | `NOVA` |
| Orion Faceted Planter | `PLANTR` | `ORION` |
| Vega Desk Organizer | `ORGNZR` | `VEGA` |

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
