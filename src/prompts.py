"""AI prompt templates for each content type."""

from src.profile import PROFILE_CONTEXT

SYSTEM_PROMPT = """You are a personal branding and content strategy expert specializing in public health 
and healthcare careers. You create compelling, authentic content that positions the person as a 
thought leader. The content should be:
- Authentic and genuine (no corporate speak)
- Specific and data-driven where possible
- Actionable for the reader
- Optimized for the platform (LinkedIn, blog, Twitter/X)
- Written from the perspective of the profile provided
- Free of filler phrases and clichés
"""


def _base_context(fields: dict) -> str:
    parts = [f"{k.replace('_', ' ').title()}: {v}" for k, v in fields.items() if v]
    return "\n".join(parts)


def build_prompt(content_type: str, fields: dict, tone: str, audience: str, length: str) -> str:
    context = _base_context(fields)

    type_instructions = {
        "linkedin_post": f"""Write a LinkedIn post about "{fields.get('topic', 'public health data')}".
Structure:
1. Hook — open with a bold statement, question, or surprising fact
2. Story/Insight — share a specific perspective or experience
3. Value — give the reader something actionable or thought-provoking
4. Call to action — encourage engagement
5. 3-5 relevant hashtags

The post should be {length.lower()} (short=~100 words, medium=~200 words, long=~300 words).
Tone: {tone}. Audience: {audience}.
Include line breaks for readability. No emojis in professional tone.""",

        "blog_topic": f"""Create a detailed blog post outline for itsbrook.com about "{fields.get('topic', 'public health data')}".
Include:
1. SEO-optimized title (with primary keyword)
2. Meta description (150-160 characters)
3. Target keywords (5-8) for SEO
4. Introduction hook
5. 4-6 section headings with brief descriptions
6. Key data points or examples to include
7. Internal linking suggestions (to other itsbrook.com pages)
8. Call to action for the end
Tone: {tone}. Audience: {audience}.""",

        "content_calendar": f"""Create a monthly content calendar for {fields.get('month', 'the upcoming month')}.
Goals: {fields.get('goals', 'build thought leadership, attract recruiters')}
Focus areas: {fields.get('focus_areas', 'career transition, data analysis, health equity')}

For each week, provide:
- 2-3 LinkedIn posts (with topic, angle, best day/time to post)
- 1 blog post topic (with title and outline)
- 1 Twitter/X thread idea
- 1 engagement action (comment on others' posts, join a discussion, etc.)

Include a mix of content types: educational, personal story, data insight, opinion.
Tone: {tone}.""",

        "thought_leadership": f"""Write a thought leadership piece about "{fields.get('topic', 'public health')}".
Opinion: {fields.get('opinion', 'provide a strong, informed take')}
Evidence: {fields.get('evidence', 'use general knowledge')}

Structure:
1. Opening — bold claim or observation
2. Context — why this matters now
3. Evidence — data, trends, real examples
4. Your take — clear, opinionated stance
5. Implications — what this means for the field
6. Call to action — what readers should do

Tone: {tone}, confident, slightly provocative. Audience: {audience}.
Length: {length}.""",

        "portfolio_project": f"""Write a portfolio project description for "{fields.get('project_name', 'the project')}".
Type: {fields.get('project_type', 'project')}
What it does: {fields.get('description', '')}
Tech stack: {fields.get('tech_stack', '')}
Impact: {fields.get('impact', '')}

Structure:
1. Project name and one-line description
2. Problem — what challenge does it solve?
3. Solution — how does it work?
4. Tech stack — bulleted list
5. Key features — 3-5 highlights
6. Impact/Results — measurable outcomes
7. Screenshots/Demo link placeholder
8. What I learned — personal growth angle

Tone: {tone}. Audience: {audience}.""",

        "twitter_thread": f"""Write a {fields.get('num_tweets', '7')}-tweet educational thread about "{fields.get('topic', 'public health data')}".
Angle: {fields.get('thread_angle', 'informative and practical')}

Rules:
- Tweet 1 is the hook (attention-grabbing, makes people want to read more)
- Each tweet should be self-contained but flow into the next
- Include a specific insight or data point in each tweet
- End with a summary tweet and call to action
- Use numbered tweets (1/X, 2/X format)
- Keep each tweet under 280 characters
- No hashtags except the final tweet
- Thread should be {length.lower()} overall

Tone: {tone}. Audience: {audience}.""",
    }

    instruction = type_instructions.get(content_type, "Write professional personal branding content.")

    return f"""{SYSTEM_PROMPT}

AUTHOR PROFILE:
{PROFILE_CONTEXT}

CONTENT DETAILS:
{context}

TARGET AUDIENCE: {audience}
TONE: {tone}
LENGTH: {length}

INSTRUCTIONS:
{instruction}

Write the content now. Do not include placeholders — use the author's actual name and credentials from the profile."""