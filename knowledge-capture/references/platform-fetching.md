# Platform Fetching Reference

## Detection

Detect by URL host, path, embed metadata, and visible page structure.

Common platform families:

- General web article/blog/news
- WeChat official account / 微信公众号
- Zhihu / 知乎
- Xiaohongshu / 小红书
- X/Twitter
- YouTube
- Bilibili
- GitHub
- arXiv / papers
- Reddit / Hacker News
- Notion public page
- Substack / Medium / Ghost blogs
- PDF/document links
- Product/tool pages

## Default fallback order

1. Platform-specific skill/tool if available.
2. Browser-readable page extraction.
3. Fetch HTML and parse metadata/readability body.
4. OCR screenshots when text is not directly extractable.
5. Ask user for exported content only when access is blocked.

## General web articles

Extract:

- canonical URL
- title
- author
- publish/update time
- body text
- headings
- tables/lists/code blocks
- all inline images and captions
- outbound references when important

Prefer readability extraction, then browser DOM text, then screenshot OCR.

## WeChat official account / 微信公众号

Use single-article extraction only. Do not design this as a bulk crawler.

Recommended fetching order:

1. HTTP request with a WeChat mobile User-Agent. This is often more reliable than browser automation for `mp.weixin.qq.com/s/...` links.
2. Extract article HTML directly from `#js_content`.
3. Extract title from `#activity-name`, account name from `#js_name`, and publish time from visible DOM or script variables such as `ct` when available.
4. Localize images from `data-src` / `src` instead of hotlinking WeChat CDN URLs.
5. If lightweight HTTP fails, try single-article community tools such as `wechat-article-to-markdown` or `wechatmp2markdown --image=save`.
6. If the article is visible only in the user's normal environment, ask the user to open it in WeChat/Desktop WeChat and export PDF/MHTML, copy text, or provide screenshots for OCR.
7. Use browser automation only as a later fallback. If a captcha, security check, login wall, or abnormal environment page appears, stop and ask for user-provided export instead of retrying aggressively.
8. If the original link is inaccessible, optionally search Sogou WeChat by article title/account name for an indexed temporary link, but treat it as unreliable.

Common constraints:

- Desktop/web automation may be blocked even when lightweight HTTP succeeds.
- There is no stable public API for arbitrary WeChat official account articles. Official APIs are mainly for accounts the user owns or manages.
- Images often contain important diagrams/screenshots and must not be treated as decorative.
- WeChat image URLs may expire or reject hotlinking; save images locally whenever possible.

Suggested HTTP headers for first attempt:

```text
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47 NetType/WIFI Language/zh_CN
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Referer: https://mp.weixin.qq.com/
```

Extract:

- canonical URL / final redirected URL
- title
- account name
- publish time if visible or derivable from page variables
- full article body from `#js_content`
- all inline images from `data-src` / `src` with local copies when possible
- image OCR/vision notes for screenshots, charts, posters, or image-heavy articles
- embedded media placeholders and available metadata
- QR/contact blocks may be marked as boilerplate unless semantically important

Recommended community tools:

- `wechat-article-to-markdown` for single public article URL to Markdown/images.
- `wechatmp2markdown --image=save` for Markdown with local image saving.

Failure handling:

- Record whether HTTP mobile UA, community tool, browser rendering, Sogou search, and user export were attempted.
- Do not attempt captcha bypass, credential reuse, proxy/account pools, or bulk crawling.

## Zhihu

Extract:

- question title
- answer/article author
- answer body
- vote/comment metadata if visible
- images
- referenced links

For discussions, keep enough context to understand the argument.

## Xiaohongshu / 小红书

Use single-note extraction by URL or note ID. Prefer the existing Xiaohongshu skill/tool when available, otherwise use the user's visible browser session. Do not design this as a bulk crawler.

Extract:

- note title/body
- author/account
- publish time if visible
- hashtags/topics
- image carousel with local copies whenever possible
- video metadata and transcript via ASR when available
- engagement metadata if visible, such as likes/favorites/comments
- 1-2 high-value related comments when available
- child comments/replies under those high-value comments when they add context
- links, product names, locations, account mentions, or external references mentioned in comments

High-value comment selection criteria:

- Adds factual context, correction, source, data point, price, location, product detail, or operational experience.
- Contains a useful link, handle, keyword, follow-up question, or author reply.
- Represents a meaningful disagreement or caveat that changes interpretation of the note.
- Has strong visible engagement only when the content is actually informative.

Comment handling rules:

- Preserve comment author display name, comment text, visible time/region if present, like count if visible, and parent-child relationship.
- Keep comments separate from the original note body in summaries.
- Do not over-collect comments. Aim for 1-2 high-value threads, including selected child replies.
- If comments are unavailable because login/access is required, record this as an extraction limitation.

Images are often the main content. Do not treat them as decorative. Run OCR/vision on image-heavy notes, posters, screenshots, charts, menus, itineraries, and product images.

## X/Twitter

Use single-post/thread extraction by URL. Avoid paid official API as the default. Prefer oEmbed/public page extraction, specialized media tools, or the user's authenticated browser session when needed.

Extract:

- full post/thread text
- author handles/display names
- timestamps
- quoted posts when relevant
- reposted/embedded context if visible and semantically important
- images/GIF/video transcript when available
- linked article previews and expanded outbound URLs when possible
- 1-2 high-value related comments/replies when available
- child replies under those high-value comments when they add useful context
- quote posts / quote replies that materially change interpretation
- links, handles, cited sources, screenshots, or external references from replies/quotes

High-value reply/quote selection criteria:

- Adds factual context, correction, source, data point, implementation detail, or firsthand experience.
- Contains a useful external link, cited source, screenshot, code snippet, account mention, or thread continuation.
- Is an author reply that clarifies the original post.
- Represents a meaningful disagreement, caveat, or alternative interpretation.
- Has strong visible engagement only when the reply itself is informative.

Reply/thread handling rules:

- Preserve ordering for the original thread.
- Keep selected replies/quotes separate from the original post body.
- Preserve parent-child relationships for selected reply chains.
- Do not scrape the whole reply tree. Aim for 1-2 high-value reply/quote threads.
- If replies/quotes require login or are blocked, record this as an extraction limitation.

For threads, preserve order. For discussions, distinguish original author content from community replies and quote commentary.

## YouTube

Extract:

- title
- channel
- URL
- description
- captions/transcript via ASR/caption tools
- chapter timestamps if available
- key frames/images if visually important

If official captions exist, prefer them. Otherwise use ASR.

## Bilibili

Extract:

- title
- uploader
- description
- subtitles/danmaku only if relevant
- transcript via ASR if subtitles unavailable
- key frames/images if visually important

## GitHub

Extract:

- repo name/URL
- README
- docs relevant to link
- stars/license/language if useful
- issue/PR discussion if URL points to issue/PR
- code snippets only when relevant

## arXiv / papers / PDFs

Extract:

- title
- authors
- abstract
- sections
- figures/tables with captions
- references when useful
- PDF text

Images/figures must be read when relevant to the paper's contribution.

## Reddit / Hacker News

Extract:

- post title/body/link
- author/community
- top comments when they add insight
- discussion structure

Summaries should distinguish original content from community commentary.

## Product/tool pages

Extract:

- product name
- value proposition
- features
- pricing/limits if visible
- target users/use cases
- screenshots/images
- docs links if relevant

## Failure notes

Always record:

- what was attempted
- why extraction was partial
- what user can provide to improve extraction
