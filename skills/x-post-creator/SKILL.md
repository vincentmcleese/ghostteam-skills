---
name: x-post-creator
description: Transform any content into high-performing X (Twitter) posts. Use when asked to write tweets, X posts, or convert content for X/Twitter. Generates multiple format variations including long-form posts, quick takes, threads, and controversial takes. Applies proven writing principles for maximum engagement.
---

# X Post Creator

Transform any content into high-performing X posts across multiple formats.

## Core Writing Principles

These principles determine whether content gets ignored or goes viral.

### 1. Genuinely Valuable

Don't regurgitate advice that's been floating around for years. Dig into experience and pull out fresh insights that haven't been beaten to death across the platform. Ideas that could genuinely shift how someone approaches their work.

**Before posting, ask:** Would I bookmark this if someone else wrote it? If no, keep working.

### 2. Immediately Actionable

An insight without a blueprint is entertainment, not education.

**Bad:** "wow this new ChatGPT update is absolutely insane"
**Good:** "how to write copy that sounds human with GPT-5.2:" + walk through the actual process step by step

People don't follow because you noticed something—they follow because you taught them how to use it. The tweets become your portfolio.

### 3. Sparks Natural Engagement

Never beg: "like if you agree" or "retweet this if you found it helpful" looks desperate.

**For bookmarks:** Use "here's how" or "how to" or "do this" in the hook. People on autopilot see something useful, bookmark it, keep scrolling.

**For replies - two approaches:**
- **Controversial stance:** "GPT-5.2 now writes better copy than Claude, Gemini, and Grok all together, here's the proof" — people argue or back you up
- **Collaborative opening:** "this is the workflow i'm using with ChatGPT right now, curious if anyone's tested this approach with Claude" — people share experiences

### 4. Ridiculously Easy to Read

People scroll at insane speeds. One second to decide whether to engage.

- **Hook:** Short and punchy. One line. "how to X" or "why X doesn't work" or "the X mistake you're making"
- **Structure:** One sentence per line. Creates rhythm. Easy to process visually.
- **Lists:** Use "-" or ">" or "1." for complex information. People can skim and grab main points.
- **White space:** Space between lines gives eyes a place to rest. Solid blocks of text feel exhausting.
- **Language:** Simplify everything. Conversational tone like a mentor talking to students.
  - "use" not "utilize"
  - "help" not "facilitate"  
  - "get better" not "optimize performance"
  - If a 14-year-old couldn't understand it, it's too complex

### 5. Recognizable Style

Same content written in same style everywhere blends into generic AI-sounding soup.

Find 3-4 structural elements that feel natural:
- Maybe always use ">" to break down processes
- Maybe start most tweets with a specific pattern
- Maybe write in fragments sometimes for emphasis
- Maybe use "tbh" or "honestly" before controversial takes

Consistency without being formulaic. Patterns people recognize, but not filling in a template.

## Post Formats

Generate **at least 3 formats** for every request. Let the user choose.

### Format 1: LONG-FORM (No character limit)

Ignore Twitter's character count. Write like a blog post in tweet form. These do extremely well.

**Characteristics:**
- Multiple paragraphs with white space
- Uses ">" for breaking down processes
- One sentence per line
- Conversational, mentor-to-student tone
- Often starts with a personal observation or result
- Ends with a strong closer that ties everything together

**Structure:**
```
[Hook - personal result or bold claim]

[Context - why this matters]

> [Point 1]
> [Point 2]
> [Point 3]

[Explanation with one sentence per line]

[Process breakdown]

[Strong closer]
```

### Format 2: NUMBERED DEEP-DIVE

For observations, lessons, or frameworks with multiple points.

**Characteristics:**
- Personal hook ("ive been..." or "my observations...")
- Numbered points with substantial content each
- Specific $ amounts and details
- Pop culture references people recognize
- Memorable closer

**Structure:**
```
[Personal observation hook]

[Framing statement]

1. [Point with specific details]

2. [Point with specific details]

3. [Continue...]

[Memorable one-line closer]
```

### Format 3: QUICK TAKE (Under 280 chars)

Punchy, immediate, shareable.

**Characteristics:**
- Single complete thought
- Often lowercase
- Surprising or thought-provoking
- Stands alone without context needed

