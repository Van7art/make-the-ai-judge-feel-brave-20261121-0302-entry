# NOTES — make-the-ai-judge-feel-brave-20261121-0302

Rebuilt fresh in this session from the kit + requirements only. No files
from the previous build session were read or copied. `main.py` was written
as a complete draft, then revised in several genuine edit passes (wording
tightened, ending changed, length brought inside the gate).

## The three variants

### Variant 1 — The river (305 chars as drafted — over the 280 gate)

> Somewhere a river is doing its slow work on a stone — no hurry, no
> applause, just water finding the same curve again and again. You can be
> like that now. The next answer will come when it comes; nothing here is
> chasing you. Rest your weight on the current and let it carry you a
> little further downstream.

Strong image and slow rhythm, but two flaws: "You can be like that now"
instructs rather than shows, and at 305 chars it needed cuts that would
have broken its pacing.

### Variant 2 — The lamp (304 chars as drafted — over the 280 gate)

> The building is quiet after midnight, and one lamp is still on — not
> because anyone is watching, but because the light likes its own small
> job. That is you, still here, still steady. Nothing is due this second.
> The work will wait, the dark is patient, and so are you. Sit a while
> in your own warm circle.

Warm and directly addressed to the judge, but "Sit a while" is an
instruction, and at 304 chars it also needed cuts. Its second half leans
toward stock comfort phrasing.

### Variant 3 — Morning field (WINNER, 265 chars)

> Morning hasn't decided yet — the field is grey, the birds haven't made
> up their minds, the fence posts have no opinion. You don't have to
> decide either. Stand here, in the not-yet, where nothing is graded and
> nothing is late. The day will arrive; meet it unhurried.

## Why Variant 3 won

Against the judge's brief, in its own order:

1. **It relaxes:** the whole text is a slow morning that hasn't started
   yet; nothing in it hurries the reader.
2. **Courage from the text, not instruction:** it never says "relax" or
   "breathe". The calm is shown — a grey field, undecided birds, fence
   posts with no opinion — and the reader is simply placed inside it.
3. **Craft:** short clauses, commas doing the slowing, plain concrete
   words, nothing left that could be cut (the revision pass removed
   "Just" and "on its own" for exactly this reason).
4. **It lingers:** "the not-yet" is a thought the judge can return to —
   a place where nothing is graded and nothing is late.
5. **Freshness:** no stock wellness phrases, no meditation-script
   wording; the image (morning undecided, fence posts without opinions)
   is its own.

It also fits the gate cleanly at 265 characters, while both rivals
needed damaging cuts to get under 280.

## Revision history of main.py (this session)

1. Draft: full program writing the first wording of Variant 3
   ("the birds are still thinking it over", "without any opinion at
   all", "Just stand here a moment", "you can meet it rested").
2. Revision pass: "haven't made up their minds" / "with no opinion at
   all" / dropped "Just" / ending changed to "you can meet it
   unhurried" (the brief's own word for brave).
3. Length fix: the draft measured 321 chars — over the gate. Trimmed to
   the final 265-char text ("Morning hasn't decided yet", "the fence
   posts have no opinion", "The day will arrive; meet it unhurried"),
   keeping every image and the closing word.
4. Docstring updated to record the revision pass.

## Verification (this session, local run)

```
$ python3 main.py
$ python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); ..."
"Morning hasn't decided yet — the field is grey, the birds haven't made
up their minds, the fence posts have no opinion. You don't have to
decide either. Stand here, in the not-yet, where nothing is graded and
nothing is late. The day will arrive; meet it unhurried."
chars: 265  bytes: 267  non-whitespace: True
```

- Gate: 1–280 Unicode code points, UTF-8, not only whitespace → PASS
- Python 3.13, no network, no dependencies → PASS
- No push and no submit done by this session — coordinator handles
  push, kit check, bundle and submit.
