---
name: youtube-to-linkedin-converter
description: Transform YouTube transcripts into LinkedIn posts with automatic post type detection and multiple hook variations in Elliot Garreffa's style
---

# YouTube to LinkedIn Converter - Claude Skill v1.0

## Purpose
Transform YouTube video transcripts into high-performing LinkedIn posts with **automatic post type detection** and **multiple hook variations** in Elliot Garreffa's authentic style.

## How This Works

When you provide a YouTube transcript + context, this skill will:

1. **Analyze the transcript content** to extract key insights, examples, and takeaways
2. **Determine which LinkedIn post types** best fit the content (top 2-3 types)
3. **For each type, generate a full LinkedIn post (242 words, 20 lines)**
4. **Create 3 hook variations** for each post type
5. **Result**: 6-9 complete LinkedIn posts to choose from

---

## Input Format

**Step 1**: Paste the YouTube transcript(s)
- Can be one or multiple video transcripts
- Auto-generated or manual transcripts both work
- No need to clean formatting - I'll extract the key content

**Step 2**: Provide context (optional but recommended)
Examples:
- "Create a post about the AI automation workflow mentioned in this video"
- "Focus on the cost-saving aspects of the tool"
- "Make this about the tutorial they showed for building agents"
- "Extract the contrarian take about no-code tools"
- "Turn this into a post announcing the new feature they revealed"

**If no context provided**: I'll analyze the entire transcript and create posts around the most compelling insights.

---

## Elliot's 8 LinkedIn Post Types

1. **Opinion/Hot Take** - 3,638 avg engagement ⭐️ (viral reach)
2. **Cost Transformation** - 2,665 avg engagement ⭐️ (value demo)
3. **Tutorial** - 1,880 avg engagement ⭐️ (education)
4. **Lead Magnet** - 1,741 avg engagement ⭐️ (lead generation)
5. **Tool Announcement** - 1,604 avg engagement (authority)
6. **Behind the Scenes** - 1,005 avg engagement (brand building)
7. **Results/Case Study** - 394 avg engagement (proof)
8. **Thought Leadership** - 62 avg engagement (discussion)

---

## LinkedIn Post Structure (Based on 204 Posts)

**Average length**: 242 words
**Average lines**: 20 lines

**Standard structure**:
```
[HOOK - 1-2 sentences that grab attention]
[CONTEXT - 2-3 sentences about the problem/situation]
[TRANSITION - "How is this possible?" or "Meanwhile, I now..."]
[MAIN CONTENT - 15-20 lines with arrows → or emoji numbers 1️⃣2️⃣3️⃣]
[IMPACT STATEMENT - "The craziest part?"]
[CTA - "Comment '[KEYWORD]'" for Lead Magnets]
```

---

## Transcript Analysis Process

### Step 1: Extract Key Elements

From the transcript, identify:

**Tools/Technologies mentioned**:
- AI tools (Claude, ChatGPT, n8n, Apify, etc.)
- Integrations and platforms
- Specific features or capabilities

**Results/Metrics mentioned**:
- Dollar amounts ($50k/month, $100/month, etc.)
- Time savings (weeks → minutes)
- Scale metrics (15 different tools → 1)
- ROI calculations

**Use cases/Examples**:
- Specific applications demonstrated
- Industry examples
- Real-world scenarios
- Problem-solution pairs

**Steps/Methods**:
- Tutorial steps shown
- Workflows explained
- Implementation processes
- Setup instructions

**Insights/Opinions**:
- Contrarian takes
- Bold predictions
- Industry commentary
- "Why this matters" statements

**Context clues**:
- Problems being solved
- What people are doing wrong
- Market gaps identified
- Future implications

### Step 2: Match to Post Types

| Transcript Content | LinkedIn Type |
|-------------------|---------------|
| Tutorial walkthrough with steps | Tutorial, Lead Magnet |
| Cost comparison or pricing revelation | Cost Transformation, Lead Magnet |
| New tool/feature demo | Tool Announcement, Tutorial |
| Build showcase or test results | Results/Case Study, Tutorial |
| Contrarian statement or hot take | Opinion/Hot Take |
| Company/team process reveal | Behind the Scenes |
| Multiple use cases shown | Lead Magnet, Tutorial |
| Industry insights or predictions | Thought Leadership, Opinion |

