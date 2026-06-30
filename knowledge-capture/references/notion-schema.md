# Notion Standard Schema Reference

This skill uses two Notion data sources created and controlled by Alma:

1. `Alma Knowledge Taxonomy` — taxonomy/classification labels.
2. `Alma Knowledge Capture` — captured content records.

If the user provides existing data sources that do not match these schemas, skip Notion read/write for that part and continue local Markdown generation only. Do not try to guess incompatible schemas.

For database/page operations, run `ntn api` with `NOTION_API_VERSION=2022-06-28` unless the config specifies another version.

## Compatibility check

A data source is compatible only if it contains the required properties below with matching semantic roles.

Property names may be bilingual aliases only if explicitly listed here. Otherwise treat as incompatible.

## Taxonomy data source: `Alma Knowledge Taxonomy`

Required properties:

| Property | Type | Required | Purpose |
|---|---|---:|---|
| `Label` | title | yes | Taxonomy label name |
| `Dimension` | select | yes | Human-readable dimension |
| `Dimension Key` | select | yes | Stable machine key |
| `Description` | rich_text | no | Meaning/scope of label |
| `Aliases` | multi_select | no | Synonyms or Chinese/English aliases |
| `Status` | select | yes | `Active`, `Deprecated` |
| `Source` | select | yes | `Seed`, `User`, `Alma` |
| `Reason` | rich_text | no | Why this label exists or was added |
| `Sort` | number | no | Optional ordering |
| `Created Time` | created_time | no | Notion auto timestamp |
| `Last Edited Time` | last_edited_time | no | Notion auto timestamp |

Required `Dimension Key` options:

- `modality`
- `usage`
- `industry`
- `subdomain`
- `content_type`
- `knowledge_stage`
- `actionability`
- `source_quality`
- `tag`

Recommended initial labels:

```json
[
  {"Label":"文本","Dimension":"模态","Dimension Key":"modality"},
  {"Label":"图片","Dimension":"模态","Dimension Key":"modality"},
  {"Label":"音频","Dimension":"模态","Dimension Key":"modality"},
  {"Label":"视频","Dimension":"模态","Dimension Key":"modality"},
  {"Label":"混合内容","Dimension":"模态","Dimension Key":"modality"},
  {"Label":"学习","Dimension":"用途","Dimension Key":"usage"},
  {"Label":"工具","Dimension":"用途","Dimension Key":"usage"},
  {"Label":"项目参考","Dimension":"用途","Dimension Key":"usage"},
  {"Label":"研究","Dimension":"用途","Dimension Key":"usage"},
  {"Label":"灵感","Dimension":"用途","Dimension Key":"usage"},
  {"Label":"决策","Dimension":"用途","Dimension Key":"usage"},
  {"Label":"AI","Dimension":"行业领域","Dimension Key":"industry"},
  {"Label":"开发者工具","Dimension":"行业领域","Dimension Key":"industry"},
  {"Label":"内容创作","Dimension":"行业领域","Dimension Key":"industry"},
  {"Label":"教育","Dimension":"行业领域","Dimension Key":"industry"},
  {"Label":"Agent","Dimension":"细分领域","Dimension Key":"subdomain"},
  {"Label":"LLM Runtime","Dimension":"细分领域","Dimension Key":"subdomain"},
  {"Label":"知识管理","Dimension":"细分领域","Dimension Key":"subdomain"},
  {"Label":"自动化编排","Dimension":"细分领域","Dimension Key":"subdomain"},
  {"Label":"成本优化","Dimension":"细分领域","Dimension Key":"subdomain"},
  {"Label":"文章","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"帖子","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"论文","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"工具","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"教程","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"视频","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"讨论","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"案例","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"产品页","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"文档","Dimension":"内容类型","Dimension Key":"content_type"},
  {"Label":"发现","Dimension":"知识阶段","Dimension Key":"knowledge_stage"},
  {"Label":"理解","Dimension":"知识阶段","Dimension Key":"knowledge_stage"},
  {"Label":"应用","Dimension":"知识阶段","Dimension Key":"knowledge_stage"},
  {"Label":"验证","Dimension":"知识阶段","Dimension Key":"knowledge_stage"},
  {"Label":"沉淀","Dimension":"知识阶段","Dimension Key":"knowledge_stage"},
  {"Label":"低","Dimension":"可执行性","Dimension Key":"actionability"},
  {"Label":"中","Dimension":"可执行性","Dimension Key":"actionability"},
  {"Label":"高","Dimension":"可执行性","Dimension Key":"actionability"},
  {"Label":"一手来源","Dimension":"来源质量","Dimension Key":"source_quality"},
  {"Label":"可信来源","Dimension":"来源质量","Dimension Key":"source_quality"},
  {"Label":"社区讨论","Dimension":"来源质量","Dimension Key":"source_quality"},
  {"Label":"观点判断","Dimension":"来源质量","Dimension Key":"source_quality"},
  {"Label":"未知","Dimension":"来源质量","Dimension Key":"source_quality"}
]
```

## Capture data source: `Alma Knowledge Capture`

Required properties:

| Property | Type | Required | Purpose |
|---|---|---:|---|
| `Title` | title | yes | Record title |
| `Original URL` | url | yes | Source URL |
| `Platform` | select | yes | Source platform |
| `Author` | rich_text | no | Author/account/channel |
| `Published At` | date | no | Original publish time |
| `Captured At` | date | yes | Capture time |
| `Content Type` | select | yes | Article/post/paper/tool/video/etc. |
| `Modality` | multi_select | yes | Text/image/audio/video/mixed |
| `Usage` | multi_select | yes | Learning/tool/project reference/etc. |
| `Industry` | multi_select | no | Industry labels |
| `Subdomain` | multi_select | no | Subdomain labels |
| `Knowledge Stage` | multi_select | no | Discovery/understanding/application/etc. |
| `Actionability` | select | no | Low/medium/high |
| `Source Quality` | select | no | Source quality |
| `Tags` | multi_select | no | Free labels from taxonomy `tag` dimension |
| `Summary` | rich_text | yes | Short summary, <= 2000 chars |
| `Key Takeaways` | rich_text | no | Compact takeaways, <= 2000 chars |
| `Original Markdown Path` | rich_text | yes | Local original.md path |
| `Summary Markdown Path` | rich_text | yes | Local summary.md path |
| `Assets Path` | rich_text | no | Local assets folder |
| `Processing Status` | select | yes | `Processed`, `Partial`, `Failed` |
| `Extraction Notes` | rich_text | no | Limitations/errors |
| `Taxonomy Updates` | rich_text | no | Labels added during processing |
| `Capture ID` | rich_text | yes | Local capture ID |

Notion page body should contain the full summary and local file references. Rich text properties should stay concise because Notion property values have practical length limits.

## Strict behavior

- If taxonomy data source lacks required taxonomy properties, skip taxonomy read/update and classify locally only.
- If capture data source lacks required capture properties, skip Notion writeback and keep local files.
- Do not mutate user-provided incompatible tables to fit this schema unless user explicitly asks.
- Prefer creating the two standard Alma data sources instead of adapting random existing tables.
