# Notion Taxonomy Reference

For database/page operations, run `ntn api` with `NOTION_API_VERSION=2022-06-28` unless the config specifies another version.

## Goal

Use the user's Notion taxonomy data source as the source of truth for classification.

## First-use requirement

The user must provide the taxonomy data source on first use. Persist it in:

```text
~/.config/alma/knowledge-capture/config.json
```

Field:

```json
{
  "notion": {
    "taxonomy_data_source": "..."
  }
}
```

After it is stored, always read from config. Do not ask again unless invalid/missing.

## Access method

Use Notion CLI `ntn` only.

Before reading taxonomy:

```bash
command -v ntn
ntn --help
```

If not logged in, ask user to run:

```bash
ntn login
```

Use `ntn` help/output to discover the correct data source query command.

## Expected taxonomy structure

The taxonomy data source may be structured in different ways. Detect schema intelligently.

Possible layouts:

1. Rows are labels, with a `Dimension` property and `Label` property.
2. Each dimension is a Notion property with select/multi-select options.
3. A table where columns are dimensions and rows list labels.

Common dimensions:

- 模态 / modality: text, image, audio, video, mixed, document
- 用途 / usage: 学习, 工具, 灵感, 研究, 项目参考, 决策, 素材, 娱乐
- 行业领域 / industry: AI, SaaS, 教育, 金融, 医疗, 消费, 游戏, 开发者工具, 内容创作, etc.
- 细分领域 / subdomain: LLM, Agent, RAG, UX, Growth, Workflow Automation, etc.
- 内容类型 / content_type: 文章, 帖子, 论文, 工具, 教程, 视频, 讨论, 案例, 产品页, 文档
- 知识阶段 / knowledge_stage: 发现, 理解, 应用, 验证, 沉淀
- 可执行性 / actionability: low, medium, high
- 来源质量 / source_quality: primary, credible, community, opinion, unknown

## Classification rules

- Prefer existing dimensions.
- Prefer existing labels.
- Multi-select is allowed when content spans multiple labels.
- Do not create a new dimension unless user explicitly asks.
- Add new labels only inside existing dimensions and only when necessary.
- New labels should be stable, reusable, and not overly specific.

Bad new labels:

- "那篇很好的文章"
- "2026年6月看到的AI东西"
- "某个作者的观点"

Good new labels:

- "AI 工作流"
- "知识管理"
- "多模态理解"
- "自动化编排"
- "产品洞察"

## New label update protocol

When adding a label:

1. Identify the dimension.
2. Explain why existing labels are insufficient.
3. Add label to the taxonomy data source through `ntn`.
4. Record update in summary:

```markdown
## Taxonomy Updates

- Dimension: 用途
- Added label: 项目参考
- Reason: Existing labels did not distinguish reusable implementation references from general learning material.
```

## Output shape

```json
{
  "modality": ["text", "image"],
  "usage": ["学习", "项目参考"],
  "industry": ["AI"],
  "subdomain": ["知识管理", "自动化编排"],
  "content_type": "文章",
  "knowledge_stage": ["发现", "理解"],
  "actionability": "high",
  "source_quality": "community",
  "tags": ["AI总结", "Notion", "自动化"],
  "new_taxonomy_labels": []
}
```
