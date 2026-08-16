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

### 🔴 That rule answers only half the question

The test above compares a neutral to **the garment next to it**. It says nothing about the neutral against **the wearer's own depth**, and those are different questions with different answers.

A neutral worn below the waist only has to not fight the top. A neutral worn **near the face** has to clear the face itself — and a camel shirt on Amber skin is **1 point of lightness** away from it. It does not clash; it disappears, and takes the face with it.

Applying the same 12-point threshold to *skin vs neutral* rather than *colour vs neutral*:

> **14 of the 24 variants list at least one season neutral that fails against their own wearer.** Warm Ivory for Ivory-warm (0) and Honey-warm (6), Camel for Amber-warm (1), Dove Grey and Cool Taupe for Amber-cool, Charcoal (8) and Deep Navy (10) for Espresso, and Black (9), Charcoal (1) and Deep Navy (0) for Cacao.

**Every variant retains at least one**, so this splits a palette's neutrals into *near the face* and *below the waist* — it never leaves someone with none.

⚠️ **This omission was live in the production tool from launch until 14 Aug 2026.** It is recorded here rather than quietly fixed, because anyone building on this data would have inherited it.

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

**✅ The Amber overlap is resolved — 15 Aug 2026.** Amber previously shared **7 of 8 colours with Golden** and produced **all six of the same pairings**, which meant the two tones were distinguishable on a chart and effectively identical in a wardrobe.

**A second and worse problem surfaced while fixing it:** Amber's palette contained **Camel `#C19A6B` at lightness 59, against Amber skin at 60** — a one-point gap. The palette listed as one of Amber's colours a shade that vanishes against Amber's own face, contradicting §3's own rule.

Three substitutions, chosen so Amber sits between its neighbours rather than shadowing one:

| Out | In | Reason |
|---|---|---|
| Camel `#C19A6B` L59 | **Sienna `#A0522D`** L40 | Removes the colour that disappears on the wearer |
| Navy `#1B2A4A` L20 | **Aubergine `#4A2545`** L22 | Same anchoring depth, different hue — this is what broke the Golden lookalike |
| Mustard `#C8921A` L44 | **Deep Mustard `#B8860B`** L38 | The intermediate step between Golden's mustard and Caramel's |

| | Before | After |
|---|---|---|
| Colours shared with Golden | 7 of 8 | **4 of 8** |
| Pairings shared with Golden | 6 of 6 | **0 of 6** |
| Colours shared with Caramel | 2 of 8 | **5 of 8** |

⚠️ **This changes the palette for anyone previously classified Amber · warm.** That is deliberate: the prior palette was wrong twice over.

**Espresso and Cacao share 5 of 8**, and Caramel and Mocha share 4. Those are defensible for adjacent depths.

**Names are not unique to hex values.** Five names carry more than one hex across the system — Deep Olive appears at three values, and Camel, Charcoal, Chocolate and Warm Ivory at two each, because neutrals are season-tuned. **Match on hex, not on name.** One value, `#F5E9D0`, carries two names: *Warm Cream* as a palette colour and *Warm Ivory* as a neutral.

**Undertone assignment is not measured here.** The dataset provides the palettes; deciding which undertone someone is remains a judgement, and the production tool makes it from self-reported vein and jewellery observation rather than instrumentation.

**No spectrophotometry anywhere.** These are specified values. Real fabric will differ by dye lot, weave and finish.

---

## 6. Corrections

If something here is wrong, opening an issue is genuinely welcome — particularly measured values, or evidence that a tone at a depth or undertone this handles badly.

**The most useful contributions now are measured values.** Every hex here is specified rather than read off fabric with an instrument — see §3 on the neutrals in particular, which are the least validated numbers in the set.

*The Amber overlap, previously listed here as the open problem, was resolved on 15 Aug 2026. See §5.*
