# Biology Book Two graphics

Completed 5 October 2026: **64 graphics in all 24 chapters** of Biology II (`vigyansetu_book6.json`).

The collection follows Biology I's mixed-media approach: **19 newly generated shaded textbook illustrations, one reused digestion illustration, and 44 editable schematics, process charts and comparison plates**. Every graphic has an English-labelled image, a Hindi caption and a Hindi learning note. The existing reader provides tap-to-zoom viewing.

The image service rejected male and female reproductive-anatomy requests, including an isolated internal-organ request. Those two figures are original anatomical schematics instead. All other planned anatomy images were generated successfully. No CLI image fallback was used.

## Content preservation and validation

- All 24 original complete chapter hashes matched after removing only the inserted graphic blocks. Titles, lesson text, worked examples and MCQs are preserved. The existing digestion pilot was replaced in place with the complete four-figure chapter set.
- Book One retains its 46 figures and original chapter baselines. The shared placement manifest now covers 40 chapters and 110 figures.
- 60 focused Flutter tests passed: graphics placement, all bundled-book schemas and chapter completeness, image decoding and phone-width zoom/open/reset/close.
- Focused static analysis found no issues in the preview or graphics tests.
- The local Flutter web review build succeeded. No Android APK was generated for this task.
- Book Two's compressed graphics total approximately **4.73 MiB**. Source PNGs and editable SVG masters remain outside bundled app assets.

## Figure review

Reviewed structures, compartment pointers, physiological arrows, stage order, inheritance probabilities and comparison labels. Corrected the nephron's cortical-capillary label, the antibody's joint heavy/light-chain antigen-binding regions, and the sarcomere's H-zone bracket. Corrected the antibiotic-selection chart's susceptible-cell colours and moved overlapping transport labels and the reproductive-tract note. The skeleton's radius/ulna and tibia/fibula endpoints were checked at full size.

Images are teaching models, not clinical diagnostic images. Source-book prose was preserved; this work does not constitute a new fact-check of every pre-existing book claim. The public-health graphic presents programme purposes rather than changing eligibility amounts or deadlines. The CPR graphic concerns adult sudden cardiac arrest and distinguishes its scope in the Hindi note.

Authoritative references used for targeted checks:

- [OpenStax: heart anatomy](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy)
- [OpenStax: kidney and nephron anatomy](https://openstax.org/books/anatomy-and-physiology-2e/pages/25-3-gross-anatomy-of-the-kidney)
- [OpenStax: ovarian reproductive system](https://openstax.org/books/anatomy-and-physiology-2e/pages/27-2-anatomy-and-physiology-of-the-ovarian-reproductive-system)
- [OpenStax: antibodies and binding domains](https://openstax.org/books/biology-2e/pages/42-3-antibodies)
- [CDC: malaria life cycle](https://www.cdc.gov/dpdx/malaria/)
- [American Red Cross: hands-only CPR](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/hands-only-cpr.html)
- [American Red Cross: CPR techniques and sequence](https://guidelines.redcross.org/guidelines-database/cpr-techniques-and-sequence/)
- [National Health Mission: vision](https://nhm.gov.in/vision.php?lang=1)
- [NHM: immunisation programme guidance](https://www.nhm.gov.in/New_Updates_2018/NHM_Components/Immunization/Guildelines_for_immunization/FAQ_on_Immunization_for_Program_Manager-English.pdf)
- [ABDM: consent and privacy principles](https://abdm.gov.in/static/media/Session%206%20-%20Digital%20health%20-%20Privacy%20%26%20Security.083a5b3e73ba533e321b.pdf)

## Reproduction

1. `python tools/plan_biology_book2.py`
2. `node tools/render_biology_book2.cjs`
3. `node tools/prepare_biology_book2.cjs`
4. `python tools/expand_biology_book2_manifest.py`
5. `python tools/apply_biology_graphics.py --check`

The raster source archive is `artifacts/biology_book2/source_images/`. The raster source manifest points to those archived PNGs for portable re-export and records the original generated paths as provenance. Figure briefs are `artifacts/biology_book2_figure_briefs.json`; placement and content-hash baselines are in `assets/biology_graphics_manifest.json` and `artifacts/biology_book2_completeness.json`.

## Review sheets

![Organisation, musculoskeletal anatomy, digestion and respiration](<D:/new projects/setu learning android app/artifacts/biology_book2/contact_1.jpg>)

![Circulation, lymph, kidneys and neurons](<D:/new projects/setu learning android app/artifacts/biology_book2/contact_2.jpg>)

![Nervous, sensory, endocrine and reproductive anatomy](<D:/new projects/setu learning android app/artifacts/biology_book2/contact_3.jpg>)

![Development, nutrition and infection](<D:/new projects/setu learning android app/artifacts/biology_book2/contact_4.jpg>)

![Pathogens, immunity, inheritance and hygiene](<D:/new projects/setu learning android app/artifacts/biology_book2/contact_5.jpg>)

![First aid, recovery, health programmes and revision](<D:/new projects/setu learning android app/artifacts/biology_book2/contact_6.jpg>)
