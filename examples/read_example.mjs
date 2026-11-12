// Build flashcards (front: character, back: pinyin + meaning + words) from the data file.
// Usage: node examples/read_example.mjs
import { readFileSync } from "node:fs";

const data = JSON.parse(readFileSync(new URL("../data/characters.json", import.meta.url), "utf8"));

const cards = data.characters.map((c) => ({
  front: c.hanzi,
  back: `${c.pinyin} (tone ${c.tone}) - ${c.meaning}; ${c.strokes} strokes`,
  words: c.words.map((w) => `${w.zh} ${w.pinyin}: ${w.en}`),
}));

for (const card of cards) {
  console.log(`${card.front}  |  ${card.back}`);
  for (const w of card.words) console.log(`      ${w}`);
}
console.log(`\n${cards.length} cards, ${data.characters.reduce((n, c) => n + c.quiz.length, 0)} quiz questions`);
