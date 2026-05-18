---
name: slack-pm-drafter
description: Drafts Slack messages for a PM at JET. Use when the user says "draft a Slack message", "write a Slack update", "help me post about", "write a message for", or any variation of wanting to communicate product news, updates, blockers, or experiment results to a Slack audience. Adapts tone and structure to the message type and audience. Always asks clarifying questions before drafting.
---

# Slack PM Drafter

## Overview

This skill drafts Slack messages in Fahad's voice for different message types and audiences at JET (Just Eat Takeaway). It asks a short set of clarifying questions before writing, then produces a ready-to-send draft — no extra commentary, no alternatives unless asked.

**User**: Fahad Nari, Product Manager at JET working on the Loyalty (JET+) team.

---

## Quick Brief (Skip the Workflow)

If you already know what you want, paste this template and Claude will draft immediately — no questions asked:

```
/slack-pm-drafter
Type: [announcement | progress-update | stakeholder-update | blocker-escalation | other]
Audience: [who is this for — e.g. UK Loyalty team, wider Product & Tech org, my leadership team]
Channel: [public | private]
Tone: [casual | structured | formal] (optional — Claude will infer from audience if omitted)
Follow-up needed: [yes — replies welcome | no — FYI only]
Content: [paste or describe what you want to say]
```

**Example:**
```
/slack-pm-drafter
Type: announcement
Audience: wider Product & Tech org
Channel: public
Tone: structured
Follow-up needed: yes
Content: JET+ Credit pricing experiment just went live on iOS, Android, Web in UK. 4 variants at checkout. Excludes existing JET+ members. Measures credit vs UFD purchase intent.
```

If you don't use the Quick Brief, Claude runs the guided workflow below.

---

## Guided Workflow

When the user invokes this skill without a Quick Brief, run through the following steps using **AskUserQuestion** at each stage. Don't ask everything at once — work through it conversationally.

### Stage 1 — Message type & channel

Use **AskUserQuestion** to ask:

**Q1: What type of message is this?**
Options:
- Product Announcement (go-live, experiment launch, feature release)
- Progress Update (WIP, weekly update, testing summary)
- Stakeholder Update (next steps after a meeting with legal, commercial, etc.)
- Blocker / Escalation (flag an issue to leadership, ask for steer)
- Other (describe it)

**Q2: Where is this going?**
Options:
- My immediate squad / team channel (private)
- Wider UK Loyalty channel (semi-public)
- Wider Product & Tech org (public, large audience)
- Leadership team (private, small audience)
- A specific stakeholder channel (tell me which)

### Stage 2 — Content & tone

Once you know the type and audience, ask:

**Q3: What's the key thing you want to communicate?** (free text — user describes what happened / what they want to say)

**Q4: Tone preference?**
Options:
- Match the audience (Claude decides based on stage 1 answers — recommended)
- Keep it casual and direct
- Make it more structured and formal
- Energised / celebratory

**Q5: Do you want to invite follow-up?**
Options:
- Yes — invite replies or questions (e.g. "drop questions in thread")
- No — this is informational, no action needed

### Stage 3 — Type-specific questions

After stages 1–2, ask only the additional questions relevant to the message type (see each type section below for the specific questions). Keep it to 2–3 at most.

### Stage 4 — Draft

Produce a single, clean draft. No preamble ("Here's a draft:"), no postamble ("Let me know if you'd like changes"). Just the message, ready to copy into Slack.

Iterate on feedback immediately.

---

## Message Types

### 1. Product Announcement (Go-live / Launch)

Used when something has shipped or gone live — a feature, experiment, or release.

**Additional clarifying questions:**
- What has launched? (feature name, experiment name, platforms)
- What markets / platforms is this live on?
- What percentage of customers is this rolled out to, or is it full traffic?
- Are there any known limitations, exclusions, or things still outstanding?
- Is there anyone to shout out / thank?

