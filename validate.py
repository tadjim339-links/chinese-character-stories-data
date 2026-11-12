#!/usr/bin/env python3
"""Check data/characters.json for structural mistakes. Exits non-zero on the first problem."""
import json
import sys
from pathlib import Path

doc = json.loads((Path(__file__).resolve().parent / "data" / "characters.json").read_text(encoding="utf-8"))
REQUIRED = ["id", "hanzi", "pinyin", "tone", "meaning", "strokes", "summary", "origin", "memory_aid", "stroke_order", "words", "quiz", "page"]
problems, seen = [], set()
for c in doc["characters"]:
    tag = c.get("hanzi", "?")
    problems += [f"{tag}: missing {k}" for k in REQUIRED if k not in c]
    if c.get("hanzi") in seen:
        problems.append(f"{tag}: duplicate")
    seen.add(c.get("hanzi"))
    if len(c.get("hanzi", "")) != 1:
        problems.append(f"{tag}: hanzi must be one character")
    if c.get("tone") not in (1, 2, 3, 4, 5):
        problems.append(f"{tag}: tone must be 1-5")
    if not isinstance(c.get("strokes"), int) or c["strokes"] < 1:
        problems.append(f"{tag}: strokes must be a positive integer")
    for w in c.get("words", []):
        if not all(w.get(k) for k in ("zh", "pinyin", "en")):
            problems.append(f"{tag}: word entry incomplete: {w}")
    for q in c.get("quiz", []):
        if not (isinstance(q.get("answer"), int) and 0 <= q["answer"] < len(q.get("options", []))):
            problems.append(f"{tag}: quiz answer index out of range: {q.get('q')}")
        if len(set(q.get("options", []))) != len(q.get("options", [])):
            problems.append(f"{tag}: duplicate quiz options: {q.get('q')}")
if doc.get("count") != len(doc["characters"]):
    problems.append("count does not match the number of characters")
if problems:
    sys.exit("\n".join(problems))
print(f"OK: {len(doc['characters'])} characters, {sum(len(c['quiz']) for c in doc['characters'])} quiz questions")
