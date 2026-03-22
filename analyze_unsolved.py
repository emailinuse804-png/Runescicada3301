#!/usr/bin/env python3
"""Frequency analysis and cryptanalysis of unsolved Liber Primus pages."""

import re
from collections import Counter

# Gematria Primus alphabet (position 0-28)
GP = {
    'ᚠ': ('F',  2,  0),  'ᚢ': ('U',  3,  1),  'ᚦ': ('TH', 5,  2),
    'ᚩ': ('O',  7,  3),  'ᚱ': ('R',  11, 4),  'ᚳ': ('C/K',13, 5),
    'ᚷ': ('G',  17, 6),  'ᚹ': ('W',  19, 7),  'ᚻ': ('H',  23, 8),
    'ᚾ': ('N',  29, 9),  'ᛁ': ('I',  31, 10), 'ᛄ': ('J',  37, 11),
    'ᛇ': ('EO', 41, 12), 'ᛈ': ('P',  43, 13), 'ᛉ': ('X',  47, 14),
    'ᛋ': ('S/Z',53, 15), 'ᛏ': ('T',  59, 16), 'ᛒ': ('B',  61, 17),
    'ᛖ': ('E',  67, 18), 'ᛗ': ('M',  71, 19), 'ᛚ': ('L',  73, 20),
    'ᛝ': ('NG', 79, 21), 'ᛟ': ('OE', 83, 22), 'ᛞ': ('D',  89, 23),
    'ᚪ': ('A',  97, 24), 'ᚫ': ('AE',101, 25), 'ᚣ': ('Y', 103, 26),
    'ᛡ': ('IA',107, 27), 'ᛠ': ('EA',109, 28),
}

# English letter frequencies (approximate, for single-letter comparison)
ENGLISH_FREQ = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7,
    'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8,
    'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2, 'G': 2.0, 'Y': 2.0,
    'P': 1.9, 'B': 1.5, 'V': 1.0, 'K': 0.8, 'J': 0.2, 'X': 0.2,
    'Q': 0.1, 'Z': 0.1
}

