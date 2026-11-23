const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const root = path.resolve(__dirname, '..');
const book = JSON.parse(fs.readFileSync(path.join(root, 'assets/content/rassetu/rassetu_book3.json'), 'utf8'));
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'artifacts/rassetu_series/book3_completion_manifest.json'), 'utf8'));
const gallery = fs.readFileSync(path.join(root, 'lib/rassetu_graphics_preview.dart'), 'utf8');
const chapterById = new Map(book.chapters.map(c => [c.id, c]));
const fail = message => { throw new Error(message); };
const stable = value => {
  const sort = v => Array.isArray(v) ? v.map(sort) : v && typeof v === 'object'
    ? Object.fromEntries(Object.keys(v).sort().map(k => [k, sort(v[k])])) : v;
  return crypto.createHash('sha256').update(JSON.stringify(sort(value))).digest('hex');
};
const snapshot = chapter => {
  const content = chapter.content, remove = new Set();
  content.forEach((block, i) => {
    if (block?.type !== 'image') return;
    remove.add(i);
    for (const j of [i + 1, i - 1]) {
      if (j >= 0 && j < content.length && content[j]?.type === 'callout' &&
          String(content[j].value || '').startsWith('**चित्र से सीखें')) { remove.add(j); break; }
    }
  });
  return { ...chapter, content: content.filter((_, i) => !remove.has(i)) };
};

if (book.chapters.length !== 44) fail(`Expected 44 Book 3 chapter records; found ${book.chapters.length}`);
if (manifest.chapters.length !== 48 || manifest.placementCount !== 48) fail(`Expected 48 manifest placements; found ${manifest.chapters.length}`);
if (manifest.distinctVisualAssets !== 24 || manifest.distinctNewAssets !== 22) fail('Unexpected distinct asset totals in manifest');
const recordsByChapter = new Map();
for (const entry of manifest.chapters) {
  const chapter = chapterById.get(entry.chapter);
  if (!chapter) fail(`Unknown manifest chapter ${entry.chapter}`);
  const base = snapshot(chapter);
  if (stable(base) !== entry.originalChapterSha256) fail(`Chapter content hash mismatch: ${entry.chapter}`);
  if (stable(base.content) !== entry.sourceContentSha256) fail(`Source content/MCQ hash mismatch: ${entry.chapter}`);
  const anchorIndexes = [];
  chapter.content.forEach((b, i) => { if (b?.type === 'text' && b.value.startsWith(entry.anchor)) anchorIndexes.push(i); });
  if (anchorIndexes.length !== 1) fail(`${entry.chapter}: anchor count is ${anchorIndexes.length}`);
  const imageIndexes = [];
  chapter.content.forEach((b, i) => { if (b?.type === 'image' && b.value === entry.image) imageIndexes.push(i); });
  if (imageIndexes.length !== 1) fail(`${entry.chapter}: expected one ${entry.image}, found ${imageIndexes.length}`);
  const index = imageIndexes[0], note = chapter.content[index + 1];
  if (index <= anchorIndexes[0] || chapter.content.slice(anchorIndexes[0] + 1, index).some(b => b?.type !== 'image' && !(b?.type === 'callout' && String(b.value).startsWith('**चित्र से सीखें')))) fail(`${entry.chapter}: image is not within its exact anchor's graphics block`);
  if (note?.type !== 'callout' || !String(note.value).startsWith('**चित्र से सीखें')) fail(`${entry.chapter}: missing adjacent learning note for ${entry.image}`);
  const assetPath = path.join(root, 'assets/images', entry.image);
  if (!fs.existsSync(assetPath)) fail(`Missing image ${entry.image}`);
  const assetHash = crypto.createHash('sha256').update(fs.readFileSync(assetPath)).digest('hex');
  if (assetHash !== entry.assetSha256) fail(`Image hash mismatch: ${entry.image}`);
  (recordsByChapter.get(entry.chapter) || recordsByChapter.set(entry.chapter, []).get(entry.chapter)).push(entry);
}
const book3Images = new Set();
for (const chapter of book.chapters) for (const block of chapter.content) {
  if (block?.type === 'image') {
    book3Images.add(block.value);
    if (!fs.existsSync(path.join(root, 'assets/images', block.value))) fail(`${chapter.id} references missing ${block.value}`);
  }
}
if (book3Images.size !== 24) fail(`Expected 24 distinct images in Book 3; found ${book3Images.size}`);
const galleryMatches = [...gallery.matchAll(/\('([^']+\.webp)'\s*,/g)].map(m => m[1]);
if (galleryMatches.length !== 99) fail(`Expected 99 gallery assets; found ${galleryMatches.length}`);
if (new Set(galleryMatches).size !== galleryMatches.length) fail('Gallery contains duplicate asset entries');
for (const image of galleryMatches) if (!fs.existsSync(path.join(root, 'assets/images', image))) fail(`Gallery references missing ${image}`);
if (!gallery.includes("const Text('99 graphics across Books 1–6 · Select and inspect')")) fail('Gallery count label is stale');
console.log(JSON.stringify({
  status: 'PASS', book3ChapterRecords: book.chapters.length,
  manifestPlacements: manifest.chapters.length,
  newPlacements: manifest.newPlacementCount,
  book3DistinctVisuals: book3Images.size,
  newVectors: manifest.newVectorAssets,
  newGeneratedScenes: manifest.newGeneratedSceneAssets,
  galleryDistinctAssets: new Set(galleryMatches).size,
  sourceAndMcqHashes: 'all matched', anchors: 'all unique', assets: 'all exist and hash-match'
}, null, 2));
