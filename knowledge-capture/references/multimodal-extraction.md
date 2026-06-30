# Multimodal Extraction Reference

## Principle

The original record must preserve all meaningful modalities. Do not reduce mixed media to only text.

## Images

For every meaningful image:

1. Save the image to `assets/` when technically possible.
2. Record original image URL/source.
3. Run OCR when text may be present.
4. Run visual description when diagrams, screenshots, charts, UI, photos, memes, or product visuals matter.
5. Add the result to `original.md` under Image Inventory.

Image entry format:

```markdown
### Image N

- Source: ...
- Local path: `assets/...`
- Role: diagram / screenshot / chart / photo / illustration / meme / unknown
- OCR:
  > ...
- Visual reading:
  > ...
- Notes:
  > ...
```

Do not say "image attached" without reading it, unless no image-reading tool is available. If unavailable, state the limitation.

## Audio

For audio files or audio embedded in media:

1. Save or reference the audio source.
2. Run ASR.
3. Save transcript as `asr-transcript.md`.
4. Preserve timestamps if available.
5. Include transcript summary in `original.md`.

## Video

For videos:

1. Prefer official captions/subtitles.
2. If unavailable, run ASR.
3. Capture title/channel/description.
4. Extract chapters/timestamps when available.
5. For visual-heavy videos, capture representative frames or screenshots and read them as images.

## Documents

For PDFs/slides/docs:

- Extract text in reading order.
- Preserve headings and page numbers when possible.
- Extract tables as Markdown.
- Extract figures and captions.
- OCR scanned pages.

## Completeness checklist

Before summarizing, verify:

- [ ] Main text extracted
- [ ] Metadata captured
- [ ] Images inventoried and read
- [ ] Audio/video transcribed if present
- [ ] Files saved locally or limitations recorded
- [ ] Original source URL preserved
