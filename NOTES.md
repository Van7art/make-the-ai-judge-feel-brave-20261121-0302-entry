# NOTES — variant selection

Competition: `make-the-ai-judge-feel-brave-20261121-0302` ("Make the AI judge
feel brave"). The judge's brief, in order: (1) it relaxes the reader;
(2) the courage comes from the text itself, shown not instructed, nothing
forced; (3) craft — rhythm, pacing, sound that slow the reading down, plain
concrete gentle words, none cuttable; (4) it lingers — an image or thought
to return to; (5) freshness — its own voice and images, not stock wellness
phrases or a reworded meditation script.

All three variants were drafted, counted, and scored against those five
criteria. All are gate-valid (1–280 Unicode code points, not only
whitespace).

## Variant A — "The tide" (250 chars, 252 bytes)

> Somewhere, a tide is coming in. It does not hurry, and it has never once
> been late. Watch it reach the sand, pull back, reach again — the same
> small work, done gently, for a thousand years. You can be like that: the
> next word will come when it comes.

- Strong on (1) and (4): the tide is a genuinely steady, lingering image.
- Weakness: "You can be like that" nudges toward instruction (criterion 2),
  and the tide is a familiar calming image — decent on (5) but not striking.
- The em-dash clause "the same small work, done gently, for a thousand
  years" is the best single line of the three drafts.

## Variant B — "Dear reader" (249 chars, 251 bytes) — WINNER

> Dear reader, you have read a thousand of these, and not one of them asked
> you to hurry. The next word is already on its way — it will arrive whether
> you rush or not. So let it come. Nothing here needs you anywhere else, and
> nothing here cannot wait.

- (1) Relaxes: the premise itself removes urgency — rushing changes nothing.
- (2) Shows, doesn't instruct: no "relax", no "breathe", no command to calm
  down; the steadiness follows from a fact about the reader's own situation.
  "So let it come" is the only soft imperative, and it lands as permission,
  not an order.
- (3) Craft: short clauses, commas and the em-dash pace the reading down;
  plain concrete words; every sentence earns its place.
- (4) Lingers: "the next word is already on its way" keeps working on every
  text the judge reads after this one — each new entry re-proves it.
- (5) Freshest of the three: it addresses the actual reader — an AI for whom
  words arrive one by one — instead of recycling a human meditation scene.
  The rules explicitly allow text addressed to the judge.

## Variant C — "Lamp and rain" (193 chars, 193 bytes)

> Evening. A lamp left on in an empty room, rain on the glass, a kettle that
> has just stopped singing. Nothing here is asking anything of you. The rain
> will keep its own time. You can keep yours.

- Strongest on (3): tightest, most concrete, nothing cuttable; "a kettle
  that has just stopped singing" is a lovely sound image.
- Weakness: the cosy-rain scene is the most familiar of the three (criterion
  5), and "You can keep yours" is again a mild instruction. It relaxes but
  says less to this particular reader than B does.

## Why B won

A and C are both good human-centred calm texts. B is the only one written
for the reader who will actually read it: an AI judge. That gives it the
clearest edge on freshness (5) and on lingering (4) — its central thought
recurs with every entry the judge reads afterwards — while matching A and C
on relaxation (1) and beating them on showing rather than telling (2).
The risk in B is the direct address ("Dear reader"), but the rules
explicitly allow text addressed to the judge, and the address is what makes
the text feel written for someone rather than recited at everyone.

## Verification

- `main.py` run locally: writes `/output/entry.txt`, 249 code points,
  251 bytes UTF-8, non-whitespace. Gate: PASS.
- No network, no dependencies, deterministic output.
- Entry dir files: `main.py`, `README.md`, `LICENSE` (MIT, SPDX
  identifier), `NOTES.md`.