### Step 3: Select Top 2-3 Types

Use this priority matrix based on content:

| Transcript About | Primary | Secondary | Tertiary |
|-----------------|---------|-----------|----------|
| Building an agency-level system | Lead Magnet | Cost Transformation | Tutorial |
| New tool walkthrough | Tool Announcement | Tutorial | Lead Magnet |
| Cost savings demo | Cost Transformation | Lead Magnet | Tutorial |
| Step-by-step tutorial | Tutorial | Lead Magnet | Results |
| Contrarian opinion | Opinion/Hot Take | Thought Leadership | - |
| Team/company showcase | Behind the Scenes | Lead Magnet | Results |
| Testing/building something | Results/Case Study | Tutorial | Lead Magnet |
| Multiple tools combined | Lead Magnet | Tutorial | Tool Announcement |

---

## Hook Patterns by Post Type

### Lead Magnet Hooks (1,741 avg engagement) ⭐️

**Hook 1: Value-first**
```
So... I now have a $[amount]/month [service], directly in my Claude.

[Brief description of capability]
```

**Hook 2: Problem-solution**
```
Most [people/companies] are still [old painful way].

Meanwhile, I [new better way].
```

**Hook 3: Curiosity**
```
I just finished building [impressive thing].

Here's what it can do:
```

### Cost Transformation Hooks (2,665 avg engagement) ⭐️

**Hook 1: Before/after**
```
[Service] used to cost $[high amount]/month [old way]

Now it's $[low amount] [new way]
```

**Hook 2: ROI focus**
```
Most companies pay $[amount]/month for [service].

I do it for $[much lower amount].

Same results. [X]x less cost.
```

**Hook 3: Time + cost savings**
```
[Service]:
• Old way: $[amount]/month, [time] of work
• New way: $[lower amount]/month, [less time] of work

[X]x cheaper. [Y]x faster.
```

### Tutorial Hooks (1,880 avg engagement) ⭐️

**Hook 1: "Here's how" direct**
```
Here's how to [achieve specific result]:
```

**Hook 2: Result + setup**
```
I [achieved impressive result].

Here's the exact setup:
```

**Hook 3: Method name**
```
The [number]-step method to [achieve result]:
```

### Tool Announcement Hooks (1,604 avg engagement)

**Hook 1: "Just released"**
```
[Tool] just released [feature], and [impact statement]
```

**Hook 2: "NEW release"**
```
NEW release: [Tool] now has [feature]

[Impact statement]
```

**Hook 3: Capability reveal**
```
[Tool] can now [impossible-sounding capability]

This changes everything.
```

### Opinion/Hot Take Hooks (3,638 avg engagement) ⭐️ HIGHEST

**Hook 1: "AI is going bananas"**
```
AI is going bananas...

[Company] just released [feature] & it's [impact]
```

**Hook 2: "Unpopular opinion"**
```
Unpopular opinion: [contrarian statement]
```

**Hook 3: Bold prediction**
```
[Bold prediction about the future]

Here's why:
```

### Behind the Scenes Hooks (1,005 avg engagement)

**Hook 1: "Ok... so"**
```
Ok... so [capability statement]

We built [internal tool] so good that [impact]
```

**Hook 2: "We built"**
```
We built [internal tool] for Ghost Team.

It was so good we had to share it.
```

**Hook 3: Milestone**
```
Ghost Team just [milestone/achievement]

Here's how we did it:
```

### Results/Case Study Hooks (394 avg engagement)

**Hook 1: "I tested"**
```
I tested [tool/feature] on [specific use case].

The results: [impressive outcome]
```

**Hook 2: "I built"**
```
I built [project] with [tool].

[Impressive metric or outcome]
```

**Hook 3: "I used"**
```
I used [tool] to [achieve impressive result].

Here's what happened:
```