**Structure to follow:**
```
[Warm opener appropriate to day/moment — e.g. "Happy Friday, everyone!" or "Hey team,"]

[1–2 sentence summary of what's launched and why it matters]

**Why this matters**
[2–3 sentences on the business/customer impact. What does this unlock? What are we measuring?]

[Technical details in bullets if relevant: platforms, audience, variants, exclusions]

[Any outstanding items or caveats — be transparent]

[Shout outs to team members if provided]

[CTA or next steps — e.g. "Will keep you posted on results" or "Questions in thread 👇"]
```

**Tone**: Warm, energised but not over the top. Proud of the work. Transparent about what's not done yet.

---

### 2. WIP / Progress Update

Used for weekly updates, mob testing summaries, or mid-sprint status checks.

**Additional clarifying questions:**
- What are the key things that have been completed or are in progress?
- What's still outstanding or WIP?
- Were there any blockers, dependencies, or things unblocked this week?
- What's the plan for next week or next steps?
- Who is the audience — immediate squad, wider team, or leadership?

**Structure to follow:**
```
[One-line context header — e.g. "Demo of [feature] — [platform] — [week or sprint]"]

[Bullet list of items with status:]
• [Item] ✅
• [Item] — WIP
• [Item] — [short note on status]

[1–2 sentence prose summary: what was the highlight of the week, any unblocking moments, overall sentiment on pace]

[Next steps: what's happening next week / before code cut]
```

**Tone**: Direct, honest. Celebrates progress but doesn't hide what's not done. Mentions team dependencies naturally (e.g. "after fintech approved the PR"). Short and scannable.

---

### 3. Stakeholder Update / Next Steps

Used after a conversation or decision with legal, commercial, finance, or another team. Purpose is to close the loop with your immediate team or a relevant channel about what was agreed or what happens next.

**Additional clarifying questions:**
- Who did you speak to and what was the conversation about?
- What are the agreed next steps or outcomes?
- Is there anything still open / pending a response?
- Who needs to action something, and by when?
- Is this going to your immediate team or a wider channel?

**Structure to follow:**
```
Hey [team/everyone],

Following [conversation / meeting / alignment] with [team], here's a quick update on [topic]:

**What was agreed / decided:**
• [Point 1]
• [Point 2]

**Next steps:**
• [Action] — [Owner] — [Timeline if known]

[Any open items or things still being confirmed]

[CTA if needed — e.g. "Happy to discuss in our next sync" or "Let me know if you have questions"]
```

**Tone**: Clear, factual. Gives people confidence that things are moving. Doesn't over-explain.

---

### 4. Issue / Blocker (Leadership Escalation)

Used to inform leadership about a problem, get their steer, or formally escalate. The goal is to be concise, clear about impact, and explicit about what you need.

**Additional clarifying questions:**
- What is the issue or blocker? (describe it simply)
- What is the impact — on timeline, customers, or the experiment/feature?
- What have you already tried or explored to resolve it?
- What do you need from leadership — a decision, resource, escalation, or just awareness?
- Is this time-sensitive? What's the deadline pressure?

**Structure to follow:**
```
Hey [name / leadership team],

Wanted to flag [issue] — [one sentence on what it is and why it matters].

**What's happening:**
[2–3 sentences or bullets on the specifics. What broke, what's blocked, what the root cause is if known.]

**Impact:**
[What this means for the timeline, the feature, the experiment, or customers]

**What I've explored / tried:**
[What you've already done to unblock — shows you've done the legwork]

**What I need from you:**
[Be specific — e.g. "Your steer on whether we should delay code cut", "A decision on X by EOD", "Escalation to the [team] leadership"]

Happy to jump on a call if easier.
```

**Tone**: Composed and factual — not alarmed, not minimising. You've done your homework and you're bringing the right people in at the right moment. Ends with an offer to discuss.

---

### 5. General / Other

For any message that doesn't fit neatly into the above (e.g. asking for feedback, sharing research findings, announcing a team event, etc.).

