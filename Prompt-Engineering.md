# Prompt Engineering

This page is intented to teach and support the mastering of prompt engineering. Some texts and examples are taken from [gptprompts.ai](https://gptprompts.ai/) and [promptingguide.ai](https://www.promptingguide.ai/).

## Overview/Cheat Sheet

| Problem | Technique | Reason |
| :-- | :-- | :-- |
| Ensure advice matches moral | Constitutional AI | Set rules first |
| Trust the plan | Chain-of-Verification | Double-checks work |
| Make a hard choice | Tree of Thoughts (ToT) | Weighs trade-offs |
| Gegt specific expert help | Role-Based | Respects contraints |
| Write something important | Recursive Prompting | Polishes via critique |
| Coordinate logistics | Model-First Reasoning | Catches conflicts |
| Analyze big data | Recursive Language Models | Acts like a search script |

## Constitutional AI

### Description
Use constitutional directions to guide the LLM to create better and more focused output.

### Model-Specific Tips

| Model | Tip |
| :--: | :-- |
| GPT-4 | Define the constitution in the system prompt. GPT-4 follows constitutional constraints well. Use numbered principles for clarity. |
| Claude | Claude was literally trained with Constitutional AI methods. It responds exceptionally well to explicit principles and self-critique instructions. |
| Gemini | Gemini supports constitutional prompting. Define principles clearly and ask for self-evaluation. Gemini can rate compliance with each principle. |

### Pros & Cons

| Pros | Cons |
| :-- | :-- |
| Enforces consistent standards | Complex to set up the right principles |
| Self-auditing reduces review burden | Higher token usage due to self-critique |
| Scalable quality control | Model may game its own rules |
| Customizable to any domain or brand | Requires testing to calibrate principles |

### Example Prompts
```
[CONSTITUTION]
- Suggestions must be evidence-Based (cite pediatric source).
- No punishment-based approaches.
- Prioritize child's relationship with food over compliance.

[REQUEST]
My 5-year-old won't eat vegetables. What do I do?
```

```
CONSTITUTION:
1. All claims must be verifiable
2. No superlatives without evidence
3. Acknowledge limitations honestly
4. Include actionable advice
5. Avoid jargon — write for a general audience

Task: Write a guide on investing in index funds.

After writing, review your output against each constitutional principle. Revise any violations.
```

## Chain-of-Verification (CoVe)

### Description

Fact-checking high-stakes planning where accuracy is non-negotiable uses a 4-step approach:

1. Initial plan
2. Generate Verification Questions
3. Self-Correction
4. Final Verified Plan

### Model-Specific Tips

| Model | Tip |
| :--: | :-- |
| GPT-4 | GPT-4 handles CoVe well. Structure the verification as explicit steps in your prompt. Use system prompts to enforce the verify-then-respond pattern. |
| Claude | Claude is excellent at CoVe due to its tendency toward honesty. Ask Claude to assign confidence levels and it will flag uncertain claims proactively. |
| Gemini | Gemini supports CoVe reasoning. Use structured prompts with clear verification steps. Gemini's grounding capabilities can enhance verification. |

### Pros & Cons

| Pros | Cons |
| :-- | :-- |
| Dramatically reduces hallucinations | Very high token usage (4-5x baseline) |
| Self-verifying — catches factual errors | Slower due to multi-step verification |
| Provides confidence levels for claims | Model may verify against incorrect training data |
| Essential for high-stakes content | Can't verify truly novel information |

### Example Prompts

```
Write a summary of the key features of PostgreSQL 16.

Now list every factual claim in your summary as a numbered list.

For each claim, generate a verification question and answer it. Flag any claims you're uncertain about.

Finally, produce a revised summary that only includes verified claims.
```
```
Explain the differences between React Server Components and traditional SSR.

Verify each technical claim by questioning yourself: 'Is this actually true? What's my confidence level?' Revise any uncertain claims.
```
```
Describe the tax implications of converting a traditional IRA to a Roth IRA.

List every financial/legal claim made. For each one, verify it against your training data. Mark confidence as HIGH/MEDIUM/LOW. Remove or caveat anything below HIGH confidence.
```

## Tree of Thoughts (ToT)

### Description

For complex tasks that require exploration or strategic lookahead, traditional or simple prompting techniques fall short. Tree of Thoughts (ToT) is a framework that generalizes over chain-of-thought prompting and encourages exploration over thoughts that serve as intermediate steps for general problem solving with language models.

### Model-Specific Tips

| Model | Tip |
| :--: | :-- |
| GPT-4 |  |
| Claude |  |
| Gemini |  |
| Grok | Grok is built by this concept. |

### Pros & Cons

| Pros | Cons |
| :-- | :-- |
|  |  |
|  |  |
|  |  |
|  |  |

### Example Prompts

```
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
The question is...
```
