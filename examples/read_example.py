#!/usr/bin/env python3
"""Print a study sheet and run the quiz for one character.  Usage: python3 examples/read_example.py [hanzi]"""
import json
import sys
from pathlib import Path

data = json.loads((Path(__file__).resolve().parent.parent / "data" / "characters.json").read_text(encoding="utf-8"))
by_hanzi = {c["hanzi"]: c for c in data["characters"]}

print("Characters in this release:")
for c in data["characters"]:
    print(f"  {c['hanzi']}  {c['pinyin']:<5} tone {c['tone']}  {c['strokes']} strokes  {c['meaning']}")

pick = sys.argv[1] if len(sys.argv) > 1 else data["characters"][0]["hanzi"]
if pick not in by_hanzi:
    sys.exit(f"{pick} is not in the data set yet")
c = by_hanzi[pick]
print(f"\n{c['hanzi']} ({c['pinyin']}): {c['meaning']}")
print(c["origin"][0])
print("Words:")
for w in c["words"]:
    literal = f" (literally: {w['literal']})" if "literal" in w else ""
    print(f"  {w['zh']}  {w['pinyin']}  {w['en']}{literal}")
print("Quiz answers:")
for q in c["quiz"]:
    print(f"  {q['q']}  ->  {q['options'][q['answer']]}")