---

## Expansion Strategy: Transcript → LinkedIn Post

### From Transcript Insight → Full LinkedIn Post (242 words)

**Example Transcript Excerpt**:
```
"...and with this new MCP integration from Apify, you can basically scrape any website directly from Claude. I tested it on market research and built a full research agency in like an hour. It cost me almost nothing compared to the $50k agencies charge..."
```

**LinkedIn Expansion Process**:

1. **Create Hook** (Choose post type first)
   - Lead Magnet: "So... I now have a $50k/month market research agency, directly in my Claude."
   - Cost Transformation: "Market research used to cost $50k/month with an agency. Now it's <$100."
   - Tutorial: "Here's how to build a market research agency in Claude:"

2. **Add Context Paragraph** (2-3 sentences)
   ```
   Most businesses are still paying $50k/month for basic market research. They wait weeks for reports. They're spending 100x more than they need to. Meanwhile, there's a better way.
   ```

3. **Add Transition** ("How is this possible?")
   ```
   How is this possible?
   
   Apify just released MCP integration for Claude. You can now scrape the entire web directly inside one chat window.
   ```

4. **Expand into Use Cases** (15-25 with arrows →)
   ```
   Here's just some of what you can now do in minutes:
   
   Sales Outreach:
   → Scrape LinkedIn for decision makers
   → Analyze their recent posts and pain points
   → Generate personalized outreach sequences
   → All without leaving Claude
   
   Market Analysis:
   → Pull Reddit comments from your industry
   → Extract sentiment and pain points at scale
   → Identify market gaps in real-time
   → Generate interactive HTML reports
   
   [Continue with 3-5 more categories...]
   ```

5. **Add Tutorial Steps** (if Tutorial type)
   ```
   Here's how it works:
   
   1️⃣ Gather the data → Prompted Claude to scrape YouTube comments from AI tool reviews
   
   2️⃣ Analyzes everything → Claude worked with Apify to find patterns in pain points
   
   3️⃣ Build the website → Claude generated a full interactive HTML report with charts
   ```

6. **Add Impact Statement** ("The craziest part?")
   ```
   The craziest part?
   
   Everything happens inside one chat window with Claude. No switching between 15 different tools. No manual data entry. No copy-pasting between apps.
   ```

7. **Add CTA** (if Lead Magnet)
   ```
   Want the complete setup guide?
   
   - Comment 'MCP'
   - I'll send you access (connect so I can DM)
   
   I'll DM you everything
   
   Happy building
   ```

**Result**: ~250 words, 20 lines, perfectly formatted LinkedIn post

---

## Complete Example Output

### Input

**Transcript**: [1200-word transcript about building AI automation with n8n]

**Context**: "Focus on the workflow builder tutorial and how it saves time"

### Output

## POST TYPE 1: TUTORIAL (Avg Engagement: 1,880) ⭐️

### Hook Variation 1: "Here's how" direct

Here's how to build any AI automation with just a prompt:

Most people are still manually connecting every single node in n8n. They're watching hour-long tutorials. They're debugging workflows for days.

Meanwhile, AI just did it in 30 seconds.

How is this possible?

n8n just released their AI Workflow Builder. You describe what you want in plain English, and it generates the entire automation for you.

Here's what you can build in minutes:

Content Automation:
→ Monitor RSS feeds for keywords
→ Extract content and summarize with AI
→ Post to LinkedIn, Twitter, and your blog
→ All on autopilot

Lead Generation:
→ Scrape LinkedIn for decision makers
→ Enrich with company data
→ Score leads with AI
→ Send personalized outreach
→ Track responses in your CRM

Customer Support:
→ Monitor support channels
→ Classify urgent issues with AI
→ Auto-respond to common questions
→ Escalate complex issues to humans
→ Log everything in your helpdesk

Sales Automation:
→ Track competitor pricing changes
→ Alert your team in Slack
→ Generate counter-proposals with AI
→ Update opportunities in Salesforce
→ Create follow-up tasks

Here's how it works:

