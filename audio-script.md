# Aster Reads — voice script

Every line in this document is **one generation → one file**. Paste the text, export, name the file exactly as shown.

---

## Read this first: two tiers

**Tier A — record by hand.** About six minutes on a phone, in a quiet room. The 23 blending clips.

Blending is the skill the whole app exists to teach, and it is the one thing text-to-speech gets wrong in a way that matters. A synthesised "s — a — t" comes out as three evenly-stressed fragments with the wrong rhythm; a person saying it stretches the first sound, leans into the word, and the child hears the word *emerge*. That difference is the lesson.

**Tier B — VoiceWave.** Everything else: instructions, praise, corrections, letter sounds, whole words, the little book. Her cloned voice is perfect for this, and it is what makes the app feel like her sitting next to him.

If it turns out she is happy to sit for twenty minutes instead of six, ask her to do the 26 letter sounds too — they will beat the TTS versions, especially the vowels.

---

## Conventions

- **Folder:** everything in `aster-reads/audio/`, flat, no subfolders.
- **Format:** `.wav` preferred (export WAV), `.mp3` at 192 kbps or better is fine. Tell me which you used.
- **Naming:** exactly as written — lowercase, underscore, no spaces.
- **Voice settings:** pick one voice, one emotion preset (warm / neutral — *not* excited), and keep both for every batch. Do not re-clone halfway through or the app will audibly change personality between screens.
- **Sample rate:** 44.1 kHz mono if it offers a choice.

## Where pauses help, and where they don't

Use `[PAUSE:x]` where a pause is part of **how a sentence is said** — the beat before "Good night!", the space before a question lands.

Do **not** put pauses inside single words, and don't build a pause into a clip that the app will follow with something else. The app inserts its own silence between clips, and it needs to *vary* that silence: wide gaps when Aster is new to blending, tighter as he speeds up. A pause baked into the file can't be tightened later.

That is also why the blending clips are per-word recordings rather than one giant file — I control the rhythm in code.

---

# Tier A — record these by hand

One take per word, six minutes total. Say the sounds slowly, with a clear gap, then the whole word. Keep your voice low and warm — this is a game, not a test.

Read it like this: **"sss — a — t … sat."** Stretch the first sound, leave about half a second between sounds, then say the word at normal speed.

| File | Say this |
| --- | --- |
| `blend_ant` | a — n — t … ant |
| `blend_sat` | s — a — t … sat |
| `blend_mat` | m — a — t … mat |
| `blend_man` | m — a — n … man |
| `blend_map` | m — a — p … map |
| `blend_pan` | p — a — n … pan |
| `blend_pin` | p — i — n … pin |
| `blend_tap` | t — a — p … tap |
| `blend_nap` | n — a — p … nap |
| `blend_dog` | d — o — g … dog |
| `blend_cat` | c — a — t … cat |
| `blend_tin` | t — i — n … tin |
| `blend_sip` | s — i — p … sip |
| `blend_mad` | m — a — d … mad |
| `blend_sad` | s — a — d … sad |
| `blend_dad` | d — a — d … dad |
| `blend_dig` | d — i — g … dig |
| `blend_dot` | d — o — t … dot |
| `blend_cot` | c — o — t … cot |
| `blend_cap` | c — a — p … cap |
| `blend_kid` | k — i — d … kid |
| `blend_mop` | m — o — p … mop |
| `blend_pot` | p — o — t … pot |

Save as `blend_<word>.wav`.

**Optional, if she has two more minutes:** the five short vowels and the six stop consonants, spoken plainly.

| File | Say this |
| --- | --- |
| `ph_a` | a (as in cat) |
| `ph_e` | e (as in bed) |
| `ph_i` | i (as in pig) |
| `ph_o` | o (as in hot) |
| `ph_u` | u (as in sun) |
| `ph_b` | b (just the puff, no "uh") |
| `ph_d` | d |
| `ph_g` | g (as in gum) |
| `ph_p` | p |
| `ph_t` | t |
| `ph_k` | k |

---

