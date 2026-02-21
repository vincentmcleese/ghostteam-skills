# Reference X Articles

Real articles demonstrating the writing style and patterns in SKILL.md. These are the gold standard for how articles should read.

---

## Example 1: "How to Sell to Agents" (Thesis-Driven Explainer)

**Type:** Concept Explainer / Thought Leadership
**Key patterns:** Historical framing → thesis → economic logic → frameworks → actionable checklist

### Selected Excerpts

**Opening — historical anchor + thesis:**

In 1937, Ronald Coase asked a question that won him a Nobel Prize: if markets are so efficient, why do firms exist at all? Why don't we just contract everything out?

His answer was transaction costs. Finding a specialist, evaluating their work, negotiating a price, enforcing the agreement. All of that takes time and money. It's cheaper to just hire someone.

For almost a century, that held.

AI agents are changing the math. An agent can discover a service, check its price, and call it in a single HTTP roundtrip. No proposal. No demo. No comparison-shopping across ten browser tabs.

**Section with concrete specifics:**

When an agent researches this itself, using a GPT-4 class model with ~16K tokens of reasoning and tool calls, it costs $0.10-0.50 and takes 10-25 seconds. Accuracy is variable because it's synthesizing from training data.

A specialized service with a curated catalog returns the same answer for $0.01-0.02 in under 200 milliseconds. Accuracy is higher because it's maintained data, not generated reasoning.

That's 7-50x cheaper and 50-100x faster. The math is the decision.

**Framework section:**

You don't sell intelligence. Agents have plenty of that. You sell access to things they literally cannot compute on their own.

**Closing — actionable checklist with reasoning:**

Machine-readable capabilities. Publish what your service does in a structured format. Not a marketing page. A JSON manifest that any agent can parse in one request.

Pricing in the protocol. Return your price in the API response, not on a webpage. Agents can't read your pricing page, and they won't try.

The web was built for humans to browse. The next layer will be built for agents to buy. The question is whether your service is ready for the new buyer.

### Why It Works

1. **Historical anchor** — Starts with a Nobel Prize-winning idea, not personal credentials. Establishes intellectual weight.
2. **"For almost a century, that held" + "AI agents are changing the math"** — Classic setup/payoff. The thesis drops in sentence three.
3. **Concrete numbers** — $0.10-0.50 vs $0.01-0.02. 7-50x cheaper. 200ms vs 25 seconds. Specificity is the argument.
4. **Sections as self-contained arguments** — Each section has its own thesis, evidence, and conclusion. Reads like an essay, not a listicle.
5. **One-liner payoffs** — "The math is the decision." "You don't sell intelligence." These land because the preceding paragraph earned them.
6. **Actionable close** — Ends with a checklist, but each item has reasoning attached. Not just "do this" but "do this because."

---

## Example 2: "i stopped writing better skills and started building skill architecture" (Builder's Breakdown)

**Type:** Technical Tutorial / Builder's Playbook
**Key patterns:** Contrarian reframe → numbered system components → problem/fix/result structure → progressive payoff

### Selected Excerpts

**Opening — contrarian reframe:**

most people think an ai skill is a well-written instruction file. a really good SKILL.md with examples, scoring criteria, maybe a decision tree. that's the baseline.

we built 11 marketing skills. 32,000 lines. the skills themselves were the easy part. the architecture around them is where the real gains came from.

here are 5 things we added and why each one moved the needle.

**Problem/fix/result pattern:**

1. persistent memory

the problem: every session starts at zero. you re-explain your brand, your audience, your positioning every single time. the skill has no idea what happened yesterday.

the fix: a shared brand directory that every skill reads from and writes to.

voice-profile.md ← /brand-voice owns
positioning.md ← /positioning owns
audience.md ← /audience-research owns

profile files have one owner. only that skill can overwrite (with a diff and confirmation). append files never truncate. they only grow.

the result: session 1 builds context that session 20 uses. the skill remembers who you are and what you've done.

**Progressive payoff close:**

the system works with zero context on day 1. no setup required. just run a skill. but over time:

no context → useful output
- voice → sounds like you
- positioning → uses your angle
- audience → targets real pain
- learnings → avoids past mistakes
- full kit → fully personalized

day 1: it works.
day 7: it works better.
day 14: it works like it knows you.

the skill file is the starting point. the architecture around it is what makes it actually perform over time.

### Why It Works