1️⃣ Describe your workflow → "When someone fills my form, enrich their data and add them to HubSpot"

2️⃣ AI builds it → n8n generates the entire workflow with proper connections

3️⃣ Test and deploy → Review, adjust if needed, and activate

That's it.

The craziest part?

You don't need to know how to code. You don't need to understand webhooks. You don't even need to know what n8n is.

Just describe what you want, and AI builds it.

Want the complete guide to automating your business with AI?

- Comment 'WORKFLOW'
- I'll send you access (connect so I can DM)

I'll DM you everything

Happy building

---

**Metadata**:
- Word count: 298
- Line count: 47
- Post type: Tutorial
- Key elements: "Here's how" hook, emoji numbers, arrows, multiple categories, CTA
- Visual suggestion: Video screen recording showing AI workflow generation in action
- Expected engagement: 1,500-2,000

---

### Hook Variation 2: Result + setup

I just automated 90% of my business operations with AI.

Here's the exact setup:

[Same main content as above, but with different hook]

---

**Metadata**:
- Word count: 295
- Line count: 46
- Key elements: Result-focused hook, emoji numbers, arrows, CTA
- Visual suggestion: Before/after comparison - manual workflow vs AI-generated
- Expected engagement: 1,400-1,800

---

### Hook Variation 3: The X-step method

The 3-step method to automate any workflow with AI:

[Same main content as above, but with method-name hook]

---

**Metadata**:
- Word count: 292
- Line count: 45
- Key elements: Method-name hook, numbered steps, use cases, CTA
- Visual suggestion: Infographic showing the 3-step process
- Expected engagement: 1,300-1,700

---

## POST TYPE 2: LEAD MAGNET (Avg Engagement: 1,741) ⭐️

### Hook Variation 1: Value-first

So... I now have a complete automation agency, directly in n8n.

Build any workflow with just a prompt. No code. No complexity.

[Full post with Lead Magnet structure including 15-25 use cases and strong CTA]

---

### Hook Variation 2: Problem-solution

Most companies are still paying developers $150/hour to build automations.

Meanwhile, I'm building them in 30 seconds with AI.

[Full post with problem-solution angle]

---

### Hook Variation 3: Curiosity

I just finished building a complete automation system that runs my entire business.

Here's what it can do:

[Full post with curiosity-driven hook]

---

## POST TYPE 3: COST TRANSFORMATION (Avg Engagement: 2,665) ⭐️

### Hook Variation 1: Before/after

Automation used to cost $10k/month with a dev team

Now it's $20/month and 30 seconds with AI

[Full post with cost transformation angle]

---

[Continue with 2 more hook variations...]

---

## RECOMMENDATION

**Highest engagement potential**: Tutorial - Hook Variation 1 ("Here's how")
- Why: Tutorial format + practical steps + strong CTA combination
- Expected: 1,500-2,000 engagement

**Best for lead generation**: Lead Magnet - Hook Variation 1 (Value-first)
- Why: "So..." hook + dollar amount + extensive use cases + CTA
- Expected: 1,400-1,800 engagement

**Best for viral reach**: Cost Transformation - Hook Variation 1
- Why: Shocking cost savings resonate widely
- Expected: 2,000-2,500 engagement

---

## Transcript Extraction Best Practices

### Extract These Elements

**1. Specific Numbers & Metrics**
- Dollar amounts mentioned ($50k, $100)
- Time savings (weeks → minutes)
- Multipliers (10x faster, 500x cheaper)
- Scale metrics (15 tools → 1)

**2. Tools & Technologies**
- Primary tools demonstrated
- Integrations mentioned
- Platforms connected
- Specific features used

**3. Use Cases & Examples**
- Real-world applications shown
- Industry examples mentioned
- Problem-solution pairs
- Specific scenarios

**4. Steps & Methods**
- Tutorial steps demonstrated
- Setup processes shown
- Implementation workflow
- Configuration details

**5. Insights & Opinions**
- "Why this matters" statements
- Contrarian takes
- Bold predictions
- Industry commentary

