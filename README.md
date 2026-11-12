# Chinese character stories: open learning data

Structured study data for beginner Chinese characters, one record per character: pinyin, tone, meaning, stroke count, a short note on where the shape comes from, a memory aid, stroke-order guidance, four or five common words and five multiple-choice quiz questions.

It is the data behind the character pages at [Chinese Character Story](https://chinesecharacterstory.com/), published here so that teachers, app builders and learners can reuse it in flashcards, worksheets or their own tools.

## What is in this release

| Character | Pinyin | Tone | Meaning | Strokes |
|---|---|---|---|---|
| 水 | shuǐ | 3 | water | 4 |
| 山 | shān | 1 | mountain | 3 |
| 日 | rì | 4 | sun; day | 4 |
| 木 | mù | 4 | tree; wood | 4 |
| 火 | huǒ | 3 | fire | 4 |
| 人 | rén | 2 | person | 2 |
| 口 | kǒu | 3 | mouth | 3 |
| 目 | mù | 4 | eye | 5 |
| 手 | shǒu | 3 | hand | 4 |
| 心 | xīn | 1 | heart | 4 |
| 月 | yuè | 4 | moon; month | 4 |
| 雨 | yǔ | 3 | rain | 8 |
| 云 | yún | 2 | cloud | 4 |
| 土 | tǔ | 3 | earth; soil | 3 |
| 田 | tián | 2 | field | 5 |
| 大 | dà | 4 | big | 3 |
| 小 | xiǎo | 3 | small | 3 |
| 上 | shàng | 4 | up; above | 3 |
| 下 | xià | 4 | down; below | 3 |
| 中 | zhōng | 1 | middle | 4 |
| 黄 | huáng | 2 | yellow | 11 |

21 characters, 102 example words, 105 quiz questions. More are added as each character page is finished; the file grows, the format stays the same. Records added from November 2026 onward also carry a `sources` list (name and link of each reference checked).

## Format

Everything is in one UTF-8 file, [`data/characters.json`](data/characters.json):

```json
{
  "id": "shan",
  "hanzi": "山",
  "pinyin": "shān",
  "tone": 1,
  "meaning": "mountain",
  "strokes": 3,
  "summary": "…one-paragraph overview…",
  "origin": ["…what the early forms show…", "…how the shape changed…"],
  "memory_aid": "…a way to remember the shape…",
  "stroke_order": "…which stroke comes first…",
  "notes": ["…usage or component notes…"],
  "words": [{ "zh": "火山", "pinyin": "huǒshān", "en": "volcano", "literal": "fire mountain" }],
  "quiz": [{ "q": "What does 山 mean?", "options": ["…", "…", "…", "…"], "answer": 2, "explain": "…" }],
  "page": "https://chinesecharacterstory.com/characters/shan/"
}
```

- `tone` is 1-4, or 5 for the neutral tone.
- `quiz[].answer` is the zero-based index into `options`.
- `words[].literal` is present only when a word-for-word gloss helps (for example 水果, "water fruit").
- `page` is the lesson page for that character, with a short video and an interactive version of the quiz.

## Using it

No dependencies in either example.

```bash
python3 examples/read_example.py 火    # study sheet + quiz answers for one character
node examples/read_example.mjs         # turn every record into a flashcard
python3 validate.py                    # structural checks on the data file
```

## How the origin notes are written

Character etymology is easy to overstate, so the notes follow two rules:

1. A statement about where a shape comes from is made only where the early written forms support it, and it is hedged where the usual account is a traditional explanation rather than settled fact ("traditionally explained as…").
2. `memory_aid` is kept separate from `origin` on purpose. A memory aid is a way to remember the modern shape. It is not a claim about history, and the text says so.

If you spot an error, please open an issue with a reference.

## License

- **Data** (`data/`): [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Reuse it for anything, including commercial work, with credit. A suitable credit line: "Character data from chinesecharacterstory.com, CC BY 4.0."
- **Code** (`examples/`, `validate.py`): MIT, see [LICENSE](LICENSE).
