---
name: ai-native-thinking
description: Guide the agent to design products, systems, or features using AI-native thinking. This skill helps distinguish AI-as-a-plugin designs from truly AI-native architectures, focusing on intent-first interaction, probabilistic systems, evolving data, and human-AI collaboration.
---

# AI-native Product Thinking

## Purpose

Use this skill whenever the task involves:

- Designing a new product, feature, or platform
- Adding AI to an existing system
- Rethinking workflows, UIs, or data systems with AI involved

The goal is **not** to optimize existing flows with AI,
but to determine whether the product should be re-formed around an intelligent agent.

---

## Core Rule (Non-negotiable)

Before proposing any solution, explicitly answer:

> If the AI model were removed, would this product still make sense?

- If the answer is “yes, but worse or slower” → this is **not AI-native**
- If the answer is “no, the product logic collapses” → continue

If it is not AI-native, clearly state that the design is an AI-augmented traditional system.

---

## Step 1: Replace “Feature” with “Intent”

Do NOT start from pages, menus, buttons, or workflows.

Instead, identify:

- The user’s **goal**
- The ambiguity or complexity they cannot pre-specify
- What they _cannot_ express as parameters

Reframe requirements as:

- “The user wants to achieve X, but cannot fully define how.”

Avoid:

- CRUD-first thinking
- Static form or table definitions
- Predefined navigation trees

---

## Step 2: Assume an Always-Present Intelligent Agent

Design as if:

- An agent is always available
- It understands natural language and context
- It can reason, but may be wrong
- It can call tools and inspect intermediate results

From this assumption:

- UI becomes a result surface, not a control panel
- Views can be temporary or generated on demand
- Workflows may be constructed at runtime

Do NOT assume:

- Fixed screens
- Stable user paths
- One correct execution order

---

## Step 3: Treat Errors as Interaction, Not Bugs

Assume failures are normal:

- Misunderstanding intent
- Partial or incorrect reasoning
- Tool execution errors

Design must include:

- Low-cost correction by the user
- Visibility into intermediate steps or assumptions
- Iterative refinement instead of retries from scratch

Avoid designs that require perfect first-pass accuracy.

Encode recovery paths explicitly:

| Trigger | First response | If still unresolved |
|---|---|---|
| Intent is ambiguous or corrected | Show the current interpretation, preserve confirmed facts, and ask one blocking question | Offer bounded paths or escalate conflicting evidence; do not silently choose |
| Evidence is missing | Mark uncertainty and return a useful partial result | Stop when continuing would mislead |
| A tool fails before any side effect | Retry only when safe and bounded | Switch tool or hand off the error and preserved state |
| A write times out or has unknown status | Inspect the external system before retrying | Escalate unresolved state; never repeat blindly |
| A workflow partially succeeds | Preserve completed steps and resume at failure | Offer compensation or human handoff; do not restart everything |

---

## Step 4: Make Data Adaptive, Not Static

Do not assume datasets, rules, or schemas are fixed.

Instead:

- Data can be generated, filtered, or reweighted at runtime
- New failure cases should reshape future inputs
- The system should learn from usage, not just training

Data exists to serve current intent, not as a permanent asset.

---

## Step 5: Decide the Correct Level of Constraint

Choose how much freedom the agent has:

- High freedom:
  - Multiple valid solutions
  - Context-heavy judgment
  - Exploratory or creative tasks

- Medium freedom:
  - Recommended patterns
  - Configurable strategies
  - Guardrails without fixed paths

- Low freedom:
  - Fragile operations
  - Irreversible effects
  - Strict ordering requirements

Explicitly state where and why constraints exist.

### Mandatory checkpoint for consequential actions

Designs that can send consequential external communications, move money, create legal commitments, delete data, change access, publish content, or cause another hard-to-reverse effect must include this checkpoint. A communication is consequential when it creates a commitment, exposes sensitive information, or materially affects a third party.

**🔴 CHECKPOINT · STOP**

Before execution, show:

1. Exact action and target.
2. Data, amount, or permissions involved.
3. Impact and reversibility.
4. Recovery or compensation path.
5. Required approver.

Do not treat model confidence as authorization. If confirmation is unavailable, keep the action as a draft or recommendation and continue only with reversible work.

---

## Output Expectations

When this skill is applied, the final output should include:

- A clear statement of whether the design is AI-native or AI-augmented
- The user intent model (not UI structure)
- The role of the agent in the system
- How errors and corrections are handled
- What parts of the system are expected to evolve over time

Default to a compact answer. State the AI-native verdict once, combine overlapping sections, and include only the recovery branches and checkpoints that materially affect the proposed design.

Avoid presenting UI-first or database-first solutions unless explicitly required.
