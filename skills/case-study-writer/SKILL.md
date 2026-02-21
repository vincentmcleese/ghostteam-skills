---
name: case-study-writer
description: Transform raw project information into compelling case studies matching Relevance AI's proven structure
---

# Case Study Writer Skill

## Purpose
Transform raw project information (voice notes, documentation, customer conversations, references) into compelling case studies that follow Relevance AI's proven structure - clear, scannable, and metric-focused.

**Behavior:** This skill ALWAYS produces a complete case study structure. It fills in whatever information is available and uses clear placeholders for missing information. It NEVER asks for clarification or additional information.

## Target Audience
Prospects and potential customers who want to quickly understand real-world implementations and results.

## Brand Voice Guidelines

**Tone:** Direct, professional, and results-focused

**Style Characteristics:**
- Extremely straightforward and scannable
- Heavy use of bullet points and section headers
- Metrics front and center
- Short paragraphs (1-3 sentences maximum)
- Conversational quotes that feel authentic
- No flowery language or excessive narrative

**What to avoid:**
- Long narrative paragraphs
- Vague claims without numbers
- Excessive storytelling
- Walls of text
- Corporate buzzwords

## Case Study Structure

### 1. Opening Summary (Single paragraph, ~40-60 words)
A concise introductory paragraph that includes:
- Company name and brief context (what they do, scale/reach)
- Partnership mention with your company
- Teaser of key results with specific numbers/timeframes
- Leadership names if relevant

**Example structure:**
"[Company], a [brief description with scale], has [transformation achieved] by [method]. Led by [names/titles], the company partnered with [your company] to [action taken] that [specific result with numbers]."

### 2. The Challenge Section
**Header format:** "The Challenge: [Specific Problem Title]"

**Content:**
- 1-2 sentence intro paragraph explaining the core problem
- Bullet points (3-5) listing specific pain points
- Direct quote from client leadership explaining the problem
- Focus on operational bottlenecks and capacity constraints

**Example quote format:**
```
[Quote explaining the problem in their words] - [Name], [Title]
```

### 3. The Solution Section  
**Header format:** "The Solution: [How They Used Your Product]"

**Content:**
- 1-2 sentence paragraph explaining your approach conceptually
- Sub-header "Key Decision Factors:" or similar with bullet points (3-5)
- OR Sub-header showing what was built/trained with bullet points
- Optional quote about what differentiated your solution
- Focus on approach and customization, not deep technical details

### 4. The Results Section
**Header format:** "The Results: [Outcome Phrase]"

**Content:**
- Opening line: "The results speak for themselves:" or similar
- Bullet points (3-5) with specific metrics
- Lead with quantitative results (numbers, percentages, dollar amounts)
- Include qualitative results (team happiness, 24/7 operation, etc.)
- Direct quote from client about impact
- Format metrics with context (before/after, timeframes, scale)

**Metric bullet format examples:**
- "$7 million in S1 pipeline generated"
- "3x the number of meetings, at 50% of the cost per meeting"
- "40 hours saved weekly across 300+ conversations"

### 5. Additional Context Sections (Optional)
If there's more detail to share, add sections with clear headers like:
- "Training the AI Workforce"
- "Building an Interconnected AI Ecosystem"  
- "Agent Development Process"

Each section should:
- Have a descriptive header
- Use bullet points or very short paragraphs
- Include quotes where relevant

### 6. What's Next Section
**Header format:** "What's Next: [Future Vision]"

**Content:**
- Optional: Image placeholder [Image description]
- 1-2 paragraphs about future expansion plans
- Quote about broader AI adoption plans
- Vision for how this scales across the organization

### 7. Call to Action (Consistent Format)
```
Build your AI Workforce
Grow your business, not your headcount
[Request demo](/link)
```

## Output Specifications

**Format:** Markdown (.md file)

**Length:** 300-400 words total (shorter and more scannable)

**Formatting:**
- Clear section headers with colons (The Challenge:, The Solution:, The Results:)
- Heavy use of bullet points
- Short paragraphs (1-3 sentences max)
- Quotes interspersed throughout (not in separate section)
- Bold for company/product names in headers only
- No excessive formatting within paragraphs

## Content Processing Instructions

**CRITICAL: Always create a complete case study structure, even with incomplete information. Never ask for clarification - just fill what you can and placeholder what you can't.**

### Processing Approach:

1. **Extract available information:**
   - Company name, what they do, scale/reach
   - Specific pain points that can be bulleted
   - Decision factors or what was built/configured
   - Concrete results with numbers
   - Client quotes
   - Future expansion plans

2. **Always create all sections:**
   - Build the complete case study structure regardless of how much information is available
   - Fill in sections with whatever information is provided
   - Use placeholders for missing information (see Placeholder Formats below)
   - NEVER ask the user for more information or leave sections blank

3. **For voice notes:**
   - Extract specific pain points
   - Pull out any numbers mentioned
   - Capture quotes verbatim
   - Identify future plans

4. **For documentation:**
   - Convert paragraphs into bullet points
   - Extract metrics and format clearly
   - Identify natural section breaks

### Placeholder Formats:

When information is missing, use these specific placeholder formats:

**Company/Context Missing:**
```
[COMPANY NAME], a [BRIEF DESCRIPTION OF WHAT THEY DO], has [TRANSFORMATION/RESULTS] by partnering with [YOUR COMPANY] to [ACTION TAKEN].
```

