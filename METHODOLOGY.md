# Methodology, and what is weak about it

Every dataset has judgement calls in it. This one writes them down.

---

## 0. Scope

**This dataset covers Monk 3 through 9 — medium to deep skin.** It does **not** cover Monk 1–2 or Monk 10.

**Depth and undertone are physical properties, not ethnic ones.** The range takes in most South Asian skin and a great deal of Middle Eastern, North African, Latin American, Southeast Asian and Black skin. It was built in India because that is where the gap was most visible to the author. **Nothing in the data is India-specific** — the India-specific material (occasion vocabulary: haldi, mehendi, sangeet) lives on the website, not here.

## 1. How the eight tones were fixed

The tone swatches are the **published Monk Skin Tone Scale** values for six of the eight. Monk was released by Ellis Monk with Google in 2023, with ten shades, six of them covering medium and deep skin — built explicitly because earlier scales under-represented darker skin.

**Two tones were added:**

| Tone | Why |
|---|---|
| **Amber** `#BB9D75` | The Intermediate band sits empty on most charts, and a large share of medium skin falls there |
| **Cacao** `#3A312A` | The deepest swatch on most charts is not the deepest skin |

**Fitzpatrick values are included for orientation only.** That scale was created in 1975 to predict how skin responds to UV — a burn-risk instrument, not a description of appearance. In its original form it did not include darker skin at all; types V and VI were appended later. It still gives four categories to light skin and two to everything else. **Do not use it to choose colours.**

## 2. How the palettes were derived

Each tone carries three undertone variants — **cool, warm, neutral** — and each variant is assigned a **12-season** classification (Cool Summer, Warm Autumn, Deep Winter, and so on). The eight colours follow from the season, constrained by depth.

**Composition rule:** each palette holds a spread across depth so that pairing is possible within it — at least two colours dark enough to anchor an outfit, and at least two saturated enough to lead one.

### Season distribution across the 24 variants

**Autumn 11 · Winter 6 · Summer 5 · Spring 2.**

That skew is the single most consequential fact in the dataset, and it produces a finding worth stating plainly:

> 🔴 **Black is a Winter neutral. It is correct for 6 of the 24 variants.** For the 11 Autumn variants, chocolate and soft charcoal do the job better.

## 3. Season neutrals

Neutrals are **not universal**, and using the wrong family is the most common way a correct palette still looks wrong. Spring takes warm ivory and camel; Summer takes dove grey and soft navy; Autumn takes chocolate, camel and olive; Winter takes black, charcoal and navy.

**Pairing rule:** a neutral must differ from the colour it sits against by **at least 12 points of lightness**, or it stops reading as a deliberate contrast. Across the 24 palettes, **15 neutral/colour combinations fail that test** and are excluded — the neutral is not dropped, because it remains correct for the season and works against other colours in the same palette.

⚠️ **These neutral hex values are the least validated numbers in the dataset.** They were chosen to match published season descriptions, **not measured from garments.** If you have measured values, they are the most useful contribution you could make.

## 4. The pairing taxonomy

Two axes, both computed from the colours themselves: **lightness gap** and **saturation of the stronger colour**. Crossed, they give four terms — Bold, Classic, Rich, Suave.

### 🔴 Ranking is relative, and that is deliberate

Fixed thresholds were tried first **and failed twice.**

**Attempt one — global cut-offs.** Summer palettes are muted by definition, so they scored **zero Bold and zero Rich**, and 2 of 24 variants returned a single name across every pairing.

**Attempt two — one median across both palette-internal and neutral pairings.** Season neutrals include pure white, black and chocolate, whose lightness gaps are enormous. **84% of neutral pairs landed in the high-contrast half and 53% of internal pairs collapsed into Rich** — the label was reporting which list a pair came from rather than anything about the pair. Nine of 24 variants ended up with no Bold pairing inside their own palette.

**Both blocks are now ranked separately, and always within the wearer's own palette.** Result across 681 pairings: Rich 30% · Bold 28% · Classic 23% · Suave 19%, with all four terms present in all four season families.

**Consequence:** the same two colours carry different names for different people. Navy and Dusty Rose is **Bold** on a Soft Summer palette and **Rich** on a Cool Summer palette. That is the system working, not a bug.

---

## 5. Known weaknesses

**🔴 Amber overlaps Golden by 7 of 8 colours.** They also share a season, so identical neutrals and identical pairing behaviour. Amber is distinguishable on a chart and close to indistinguishable in a wardrobe. Amber was added because the Intermediate band was empty — a classification argument that the palette does not yet fully earn. **Unresolved.**

**Espresso and Cacao share 5 of 8**, and Caramel and Mocha share 4. Those are defensible for adjacent depths; the Amber case is not.

**Names are not unique to hex values.** Five names carry more than one hex across the system — Deep Olive appears at three values, and Camel, Charcoal, Chocolate and Warm Ivory at two each, because neutrals are season-tuned. **Match on hex, not on name.** One value, `#F5E9D0`, carries two names: *Warm Cream* as a palette colour and *Warm Ivory* as a neutral.

**Undertone assignment is not measured here.** The dataset provides the palettes; deciding which undertone someone is remains a judgement, and the production tool makes it from self-reported vein and jewellery observation rather than instrumentation.

**No spectrophotometry anywhere.** These are specified values. Real fabric will differ by dye lot, weave and finish.

---

## 6. Corrections

If something here is wrong, opening an issue is genuinely welcome — particularly measured values, or evidence that a tone at a depth or undertone this handles badly.

**The Amber overlap is the known open problem.** A palette that keeps Amber between its neighbours rather than duplicating Golden would be the single most valuable fix.
