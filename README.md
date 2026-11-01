# Portfolio — Shakti Prasad Muduli

Personal portfolio site. Static, single page, no build step and no dependencies.

**Live:** enable GitHub Pages on this repo (Settings → Pages → Branch: `main`, folder `/`).

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The site. Generated — edit `portfolio.html` instead. |
| `portfolio.html` | Source. A fragment (no `<head>`/`<body>`), so it also publishes straight to a Claude Artifact. |
| `build.py` | Wraps `portfolio.html` in a document skeleton and reset to produce `index.html`. |
| `assets/shakti.png` | Portrait cutout, background removed. |

## Editing

Change `portfolio.html`, then regenerate:

```
python build.py
```

Preview locally:

```
python -m http.server 8777
```

## Notes

- Fonts come from Google Fonts (IBM Plex Sans / Sans Condensed / Mono). Everything else is inline.
- Light and dark themes are both defined, following the visitor's system setting, with a manual toggle in the nav that persists in `localStorage`.
- Colour and type live in the `:root` token block at the top of the `<style>`; change tokens there rather than individual rules.
