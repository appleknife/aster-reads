# Art and asset plan

What the app needs, what to buy, what to take for free, and the two things that matter more than style.

---

## What the app actually needs

Small. Smaller than you'd think.

| Asset | Count | Notes |
| --- | --- | --- |
| Word pictures | 23 | the whole vocabulary for the first version |
| Mascot poses | 8 | carries every word that isn't an object |
| UI icons | 5 | speaker, replay, back, tick, arrow |
| Background | 1 | near-white, almost invisible |
| Fonts | 2 | letters, plus UI chrome |
| Sound effects | 3 | soft tap, soft ding, page turn |

That's it. This is a 40-asset app, not a 400-asset app. Almost all of the perceived quality comes from the voice, the pacing, and the pictures being *unambiguous* — not from volume.

### The word list, and what each picture has to be

Half of these aren't objects, which is the thing most DIY phonics apps get wrong: you cannot illustrate "sat" with a picture of a mat. You need a character who is *doing* it.

| Word | Picture | Watch out |
| --- | --- | --- |
| ant | object | a single ant, clearly an insect |
| sat | pose | mascot sitting **on something**, so it reads as past tense |
| mat | object | flat rectangle, floor mat |
| man | person | adult, neutral |
| map | object | folded paper map, not a phone map |
| pan | object | frying pan with a handle |
| pin | object | pushpin or safety pin — pick one and never change it |
| tap | pose | mascot tapping something with a finger |
| nap | pose | mascot asleep, "z"s |
| dog | object | one dog, side view |
| cat | object | one cat, side view |
| tin | object | a tin can — **ambiguous name** (see below) |
| sip | pose | mascot drinking through a straw |
| mad | face | mascot cross, not scary |
| sad | face | mascot sad, not distressing |
| dad | person | adult with a child — never shown beside "man" |
| dig | pose | mascot with a spade |
| dot | object | a single bold dot on white |
| cot | object | small bed with sides |
| cap | object | **baseball cap**, not a bottle cap |
| kid | person | child, about Aster's age |
| mop | object | mop with a handle |
| pot | object | cooking pot with two handles — never shown beside "pan" |
| sit | — | **cut "sit" from the word list.** "Sat" and "sit" would share one picture, and a four-year-old cannot tell them apart. |

Two rules fall out of that table, and they are the actual content design:

**1. One picture, one name, no synonyms.** A picture that could be called "mug" or "cup", "hat" or "cap", "can" or "tin" is fine in the *first-sound* game — he taps, he doesn't name it. It is fatal in the *blending* game, where the picture has to be *the* word. So pick the most obvious, most boring name for each drawing, and write it under the picture in the parent's guide.

**2. Never put two confusable pictures in the same three.** Pan and pot. Man and dad. Cat and dog are fine — different sounds, different shapes, easily told apart at thumbnail size. This is a rule the app enforces, not the artist, but the artist needs to know it so the pictures stay distinguishable when they're small.

---

## The two decisions that matter more than style

You said the prototype's art was loosely drawn, and that's fine — style is the least important variable here. These two are the important ones.

### Realism beats charm, for the pictures specifically