### Ignore These Elements

- Sponsor reads (unless about the featured tool)
- Channel housekeeping (like, subscribe, etc.)
- Unrelated tangents
- Off-topic discussions
- Technical errors or corrections
- Filler words and repeated content

---

## Quality Checklist

Before finalizing, verify each LinkedIn post has:

- [ ] 200-300 words (target: 242)
- [ ] 15-25 lines (target: 20)
- [ ] Hook matches post type
- [ ] Context paragraph (2-3 sentences on problem)
- [ ] Transition ("How is this possible?" or similar)
- [ ] Main content uses arrows (→) or emoji numbers (1️⃣2️⃣3️⃣)
- [ ] 15-25 use cases across 3-5 categories
- [ ] Step-by-step tutorial section (if Tutorial type)
- [ ] "The craziest part?" impact statement
- [ ] CTA with "Comment '[KEYWORD]'" (if Lead Magnet)
- [ ] Maintains Elliot's authentic voice
- [ ] Includes specific numbers/metrics from transcript
- [ ] More expanded and educational than original video
- [ ] Visual suggestion provided
- [ ] Estimated engagement range

---

## LinkedIn-Specific Formatting

### 1. Use Arrows (→) for Lists (43.6% of posts use them)
```
Content Automation:
→ Monitor RSS feeds for keywords
→ Extract content and summarize with AI
→ Post to LinkedIn, Twitter, and your blog
→ All on autopilot
```

### 2. Use Emoji Numbers for Steps (Tutorial posts)
```
Here's how it works:

1️⃣ Describe your workflow → "When someone fills my form, add them to HubSpot"

2️⃣ AI builds it → n8n generates the entire workflow

3️⃣ Test and deploy → Review, adjust, and activate
```

### 3. Use Category Groupings (15-25 use cases across 3-5 categories)
```
Sales Automation:
→ [4-6 specific use cases]

Customer Support:
→ [4-6 specific use cases]

Content Creation:
→ [4-6 specific use cases]
```

### 4. Use "The craziest part?" Transition
```
The craziest part?

You don't need to know how to code. You don't need to understand webhooks. Just describe what you want, and AI builds it.
```

### 5. Use Standard CTA Format (Lead Magnets only)
```
Want the complete [guide/setup/playbook]?

- Comment '[KEYWORD]'
- I'll send you access (connect so I can DM)

I'll DM you everything

Happy building
```

---

## Common Mistakes to Avoid

### ❌ Don't Do This

1. **Just summarizing the video**
   - ❌ "In this video, they showed how to..."
   - ✅ "I just automated 90% of my business operations with AI. Here's the exact setup:"

2. **Not expanding enough**
   - ❌ 3-5 use cases (too short)
   - ✅ 15-25 use cases across multiple categories

3. **Losing Elliot's voice**
   - ❌ "I would like to share an interesting tutorial..."
   - ✅ "So... I now have a complete automation agency, directly in n8n."

4. **Including video references**
   - ❌ "As shown in the video..." or "The creator mentioned..."
   - ✅ Make it your own experience: "I tested this..." or "I built..."

5. **Wrong hook for content**
   - ❌ Using cost transformation hook for tutorial content
   - ✅ Match hook to post type

6. **No CTA for Lead Magnets**
   - ❌ Ending without call-to-action
   - ✅ Include "Comment '[KEYWORD]'" format

---

## Voice & Tone Guidelines

**Elliot's Authentic Voice**:
- Conversational and casual
- Uses lowercase for accessibility  
- Direct and no-BS
- Results-focused
- Anti-gatekeeping
- Builds in public
- Educational > promotional
- Specific numbers and metrics
- "So..." and "ok..." openings
- "The craziest part?" transitions

**Maintain**:
- Technical accuracy from transcript
- Specific tool names and features
- Real metrics and results mentioned
- Practical, actionable content

**Add**:
- Elliot's conversational tone
- Expanded use cases (15-25)
- Cost comparisons where relevant
- Tutorial breakdowns
- Impact statements
- CTAs where appropriate

