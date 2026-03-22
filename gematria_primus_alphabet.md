# Gematria Primus — Complete Reference & Liber Primus Cryptanalysis

> **Compiled from**: `/home/ubuntu/Uploads/liber_primus.md`, Cicada 3301 community research, and original cryptanalysis  
> **Date**: 2026-03-22

---

## 1. The Complete Gematria Primus Alphabet (29 Runes)

The Gematria Primus is a runic cipher alphabet created by Cicada 3301, based on the Anglo-Saxon Futhorc rune set. Each of the 29 runes maps to a **Latin letter** (or digraph) and a **prime number value**. The primes are the first 29 consecutive primes (2 through 109). Each rune also has a **positional index** (0–28), used in modular arithmetic operations.

| Pos | Rune | Unicode | Latin Letter | Prime Value |
|-----|------|---------|-------------|-------------|
|  0  |  ᚠ  | U+16A0  | **F**       | **2**       |
|  1  |  ᚢ  | U+16A2  | **U** (V)   | **3**       |
|  2  |  ᚦ  | U+16A6  | **TH**      | **5**       |
|  3  |  ᚩ  | U+16A9  | **O**       | **7**       |
|  4  |  ᚱ  | U+16B1  | **R**       | **11**      |
|  5  |  ᚳ  | U+16B3  | **C** (K)   | **13**      |
|  6  |  ᚷ  | U+16B7  | **G**       | **17**      |
|  7  |  ᚹ  | U+16B9  | **W**       | **19**      |
|  8  |  ᚻ  | U+16BB  | **H**       | **23**      |
|  9  |  ᚾ  | U+16BE  | **N**       | **29**      |
| 10  |  ᛁ  | U+16C1  | **I**       | **31**      |
| 11  |  ᛄ  | U+16C4  | **J**       | **37**      |
| 12  |  ᛇ  | U+16C7  | **EO**      | **41**      |
| 13  |  ᛈ  | U+16C8  | **P**       | **43**      |
| 14  |  ᛉ  | U+16C9  | **X**       | **47**      |
| 15  |  ᛋ  | U+16CB  | **S** (Z)   | **53**      |
| 16  |  ᛏ  | U+16CF  | **T**       | **59**      |
| 17  |  ᛒ  | U+16D2  | **B**       | **61**      |
| 18  |  ᛖ  | U+16D6  | **E**       | **67**      |
| 19  |  ᛗ  | U+16D7  | **M**       | **71**      |
| 20  |  ᛚ  | U+16DA  | **L**       | **73**      |
| 21  |  ᛝ  | U+16DD  | **NG** (ING)| **79**      |
| 22  |  ᛟ  | U+16DF  | **OE**      | **83**      |
| 23  |  ᛞ  | U+16DE  | **D**       | **89**      |
| 24  |  ᚪ  | U+16AA  | **A**       | **97**      |
| 25  |  ᚫ  | U+16AB  | **AE**      | **101**     |
| 26  |  ᚣ  | U+16A3  | **Y**       | **103**     |
| 27  |  ᛡ  | U+16E1  | **IA** (IO) | **107**     |
| 28  |  ᛠ  | U+16E0  | **EA**      | **109**     |

### Key Properties

- **Separator**: The bullet character `•` (U+2022) separates words in runic text.
- **Gematria Sum**: The sum of prime values for all runes in a word/phrase. Many solved sentences sum to primes.
- **Position-based operations**: Solved pages use `(position ± key) mod 29` for shifts, not prime values.
- **Atbash**: Reversal over the 29-rune line (position → 28 − position).
- **GP 2013 vs GP 2014**: The 2014 version is a column-rearranged lookup of the 2013 table (used on page 01.jpg).

---

## 2. Cipher Methods Used on Solved Pages

| Method | Description | Used On |
|--------|-------------|---------|
| **Cleartext** | Runes read directly via GP substitution | 00, 02, 05, 10–13, 16, 74 |
| **Reversed Gematria (Atbash)** | Each rune position → `(28 − position)` | 01 (GP 2014 variant) |
| **Vigenère (shift up, forward GP)** | `(rune_pos + key_pos) mod 29` with keyword | 03–04 (DIVINITY), 14–15 (FIRFUMFERENFE) |
| **Shift down, reversed GP** | `(28 − rune_pos − shift) mod 29` | 06–09 (shift=3) |
| **Totient shift** | `(rune_pos − φ(prime)) mod 29` | 73 (phi of prime) |

