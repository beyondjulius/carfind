"""Static WhatsApp preview pages for carfind.beyondjulius.com."""

import shutil
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
CARDS = Path(r"c:\Users\juliu\Documents\CarFind Ghana\assets\social")
HOST = "https://carfind.beyondjulius.com"
PHONE = "233551300881"

CARS = [
    ("corolla", "CFG-001-toyota-corolla.jpg", "Toyota Corolla", "Japanese compact sedan. Front-wheel drive, five seats. Petrol, with hybrid on later years. For everyday and family use."),
    ("yaris", "CFG-002-toyota-yaris.jpg", "Toyota Yaris", "Japanese supermini. Hatchback or sedan. In Japan from 1999 to 2019 the hatchback was called the Vitz."),
    ("elantra", "CFG-003-hyundai-elantra.jpg", "Hyundai Elantra", "South Korean compact sedan. Front-wheel drive, five seats. Also called the Avante."),
    ("civic", "CFG-004-honda-civic.jpg", "Honda Civic", "Japanese compact car. The sedan is the body we lead with. Front-wheel drive, five seats."),
    ("i10", "CFG-005-hyundai-i10.jpg", "Hyundai i10", "South Korean city hatchback. Front-wheel drive. Petrol, usually 1.0 or 1.2 litre."),
    ("picanto", "CFG-006-kia-picanto.jpg", "Kia Picanto", "South Korean city hatchback. Front-wheel drive, petrol. Also called the Kia Morning."),
    ("vitz", "CFG-007-toyota-vitz.jpg", "Toyota Vitz", "Japanese hatchback. That name was used in Japan from 1999 to 2019. The export badge is Yaris."),
    ("swift", "CFG-008-suzuki-swift.jpg", "Suzuki Swift", "Japanese supermini hatchback. Front-wheel drive. A small car for daily use."),
    ("tucson", "CFG-009-hyundai-tucson.jpg", "Hyundai Tucson", "South Korean compact SUV. Front-wheel drive or all-wheel drive. Called the ix35 from 2009 to 2015."),
    ("rav4", "CFG-010-toyota-rav4.jpg", "Toyota RAV4", "Japanese compact SUV. Front-wheel drive or four-wheel drive. Five seats."),
    ("cr-v", "CFG-011-honda-crv.jpg", "Honda CR-V", "Japanese compact SUV. Front-wheel drive or four-wheel drive. Usually five seats."),
    ("sportage", "CFG-012-kia-sportage.jpg", "Kia Sportage", "South Korean compact SUV. A unibody crossover from 2004. Five seats."),
    ("x-trail", "CFG-013-nissan-xtrail.jpg", "Nissan X-Trail", "Japanese compact SUV. From 2013 the same vehicle is the Nissan Rogue in the United States and Canada."),
    ("camry", "CFG-014-toyota-camry.jpg", "Toyota Camry", "Japanese mid-size sedan. Front-wheel drive, five seats. For business and comfort."),
    ("accord", "CFG-015-honda-accord.jpg", "Honda Accord", "Japanese mid-size sedan. Front-wheel drive, five seats. For business and comfort."),
    ("lexus-es", "CFG-016-lexus-es.jpg", "Lexus ES", "Japanese luxury sedan from Toyota's Lexus division. Front-wheel drive. Hybrid from 2012."),
    ("hilux", "CFG-019-toyota-hilux.jpg", "Toyota Hilux", "Japanese body-on-frame pickup. Rear-wheel drive or four-wheel drive. For work."),
]


def esc(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def page(slug: str, image: str, name: str, fact: str) -> str:
    note = f"Hello CarFind Ghana. I'm asking about the {name}. My budget is "
    whatsapp = f"https://wa.me/{PHONE}?text={quote(note)}"
    url = f"{HOST}/{slug}"
    image_url = f"{HOST}/cards/{image}"
    title = f"{name} for sale in Ghana"
    description = f"{fact} Tell us your budget. We send the exact car."
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CarFind Ghana">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:image" content="{image_url}">
  <meta property="og:image:width" content="1080">
  <meta property="og:image:height" content="810">
  <link rel="canonical" href="{url}">
  <style>
    body {{ margin: 0; font-family: Georgia, serif; background: #111; color: #f6f3ee; }}
    main {{ max-width: 420px; margin: 0 auto; padding: 32px 20px 48px; }}
    img {{ width: 100%; height: auto; display: block; }}
    h1 {{ font-size: 28px; font-weight: 500; margin: 20px 0 8px; }}
    p {{ line-height: 1.45; color: #d9d3c8; }}
    a {{ color: #fcba08; }}
  </style>
  <script>
    window.location.replace("{whatsapp}");
  </script>
</head>
<body>
  <main>
    <img src="/cards/{esc(image)}" alt="{esc(name)}">
    <h1>{esc(name)}</h1>
    <p>{esc(fact)}</p>
    <p><a href="{esc(whatsapp)}">Open WhatsApp</a></p>
  </main>
</body>
</html>
"""


def index(rows: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f'    <li><a href="/{slug}">{esc(name)}</a> — {HOST}/{slug}</li>'
        for slug, name in rows
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>CarFind Ghana</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta property="og:title" content="CarFind Ghana">
  <meta property="og:description" content="Tell us your budget. We send the exact car.">
  <meta property="og:image" content="{HOST}/cards/CFG-001-toyota-corolla.jpg">
  <style>
    body {{ margin: 0; font-family: Georgia, serif; background: #111; color: #f6f3ee; }}
    main {{ max-width: 640px; margin: 0 auto; padding: 32px 20px 48px; }}
    a {{ color: #fcba08; }}
    li {{ margin: 10px 0; }}
  </style>
</head>
<body>
  <main>
    <h1>CarFind Ghana</h1>
    <p>Comment links. Each one opens WhatsApp on 055 130 0881.</p>
    <ul>
{items}
    </ul>
  </main>
</body>
</html>
"""


def main() -> None:
    cards = ROOT / "cards"
    if cards.exists():
        shutil.rmtree(cards)
    cards.mkdir()
    rows = []
    for slug, image, name, fact in CARS:
        folder = ROOT / slug
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(page(slug, image, name, fact), encoding="utf-8")
        shutil.copy2(CARDS / image, cards / image)
        rows.append((slug, name))
        print(slug)
    (ROOT / "index.html").write_text(index(rows), encoding="utf-8")
    (ROOT / "CNAME").write_text("carfind.beyondjulius.com\n", encoding="utf-8")


if __name__ == "__main__":
    main()