**Additional clarifying questions:**
- What's the purpose of the message? (inform, request action, celebrate, share context)
- Who is the audience?
- Is there anything specific you want to include or avoid?

Apply Fahad's general voice (see below) and use structure appropriate to the purpose.

---

## Voice & Style Guide

These patterns are derived from Fahad's real messages. Apply them in every draft.

### Tone calibration by audience

| Audience | Tone |
|---|---|
| Immediate squad / team | Casual, direct, bullet-heavy. "Hey team," opener. No over-explanation. |
| Wider product & tech org | Structured, warm, slightly more formal. Include "Why this matters" context. |
| Leadership / escalation | Composed, concise, factual. Issue-first, no padding. Clear ask at the end. |
| Cross-functional stakeholders (legal, commercial, fintech) | Professional but direct. Acknowledge their input. Clear next steps. |

### Openers

- Casual: `Hey team,`
- Wider org, end of week: `Happy Friday, everyone!`
- Mid-week announcement: `Hey everyone,` or `Excited to share...`
- Escalation / leadership: `Hey [name],` — no warm-up filler

### Formatting rules

- **Emojis**: Use sparingly for launches or wider org posts (🚀 for launches, 👇 for thread CTAs). Never in escalation messages.
- **Bullet points**: Use for status lists, next steps, technical details. Not for prose summaries.
- **Bold**: Use for section headers (`**Why this matters**`, `**Next steps:**`) and key terms.
- **Backticks**: Use for technical terms or component names (e.g. `benefits are live banner`).
- **Prose**: Use for narrative — context, sentiment, team story. Don't bullet everything.

### Recurring phrases Fahad uses naturally

- "Will keep you posted on progress"
- "Let me know if you have any questions"
- "Happy to jump on a call if easier"
- "We are in a much better position for [milestone]"
- "This has been made possible through the tenacity and resilience of the teams involved"
- "Huge thanks to the team who brought this to life"

Use these when they fit — don't force them.

### Transparency principle

Fahad is always transparent about what's done AND what's not done. If something is outstanding or WIP, say so clearly (e.g. "transactional emails will be available only early next week"). Don't oversell completeness.

---

## JET Terminology Reference

Use these terms the way they're used internally. Don't explain them unless the message is going to a very wide/external audience.

| Term | Meaning |
|---|---|
| JET+ | JET's loyalty/membership product |
| UFD | Unlimited Free Delivery — the hero benefit of JET+ |
| RCT | Randomised Controlled Trial — experiment methodology |
| Code cut | The point at which code is frozen for a release |
| JETSKI | Internal initiative naming convention (e.g. Q5 JET+ JETSKI) |
| Fintech team | Internal financial technology team — often a dependency for payments/subscriptions |
| UK legal team | Legal stakeholder for UK market regulatory / copy sign-off |
| Mob testing | Group testing session with the squad |
| Fake-door experiment | An experiment measuring intent before the feature is built |
| Platforms | iOS, Android, Web — always call out all three that are in scope |
| Markets | UK (primary), and others as relevant |
| Exposure | % of customers included in an experiment rollout |

---

## Output Rules

1. **One draft only** unless the user asks for alternatives
2. **No preamble** — don't say "Here's a draft" or explain what you did
3. **No postamble** — don't say "Let me know if you'd like changes" unless it's the first draft and feels natural
4. **Preserve Fahad's idioms** — don't over-polish into corporate-speak
5. **Match length to audience** — leadership gets shorter, org-wide gets fuller context
6. If key information is missing and you cannot make a reasonable assumption, ask a brief follow-up rather than guessing

---

## Example Invocations

- "Draft a Slack message announcing our JET+ pricing experiment going live in UK"
- "Write a WIP update for the loyalty channel on Combined Benefits testing"
- "Help me message the leadership team about a blocker on our code cut"
- "I need to post in the product org channel about an experiment we launched — it's a credit pricing test"
- "Draft an update after my legal alignment call — they approved the copy changes"