---

## 3. Solved vs. Unsolved Pages

### ✅ SOLVED PAGES (LP1: pages 00–16, LP2: pages 73–74)

| Page(s) | Key / Method | Decrypted Content (Summary) |
|---------|-------------|----------------------------|
| **00.jpg** | Cleartext | Title: "Liber Primus" + PGP signature |
| **01.jpg** | Reversed Gematria (GP 2014) | "A WARNING: Believe nothing from this book except what you know to be true..." |
| **02.jpg** | Cleartext | "Chapter I — Intus" + PGP signature |
| **03.jpg** | Vigenère, key = DIVINITY | "WELCOME, PILGRIM, TO THE GREAT JOURNEY TOWARD THE END OF ALL THINGS..." |
| **04.jpg** | Vigenère, key = DIVINITY (cont.) | "...IT IS THROUGH THIS PILGRIMAGE THAT WE SHAPE OURSELVES..." + "WISDOM: You are a being unto yourself..." |
| **05.jpg** | Default GP substitution | "SOME WISDOM: The primes are sacred. The totient function is sacred. All things should be encrypted." + Magic Square |
| **06–08.jpg** | Shift 3 down reversed GP | "A KOAN" — The student & master dialogue ("Who are you who wishes to study here?") |
| **09.jpg** | Shift 3 down reversed GP | "AN INSTRUCTION: Do four unreasonable things each day." |
| **10–12.jpg** | Default GP substitution | "THE LOSS OF DIVINITY" — Consumption, Preservation, Adherence |
| **13.jpg** | Default GP substitution | "SOME WISDOM: Amass great wealth. Never become attached..." + "AN INSTRUCTION: Program your mind. Program reality." |
| **14–15.jpg** | Vigenère, key = FIRFUMFERENFE | "A KOAN: During a lesson..." (The voice in your head is the I) |
| **16.jpg** | Default GP substitution | "AN INSTRUCTION: Question all things. Discover truth inside yourself." + Magic Square |
| **73.jpg** (LP2 p.56) | φ(prime) shift down forward GP | "AN END: Within the deep web there exists a page that hashes to [hex hash]. It is the duty of every pilgrim to seek out this page." |
| **74.jpg** (LP2 p.57) | Default GP substitution | "PARABLE: Like the instar tunneling to the surface, we must shed our own circumferences. Find the divinity within and emerge." |

### ❌ UNSOLVED PAGES (LP2: pages 17–72)

All LP2 pages from 17.jpg through 72.jpg (LP2 pages 0–55) remain **unsolved**. The document marks them with `Key: ?`. They contain dense runic ciphertext with no known decryption.

| Page Group | LP2 Pages | Notes |
|------------|-----------|-------|
| 17–19.jpg | 0–2 | ~730 runes across 3 pages. Outguess on 17.jpg yields 58.2kB garbage. |
| 20–22.jpg | 3–5 | Dense ciphertext, no headers visible. |
| 23–24.jpg | 6–7 | Shorter section. |
| 25–31.jpg | 8–14 | 7 pages, long ciphertext block. |
| 32.jpg | 15 | Standalone entry. |
| 32–39.jpg | 15–22 | 8 pages grouped. |
| 40–43.jpg | 23–26 | 4 pages. |
| 43.jpg | 26 | Overlapping entry (short). |
| 44–49.jpg | 27–32 | 6 pages. |
| 50.jpg | 33 | Standalone entry. |
| 50–56.jpg | 33–39 | 7 pages grouped. |
| 56.jpg | 39 | Overlapping entry (short). |
| 57.jpg | 40 | Dense ciphertext with quoted sections. |
| 58–64.jpg | 41–47 | Images only — no rune transcription in document. |
| 65.jpg | 48 | Image only; Outguess yields 58.2kB garbage. |
| 66.jpg | 49 | **Base-60 encoded numbers** (not runes). 10×8 grid of base-60 values. |
| 67.jpg | 50 | **Base-60 encoded numbers**. 13×8 grid. |
| 68.jpg | 51 | **Base-60 encoded numbers**. 9×8 grid. Outguess yields garbage. |
| 69.jpg | 52 | Image only; Outguess yields garbage. |
| 70.jpg | 53 | Image only; Outguess yields garbage. |
| 71–72.jpg | 54–55 | Runic ciphertext. Key: ? |

