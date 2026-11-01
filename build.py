"""Wrap portfolio.html (an Artifact fragment) into a standalone index.html.

The Artifact platform supplies the document skeleton and a small reset at publish
time; a static host does not. This adds both so the same source works in either
place. Run after editing portfolio.html:  python -I build.py
"""
import pathlib

SRC = pathlib.Path("portfolio.html")
OUT = pathlib.Path("index.html")

DESCRIPTION = (
    "Shakti Prasad Muduli - Chief Information Security Officer at Accesco. "
    "Application and API security, cloud security, penetration testing, "
    "platform engineering and AI automation."
)

RESET = """
/* --- host skeleton reset (supplied by the Artifact platform; added here for static hosting) --- */
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
"""

src = SRC.read_text(encoding="utf-8")

marker = "</style>"
head_src, body_src = src.split(marker, 1)
head_src = head_src.replace("<style>", "<style>" + RESET, 1)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{DESCRIPTION}">
<meta property="og:type" content="profile">
<meta property="og:title" content="Shakti Prasad Muduli">
<meta property="og:description" content="{DESCRIPTION}">
<meta property="og:image" content="assets/shakti.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/shakti.png">
{head_src.strip()}
{marker}
</head>
<body>
{body_src.strip()}
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print(f"wrote {OUT} ({len(html):,} bytes)")
