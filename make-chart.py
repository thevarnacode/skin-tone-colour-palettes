#!/usr/bin/env python3
"""
Regenerate tone-chart.png from data/tones.json.

    python3 tools/make-chart.py

Requires Pillow.  Fonts: Lora (serif) and Lato (sans) — substitute freely,
the paths are the only thing to change.

Why this exists: the chart must never be hand-edited. If a tone value ever
changes in tones.json, run this and the image follows. Any chart that cannot
be regenerated from the data will drift away from it.
"""
from PIL import Image, ImageDraw, ImageFont
import json, os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TONES = json.load(open(os.path.join(HERE, 'data/tones.json'), encoding='utf-8'))

# Tokens — keep in step with the brand system
BG, INK, MUT, RULE = '#F2EDE4', '#171412', '#71685E', '#D6CCBD'
LORA = '/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf'
LATO = '/usr/share/fonts/truetype/lato/Lato-Regular.ttf'
LATO_B = '/usr/share/fonts/truetype/lato/Lato-Semibold.ttf'

S = 2                       # supersample, then LANCZOS down — keeps text crisp
W, H, M = 1600 * S, 900 * S, 112 * S

im = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(im)
F = lambda p, s: ImageFont.truetype(p, s * S)

d.text((M, 96 * S), 'The eight tones', font=F(LORA, 76), fill=INK)
d.text((M, 200 * S), 'Indian skin, sorted by depth and undertone — not "wheatish".',
       font=F(LATO, 30), fill=MUT)

n, gap = len(TONES), 25 * S
sw = (W - 2 * M - gap * (n - 1)) // n
top, sh = 320 * S, 260 * S

for i, t in enumerate(TONES):
    x = M + i * (sw + gap)
    d.rectangle([x, top, x + sw, top + sh], fill=t['swatch'])   # square corners
    for dy, txt, font, col in (
        (28, t['name'].upper(),              F(LATO_B, 24), INK),
        (66, 'MST %s' % t['monk_skin_tone'], F(LATO, 21),   MUT),
        (102, t['swatch'].upper(),           F(LATO, 19),   MUT)):
        tw = d.textlength(txt, font=font)
        d.text((x + (sw - tw) / 2, top + sh + dy * S), txt, font=font, fill=col)

fy = H - 120 * S
d.rectangle([M, fy, W - M, fy + 2 * S], fill=RULE)
d.text((M, fy + 26 * S), 'varnacode.in', font=F(LATO_B, 24), fill=INK)
cap = 'Six of the eight are Monk Skin Tone Scale values. Amber and Cacao fill gaps it leaves.'
f = F(LATO, 22)
d.text((W - M - d.textlength(cap, font=f), fy + 26 * S), cap, font=f, fill=MUT)

im = im.resize((W // S, H // S), Image.LANCZOS)
im.save(os.path.join(HERE, 'tone-chart-1600x900.png'))
im.resize((800, 450), Image.LANCZOS).save(os.path.join(HERE, 'tone-chart.png'))
print('wrote tone-chart-1600x900.png and tone-chart.png')
