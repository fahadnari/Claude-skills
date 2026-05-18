---
name: context-bootstrapper
description: 'Set up context files for a new product or project so all other skills have the grounding they need. Use when: new project setup, set up context, bootstrap context, start new product, create context files, set up personas, set up product context.'
---

# Context Bootstrapper

Set up the four core context files that power every other skill in this toolkit — personas, product, company, and competitors — so you get grounded, relevant output from day one instead of generic templates.

## Why This Exists

Every skill in this toolkit reads `context/` files before doing any work. When those files are empty or missing, the skills produce generic output. When they're populated, the skills produce grounded, specific output that references your real users, your real metrics, and your real constraints.

This skill gets those files set up quickly — whether you're starting a brand new project or inheriting an existing one.

## What You'll Get

Four populated context files saved to your `context/` folder:
- `context/personas.md` — Who your users are, their jobs, pains, and gains
- `context/product.md` — What you're building, current metrics, known issues, roadmap status
- `context/company.md` — Strategic priorities, risk tolerance, past failures, org constraints
- `context/competitors.md` — Who you're competing with, what they do well, where they fall short

## When to Use This Skill

- Starting a new product initiative or project
- Joining a new team and wanting to hit the ground running
- Before your first use of any skill in this toolkit on a new area
- When other skills keep saying "I don't have enough context"

## What You'll Need

