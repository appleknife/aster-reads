#!/usr/bin/env python3
# Check the Aster Reads voice folder against the script.
#   python tools/check_audio.py           (looks in ../audio)
#   python tools/check_audio.py path/to/audio
# Reports missing files by batch, unexpected files, and durations or levels that
# look wrong. Writes audio/manifest.json for the app. Standard library only.

import json
import os
import struct
import sys
import wave

PHONEMES_B1 = ["s", "a", "t", "m", "n", "i", "p", "o", "d", "g", "c", "k"]
PHONEMES_B3 = ["e", "u", "r", "h", "b", "f", "l", "j", "v", "w", "x", "y", "z", "q"]

WORDS_B1 = ["ant", "sat", "mat", "man", "map", "pan", "pin", "tap", "nap", "dog", "cat"]
WORDS_B2 = ["tin", "sip", "mad", "sad", "dad", "dig", "dot", "cot", "cap", "kid", "mop", "pot"]

UI_B1 = ["ui_welcome", "ui_ready", "ui_listen", "ui_again", "q_which_starts",
         "ui_blend_intro", "ui_this_is", "ui_lets_try", "ui_hint", "ui_end", "ui_gate"]
UI_B2 = ["ui_slow", "ui_read_to_me"]
UI_B3 = ["ui_trace", "q_which_rhymes"]

BOOK = ["book_title"] + ["book_p%d" % i for i in range(1, 9)]
PRAISE = ["praise_%d" % i for i in range(1, 9)]
TRYAGAIN = ["try_%d" % i for i in range(1, 7)]
NAMES = ["name_" + c for c in "abcdefghijklmnopqrstuvwxyz"]

AUDIO_EXT = (".wav", ".mp3", ".m4a", ".ogg", ".flac")


def expected():
    # stem -> batch number, or "A" for hand-recorded
    out = {}
    for s in PHONEMES_B1:
        out["ph_" + s] = 1
    for s in PHONEMES_B3:
        out["ph_" + s] = 3
    for w in WORDS_B1:
        out["word_" + w] = 1
        out["blend_" + w] = "A"
    for w in WORDS_B2:
        out["word_" + w] = 2
        out["blend_" + w] = "A"
    for u in UI_B1:
        out[u] = 1
    for u in UI_B2:
        out[u] = 2
    for u in UI_B3:
        out[u] = 3
    for b in BOOK:
        out[b] = 2
    for p in PRAISE:
        out[p] = 1
    for t in TRYAGAIN:
        out[t] = 1
    for n in NAMES:
        out[n] = 3
    return out


def duration_seconds(path):
    if not path.lower().endswith(".wav"):
        return None
    try:
        with wave.open(path, "rb") as w:
            return w.getnframes() / float(w.getframerate())
    except Exception:
        return None


def peak_level(path):
    if not path.lower().endswith(".wav"):
        return None
    try:
        with wave.open(path, "rb") as w:
            if w.getsampwidth() != 2:
                return None
            frames = w.readframes(w.getnframes())
        peak = 0
        for (v,) in struct.iter_unpack("<h", frames):
            if v < 0:
                v = -v
            if v > peak:
                peak = v
        return peak / 32768.0
    except Exception:
        return None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    default = os.path.join(os.path.dirname(here), "audio")
    root = sys.argv[1] if len(sys.argv) > 1 else default

    if not os.path.isdir(root):
        print("No such folder: %s" % root)
        return 2

    want = expected()
    found = {}
    extras = []
    for name in sorted(os.listdir(root)):
        stem, ext = os.path.splitext(name)
        if ext.lower() not in AUDIO_EXT:
            continue
        if stem in want:
            found[stem] = os.path.join(root, name)
        else:
            extras.append(name)

    missing = {1: [], 2: [], 3: [], "A": []}
    for stem, batch in want.items():
        if stem not in found:
            missing[batch].append(stem)

    total = len(want)
    have = len(found)
    print("")
    print("%d of %d clips present (%d%%)" % (have, total, round(100.0 * have / total)))
    for batch in ("A", 1, 2, 3):
        label = "hand-recorded" if batch == "A" else "batch %d" % batch
        n_want = sum(1 for b in want.values() if b == batch)
        n_have = n_want - len(missing[batch])
        state = "complete" if not missing[batch] else "%d missing" % len(missing[batch])
        print("  %-16s %3d/%-3d  %s" % (label, n_have, n_want, state))

    for batch in ("A", 1, 2, 3):
        if missing[batch]:
            label = "hand-recorded" if batch == "A" else "batch %d" % batch
            print("")
            print("Missing (%s):" % label)
            for stem in missing[batch]:
                print("  " + stem)

    if extras:
        print("")
        print("Not in the script (check the spelling):")
        for name in extras:
            print("  " + name)

    suspicious = []
    for stem in sorted(found):
        path = found[stem]
        d = duration_seconds(path)
        if d is None:
            continue
        peak = peak_level(path)
        flags = []
        if d < 0.12:
            flags.append("very short (%d ms)" % round(d * 1000))
        if d > 12:
            flags.append("very long (%.1f s)" % d)
        if peak is not None and peak < 0.05:
            flags.append("very quiet (peak %d%%)" % round(peak * 100))
        if peak is not None and peak > 0.999:
            flags.append("clipping")
        if flags:
            suspicious.append((stem, "; ".join(flags)))

    if suspicious:
        print("")
        print("Worth a listen:")
        for stem, why in suspicious:
            print("  %-22s %s" % (stem, why))

    clips = {}
    for stem in sorted(found):
        path = found[stem]
        d = duration_seconds(path)
        clips[stem] = {
            "file": os.path.basename(path),
            "batch": want[stem],
            "seconds": round(d, 3) if d else None,
        }
    out = os.path.join(root, "manifest.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump({"count": len(clips), "clips": clips}, fh, indent=2)
    print("")
    print("Wrote " + out)

    return 0 if not missing["A"] else 1


if __name__ == "__main__":
    sys.exit(main())