---

## Usage Instructions

### Quick Start

1. **Paste transcript**: Copy the YouTube transcript (or multiple transcripts)
2. **Add context** (optional): "Focus on [specific aspect]" or "Make this about [angle]"
3. **Get output**: Receive 6-9 complete LinkedIn posts across 2-3 post types
4. **Choose**: Pick the type and hook that fits your goal
5. **Post**: Copy and post directly, or customize further

### Advanced Usage

**For multiple transcripts**:
```
"Here are 3 video transcripts about AI automation. Create posts that combine insights from all of them, focusing on the cost-saving aspects."
```

**For specific angles**:
```
"Turn this transcript into an Opinion/Hot Take post about why no-code is better than code"
```

**For targeted outcomes**:
```
"Create Lead Magnet posts with strong CTAs for this tutorial transcript"
```

---

## Performance Expectations

Based on Elliot's 204 LinkedIn posts:

| Post Type + Hook | Expected Engagement | Best For |
|------------------|---------------------|----------|
| Tutorial + "Here's how" + emoji numbers | 1,500-2,000 | Education + engagement |
| Lead Magnet + "So..." + dollars | 1,500-2,200 | Lead generation |
| Cost Transformation + before/after | 1,800-2,500 | Value demonstration |
| Opinion/Hot Take + "AI is bananas" | 2,500-3,500 | Viral reach |
| Tool Announcement + "just released" | 1,200-1,600 | Authority building |
| Results/Case Study + "I tested" | 600-1,000 | Proof + credibility |

**Key Insights**:
- Posts with **video** get 705 avg engagement vs 115 for images
- **"So..." hook + dollar amounts** = highest performing combination
- **Emoji numbers (1️⃣2️⃣3️⃣)** in tutorials boost engagement
- **15-25 use cases** across categories perform better than 3-5
- **Lead Magnet CTAs** generate significant comments

---

## Example Prompts

### Basic Conversion
```
[Paste transcript]

Convert this YouTube transcript to LinkedIn posts
```

### Focused Conversion
```
[Paste transcript]

Create LinkedIn posts about the cost savings mentioned in this video. Focus on Cost Transformation and Lead Magnet types.
```

### Multi-Transcript Synthesis
```
[Paste 3 transcripts]

These are 3 videos about AI automation. Create Tutorial posts that combine the best insights from all of them.
```

### Specific Post Type
```
[Paste transcript]

Create Opinion/Hot Take posts about the contrarian view on no-code tools mentioned in this video.
```

---

## Metadata Tracking

Each generated post includes:

- **Word count**: Target 242 (200-300 acceptable)
- **Line count**: Target 20 (15-25 acceptable)
- **Post type**: Which of the 8 types
- **Hook variation**: 1, 2, or 3
- **Key elements**: Hooks, arrows, emoji numbers, CTA, etc.
- **Visual suggestion**: Recommended accompanying media
- **Expected engagement**: Range based on historical data

This helps you choose the best post and create matching visuals.

---

## Tips for Maximum Engagement

1. **Always add video** when posting
   - Screen recordings of the tutorial
   - Demo of the tool in action
   - Before/after comparisons
   - Video posts get 6x more engagement

2. **Use Lead Magnet CTAs** when offering guides
   - "Comment '[KEYWORD]'"
   - Creates high comment counts
   - Builds email list

3. **Match post type to goal**
   - Lead generation → Lead Magnet
   - Viral reach → Opinion/Hot Take
   - Education → Tutorial
   - Authority → Tool Announcement

4. **Test different hooks**
   - Try all 3 variations
   - See which resonates with your audience
   - Double down on what works

5. **Post at optimal times**
   - Tuesday-Thursday
   - 8-10am or 12-1pm
   - When Elliot's audience is most active

---

## Version History

**v1.0** - Initial release
- 8 post types with 3 hook variations each
- Transcript analysis and extraction
- 242-word average posts with 20 lines
- Lead Magnet CTA formatting
- Multiple category use cases (15-25)
- Voice and tone guidelines