# Extract runes from pages 17-19 (first unsolved section)
pages_17_19 = """ᛋᚻᛖᚩᚷᛗᛡᚠ•ᛋᚣᛖᛝᚳ
ᚦᛄᚷᚫ•ᚠᛄᛟ•ᚩᚾᚦ•ᚾᛖᚹᛒᚪᛋᛟᛇᛁᛝᚢ•ᚾᚫᚷᛁᚦ•ᚻᛒᚾᛡ•ᛈᛒᚾ•ᛇᛄᚦ•ᚪᛝᚣᛉ•ᛒᛞᛈ•ᛖᛡᚠᛉᚷᚠ•ᛋᛈᛏᚠᛈᚢᛝᚣᛝᛉᛡ•ᚣᚻ•ᛒᚢ•ᚷᚩᛈ•ᛝᚫᚦ•ᛁᚫᚻᛉᚦᛈᚷ•ᚣᚠᛝᚳᛄ•ᚦᚪᛗᛁᛝᛁᛡᚣ•ᚻᛇ•ᛏᚻᚫᛡ•ᛉᚣ•ᛖᚢᛝ•ᚳᚠᚾ•ᛇᚦᛄᛁᚦ•ᚦᛈ•ᚣᛝᛠ•ᚣᚾᛖᚣ•ᛞᛉᛝᚹ•ᛒᚳᛉᛞᛒᚠ•ᛗᛏᚾᛖ•ᛠᛄᚾᛚᚷᛒ•ᛉᚷᚦ
ᚣᛁᛞᚪ•ᛝᚷᛗᛄᚱᚩᛚᛇ•ᚣᛏᛈᛁᚦᛞᛄ•ᛟᚻᛚ•ᛠ•ᚠᛉᚫᛈᚷᛉ•ᚠᛚᚹᛇᛏᚫ•ᚠᚷᚾ•ᛗᛇᛚᚾ•ᛝᛗᚠᚱᛡ•ᚪᛋ•ᛠᛗᛝᛉᛉᛇᛞᛒ•ᛟᛞᛗᚩ•ᛠᛇᚻ•ᛞᛝᚷ•ᛟᛝᛚᚢᚱᚾᛏ•ᚫᛋᚣᚢᚻᚱᛏ•ᚻᚳ•ᛋᛟᛏᛟᛝᚢᚱ•ᛋ•ᚠᚩᛖᚹᛠᛟᛚᚠᚫ•ᛗᚱᛝ•ᛞᚪᛗᚱ•ᚹᚪᛁᛗᛋᚾ•ᛋᛟᚱᚢᚹᛋᛚᛡ
ᛟᚪᚫᛝᛋᛞᛈᛏ•ᚳᚱᚦᛡ•ᚱᛒᚩᛞᚦᚠ•ᚣᛉᛁᛏ
ᛟᛁ•ᚠᛚᚩ•ᚠᛠ•ᚱᚩᛟᛗᚻᛗᚷᛈᚻ•ᚫᚻᚾᚩᚻᚣ•ᛟᛋᛚ•ᚾᚷ•ᚫᚣ•ᛟᚳᛒᛚᛄ•ᛝᛚᛟ•ᚫᛄᛠᚹ•ᛠᚦᚩ•ᛒᛟᚣ•ᚳᚠᚳᛄ•ᛚᚫ
ᚾ•ᚦᛈ•ᚢᛉ•ᛟᛉᚷ•ᛈᚠᛋᛇᚫᛟ•ᛝᛈᛇᚩᛖᚪ•ᚷᚫᛡᛝᚦᚩ•ᛈᚪᛟᚦᚱᛝᚫ•ᚳᛋᛒᛇᚣᚻ•ᛏᛉᛖᛚᚱ
ᚷᚹᚣ•ᛄᚠᛁᚾᛡᚳᚣᛠᛁᛡ•ᚩᚦ•ᛖᚳᚫᚳᛉᛡᛠ•ᚩᛚᚳ•ᚠᚱᛞᛝᛖᚢ•ᛞᚳᛚᛠᛋᛉᚳᚷᛡ
ᚹᛋᚦ•ᚠᛞᛝ•ᛁᛡᛗᚪᚫᚷ•ᚹᛋ•ᚾᛞ•ᚳᛈᚦᛉᛈᛠᛠ•ᚹᚢ•ᛠᚹ•ᚠᚹᛄᚣ•ᛉᛞᚹᚳᚷᚳᛟ•ᛞᛉᛟ•ᚱᛡᚷ•ᚾᛈᚪᚣᛈ•ᚳᚣᚻ•ᚠᛖᛄᛠᚾ•ᛟᚫ•ᚢᚪ•ᚻᚱ•ᛖᛠᚦᚠᛄᚪ•ᛚᛉᛋᛏ•ᛗᚠᛚᚠᛏ•ᚷᛁᚦ•ᚢᛚᚷ•ᛉᛠᛏᛋᛚᛄᛈ•ᛚᛉᛁᛟᛗ•ᚢ
ᚻᛏ•ᛒᛇᛚᛞᚻᛒᛗ•ᛠᚱᛒ•ᚾᚻᛒᛖᚷᛇ•ᛞᛚᚹᛇᛡᛈᚩ•ᚻᛖᛠ•ᚹᛁᚱᛁᚻ•ᚢᚦᚻᚣ•ᚾᛉᛒᚷᛄᛈᚢ•ᛝᛠᚠᚾᛁᛖᛞᛡᛝᚱ•ᛞᛒᛄᛡᛟᛗᛁ•ᚠᛏ•ᛄᛞᛁᚦᚱᛚᛋ•ᛖᛇᚩᚷᛒᛏᛞ•ᚦᚪᚾᚳᚣ•ᛡᛋᚦᛞ•ᛝᚠᛚᛖᚷᚻᚳ•ᛖᚩᛁᛏᚾᛉ•ᛈᛏᚠᚻᚱᛞᛖᚠᛏ•ᚫᚹᚻ•ᛒᚳ•ᚠ•ᛈᚪᛚᚢᛠᚾᛚᛄ•ᛄᚳᛚᚹᛠᛞᚢᛞᛇ•ᛠᛉᛞᚹᚻᛠ•ᚦᛡᚫᚳᛚᛏᚹᛖᛁᚳ•ᛈᛟᛞᚳ•ᚾᚻᚪ•ᚱᛁᚷᚦᛠᛖᛏᚷ•ᚦᚻᚩᛡᚹᚫᛄᛖ•ᛝᛠᛞ•ᚩᚫ•ᚪᛚ•ᛒᛄᚳᚢᛉᛏᚪᛒᛄᛈ•ᚠᛠ•ᚻᛞᚾᛡᚢᛈᛋᚢᚹ"""

