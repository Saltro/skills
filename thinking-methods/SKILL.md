---
name: thinking-methods
description: >-
  A toolbox of 15 structured thinking frameworks (first principles, contradiction
  analysis, MECE, 5-Why, thesis-antithesis-synthesis, six thinking hats, mental
  models, Pareto, Eisenhower matrix, falsifiability, reflexivity, misjudgment
  psychology, second-level thinking, black swan / antifragility, Gödel
  incompleteness) that help reason deeply and avoid shallow or biased conclusions.
  Use this skill whenever the user faces a complex decision, an open-ended
  strategy/analysis question, a root-cause investigation, a trade-off, a
  "should I / why / how to think about this" question, or explicitly asks for
  deep thinking, structured breakdown, multi-angle analysis, root cause, or
  bias-checking — even if they don't name a specific method. Do NOT use it for
  simple factual lookups, single-step tasks, or when the user just wants a quick
  direct answer.
---

# Thinking Methods

A curated set of thinking frameworks for reasoning about hard problems. The goal
is not to sound clever, but to reach conclusions that are less shallow, less
biased, and more robust than an off-the-cuff answer.

## Core principle: select, don't dump

There are 15 frameworks in `references/methods.md`. Applying all of them to every
question produces bloated, low-signal output. Instead, **diagnose the question,
use the minimum number of frameworks that changes the analysis, usually 2–4.**
Use one framework when it is sufficient. A focused analysis through the right
lens beats a shallow pass through several.

Only walk through all 15 if the user explicitly asks for "全量/走一遍所有方法" or a
"thinking audit".

## When it triggers

Reach for this skill on complex, open-ended reasoning — strategy calls,
trade-offs, root-cause hunts, "why is this happening / what should we do"
questions, or any request for deep, structured, or multi-angle thinking. Skip it
for lookups, one-step tasks, or when a quick direct answer is what's wanted.

## Workflow

### 1. Frame the question
State the real question in one sentence. If the user's phrasing is vague, name the
underlying decision or uncertainty. Note what a good answer would need to resolve.

### 2. Select frameworks
Match the question type to frameworks (see the selection map below and the fuller
descriptions in `references/methods.md`). Select 2–4 by default, or one for a
narrow problem. Use each only if it produces a distinct decision-relevant insight.
Framework names are optional: show them when the user asks for an audit or when
they make the reasoning easier to challenge.

### 3. Apply each framework in depth
For each selected framework, produce genuine analysis, not a definition. The value
is in the specific findings (the actual root cause, the actual key 20%, the actual
bias you might be under), not in naming the method. Merge overlapping findings
instead of repeating the same conclusion under different headings.

### 4. Synthesize
Frameworks often disagree. Reconcile them into a single coherent judgment. State
the conclusion, the confidence level, and what would change your mind. Do not
average incompatible conclusions: identify the assumption or decision criterion
that determines which one applies.

### 5. Surface the blind spot (always)
Close with what this analysis itself might be missing — the boundary of the current
framing (Gödel-style). This keeps the output honest rather than falsely complete.

## Failure handling

| Trigger | First response | If still unresolved |
|---|---|---|
| Key facts are missing | Separate known facts, assumptions, and unknowns; ask one question only if it can change the recommendation | Give conditional scenarios and specify the evidence that selects among them |
| Selected frameworks produce the same insight | Merge the finding and drop redundant framework sections | Use fewer frameworks; do not add methods to satisfy a target count |
| Frameworks conflict | Identify the assumptions, time horizon, or objective behind the conflict | Present the decision rule that would favor each conclusion |
| A framework yields no specific insight | Drop it silently | Reframe the question or choose a different lens |
| The user requests a quick answer | Give the conclusion, key reason, and main uncertainty; use frameworks internally | Offer deeper analysis only if it would change the decision |
| A high-impact recommendation depends on an unknown fact | Mark the recommendation provisional and identify the blocking fact | **🔴 CHECKPOINT · STOP:** ask for that fact before recommending an irreversible commitment |

## Selection map (question type → frameworks)

- **Root cause / "why did this happen"** → 5-Why, contradiction analysis, first principles
- **Strategy / decision under uncertainty** → second-level thinking, black swan/antifragility, reflexivity, thesis-antithesis-synthesis
- **Prioritization / "what to do first"** → Pareto (80/20), Eisenhower matrix, contradiction analysis
- **Structuring a messy problem** → MECE, first principles, six thinking hats
- **Evaluating a belief/claim** → falsifiability, misjudgment psychology, second-level thinking
- **Cross-domain / systemic problem** → multiple mental models, reflexivity, contradiction analysis
- **Checking my own reasoning** → misjudgment psychology, falsifiability, Gödel incompleteness

Read `references/methods.md` for each framework's description, key question,
application guidance, and common failure mode.

## Output format

Lead with the answer, not the framework inventory. Default shape:

```
## 综合判断
[conclusion · confidence · what would change my mind]

## 关键依据
[distinct findings, merged across frameworks]

## 下一步验证
[evidence or low-cost action that reduces the main uncertainty]

## 本分析的边界与盲区
[Gödel-style: what this framing itself may be missing]
```

Add `问题重述` when the user's framing is misleading or ambiguous. Add `选用的思维框架`
only when the user asks for methodology, an audit trail is useful, or framework
choice itself is debatable. Adapt depth to the decision; do not pad.

## Anti-pattern blacklist

- Do not force 3–5 frameworks when fewer are sufficient.
- Do not repeat one insight under several framework names.
- Do not substitute framework definitions for analysis of the user's problem.
- Do not manufacture facts, precision, confidence, or consensus.
- Do not use a framework to rationalize a conclusion chosen in advance.
- Do not turn a quick-answer request into a thinking-methods lecture.

## Boundaries

- This skill only structures reasoning; it does not execute side-effecting actions
  (no deploying, deleting, sending, or spending). If analysis suggests such an
  action, recommend it — let the user decide.
- Frameworks are lenses, not oracles. Flag when a conclusion rests on weak evidence.
- Don't fabricate data to fit a framework. If you lack facts, say so and treat the
  framework output as a hypothesis to verify.
