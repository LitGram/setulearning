# Biology graphics pilot

Local Flutter preview uses the actual bundled biology chapter JSON and shared ContentBlockWidget. It opens in figures-only mode, with a toggle to read the full original chapter. This entry point is for local review; it does not change the Android home screen.

- Biology Part 1, chapter 3: plant/animal cells, bilingual label glossary and comparison notes.
- Biology Part 1, chapter 4: mitosis stages, chromosome count example and recall question.
- Biology Part 2, chapter 3: digestive organs, bilingual food route and accessory-organ distinction.
- Tap image to open InteractiveViewer; pinch/drag or use zoom buttons (1x–5x), reset and close.
- All three complete original chapters and MCQs preserved, checked with canonical pre-pilot chapter hashes.

Built-in image_gen generated the three PNG assets in assets/images/biology_*.png. Diagrams use readable English labels; Hindi terms and learning guidance are selectable reader text below each image. They are schematic illustrations, not to scale. These are a pilot, not all biology chapters.

## Final prompt set

Cells: Original textbook comparison of a plant cell with wall, membrane, large central vacuole, chloroplasts, nucleus, mitochondria and cytoplasm; animal cell with membrane, nucleus, mitochondria, small vesicles and cytoplasm, without wall or chloroplasts. White background, clean coloured illustration, large English labels and accurate leader lines. Correction: move both Nucleus endpoints from dark nucleolus to surrounding light-purple nucleoplasm, preserving other features.

Mitosis: Four labelled panels (Prophase, Metaphase, Anaphase, Telophase and cytokinesis), 2n=4 animal-cell model. Four duplicated X chromosomes before separation; four daughter chromosomes at each pole after separation; four chromosomes in each daughter cell. Large typography, spindle fibres, white background, and caption explaining maintained chromosome number.

Digestion: Isolated digestive organs only, no human figure, on white background. Mouth connected to oesophagus and J-shaped stomach; liver at viewer left, gallbladder below liver, pancreas below/behind stomach connected to duodenum, small intestine framed by large intestine and rectum below. Precise leader lines and large English labels. Caption distinguishes food passage through alimentary canal from secretions of accessory organs. The first torso version failed the image generator safety check; the isolated-organ version succeeded.

## Accuracy checks

Visually checked label endpoints, plant-only structures, mitosis stage order and chromosome counts, and digestive-organ positions. The cell nucleus label was corrected before use. Bilingual notes clarify that not all plant cells have chloroplasts, DNA duplicates in S phase, and food does not pass through liver/pancreas. Reference texts:
- cells: https://ncert.gov.in/textbook/pdf/kebo108.pdf
- mitosis: https://openstax.org/books/biology-2e/pages/10-2-the-cell-cycle
- digestion: https://openstax.org/books/biology-2e/pages/34-1-digestive-systems

## Repeatable content insertion

assets/biology_graphics_manifest.json stores each insertion anchor, image/caption/notes, and complete pre-pilot chapter hash.

Run `python tools/apply_biology_graphics.py --check` to verify figures, order, and preservation of all existing content/MCQs. Run without --check after a source reimport to reapply figures. If the original source chapter changes, the script requires anchor/source review instead of silently applying stale content.

## Local launch

`flutter build web --target lib/biology_preview.dart --output artifacts/biology-preview --no-web-resources-cdn`

`python -m http.server 8765 --bind 127.0.0.1 --directory artifacts/biology-preview`

Open http://127.0.0.1:8765. No APK is built for this pilot.
