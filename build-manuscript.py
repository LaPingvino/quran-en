#!/usr/bin/env python3
"""Build English-only manuscript from translation files."""
import os

NAMES = {
    1: "Al-Fatihah — The Opening", 2: "Al-Baqarah — The Cow", 3: "Al-Imran — The Family of Imran",
    4: "An-Nisa — The Women", 5: "Al-Ma'idah — The Table", 6: "Al-An'am — The Cattle",
    7: "Al-A'raf — The Heights", 8: "Al-Anfal — The Spoils", 9: "At-Tawbah — Repentance",
    10: "Yunus — Jonah", 11: "Hud", 12: "Yusuf — Joseph", 13: "Ar-Ra'd — The Thunder",
    14: "Ibrahim — Abraham", 15: "Al-Hijr", 16: "An-Nahl — The Bee",
    17: "Al-Isra — The Night Journey", 18: "Al-Kahf — The Cave", 19: "Maryam — Mary",
    20: "Ta-Ha", 21: "Al-Anbiya — The Prophets", 22: "Al-Hajj — The Pilgrimage",
    23: "Al-Mu'minun — The Believers", 24: "An-Nur — The Light", 25: "Al-Furqan — The Criterion",
    26: "Ash-Shu'ara — The Poets", 27: "An-Naml — The Ant", 28: "Al-Qasas — The Stories",
    29: "Al-Ankabut — The Spider", 30: "Ar-Rum — The Romans", 31: "Luqman",
    32: "As-Sajdah — The Prostration", 33: "Al-Ahzab — The Confederates", 34: "Saba — Sheba",
    35: "Fatir — The Originator", 36: "Ya-Sin", 37: "As-Saffat — The Ranged", 38: "Sad",
    39: "Az-Zumar — The Crowds", 40: "Ghafir — The Forgiver", 41: "Fussilat — Expounded",
    42: "Ash-Shura — The Consultation", 43: "Az-Zukhruf — The Ornaments",
    44: "Ad-Dukhan — The Smoke", 45: "Al-Jathiyah — The Kneeling",
    46: "Al-Ahqaf — The Sand-Dunes", 47: "Muhammad", 48: "Al-Fath — The Victory",
    49: "Al-Hujurat — The Chambers", 50: "Qaf", 51: "Adh-Dhariyat — The Scatterers",
    52: "At-Tur — The Mount", 53: "An-Najm — The Star", 54: "Al-Qamar — The Moon",
    55: "Ar-Rahman — The Merciful", 56: "Al-Waqi'ah — The Event", 57: "Al-Hadid — The Iron",
    58: "Al-Mujadilah — The Disputer", 59: "Al-Hashr — The Gathering",
    60: "Al-Mumtahanah — The Examined", 61: "As-Saff — The Row",
    62: "Al-Jumu'ah — The Congregation", 63: "Al-Munafiqun — The Hypocrites",
    64: "At-Taghabun — Mutual Cheating", 65: "At-Talaq — Divorce",
    66: "At-Tahrim — The Forbidding", 67: "Al-Mulk — The Dominion", 68: "Al-Qalam — The Pen",
    69: "Al-Haqqah — The Reality", 70: "Al-Ma'arij — The Ways of Ascent", 71: "Nuh — Noah",
    72: "Al-Jinn — The Spectres", 73: "Al-Muzzammil — The Enwrapped",
    74: "Al-Muddaththir — The Cloaked", 75: "Al-Qiyamah — The Resurrection",
    76: "Al-Insan — The Human", 77: "Al-Mursalat — The Sent Ones", 78: "An-Naba — The Tidings",
    79: "An-Nazi'at — The Pluckers", 80: "'Abasa — He Frowned", 81: "At-Takwir — The Folding Up",
    82: "Al-Infitar — The Cleaving", 83: "Al-Mutaffifin — The Defrauders",
    84: "Al-Inshiqaq — The Splitting", 85: "Al-Buruj — The Constellations",
    86: "At-Tariq — The Night-Comer", 87: "Al-A'la — The Most High",
    88: "Al-Ghashiyah — The Overwhelming", 89: "Al-Fajr — The Dawn", 90: "Al-Balad — The City",
    91: "Ash-Shams — The Sun", 92: "Al-Layl — The Night", 93: "Ad-Duha — The Morning Hours",
    94: "Ash-Sharh — The Opening Forth", 95: "At-Tin — The Fig", 96: "Al-Alaq — The Clot",
    97: "Al-Qadr — The Power", 98: "Al-Bayyinah — The Clear Proof",
    99: "Az-Zalzalah — The Earthquake", 100: "Al-Adiyat — The Chargers",
    101: "Al-Qari'ah — The Striking", 102: "At-Takathur — Rivalry",
    103: "Al-Asr — The Fading Day", 104: "Al-Humazah — The Slanderer",
    105: "Al-Fil — The Elephant", 106: "Quraysh", 107: "Al-Ma'un — Small Kindnesses",
    108: "Al-Kawthar — Abundance", 109: "Al-Kafirun — Those Who Conceal",
    110: "An-Nasr — The Help", 111: "Al-Masad — The Fibre", 112: "Al-Ikhlas — The Sincerity",
    113: "Al-Falaq — Dawn", 114: "An-Nas — Humanity",
}

with open('manuscript.md', 'w') as out:
    out.write('---\ntitle: "The Recitation"\nsubtitle: "A Root-Recovery Translation of the Qur\'an"\nauthor: "Joop Kiefte"\nlang: en\n---\n\n')
    out.write('# Preface\n\nThis translation recovers meanings hidden in the Arabic roots of the Qur\'an. Key choices: *kafir* (k-f-r) becomes "those who conceal"; *muslim* (s-l-m) becomes "the Devoted"; *hur* (h-w-r) becomes "the Returners" — the same root as Jesus\'s disciples; *al-Qur\'an* (q-r-\') becomes "the Recitation."\n\n\\newpage\n\n')
    for snum in range(1, 115):
        path = f'{snum:03d}.md'
        if not os.path.exists(path): continue
        with open(path) as f:
            lines = f.readlines()
        name = NAMES.get(snum, f"Surah {snum}")
        for i, line in enumerate(lines):
            if line.startswith('# '):
                lines[i] = f'# Surah {snum}: {name}\n'
                break
        out.write(''.join(l for l in lines if not l.startswith('## ')))
        out.write('\n\\newpage\n\n')
    out.write('# Appendix: Root Discoveries\n\n')
    with open('roots.md') as f:
        for line in f:
            if line.startswith('# '): continue
            out.write(line)

print('manuscript.md built')