1. **Contrarian reframe** — "most people think X. that's the baseline." Immediately signals you're going deeper than the obvious.
2. **Specific scale** — "11 marketing skills. 32,000 lines." Concrete numbers establish that this isn't theoretical.
3. **Problem/fix/result** — Every section follows the same structure. The reader always knows where they are.
4. **Technical specificity** — File names, ownership rules, TTL ranges (< 7 days, 7-30 days, 30-90 days). Real implementation details.
5. **Progressive payoff** — The "day 1 / day 7 / day 14" close shows compounding value. The system gets better the more you use it.
6. **Lowercase casual** — Entire article in lowercase. Feels like a builder sharing notes, not a thought leader performing.

---

## Example 3: "Apps are dead. Now what?" (Industry Analysis / Prediction Piece)

**Type:** Thought Leadership / Strategic Analysis
**Key patterns:** Personal experience → industry diagnosis → framework taxonomy → actionable timeline

### Selected Excerpts

**Opening — personal experience as evidence:**

I've been building my AI chief of staff, Claudia, over the past couple weeks. She has access to my calendar, email, our team's Notion workspace, meeting transcripts, financial history, and more. I've built over a dozen powerful automations. And I've stopped opening half my tools. Not because they're bad. Because my agent replaced the need to.

You've heard the diagnosis. @satyanadella said SaaS is dead. @steipete visited YC and declared 80% of apps will become APIs or disappear.

What's missing is the prescription: if apps are dying, what do you build instead?

**Taxonomy / framework:**

Not All Apps Die Equal

Dead on arrival: CRUD tools, dashboards, anything that's mostly "show me data and let me edit it." Agents handle this natively. If your product is a prettier spreadsheet, you're already losing.

Vulnerable but defensible: Workflow tools, project management, CRMs. The data is valuable. The interface is not. These have a window to pivot.

Trenchcoat companies: Multiple businesses in one. LinkedIn's identity graph is a durable moat, but agents that evaluate candidates across GitHub and portfolios don't need a profile page. The eyeballs stay; the intent leaves.

Last to fall: Creative tools, design surfaces, strategy canvases. Anything where the seeing IS the thinking.

**"How this goes wrong" pattern:**

How this goes wrong: You go headless but your API is poorly documented, rate-limited to uselessness, or missing critical endpoints. Agents route around you to a competitor who did it right. Headless only works if the API is genuinely great.

**Actionable timeline close:**

This week: Audit your API. Can an agent do everything your UI does? If not, that's your roadmap. If yes, ask why anyone would open your dashboard.

This month: Talk to the agent builders. What do they need from you? What's broken? Where are they routing around you?

This quarter: Pick your path. Headless, irreplaceable UI, or agent-to-agent. Each requires different teams, different pricing, different product thinking. Straddling all three is how you end up with none.

### Why It Works

1. **Personal experience as thesis evidence** — Doesn't just claim apps are dying. Shows it happening in real-time with specific tools (Fathom, Notion).
2. **Diagnosis → prescription framing** — "You've heard the diagnosis. What's missing is the prescription." Positions the article as the answer to a question everyone's already asking.
3. **Named taxonomies** — "Dead on arrival", "Trenchcoat companies", "Last to fall". Memorable labels that people will reuse.
4. **"How this goes wrong"** — Every recommendation includes the failure mode. Shows nuance, builds trust.
5. **Three Futures framework** — Gives readers a mental model they can apply to their own company immediately.
6. **Timeline close** — This week / this month / this quarter. Graduated urgency. Reader knows exactly what to do Monday morning.
7. **Quotes real people** — @satyanadella, @steipete, @IDC. External authority reinforces the thesis.

---

## Key Patterns Across All Three

### What these articles share:

1. **Thesis-first, not transformation-first** — The hook establishes what the article argues, not just personal credentials
2. **Concrete specifics** — Dollar amounts, percentages, time comparisons, named companies and tools
3. **Frameworks and taxonomies** — Named categories readers can apply to their own situation
4. **Sections as self-contained arguments** — Each section could stand alone as a post
5. **One-liner payoffs** — Short sentences that land after longer explanatory passages
6. **Failure modes included** — "How this goes wrong" or "But the build boundary shifts" — nuance builds trust
7. **Actionable closes** — Checklists, timelines, or specific next steps
8. **Mixed sentence rhythm** — Short punchy lines AND flowing explanatory passages, not rigidly one-sentence-per-line

### What these articles DON'T do:

1. No forced "spicy takes" — The opinions are strong but earned through argument, not provocation
2. No "8 months ago I was nobody" transformation hooks — Authority comes from analysis and experience, not before/after
3. No "like if you agree" engagement bait — Engagement comes from the ideas being worth discussing
4. No rigid one-sentence-per-line throughout — Uses it strategically for emphasis, not as a formatting rule
5. No generic "subscribe to my newsletter" — CTAs are specific and tied to the article's thesis