# Count individual rune frequencies
rune_chars = [c for c in pages_17_19 if c in GP]
total = len(rune_chars)
freq = Counter(rune_chars)

print(f"=== Frequency Analysis: Pages 17-19 (First Unsolved Section) ===")
print(f"Total runes: {total}")
print(f"Unique runes: {len(freq)}")
print()

# Sort by frequency
print(f"{'Rune':<5} {'GP Letter':<8} {'Count':<8} {'Freq%':<8} {'Position':<8}")
print("-" * 45)
for rune, count in freq.most_common():
    letter, prime, pos = GP[rune]
    pct = 100.0 * count / total
    print(f"{rune:<5} {letter:<8} {count:<8} {pct:<8.2f} {pos:<8}")

print()

# Index of Coincidence
print("=== Index of Coincidence ===")
ic = sum(c * (c-1) for c in freq.values()) / (total * (total - 1))
print(f"IC = {ic:.6f}")
print(f"Expected IC for English (26 letters): ~0.0667")
print(f"Expected IC for random (29 symbols): {1/29:.6f} = ~0.0345")
print(f"Expected IC for monoalphabetic on 29: ~0.0667 (adjusted)")
print()

# Bigram analysis
words = pages_17_19.replace('\n', '•').split('•')
words = [w for w in words if w.strip()]
bigrams = Counter()
for word in words:
    runes = [c for c in word if c in GP]
    for i in range(len(runes)-1):
        bigrams[runes[i] + runes[i+1]] += 1

print("=== Top 20 Bigrams ===")
for bg, count in bigrams.most_common(20):
    r1, r2 = bg[0], bg[1]
    l1 = GP[r1][0]
    l2 = GP[r2][0]
    print(f"  {r1}{r2} ({l1}{l2}): {count}")

print()

# Word length distribution
word_lengths = [len([c for c in w if c in GP]) for w in words]
length_dist = Counter(word_lengths)
print("=== Word Length Distribution ===")
for length in sorted(length_dist.keys()):
    print(f"  Length {length}: {length_dist[length]} words")

# Check for repeated words
word_rune_strings = [''.join(c for c in w if c in GP) for w in words]
word_freq = Counter(word_rune_strings)
repeated = {w: c for w, c in word_freq.items() if c > 1 and len(w) > 1}
print()
print("=== Repeated Rune Words ===")
for w, c in sorted(repeated.items(), key=lambda x: -x[1])[:15]:
    letters = ''.join(GP[r][0] for r in w)
    print(f"  {''.join(w)} ({letters}): {c} occurrences")

# Kasiski-like analysis: find repeated trigrams
print()
print("=== Repeated Trigrams (Kasiski-like) ===")
all_runes = ''.join(rune_chars)
trigrams = Counter()
trigram_positions = {}
for i in range(len(all_runes) - 2):
    tri = all_runes[i:i+3]
    trigrams[tri] += 1
    if tri not in trigram_positions:
        trigram_positions[tri] = []
    trigram_positions[tri].append(i)

repeated_tri = {t: p for t, p in trigram_positions.items() if len(p) > 2}
print(f"Trigrams appearing 3+ times: {len(repeated_tri)}")
for tri, positions in sorted(repeated_tri.items(), key=lambda x: -len(x[1]))[:10]:
    letters = ''.join(GP[r][0] for r in tri)
    diffs = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
    print(f"  {''.join(tri)} ({letters}): {len(positions)} times, spacings: {diffs}")