# Tier B, batch 1 — the playable set

Generate these first. With batch 1 plus Tier A you have everything needed for the first two games.

## Letter sounds

| File | Paste this | Note |
| --- | --- | --- |
| `ph_s` | ssssss | |
| `ph_m` | mmmmmm | |
| `ph_n` | nnnnnn | |
| `ph_a` | at | ⚠ trim to the vowel only |
| `ph_i` | it | ⚠ trim to the vowel only |
| `ph_o` | on | ⚠ trim to the vowel only |
| `ph_t` | taaa | ⚠ trim to the consonant only |
| `ph_p` | paaa | ⚠ trim |
| `ph_d` | daaa | ⚠ trim |
| `ph_g` | gaaa | ⚠ trim |
| `ph_c` | kaaa | ⚠ trim |
| `ph_k` | kaaa | ⚠ trim — same sound as `ph_c`, generate once and save twice |

**How to trim:** VoiceWave's editor has split and delete. For the consonants, keep roughly the first 120 ms (the release) and cut the vowel tail. For the vowels, keep the vowel and cut the final consonant. If a trim sounds clipped or unnatural, the hand-recorded version above is better than a bad trim — use it.

## Note on the letter sounds

`ph_c` and `ph_k` are the same sound. Generate `kaaa` once, export it as both filenames.

## Words

Say each one warmly, as if pointing at a picture. A slight smile, not sing-song.

| File | Paste this |
| --- | --- |
| `word_ant` | ant |
| `word_sat` | sat |
| `word_mat` | mat |
| `word_man` | man |
| `word_map` | map |
| `word_pan` | pan |
| `word_pin` | pin |
| `word_tap` | tap |
| `word_nap` | nap |
| `word_dog` | dog |
| `word_cat` | cat |

If a single word comes out with a rising, questioning tone, add a full stop and regenerate, or try it as `cat.` on its own line. TTS engines are oddly bad at one-word utterances.

## Instructions and navigation

| File | Paste this |
| --- | --- |
| `ui_welcome` | Hi Aster. [PAUSE:0.6] Ready to play with sounds? |
| `ui_ready` | Tap the green button. [PAUSE:0.4] I'll wait. |
| `ui_listen` | Listen. |
| `ui_again` | Hear it again. |
| `q_which_starts` | Which one starts with... |
| `ui_blend_intro` | Listen to the sounds. [PAUSE:0.5] Then find the picture. |
| `ui_this_is` | This one is... |
| `ui_lets_try` | Let's do this one together. [PAUSE:0.6] |
| `ui_hint` | Here's a hint. |
| `ui_end` | That's it for today. [PAUSE:0.5] You did really well, Aster. |
| `ui_gate` | Grown-ups only. [PAUSE:0.5] Hold the button. |

`q_which_starts` deliberately trails off — the app plays the letter sound immediately after it, so together they say *"Which one starts with… sss."*

## Praise — vary these, never repeat twice in a row

| File | Paste this |
| --- | --- |
| `praise_1` | That's it! |
| `praise_2` | Yes! You heard it. |
| `praise_3` | You got it, Aster. |
| `praise_4` | Nice listening. |
| `praise_5` | That's the one. |
| `praise_6` | Look at you go. |
| `praise_7` | Mm. Perfect. |
| `praise_8` | You found it. |

## Try again — never "wrong", never a buzzer

| File | Paste this |
| --- | --- |
| `try_1` | Not quite. [PAUSE:0.5] Let's listen again. |
| `try_2` | Close. [PAUSE:0.4] Try once more. |
| `try_3` | Hmm. [PAUSE:0.5] Listen carefully. |
| `try_4` | That one's tricky. [PAUSE:0.4] One more try. |
| `try_5` | Almost. [PAUSE:0.4] You're nearly there. |
| `try_6` | Let's hear it again. [PAUSE:0.5] Then you pick. |

---

# Tier B, batch 2 — the rest of the word set and the book

## More words