Whatever you have. This skill works with anything:
- A product brief, PRD, or strategy doc
- A deck or one-pager
- Bullet points you type in chat
- Nothing at all (I'll guide you through the key questions)

## Process

### Step 1: Check What Already Exists

First, look for an existing `context/` folder:
- If files exist → read them and tell the user what's already there, then offer to fill gaps
- If files are empty or missing → proceed to gather inputs

Tell the user:
> "I found [X] in your context folder. I'll update the gaps rather than overwrite what's already there."
> OR
> "Your context folder is empty. Let's build it from scratch — I'll ask a few questions and we can start with what you know today."

### Step 2: Gather Inputs

Ask for any documents the user already has. If they have nothing, run through the four areas conversationally with targeted questions.

**If gathering from scratch, ask one area at a time:**

**Personas:**
> "Who are the main types of users you're building for? For each, I need:
> - Their role and context (e.g., 'PM at a 50-person agency')
> - The main job they're trying to do
> - Their biggest frustration with how they do it today
> - What success looks like for them"

**Product:**
> "Tell me about what you're building:
> - What does the product do in one sentence?
> - What are the key metrics you track today (even rough numbers)?
> - What's on the roadmap for the next quarter?
> - What are the known problems or complaints users have?"

**Company:**
> "A few questions about your company's context:
> - What are the top 1-2 strategic priorities this year?
> - What's the team's appetite for risk — do you move fast or carefully?
> - Any past failures or constraints worth knowing about?
> - What does 'success' look like for your team this quarter?"

**Competitors:**
> "Who are the alternatives to your product?
> - Direct competitors (solving the same problem)
> - Indirect competitors (how users solve the problem today without you)
> - What do competitors do really well?
> - Where do they fall short or leave users underserved?"

**If the user provides a document**, extract the relevant information directly without asking questions that are already answered.

### Step 3: Fill Gaps with Honest Placeholders

For anything unknown, use clear placeholders rather than invented content:

```
[PLACEHOLDER — ask: What are your current conversion metrics?]
[UNKNOWN — to be researched: competitor pricing]
[ASSUMED — validate: users prefer self-serve onboarding]
```

This ensures the context files are useful immediately while being honest about what still needs to be confirmed.

### Step 4: Write the Four Files

Write all four files to `context/`. If a file already exists, merge new information rather than overwriting.

---

## Output Templates

### context/personas.md

```markdown
# Personas

*Last updated: [Date]*
*Source: [How this was generated — interview notes, product brief, bootstrapped from scratch, etc.]*

---

## [Persona Name] — [Role]

**Who they are:**
[1-2 sentences describing their role, company size, and context]

**Jobs to be done:**
- **Primary job:** [The main thing they're trying to accomplish]
- **Secondary jobs:** [Other things they need to do]

**Pains:**
- **Extreme:** [The pain that makes them switch products or pay more to avoid]
- **Moderate:** [Frustrations they tolerate but complain about]
- **Minor:** [Annoyances, not blockers]

**Gains:**
- **Required:** [What they expect as baseline]
- **Desired:** [What would delight them]

**Current solution:**
[How they solve this today — competing product, workaround, or nothing]

**Quote:**
> "[A real or representative quote that captures their frustration or goal]"

**Where to find them:**
[Slack channel, customer segment, Salesforce tag, etc. — so you can recruit for research]

---

## [Second Persona — same structure]

---

## Personas Not Yet Documented

- [ ] [Persona type we know exists but haven't mapped yet]

## Updates Log

| Date | Change | Source |
|------|--------|--------|
| [Date] | [What changed] | [Interview / feedback / assumption] |
```

---

### context/product.md

```markdown
# Product Context

*Last updated: [Date]*

---

## What We Build

**One-liner:**
[Product in one sentence — what it does and for whom]

**Value proposition:**
[Why users choose us over alternatives]

**Current stage:**
[Early / Growth / Mature / Declining — and what that means for priorities]

---

## Key Metrics

*Use [PLACEHOLDER] for anything unknown. Update as you learn.*

| Metric | Current Value | Target | Last Updated |
|--------|--------------|--------|--------------|
| [Primary success metric] | [Value or PLACEHOLDER] | [Target] | [Date] |
| [Activation / onboarding metric] | [Value or PLACEHOLDER] | [Target] | [Date] |
| [Retention metric] | [Value or PLACEHOLDER] | [Target] | [Date] |
| [Revenue / conversion metric] | [Value or PLACEHOLDER] | [Target] | [Date] |

---

## Roadmap Status

### Now (this quarter)
- [Feature / initiative in active development]

### Next (next quarter)
- [Feature / initiative planned]

### Later (backlog)
- [Feature / initiative under consideration]

### Recently shipped
- [Feature shipped in last 90 days — and what we learned]

---

## Known Issues & Complaints

*Top user pain points and internal known problems:*

| Issue | Source | Priority | Status |
|-------|--------|----------|--------|
| [User complaint or known bug] | [Feedback / interview / support ticket] | High/Med/Low | [Open / In progress / Fixed] |

---

## Technical Context

*For skills that need to assess feasibility:*

- **Tech stack:** [Brief description or PLACEHOLDER]
- **Key dependencies:** [Systems or services the product relies on]
- **Known technical debt:** [Areas that slow down development]
- **Typical sprint velocity:** [Rough indicator — fast / medium / slow]

---

## Updates Log

| Date | Change | Source |
|------|--------|--------|
| [Date] | [What changed] | [Where the info came from] |
```

---

### context/company.md

```markdown
# Company Context

*Last updated: [Date]*

---

## Strategic Priorities

*What the company is optimising for this year:*

1. [Priority 1 — e.g., "Win the SMB segment in UK"]
2. [Priority 2 — e.g., "Improve retention from 70% to 85%"]
3. [Priority 3 — e.g., "Launch in two new markets"]

**North Star metric:**
[The one number that captures company success — e.g., Weekly Active Orders]

---

## Risk Tolerance

**Experimentation culture:**
[Move fast / balanced / conservative — with a brief explanation]

**Typical decision-making speed:**
[How quickly does the team ship and decide? What slows things down?]

**Regulatory or compliance constraints:**
[Any rules that affect what you can build or test — GDPR, financial regulations, etc.]

---

## Team & Resources

*For skills that need to assess feasibility and effort:*

- **PM team size:** [Number or PLACEHOLDER]
- **Engineering capacity:** [Rough — e.g., "2 squads of 4 engineers"]
- **Design capacity:** [Rough — e.g., "1 designer shared across 2 PMs"]
- **Data / analytics:** [Self-serve / analyst support / limited]

---

## Past Failures & Lessons

*Grounding challenge questions in real history:*

| Initiative | What happened | Lesson |
|-----------|--------------|--------|
| [Feature or project] | [What went wrong or underperformed] | [What to watch for next time] |

---

## Org Dynamics

*What every PM needs to know about getting things done here:*

- **Key stakeholders to align early:** [Names or roles]
- **Common blockers:** [What tends to slow down approvals or launches]
- **What "done" means here:** [How the company defines launch-ready]

---

## Updates Log

| Date | Change | Source |
|------|--------|--------|
| [Date] | [What changed] | [Where the info came from] |
```

---

### context/competitors.md

```markdown
# Competitor Context

*Last updated: [Date]*

---

## Competitive Landscape

**How users solve this problem today:**
[Including workarounds and non-software solutions, not just direct competitors]

---

## Direct Competitors

### [Competitor Name]

**What they do:**
[One-sentence description]

**Their strengths:**
- [What they do really well]
- [Where they're winning]

**Their weaknesses:**
- [Where users complain about them]
- [What they don't solve well]

**Pricing:**
[Their model — or PLACEHOLDER if unknown]

**Key differentiator vs. us:**
[How we're different — or where we're similar]

**Recent moves:**
[Any recent product launches, pricing changes, or market moves worth tracking]

---

### [Second Competitor — same structure]

---

## Indirect Competitors / Alternatives

| Alternative | Who uses it | Why they choose it over us | Our response |
|-------------|------------|---------------------------|--------------|
| [Spreadsheets / manual process] | [User segment] | [Reason] | [How we address this] |
| [Adjacent tool] | [User segment] | [Reason] | [How we address this] |

---

## Competitive Gaps

*Where competitors are weak and we could win:*

| Gap | Competitor weakness | Our opportunity |
|-----|--------------------|--------------  |
| [Area] | [What they don't do well] | [How we could differentiate] |

---

## Table Stakes

*Features users expect as baseline — if we don't have these, we'll lose deals:*

- [ ] [Feature every competitor has]
- [ ] [Feature users consider standard]

---

## Updates Log

| Date | Change | Source |
|------|--------|--------|
| [Date] | [What changed] | [Where the info came from] |
```

---

## After Bootstrapping

Once the context files are created, the user should:

1. **Keep them alive** — Update after every user interview, experiment, or strategy change
2. **Treat them as the source of truth** — Other skills will cite them, so accuracy matters
3. **Add an Updates Log entry** — Every change should be dated and sourced so you know how fresh the information is

## Skills That Benefit From These Files

Every skill in this toolkit reads context files. But these benefit most from a well-populated context:

| Skill | Most important context file |
|-------|--------------------------|
| JTBD Extractor | `personas.md` |
| Value Prop Canvas | `personas.md` + `competitors.md` |
| Opportunity Solution Tree | `product.md` + `personas.md` |
| OKR Coach | `company.md` + `product.md` |
| PRD Generator | All four |
| Devil's Advocate | `company.md` + `competitors.md` |
| Product Brief Writer | All four |
| A/B Test Designer | `product.md` |
| Experiment Designer | `product.md` + `company.md` |

## Tips for Best Results

1. **Done is better than perfect** — A rough context file beats an empty one. Use PLACEHOLDER liberally.
2. **Update after every interview** — Add the key insight while it's fresh.
3. **One source of truth** — Don't duplicate persona info across multiple docs. Keep it all here.
4. **Be honest about assumptions** — Tag anything you haven't validated with ⚠️ ASSUMED.
5. **Date everything** — Old data is worse than no data. Timestamps help you know when to refresh.