**Metrics Missing:**
```
- [METRIC: e.g., "X% increase in lead volume"]
- [METRIC: e.g., "X hours saved per week"]
- [METRIC: e.g., "$X in revenue/pipeline generated"]
```

**Pain Points Missing:**
```
- [PAIN POINT: specific operational challenge]
- [PAIN POINT: capacity or scaling issue]
- [PAIN POINT: manual process that was bottleneck]
```

**Quotes Missing:**
```
[QUOTE NEEDED from [client name/title] about [specific aspect - e.g., "the main challenge" or "the results achieved"]]
```

**Solution Details Missing:**
```
Key Decision Factors:
- [DECISION FACTOR: why they chose your solution]
- [DECISION FACTOR: key differentiator]
- [DECISION FACTOR: specific capability that mattered]
```

**Future Plans Missing:**
```
[CLIENT] is now exploring how to expand [YOUR SOLUTION] across [OTHER DEPARTMENTS/USE CASES]. [QUOTE NEEDED from client about future vision]
```

## Quality Checklist

Before finalizing, ensure:

- [ ] Complete structure with all 7 sections present
- [ ] Opens with company context (even if using placeholder)
- [ ] All major sections have clear headers with colons
- [ ] Challenge section has 3-5 bullets (use placeholders if needed)
- [ ] Solution section explains approach with bullets
- [ ] Results section has "The results speak for themselves:" opener
- [ ] At least 3 metrics in Results (use placeholders for missing ones)
- [ ] 2-3 quotes present (use [QUOTE NEEDED...] format if missing)
- [ ] Paragraphs are 1-3 sentences maximum
- [ ] Target length 300-400 words (excluding placeholders)
- [ ] Heavy use of bullets and scannable format
- [ ] Ends with "What's Next" section and CTA
- [ ] Clear placeholders for any missing information

## Example Sections from Relevance AI Case Studies

**Opening Summary Examples:**

✅ "Qualified, an agentic marketing platform, has reimagined their revenue operations by building a sophisticated AI workforce. The company partnered with Relevance AI to build 35+ specialized AI agents that generated a further $7 million in pipeline and $500,000 in closed revenue over just six months."

✅ "Send Payments, a global payment infrastructure provider serving Australian customers worldwide, has elevated their operations by building an interconnected AI agent workforce. Led by CTO Ryk Neethling and Head of Product Eldert Bongers, the company partnered with Relevance AI to create specialized agents that deliver 24/7 customer service, automate compliance tasks, and give back 40 hours per week to their team."

**Challenge Section Example:**

```
The Challenge: Manual Processes Holding Back Growth

Qualified was stuck in the typical scaling trap:
- Revenue targets growing faster than team capacity
- Manual tasks consuming valuable time across all levels
- Expensive, hard-to-scale human-intensive processes and repetitive work like data cleanup, research, and outreach

[Quote from client]
```

**Results Section Example:**

```
The Results: $7M Pipeline in Six Months

Quantified Impact:
- $7 million in S1 pipeline generated
- $3.5 million in S2 pipeline created
- $500,000 in closed revenue achieved
- 35 AI agents now handling diverse business functions

Quality & Efficiency:
- AI-generated content often outperformed human-created versions
- 24/7 operation with consistent high-quality output
- Breakthrough moment: 3 meetings booked automatically while manager was traveling

[Quote from client]
```

## Notes

- This structure prioritizes scannability over narrative flow
- Quotes should feel conversational and authentic, not polished
- Every metric should include context (timeframe, scale, before/after)
- Section headers are critical for structure - always use them
- Keep it short - better to have a tight 300 words than a loose 500

## Example: Case Study with Partial Information

**When you only have limited information (e.g., just the problem and some results), output should look like:**

```markdown
[COMPANY NAME], a [COMPANY DESCRIPTION], has [TRANSFORMATION ACHIEVED] by partnering with [YOUR COMPANY] to implement [SOLUTION TYPE] that [KEY RESULT].

The Challenge: [Problem Title]

[CLIENT] faced significant operational challenges:
- Manual processes consuming [X hours/resources]
- [SPECIFIC PAIN POINT from available info]
- [PAIN POINT: scaling/capacity constraint]

[QUOTE NEEDED from [client contact] about the main challenge they faced]

The Solution: [How They Implemented Your Product]

[CLIENT] partnered with [YOUR COMPANY] to [high-level approach].

Key Decision Factors:
- [DECISION FACTOR: specific capability mentioned in materials]
- [DECISION FACTOR: why they chose your solution vs alternatives]
- [DECISION FACTOR: customization or integration capability]

[QUOTE NEEDED from [client contact] about what differentiated the solution]

The Results: [Outcome Phrase]

The results speak for themselves:
- [ACTUAL METRIC from materials - e.g., "3x increase in meetings booked"]
- [METRIC: time savings achieved]
- [METRIC: cost reduction or efficiency gain]
- 24/7 operation with consistent output

[QUOTE NEEDED from [client contact] about the impact achieved]

What's Next: [Future Vision]

[CLIENT] is now exploring how to expand [YOUR SOLUTION] across other departments including [AREAS]. The success in [INITIAL USE CASE] has opened opportunities for [BROADER APPLICATION].

[QUOTE NEEDED from [client contact] about future AI adoption plans]

Build your AI Workforce
Grow your business, not your headcount
[Request demo](/link)
```

**Key Principle:** Always deliver a complete structure. Better to have placeholders the user can fill in than an incomplete document.