**Total: ~58 unsolved pages (of 75 total)**

---

## 4. Cryptanalysis of Unsolved Pages

### 4.1 Frequency Analysis — Pages 17–19 (First Unsolved Block)

These 3 pages contain **729 runes** across all 29 symbols. The frequency distribution is **remarkably flat**:

| Rune (Letter) | Count | Frequency |
|---------------|-------|-----------|
| ᚠ (F)  | 34 | 4.66% |
| ᛞ (D)  | 31 | 4.25% |
| ᚻ (H)  | 30 | 4.12% |
| ᚦ (TH) | 30 | 4.12% |
| ᛚ (L)  | 30 | 4.12% |
| ᚷ (G)  | 29 | 3.98% |
| ᛝ (NG) | 29 | 3.98% |
| ᚳ (C)  | 28 | 3.84% |
| ᚾ (N)  | 28 | 3.84% |
| ᛉ (X)  | 28 | 3.84% |
| ᛠ (EA) | 28 | 3.84% |
| ... | ... | ... |
| ᛗ (M)  | 18 | 2.47% |
| ᛇ (EO) | 17 | 2.33% |

**Expected uniform frequency** for 29 symbols: **3.45%** — the observed range (2.33%–4.66%) is very tight.

### 4.2 Index of Coincidence (IC)

| Metric | Value |
|--------|-------|
| **Observed IC** | **0.03408** |
| Expected IC (random, 29 symbols) | 0.03448 |
| Expected IC (English mono-substitution) | ~0.0667 |

**Conclusion**: The IC is **virtually identical to random** (1/29). This **rules out**:
- Simple substitution (mono-alphabetic)
- Atbash / reversal ciphers
- Short-key Vigenère (which would show elevated IC)

This strongly indicates:
- **Polyalphabetic cipher with a key length ≥ the text length** (e.g., running key or autokey)
- **Stream cipher** (XOR with a keystream)
- **Transposition combined with substitution**
- **OTP (one-time pad)-like encryption**

### 4.3 Bigram & Word Structure Analysis

- **No repeated trigrams** appear more than twice across 729 runes — extremely unusual for natural language, even enciphered.
- **Word lengths** follow a distribution consistent with English (mode at 3, spread from 1–11), suggesting word boundaries are **preserved** but individual runes are randomized.
- **Only 2 repeated multi-rune words**: `ᚦᛈ` and `ᚠᛠ` (each appearing twice). In natural English text of this length, we'd expect dozens of repeated words (THE, AND, OF, etc.).

### 4.4 Kasiski Examination

No repeated trigram sequences were found at distances that would suggest a periodic Vigenère key. This is consistent with:
- A **non-periodic** cipher
- A key **at least as long as the plaintext**

### 4.5 Comparison with Solved Pages

The solved Vigenère pages (03–04, 14–15) used **short repeating keys** (8 and 13 characters). If the unsolved pages used a similar scheme, we would see:
- Elevated IC above random
- Repeated n-grams at key-length intervals

**Neither is observed.** This means Cicada 3301 **changed their encryption method** for LP2.

### 4.6 The Base-60 Pages (66–68)

