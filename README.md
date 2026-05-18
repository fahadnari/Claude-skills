# Claude PM Skills

A collection of AI-powered skills for Product Managers, built for Claude (Cowork & Claude Code). These skills turn Claude into a hands-on PM collaborator — from discovery through to delivery.

---

## Skills Overview

| Skill | What It Does | Trigger |
|---|---|---|
| [continuous-discovery](#continuous-discovery) | Applies Teresa Torres's continuous discovery framework | `/continuous-discovery` |
| [opportunity-solution-tree](#opportunity-solution-tree) | Builds visual OSTs mapping outcomes → opportunities → solutions | `/opportunity-solution-tree` |
| [jtbd-extractor](#jtbd-extractor) | Turns raw research into Jobs-to-be-Done statements | `/jtbd-extractor` |
| [prd-generator](#prd-generator) | Transforms ideas into structured PRDs | `/prd-generator` |
| [product-brief-writer](#product-brief-writer) | Writes one-page product briefs for buy-in | `/product-brief-writer` |
| [one-pager-creator](#one-pager-creator) | Creates concise one-pagers for stakeholder alignment | `/one-pager-creator` |
| [okr-coach](#okr-coach) | Writes and refines OKRs with quality feedback | `/okr-coach` |
| [value-proposition-canvas](#value-proposition-canvas) | Maps customer needs to product value using Strategyzer's framework | `/value-proposition-canvas` |
| [experiment-designer](#experiment-designer) | Designs product experiments beyond simple A/B tests | `/experiment-designer` |
| [ab-test-designer](#ab-test-designer) | Designs statistically sound A/B tests with sample size calculations | `/ab-test-designer` |
| [devils-advocate](#devils-advocate) | Challenges PRDs and specs to surface blind spots | `/devils-advocate` |
| [context-bootstrapper](#context-bootstrapper) | Sets up product/company context files for all other skills | `/context-bootstrapper` |
| [product-manager](#product-manager) | AI product owner for ticket management and sprint refinement | Auto-activates |
<<<<<<< HEAD
=======
| [slack-pm-drafter](#slack-pm-drafter) | Drafts Slack messages in your voice — announcements, updates, escalations | `/slack-pm-drafter` |
>>>>>>> 062ce06 (Add slack-pm-drafter skill)

---

## Installation

### Claude.ai Desktop (Cowork mode)
1. Go to **Settings → Capabilities → Skills**
2. Click **+ Add** → **Upload a skill**
3. Select the skill's ZIP file (or the folder directly)

### Claude Code (Terminal / Desktop)
1. Copy the skill folder into `~/.claude/skills/`
2. Restart Claude Code

> **Tip:** Place skills in `.claude/skills/` inside a specific project folder for project-scoped use.

---

## Skill Details

### continuous-discovery
Applies **Teresa Torres's Continuous Discovery Habits** framework to help product teams discover products that create customer and business value. Covers setting outcomes, interviewing customers, mapping opportunities, generating solutions, and testing assumptions.

Includes reference files on core thesis, principles, techniques, anti-patterns, and workflows for each discovery habit.

---

### opportunity-solution-tree
Creates **visual Opportunity Solution Trees** that map a business outcome down through user opportunities to testable solutions — the core artefact from continuous discovery.

---

### jtbd-extractor
Turns raw research (interviews, surveys, support tickets) into structured **Jobs-to-be-Done statements** — reframing feature requests as underlying user needs to uncover real innovation opportunities.

---

### prd-generator
Transforms messy ideas into **structured PRDs** that get stakeholder alignment before engineering starts building. Covers problem statement, goals, non-goals, requirements, and success metrics.

---

### product-brief-writer
Writes **one-page product briefs** to pitch ideas and get buy-in before investing in a full spec. Ideal for early-stage alignment with leadership or cross-functional partners.

---

### one-pager-creator
Creates concise **one-pagers** for quick stakeholder decisions — feature proposals, initiative pitches, and alignment docs.

---

### okr-coach
Writes and refines **OKRs** with feedback on ambition, measurability, and alignment to company goals. Helps avoid common traps like output-focused key results or misaligned objectives.

---

### value-proposition-canvas
Creates a **Value Proposition Canvas** using Strategyzer's framework — mapping customer jobs, pains, and gains to your product's features, pain relievers, and gain creators.

---

### experiment-designer
Designs **product experiments** beyond simple web A/B tests — pricing changes, feature rollouts, operational experiments, and pilots — with clear hypotheses and success criteria.

---

### ab-test-designer
Designs **statistically sound A/B tests** with structured hypotheses, sample size calculations, primary/secondary/guardrail metrics, and a pre-registered decision framework.

---

### devils-advocate
**Challenges your PRDs and specs** to find blind spots, hidden assumptions, and failure scenarios. Surfaces the hard questions sceptical stakeholders will ask before you're in the room.

---

### context-bootstrapper
Sets up the four core **context files** — personas, product, company, and competitors — that ground every other skill so you get relevant, personalised output instead of generic templates.

---

### slack-pm-drafter
Drafts **Slack messages in Fahad's voice** for the four main PM communication types: product announcements, WIP progress updates, stakeholder next-steps updates, and blocker escalations to leadership. Runs a guided workflow (type → audience → channel → tone → content) or accepts a Quick Brief template to skip straight to the draft. Built around real message examples and JET-specific terminology (JET+, UFD, RCT, code cut, etc.).

---

>>>>>>> 062ce06 (Add slack-pm-drafter skill)
### product-manager
An **AI Product Owner** for ticket management and sprint refinement. Works with Linear, GitHub Issues, and local Markdown files. Helps create, analyse, and improve tickets; identifies gaps in epics; and generates structured refinement session discussion points.

Supports: Linear · GitHub Issues · Local Markdown

---

## Adding a New Skill

1. Create a folder with your skill name inside this repo (e.g. `my-new-skill/`)
2. Add a `SKILL.md` with the skill's instructions and a `README.md` describing it
3. Push to GitHub (see below)

---

## Pushing to GitHub

This repo is hosted at: **https://github.com/fahadnari/Claude-skills**

To push new or updated skills:

```bash
cd /path/to/Skills

# Stage your new skill folder
git add my-new-skill/

# Commit
git commit -m "Add my-new-skill"

# Push
git push origin main
```

Or use the helper script included in this repo:

```bash
./push-skill.sh "Add my-new-skill"
```

---

## About

These skills are designed for product managers working in fast-moving teams. They encode PM best practices (Teresa Torres, Strategyzer, OKR frameworks, Jobs-to-be-Done, etc.) directly into Claude so you spend less time on process and more time on insight.

Built for use with [Claude](https://claude.ai) · Maintained by [@fahadnari](https://github.com/fahadnari)