| File | Paste this |
| --- | --- |
| `word_tin` | tin |
| `word_sip` | sip |
| `word_mad` | mad |
| `word_sad` | sad |
| `word_dad` | dad |
| `word_dig` | dig |
| `word_dot` | dot |
| `word_cot` | cot |
| `word_cap` | cap |
| `word_kid` | kid |
| `word_mop` | mop |
| `word_pot` | pot |

## "Cat and Ant" — read-along book

This is the reward at the end of the ladder: a real book he can decode. Slow it down, and let the full stops land.

| File | Paste this |
| --- | --- |
| `book_title` | Cat and Ant. [PAUSE:0.8] Read it with me. |
| `book_p1` | Cat. |
| `book_p2` | Cat sat. |
| `book_p3` | Cat sat on a mat. |
| `book_p4` | Ant! |
| `book_p5` | Ant sat on the mat. |
| `book_p6` | Cat and ant. |
| `book_p7` | Cat! [PAUSE:0.5] Ant is sad. |
| `book_p8` | Cat did nap. [PAUSE:0.5] Ant did nap. [PAUSE:0.8] Good night! |

## Two more instructions

| File | Paste this |
| --- | --- |
| `ui_slow` | Let's go slowly. |
| `ui_read_to_me` | I'll read it. [PAUSE:0.4] You follow with your finger. |

---

# Tier B, batch 3 — the rest of the alphabet

Not needed for the first version. Generate when the first two games are working and he is ready for more letters.

## Remaining letter sounds

| File | Paste this | Note |
| --- | --- | --- |
| `ph_r` | rrrrrr | |
| `ph_h` | hhhhhh | |
| `ph_f` | ffffff | |
| `ph_l` | llllll | |
| `ph_v` | vvvvvv | |
| `ph_z` | zzzzzz | |
| `ph_j` | jjjjjj | check it isn't "jay-jay-jay" |
| `ph_e` | egg | ⚠ trim to the vowel only |
| `ph_u` | up | ⚠ trim to the vowel only |
| `ph_b` | baaa | ⚠ trim |
| `ph_w` | wooo | ⚠ trim |
| `ph_x` | eks | ⚠ trim to "ks" |
| `ph_y` | yeee | ⚠ trim |
| `ph_q` | kooo | ⚠ trim to "kw" |

## Letter names

Phonetic spellings, so the engine says the name and not a word. (Names come *after* sounds — knowing "aitch" doesn't help him read "hat".)

| File | Paste this |
| --- | --- |
| `name_a` | ay |
| `name_b` | bee |
| `name_c` | see |
| `name_d` | dee |
| `name_e` | ee |
| `name_f` | eff |
| `name_g` | jee |
| `name_h` | aitch |
| `name_i` | eye |
| `name_j` | jay |
| `name_k` | kay |
| `name_l` | ell |
| `name_m` | em |
| `name_n` | en |
| `name_o` | oh |
| `name_p` | pee |
| `name_q` | cue |
| `name_r` | ar |
| `name_s` | ess |
| `name_t` | tee |
| `name_u` | you |
| `name_v` | vee |
| `name_w` | double-you |
| `name_x` | ex |
| `name_y` | why |
| `name_z` | zee |

## Two more instructions

| File | Paste this |
| --- | --- |
| `ui_trace` | Start at the green dot. [PAUSE:0.4] Go around, and down. |
| `q_which_rhymes` | Which one rhymes with... |

---

# Quality check before you hand them back

Listen to every clip once. You are listening for four things:

1. **A stray "uh" on a consonant.** If a letter sound comes out as "buh" or "tuh", it is unusable — that schwa is exactly what makes blending fail. Re-trim, or use the hand-recorded version.
2. **Question intonation on a single word.** "cat?" instead of "cat." Regenerate with a full stop.
3. **A different voice between batches.** Play the first and last clip back to back.
4. **Clipped starts or ends.** The app adds a tiny fade, but it cannot invent a missing phoneme.

Then drop the whole folder in `aster-reads/audio/` and run:

```
python tools/check_audio.py
```

It will tell you exactly which files are missing and which are suspiciously short.