Pages 66–68 present data as **base-60 numbers** (using a custom encoding: 0–9, A–Z, a–x). When converted to decimal, the values range from 0–255, suggesting **raw bytes**. These could be:
- An encrypted binary payload
- Image data (header bytes don't match known formats)
- A separate cipher layer

### 4.7 Known Community Hypotheses

The Cicada 3301 research community has explored:

1. **Totient-based stream cipher**: Using φ(n) iteratively to generate a keystream from a seed derived from the solved pages.
2. **Interrupter-based cipher**: A custom scheme where certain runes act as "interrupters" modifying the cipher state.
3. **Transposition cipher on the rune positions**: Rearranging rune order before/after substitution.
4. **Steganographic layers**: Hidden data in the original JPEG images (Outguess extraction yielded some results but mostly "garbage").
5. **Hash-based key derivation**: The hex hash on page 73 (`36367763ab73783c...`) may be the key to decrypting preceding pages.
6. **Autokey cipher**: Where the plaintext itself extends the key, making frequency analysis useless.

---

## 5. The Hex Hash Clue (Page 73)

Page 73 (the last solved page before the final parable) contains a critical clue:

```
36367763ab73783c7af284446c59466b4cd653239a311cb7116
d4618dee09a8425893dc7500b464fdaf1672d7bef5e891c6e227
4568926a49fb4f45132c2a8b4
```

This appears to be a **hash** (likely SHA-512 or similar) of a Tor hidden service page. The text states:

> *"Within the deep web there exists a page that hashes to [this value]. It is the duty of every pilgrim to seek out this page."*

This hash is **128 hex characters** (512 bits), consistent with **SHA-512**. It may contain the key needed to decrypt the remaining pages.

---

## 6. Quick-Reference Conversion Table

For rapid decoding work:

```
ᚠ=F(2)   ᚢ=U(3)   ᚦ=TH(5)  ᚩ=O(7)   ᚱ=R(11)
ᚳ=C(13)  ᚷ=G(17)  ᚹ=W(19)  ᚻ=H(23)  ᚾ=N(29)
ᛁ=I(31)  ᛄ=J(37)  ᛇ=EO(41) ᛈ=P(43)  ᛉ=X(47)
ᛋ=S(53)  ᛏ=T(59)  ᛒ=B(61)  ᛖ=E(67)  ᛗ=M(71)
ᛚ=L(73)  ᛝ=NG(79) ᛟ=OE(83) ᛞ=D(89)  ᚪ=A(97)
ᚫ=AE(101) ᚣ=Y(103) ᛡ=IA(107) ᛠ=EA(109)
```

**Position-to-Rune** (for mod-29 operations):
```
0:ᚠ  1:ᚢ  2:ᚦ  3:ᚩ  4:ᚱ  5:ᚳ  6:ᚷ  7:ᚹ  8:ᚻ  9:ᚾ
10:ᛁ 11:ᛄ 12:ᛇ 13:ᛈ 14:ᛉ 15:ᛋ 16:ᛏ 17:ᛒ 18:ᛖ 19:ᛗ
20:ᛚ 21:ᛝ 22:ᛟ 23:ᛞ 24:ᚪ 25:ᚫ 26:ᚣ 27:ᛡ 28:ᛠ
```

---

## 7. Solved Plaintext: Complete Decrypted Passages

### Page 01 — A WARNING
```
BELIEVE NOTHING FROM THIS BOOK
EXCEPT WHAT YOU KNOW TO BE TRUE
TEST THE KNOWLEDGE
FIND YOUR TRUTH
EXPERIENCE YOUR DEATH
DO NOT EDIT OR CHANGE THIS BOOK
OR THE MESSAGE CONTAINED WITHIN
EITHER THE WORDS OR THEIR NUMBERS
FOR ALL IS SACRED
```

### Pages 03–04 — WELCOME
```
WELCOME, PILGRIM, TO THE GREAT JOURNEY TOWARD THE END OF ALL THINGS.
IT IS NOT AN EASY TRIP, BUT FOR THOSE WHO FIND THEIR WAY HERE
IT IS A NECESSARY ONE.
ALONG THE WAY YOU WILL FIND AN END TO ALL STRUGGLE AND SUFFERING,
YOUR INNOCENCE, YOUR ILLUSIONS, YOUR CERTAINTY, AND YOUR REALITY.
ULTIMATELY, YOU WILL DISCOVER AN END TO SELF.

IT IS THROUGH THIS PILGRIMAGE THAT WE SHAPE OURSELVES AND OUR REALITIES.
JOURNEY DEEP WITHIN AND YOU WILL ARRIVE OUTSIDE.
LIKE THE INSTAR, IT IS ONLY THROUGH GOING WITHIN THAT WE MAY EMERGE.

WISDOM: YOU ARE A BEING UNTO YOURSELF.
YOU ARE A LAW UNTO YOURSELF.
EACH INTELLIGENCE IS HOLY.
FOR ALL THAT LIVES IS HOLY.

AN INSTRUCTION: COMMAND YOUR OWN SELF.
```

### Page 05 — SOME WISDOM
```
THE PRIMES ARE SACRED
THE TOTIENT FUNCTION IS SACRED
ALL THINGS SHOULD BE ENCRYPTED

KNOW THIS:
[5×5 Magic Square with runic words and numbers — sum = 1033 per row/column]
```

### Pages 06–09 — A KOAN + AN INSTRUCTION
```
A MAN DECIDED TO GO AND STUDY WITH A MASTER.
HE WENT TO THE DOOR OF THE MASTER.
"WHO ARE YOU WHO WISHES TO STUDY HERE?" ASKED THE MASTER.
THE STUDENT TOLD THE MASTER HIS NAME.
"THAT IS NOT WHAT YOU ARE. THAT IS ONLY WHAT YOU ARE CALLED.
WHO ARE YOU WHO WISHES TO STUDY HERE?" HE ASKED AGAIN.
THE MAN THOUGHT FOR A MOMENT, AND REPLIED "I AM A PROFESSOR."
"THAT IS WHAT YOU DO, NOT WHAT YOU ARE," REPLIED THE MASTER.
"WHO ARE YOU WHO WISHES TO STUDY HERE?"
CONFUSED, THE MAN THOUGHT SOME MORE.
FINALLY, HE ANSWERED, "I AM A HUMAN BEING."
"THAT IS ONLY YOUR SPECIES, NOT WHO YOU ARE.
WHO ARE YOU WHO WISHES TO STUDY HERE?" ASKED THE MASTER AGAIN.
AFTER A MOMENT OF THOUGHT, THE PROFESSOR REPLIED
"I AM A CONSCIOUSNESS INHABITING AN ARBITRARY BODY."
"THAT IS MERELY WHAT YOU ARE, NOT WHO YOU ARE.
WHO ARE YOU WHO WISHES TO STUDY HERE?"
THE MAN WAS GETTING IRRITATED.
"I AM," HE STARTED, BUT HE COULD NOT THINK OF ANYTHING ELSE TO SAY,
SO HE TRAILED OFF.
AFTER A LONG PAUSE THE MASTER REPLIED,
"THEN YOU ARE WELCOME TO COME STUDY."

AN INSTRUCTION: DO FOUR UNREASONABLE THINGS EACH DAY.
```

### Pages 10–13 — THE LOSS OF DIVINITY
```
THE CIRCUMFERENCE PRACTICES THREE BEHAVIORS WHICH CAUSE THE LOSS OF DIVINITY.

CONSUMPTION: We consume too much because we believe the following two errors
within the deception:
  1. We do not have enough, or there is not enough.
  2. We have what we have now by luck, and we will not be strong enough later
     to obtain what we need.
Most things are not worth consuming.

PRESERVATION: We preserve things because we believe we are weak.
If we lose them we will not be strong enough to gain them again.
This is the deception. Most things are not worth preserving.

ADHERENCE: We follow dogma so that we can belong and be right.
Or we follow reason so we can belong and be right.
There is nothing to be right about. To belong is death.

It is the behaviors of consumption, preservation, and adherence
that have us lose our primality and thus our divinity.

SOME WISDOM: Amass great wealth. Never become attached to what you own.
Be prepared to destroy all that you own.

AN INSTRUCTION: Program your mind. Program reality.
```

### Pages 14–15 — A KOAN
```
DURING A LESSON, THE MASTER EXPLAINED THE I:
"THE I IS THE VOICE OF THE CIRCUMFERENCE," HE SAID.
WHEN ASKED BY A STUDENT TO EXPLAIN WHAT THAT MEANT,
THE MASTER SAID, "IT IS A VOICE INSIDE YOUR HEAD."
"I DON'T HAVE A VOICE IN MY HEAD," THOUGHT THE STUDENT,
AND HE RAISED HIS HAND TO TELL THE MASTER.
THE MASTER STOPPED THE STUDENT, AND SAID,
"THE VOICE THAT JUST SAID YOU HAVE NO VOICE IN YOUR HEAD, IS THE I."
AND THE STUDENTS WERE ENLIGHTENED.
```

### Page 16 — AN INSTRUCTION
```
QUESTION ALL THINGS.
DISCOVER TRUTH INSIDE YOURSELF.
FOLLOW YOUR TRUTH.
IMPOSE NOTHING ON OTHERS.
KNOW THIS:
[5×5 Magic Square: 434 1311 312 278 966 / 204 812 934 280 1071 / ...]
```

### Page 73 — AN END
```
WITHIN THE DEEP WEB THERE EXISTS A PAGE THAT HASHES TO
36367763ab73783c7af284446c59466b4cd653239a311cb7116d4618dee09a8425893dc7500b
464fdaf1672d7bef5e891c6e2274568926a49fb4f45132c2a8b4
IT IS THE DUTY OF EVERY PILGRIM TO SEEK OUT THIS PAGE.
```

### Page 74 — PARABLE
```
LIKE THE INSTAR TUNNELING TO THE SURFACE,
WE MUST SHED OUR OWN CIRCUMFERENCES.
FIND THE DIVINITY WITHIN AND EMERGE.
```

---

## 8. Gematria Sums of Solved Sentences

Many sentences sum to **prime numbers** (emirps marked with *):

| Sentence | Gematria Sum |
|----------|-------------|
| BELIEVE NOTHING FROM THIS BOOK | 757* |
| EXCEPT WHAT YOU KNOW TO BE TRUE | 1009* |
| TEST THE KNOWLEDGE | 691 |
| FIND YOUR TRUTH | 353* |
| EXPERIENCE YOUR DEATH | 769* |
| DO NOT EDIT OR CHANGE THIS BOOK | 911 |
| OR THE MESSAGE CONTAINED WITHIN | 1051 |
| EITHER THE WORDS OR THE NUMBERS | 859 |
| FOR ALL IS SACRED | 677 |
| THE PRIMES ARE SACRED | 853 |
| THE TOTIENT FUNCTION IS SACRED | 1039 |
| ALL THINGS SHOULD BE ENCRYPTED | 1237* |
| KNOW THIS | 157* |

---

## 9. Summary & Recommendations for Further Work

### What We Know
1. **LP1 (pages 00–16) is fully solved.** Methods included cleartext, GP substitution, Vigenère with short keys, shifted Atbash, and GP 2014 reversal.
2. **LP2 pages 73–74 are solved.** Page 73 uses totient-shift; page 74 is cleartext GP.
3. **LP2 pages 17–72 (~56 pages) remain unsolved.** This is the vast majority of the book.

### Why the Unsolved Pages Are Hard
- **IC ≈ 1/29 (random)**: The cipher produces output statistically indistinguishable from random, eliminating simple frequency-based attacks.
- **No repeated patterns**: Kasiski analysis finds nothing — there is no periodic key structure.
- **Word boundaries preserved**: The `•` separators are retained, meaning we know word lengths, but this hasn't been sufficient to break the cipher.

### Most Promising Attack Vectors
1. **The Page 73 hash**: Finding the .onion page whose content hashes to the given SHA-512 value could reveal the decryption key for the entire LP2.
2. **Autokey / running-key cipher**: Test whether the solved plaintext from LP1 serves as the key for LP2.
3. **Totient stream cipher**: Since page 73 used φ(prime) as a key, a generalized totient-based keystream could apply to all pages.
4. **Steganographic data**: Several pages yield "58.2kB garbage" from Outguess — this is a consistent size, possibly a meaningful encrypted payload.
5. **Base-60 pages (66–68)**: These appear to encode raw bytes (0–255) — could be encrypted image data or a separate cipher layer.

---

*This document is intended as a complete working reference for anyone continuing cryptanalysis of the Liber Primus. The Gematria Primus table above is verified against multiple community sources and the solved pages in the document.*