There's a consistent finding in the picture-word learning literature: **the more iconic the image, the better young children map a name onto it.** In Ganea, Pickard & DeLoache's study, 15-month-olds extended a newly learned label to the real object from photographs and realistic drawings, but not from cartoons — and neither age group could generalise from the cartoons ([PDF](https://languageandlearninglab.com/wp-content/uploads/Transfer-between-picture-books-and-the-real-world-by-very-young-children.pdf)). A [2018 review](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.00050/full) puts it plainly: if the goal is teaching words, realistic images are best, especially for the youngest children. Three- and four-year-olds seem to know this too — they judge detailed pictures as better symbols ([Yale study](https://minddevlab.yale.edu/sites/default/files/files/Do%20Young%20Children%20Know%20What%20Makes%20A%20picture%20Useful%20To%20Other%20People%20allenetal.pdf)).

So the split I'd draw:

- **Vocabulary pictures** — flat vector, but *realistic in shape and proportion*. A cat that looks like a cat. Muted palette, plain background, one object, nothing else in frame.
- **Mascot and chrome** — as cartoony and charming as you like. This is where personality lives, and it costs nothing pedagogically.

Two consequences: no decorative backgrounds behind the word pictures (extraneous detail is measurably bad for young learners), and one object per card, large, centred.

### The mascot is worth more than the pictures

Because eight of the 23 words are verbs and feelings, and no stock library has "a mascot who is disappointed but not upset". One character, drawn once in eight poses, ties the whole app together and gives you something cheap to animate (a two-frame bob and a blink is plenty). Budget for the character sheet before you budget for anything else.

---

## Free, and clean enough to ship

| Source | Licence | What it's for |
| --- | --- | --- |
| [Andika](https://software.sil.org/andika/) (SIL) | OFL | **The font.** Designed specifically for beginning readers — clear letterforms that don't get confused with one another. Single-storey *a* and *g*, which is what he'll be taught to write. Bundling it in an app is explicitly allowed. |
| [Kenney](https://kenney.nl/assets) | CC0 | Icons, UI frames, animals, food, furniture. No attribution needed, commercial use fine. Start with **UI Pack**, **Board Game Icons**, **Animal Pack**, **Food Kit**. Also has a free interface-sound pack for the three SFX. |
| [Twemoji](https://github.com/jdecked/twemoji) | MIT | Flat, consistent, covers every concrete noun in the list. The most permissive of the emoji sets. |
| [Noto Emoji](https://github.com/googlefonts/noto-emoji) | OFL | Same idea, Google's set, also permissive. |
| [OpenMoji](https://openmoji.org/) | CC BY-SA 4.0 | Nicest-looking of the three, one consistent style guide — but the share-alike term is viral. Fine for a personal app, avoid it if this might ever be sold. |
| [Pexels](https://www.pexels.com/) / [Unsplash](https://unsplash.com/) | Free, attribution not required | Photographs, if you want to test the realism argument directly. Watch for branded objects and identifiable people. |
| Google Fonts — Fredoka, Baloo 2, Nunito | OFL | Rounded, friendly UI chrome. Don't use these for the *letters he's learning* — that's Andika's job. |

## Paid, if the free stuff isn't enough

| Source | Cost | Verdict |
| --- | --- | --- |
| [Streamline](https://www.streamlinehq.com/) | from ~$30/mo, or one-time packs | Best icon consistency anywhere. Overkill for five icons. |
| [CraftPix](https://craftpix.net/) | $5–20 per pack | Cheap game art; good for UI frames and effects, weak for the pictures. |
| [Envato Elements](https://elements.envato.com/) | ~$16.50/mo | Huge vector library, includes children's illustration sets. Read the licence for app embedding before relying on it. |
| [Creative Market](https://creativemarket.com/) | $10–50 per pack | Very variable. Filter hard for "children's book". |
| [Blush](https://blush.design/) | free tier, paid | Mix-and-match character kits — the fastest route to a consistent mascot in eight poses. |
| Children's book illustrator, Fiverr/Upwork | $15–40 per drawing at decent quality; $40–120 at real quality | **This is where the money should go.** Search "children's book illustration flat vector" or "phonics flashcard". Ask for three sample pictures in a proposed style before commissioning all 23. |

## The DIY route

Drawing them as inline SVG (what the prototype did) is legitimate, and has real advantages: consistent by construction, infinitely scalable, tiny files, no licence questions. The honest limitation is that hand-authored SVG looks like programmer art unless you have an eye for it. Fine as a placeholder to find out whether Aster engages; not what you want him looking at for a year.

## Recommended path

1. **This week, free:** Twemoji or Noto Emoji for the 23 pictures, Kenney for icons and sounds, Andika for letters. Build it, put it in front of him, find out whether he actually wants to play it.
2. **If he does:** commission one character sheet (8 poses) and 23 flat illustrations in a locked palette. Expect **$400–900**, four to six weeks. That single purchase is the difference between a prototype and something he'll still be using at six.

Don't buy anything before step 1. The thing that predicts whether this works is not how it looks.

---

## Keep a CREDITS.md

If this ends up as a repo of yours: list every asset, its source, its licence, and whether it was modified. Two minutes now, and it's the difference between a project you can publish and one you have to audit later. CC0 and MIT (Kenney, Twemoji) need nothing. OFL (fonts) needs the licence file to travel with the font. CC BY-SA (OpenMoji) needs attribution *and* would put your derivative under the same licence.
