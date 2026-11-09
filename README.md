# Aster Reads

A reading app for Aster, in his mother's voice.

Two games and a book, built around the six letters he will learn first.

**Recorder, live:** <https://appleknife.github.io/aster-reads/recorder/> — open it on a
laptop or an iPad, no install, nothing uploaded.

## Start here

1. **[recorder/](recorder/index.html)** - the recording studio for Aster's mother. It
   shows her one line at a time, records it in the browser, trims it, and hands back
   a zip of correctly named `.wav` files.
2. **[audio-script.md](audio-script.md)** - the same 136 lines as a printable sheet,
   with the exact filename for each clip and what to paste into VoiceWave.
3. **[art-plan.md](art-plan.md)** - what pictures the app needs, what the pictures
   have to be (stricter than you would guess), and what to buy versus take for free.

## Recording

**<https://appleknife.github.io/aster-reads/recorder/>** — this is the easy path. It is
served over HTTPS, so the microphone works on an iPad or a phone as well as a laptop.

To run it locally instead, from the project root:

```
powershell -NoProfile -ExecutionPolicy Bypass -File serve.ps1
```

then open <http://localhost:8777/aster-reads/recorder/>. It needs a real origin -
the microphone is blocked on `file://`.

The recorder only asks her for the **34 clips that need a human**: the 23 blends and
the 11 letter sounds a synthesiser cannot produce cleanly. The other 102 are whole
words and whole sentences, which VoiceWave does well in her cloned voice. She can
switch to "all 136" if she would rather do the lot.

### The rule behind the split

TTS is safe for a **whole word** or a **whole sentence**. It is unsafe for a
**fragment of a word** - an isolated phoneme, a stretched consonant, a trimmed
burst. A synthesiser puts a schwa on a lone consonant (`b` becomes "buh"), and that
schwa is precisely what makes blending fail: "buh-a-tuh" does not sound like "bat".
The blends are also the one clip that *models the skill*, so getting the rhythm
wrong teaches the wrong thing.

## The audio contract

- Flat folder: `audio/`
- Lowercase filenames, exactly as written in the script
- `.wav` (preferred) or `.mp3`
- One clip per generation, same voice preset throughout

When the folder is populated:

```
python tools/check_audio.py
```

It reports what is missing by batch, flags clips that are clipped or suspiciously
short, and writes `audio/manifest.json` for the app to read.

## Why these design choices

Phonemic awareness is the one thing apps demonstrably move, and a meta-analysis
found computer programs and parents work as well as teachers for it - no
significant difference. The effect size for literacy apps is around 0.35, real but
modest, and roughly half that of parent-led work. Five minutes a day is the sweet
spot; both more and less do worse. Hence: short sessions, a hard stop, and a
parent voice doing the talking.

## Status

- [x] research
- [x] voice script and audio contract
- [x] art plan
- [ ] audio generated
- [ ] app built
