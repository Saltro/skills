---
name: knowledge-capture
description: Turn user-shared content into a structured Notion knowledge record.
---

# Skill: 

Turn user-shared content into a structured Notion knowledge record.

## Goal

Workflow:

1. User sends a link, raw content, image, audio, video, document, or mixed content.
2. If it is a link, identify platform and fetch complete content with platform-specific tools.
3. If content includes images, read every image fully and preserve image assets.
4. If content includes audio/video, use ASR to transcribe and preserve transcript.
5. Save the complete original material as Markdown, including original URL, text, images, image readings, ASR transcript, and extraction notes.
6. Read the user's Notion taxonomy/classification data source using Notion CLI `ntn`.
7. Classify/tag the content by dimensions such as modality, usage, industry, subdomain, content type, knowledge stage, actionability, source quality, etc.
8. Prefer existing taxonomy labels. If a dimension lacks a precise label, add a new label inside that dimension and update the Notion taxonomy data source through `ntn`.
9. Generate a purpose-aware summary Markdown file.
10. Write original link/path/content, summary, and classification tags into the user's Notion capture data source using `ntn`.

## Notion-only constraint

This skill currently supports Notion only.

Use Notion CLI `ntn` for all Notion operations. Do not use direct Notion REST API or Notion MCP unless the user explicitly changes this skill later.

For database-style operations, set `NOTION_API_VERSION=2022-06-28` when calling `ntn api`. This keeps Notion database/page APIs stable and avoids newer data-source schema differences.

If `ntn` is not installed, install it:

```bash
curl -fsSL https://ntn.dev | bash
```

Then ask the user to complete login:

```bash
ntn login
```

After login, use `ntn` to send requests and access Notion data sources.

## First-run setup

Config path:

```text
~/.config/alma/knowledge-capture/config.json
```

If config is missing or incomplete, ask the user for the missing Notion data source IDs/names and stop before Notion read/write operations.

Required user-provided fields on first use if Alma has not created the standard tables yet:

- `taxonomy_data_source`: Notion data source/database/table for taxonomy/classification system.
- `capture_data_source`: Notion data source/database/table where processed content records should be written.

Preferred path: create two standard Notion data sources named `Alma Knowledge Taxonomy` and `Alma Knowledge Capture` using `references/notion-schema.md`, then persist their IDs. If the user provides existing tables that do not match the standard schema, skip Notion taxonomy/writeback and continue local Markdown only.

Optional fields:

- `workspace_root`: local library path. Default: `~/.config/alma/knowledge-capture/library`
- `notion_cli`: CLI command name. Default: `ntn`

Persist the provided config to:

```text
~/.config/alma/knowledge-capture/config.json
```

Recommended config shape:

```json
{
  "notion": {
    "mode": "ntn",
    "cli": "ntn",
    "api_version": "2022-06-28",
    "taxonomy_data_source": "",
    "capture_data_source": ""
  },
  "workspace_root": "~/.config/alma/knowledge-capture/library",
  "output": {
    "target": "notion",
    "save_original_md": true,
    "save_summary_md": true
  }
}
```

Do not ask again once the values are stored, unless the config is missing, invalid, or the user asks to change it.

## References to read before execution

Always read these files before running the workflow:

- `/Users/bytedance/.config/alma/skills/knowledge-capture/references/notion-schema.md`
- `/Users/bytedance/.config/alma/skills/knowledge-capture/references/platform-fetching.md`
- `/Users/bytedance/.config/alma/skills/knowledge-capture/references/multimodal-extraction.md`
- `/Users/bytedance/.config/alma/skills/knowledge-capture/references/notion-taxonomy.md`
- `/Users/bytedance/.config/alma/skills/knowledge-capture/references/summary-methods.md`
- `/Users/bytedance/.config/alma/skills/knowledge-capture/references/notion-writeback.md`

Use templates:

- `/Users/bytedance/.config/alma/skills/knowledge-capture/templates/original.md`
- `/Users/bytedance/.config/alma/skills/knowledge-capture/templates/summary.md`

## Main workflow

### 0. Ensure Notion CLI is ready

Check `ntn`:

```bash
command -v ntn
ntn --help
```

If missing, install:

```bash
curl -fsSL https://ntn.dev | bash
```

If not logged in or requests fail due to auth, ask the user to run:

```bash
ntn login
```

Do not continue Notion operations until login works.

### 1. Load or create config

Check config:

```bash
test -f ~/.config/alma/knowledge-capture/config.json && cat ~/.config/alma/knowledge-capture/config.json
```

If missing/incomplete, ask user for:

```text
taxonomy_data_source
capture_data_source
```

Then persist those values to config.

### 2. Normalize input

Create capture ID:

```text
YYYYMMDD-HHMMSS-short-slug
```

Create folders:

```text
<workspace_root>/<capture_id>/
<workspace_root>/<capture_id>/assets/
```

Save raw user input:

```text
<workspace_root>/<capture_id>/raw-input.txt
```

### 3. Detect content type/platform

Classify as URL, raw text, image, audio, video, document/file, or mixed content.

For URLs, detect platform using `references/platform-fetching.md`.

### 4. Fetch complete content

Capture:

- canonical URL
- title
- author/account/channel
- publish time
- platform/source
- full text body
- all visible image URLs/files and image descriptions/OCR
- all audio/video transcripts
- important comments/threads when relevant and available
- extraction timestamp
- extraction limitations/errors

Use available skills/tools first. If platform-specific extraction fails, fall back to browser rendering and visible text extraction.

### 5. Multimodal extraction

Follow `references/multimodal-extraction.md`.

Hard rules:

- Do not ignore images.
- Save every image asset when technically possible.
- Read images with OCR/vision tools if available.
- For audio/video, run ASR and save transcript.
- Preserve source URLs and local asset paths.

### 6. Save original Markdown

Write:

```text
<workspace_root>/<capture_id>/original.md
```

Use `templates/original.md`.

### 7. Read Notion taxonomy data source

First validate both configured data sources against `references/notion-schema.md`. If incompatible, skip Notion operations and continue local Markdown/classification only.

Use `ntn` and `taxonomy_data_source` from config to fetch the latest taxonomy table/data source.

Do not assume exact property names. Map columns intelligently.

Expected taxonomy dimensions may include:

- modality / 模态
- usage / 用途
- industry / 行业领域
- subdomain / 细分领域
- content_type / 内容类型
- knowledge_stage / 知识阶段
- actionability / 可执行性
- source_quality / 来源质量
- custom user dimensions

### 8. Classify and tag

Prefer existing labels. Add a new label inside an existing dimension only if all existing labels are insufficient.

Never create a new dimension unless the user explicitly asks.

Classification output shape:

```json
{
  "modality": [],
  "usage": [],
  "industry": [],
  "subdomain": [],
  "content_type": "",
  "knowledge_stage": [],
  "actionability": "",
  "source_quality": "",
  "tags": [],
  "new_taxonomy_labels": [
    {
      "dimension": "",
      "label": "",
      "reason": ""
    }
  ]
}
```

If new labels are needed, update taxonomy data source first through `ntn` and log the reason in the local summary.

### 9. Generate summary Markdown

Use `references/summary-methods.md`.

Write:

```text
<workspace_root>/<capture_id>/summary.md
```

Use `templates/summary.md`.

Required sections:

- 一句话结论
- 简明摘要
- 关键要点
- 重要证据/细节
- 对之洋的启发
- 可执行动作/项目想法/后续问题
- 局限与不确定性
- 使用的分类标签

### 10. Write back to Notion

Use `references/notion-writeback.md`.

Write one capture record to `capture_data_source` via `ntn`, containing:

- title
- original URL
- platform/source
- content type
- original Markdown path/link/content
- summary Markdown path/link/content
- summary
- key takeaways
- classification tags
- captured time
- processing status
- extraction notes

If Notion writeback fails:

- Keep local files.
- Create `notion-writeback-error.md`.
- Tell the user what succeeded and what needs fixing.

### 11. Final response

Return concisely:

- original Markdown path
- summary Markdown path
- Notion record link if created
- tags/categories used
- taxonomy additions, if any
- extraction limitations, if any

## Privacy/safety

- Never print secrets or auth material.
- Preserve provenance.
- If login/paywall/private access is required, ask the user to authorize access.
- Do not silently skip modalities.