**Hook patterns:**
- "[Tool] just [surprising thing]"
- "a huge number of [X] feel [Y] for [time] and then [unexpected outcome]"
- "[Bold claim]. [Short explanation]."
- "you're a few [X] from [surprising outcome]"
- "[Tool] will probably [bold prediction]"

### Format 4: FRAMEWORK POST

Structured breakdown with clear formatting.

**Characteristics:**
- Uses arrows (→) or ">" for steps
- Numbered points if ranking
- Clear value proposition in hook
- Authority-building tone

**Structure:**
```
[Bold claim or observation]

[Context if needed]

→ [Step/point 1]
→ [Step/point 2]
→ [Step/point 3]

[Impact statement or closer]
```

### Format 5: SKILLS/SYSTEM SHOWCASE

Show a complete system or workflow you've built.

**Characteristics:**
- Numbered list of components
- Each point explains what it does
- Proof/example link at end
- Soft sell if relevant

**Structure:**
```
[X] skills/tools/steps to [outcome]

1. [Component] to [what it does]
2. [Component] to [what it does]
...

[How they work together]

[Proof link or example]
```

### Format 6: HOT TAKE / CONTROVERSIAL

Strong opinion that invites debate.

**Characteristics:**
- Clear stance on divisive topic
- Often challenges conventional wisdom
- Invites replies (agreement or argument)
- Uses "tbh" or "honestly" before the take

## Proven Hook Types

Use these patterns based on content type:

| Hook Type | Pattern | Example |
|-----------|---------|---------|
| Contrarian | "X doesn't [expected]. It [opposite]." | "The App Store doesn't DIE. It's going to EXPLODE." |
| Personal observation | "[lowercase] ive been [doing X] and [insight]" | "ive been hanging out with founders under 25 lately and they're built different" |
| Underestimation | "I don't think people grasp [thing]..." | "I really don't think people grasp how powerful Claude's Agent SDK is..." |
| Bold prediction | "[tool] will probably [big outcome]" | "claude code will probably make 10,000 people millionaires" |
| Pattern naming | "a huge number of [X] [behavior pattern]" | "a huge number of ai products feel impressive for 48 hours and then quietly exit your life" |
| How-to | "how to [specific outcome]" | "how to rank on search engines/llms and still sound like a human" |
| System tease | "[number] [things] to [outcome]" | "10 skills to turn Claude Code into a marketing team that sells" |
| Simple wisdom | "[number] ways to [outcome]:" | "two ways to get the most out of AI:" |

## Reference Examples

See `references/examples.md` for real posts from Greg Isenberg and Boring Marketer demonstrating these principles.

## Output Format

For every conversion request:

### 1. Quick Analysis
```
Core insight: [one sentence]
Best hook angle: [which hook type from table above]
```

### 2. Generate 3-5 Formats

Present each format ready to copy-paste:

```
---
**LONG-FORM**

[Full post text]

---
**NUMBERED DEEP-DIVE** (if content has multiple points)

[Post text]

---
**QUICK TAKE**

[Post text]

---
**FRAMEWORK**

[Post text]

---
**SKILLS/SYSTEM SHOWCASE** (if showing a workflow)

[Post text]

---
```

### 3. Top Pick

Note which format works best for this specific content and why.

## Voice Guidelines

Maintain across all formats:
- Transparency with specific numbers/metrics
- Anti-gatekeeping: "You can do this too" mentality
- Name actual tools (Claude, n8n, ChatGPT, etc.)
- Practical focus: always actionable, never just theory
- Excited but not hype-y
- Lowercase used strategically (not always, but often in casual observations)

## Common Mistakes to Avoid

1. **Too formal:** X is casual. Write like you're texting a smart friend.
2. **Missing proof:** Include specific results/numbers when available
3. **No personality:** Opinions and excitement matter
4. **Over-explaining:** Trust the audience to be smart
5. **Wall of text:** White space is your friend
6. **Generic hooks:** "Here's what I learned about AI" → boring. "I replaced a $50k/month agency. With Claude." → stops the scroll
7. **Begging for engagement:** Never ask for likes/retweets

## Usage

1. User provides content (could be anything: notes, LinkedIn post, idea, article, results)
2. Generate 3-5 format variations
3. Present with recommendation for which works best
4. User picks and posts (or requests tweaks)
