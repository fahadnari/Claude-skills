# Context Bootstrapper

Set up the four core context files that power every other skill in your product toolkit — personas, product, company, and competitors.

---

## Why This Skill Exists

Every skill in this toolkit reads `context/` files before doing any work. When those files are empty, skills produce generic output. When they're populated with your real users, metrics, and constraints, skills produce grounded, specific output.

This skill sets those files up quickly — whether you're starting from scratch or filling in gaps.

---

## Installation

Move the `context-bootstrapper` folder into your `.claude/skills/` directory and restart Claude.

---

## How to Use

```
/context-bootstrapper
```

Claude will ask about your users, product, company priorities, and competitors — then write four populated context files to your `context/` folder.

**Start with any of these:**
- "I'm starting a new project — set up my context files"
- "Here's our product brief — bootstrap context from this"
- "My other skills keep saying they don't have enough context"

---

## What You'll Get

Four files written to `context/`:

| File | What's in it |
|------|-------------|
| `personas.md` | User types, jobs, pains, gains, current solutions |
| `product.md` | What you build, key metrics, roadmap, known issues |
| `company.md` | Strategic priorities, risk tolerance, past failures, team size |
| `competitors.md` | Direct competitors, alternatives, gaps, table-stakes features |

---

## Skills That Use These Files

All of them — but especially:

- **PRD Generator** — reads all four
- **Devil's Advocate** — reads `company.md` + `competitors.md`
- **OKR Coach** — reads `company.md` + `product.md`
- **JTBD Extractor** — reads `personas.md`
- **Value Prop Canvas** — reads `personas.md` + `competitors.md`

---

## Tips

- Use `[PLACEHOLDER]` liberally — a rough file beats an empty one
- Update after every user interview or strategy change
- Add an Updates Log entry each time so you know how fresh the data is
