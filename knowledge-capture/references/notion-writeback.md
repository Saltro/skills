# Notion Writeback Reference

For database/page operations, run `ntn api` with `NOTION_API_VERSION=2022-06-28` unless the config specifies another version.

## Scope

Use Notion CLI `ntn` only. Do not use direct Notion REST API or MCP for this skill unless the user revises the skill.

## CLI setup

Install if missing:

```bash
curl -fsSL https://ntn.dev | bash
```

Login:

```bash
ntn login
```

After login, use `ntn` to send requests and access data sources.

## Config source

Read:

```text
~/.config/alma/knowledge-capture/config.json
```

Required fields:

```json
{
  "notion": {
    "mode": "ntn",
    "cli": "ntn",
    "taxonomy_data_source": "...",
    "capture_data_source": "..."
  }
}
```

If `taxonomy_data_source` or `capture_data_source` is missing, ask the user to provide it and persist it before continuing.

## Data source access

Use `ntn --help` and relevant `ntn` subcommands to:

1. Inspect/list data sources if needed.
2. Fetch rows/items from the taxonomy data source.
3. Create/update rows/items in taxonomy and capture data sources.
4. Store returned Notion page/record URL or ID locally.

Because `ntn` command surface may evolve, inspect help first instead of guessing exact flags.

## Property mapping

Do not assume exact property names. Map intelligently.

Common target properties:

- Title / 名称 / 标题
- URL / Original URL / 原链接
- Platform / Source / 来源平台
- Content Type / 内容类型
- Summary / 摘要
- Key Takeaways / 关键要点
- Tags / 标签
- Modality / 模态
- Usage / 用途
- Industry / 行业领域
- Subdomain / 细分领域
- Original Markdown / 原文 MD
- Summary Markdown / 总结 MD
- Raw Content / 原文内容
- Captured Time / 收录时间
- Processing Status / 处理状态
- Notes / 备注

If a property is missing, write critical data into page body/content rather than failing entirely.

## Page/body structure

Recommended content body:

```markdown
## Source

- URL: ...
- Platform: ...
- Author: ...
- Published: ...
- Captured: ...

## Summary

...

## Key Takeaways

...

## Classification

...

## Local Files

- Original: ...
- Summary: ...
- Assets: ...

## Extraction Notes

...
```

## Writeback order

1. If classification created new labels, update taxonomy data source first.
2. Create one capture record in `capture_data_source`.
3. Include original URL and local Markdown paths.
4. Add summary and classification tags.
5. Save Notion returned URL/ID to:

```text
<workspace_root>/<capture_id>/notion-record.txt
```

## Failure handling

If writeback fails, create:

```text
<workspace_root>/<capture_id>/notion-writeback-error.md
```

Include:

- `ntn` command attempted, with secrets redacted if any
- error message
- config fields present/missing
- local files successfully created
- next fix needed
