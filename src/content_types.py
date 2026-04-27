"""Content type definitions and field configurations."""

CONTENT_TYPES = {
    "linkedin_post": {
        "label": "💼 LinkedIn Post",
        "description": "Professional post for LinkedIn with hashtags",
        "fields": [
            {"key": "topic", "label": "Topic", "type": "select", "options_source": "topics"},
            {"key": "key_message", "label": "Key Message", "type": "textarea", "placeholder": "What's the main point you want to make?"},
            {"key": "personal_story", "label": "Personal Story/Angle (optional)", "type": "textarea", "placeholder": "E.g., a moment from clinical practice that shaped your view"},
        ],
    },
    "blog_topic": {
        "label": "📝 Blog Topic",
        "description": "Blog post outline with SEO keywords for itsbrook.com",
        "fields": [
            {"key": "topic", "label": "Topic", "type": "select", "options_source": "topics"},
            {"key": "title_idea", "label": "Working Title Idea (optional)", "type": "text", "placeholder": "E.g., Why Every Public Health Team Needs a Data Analyst"},
            {"key": "key_points", "label": "Key Points to Cover", "type": "textarea", "placeholder": "E.g., STATA vs Python for PH, real-world examples, career tips"},
        ],
    },
    "content_calendar": {
        "label": "📅 Content Calendar",
        "description": "Monthly content plan with posting schedule",
        "fields": [
            {"key": "month", "label": "Month", "type": "text", "placeholder": "E.g., May 2026"},
            {"key": "goals", "label": "Content Goals", "type": "textarea", "placeholder": "E.g., build thought leadership, attract recruiters, share portfolio projects"},
            {"key": "focus_areas", "label": "Focus Areas (select multiple)", "type": "textarea", "placeholder": "E.g., career transition, data viz tips, health equity"},
        ],
    },
    "thought_leadership": {
        "label": "💡 Thought Leadership",
        "description": "Opinion piece on a public health trend",
        "fields": [
            {"key": "topic", "label": "Topic", "type": "select", "options_source": "topics"},
            {"key": "opinion", "label": "Your Take/Stance", "type": "textarea", "placeholder": "E.g., AI will democratize public health data, not replace analysts"},
            {"key": "evidence", "label": "Supporting Evidence (optional)", "type": "textarea", "placeholder": "E.g., CDC data showing X trend, recent JAMA article on Y"},
        ],
    },
    "portfolio_project": {
        "label": "🔬 Portfolio Project",
        "description": "Write-up of a project for your portfolio",
        "fields": [
            {"key": "project_name", "label": "Project Name", "type": "text", "placeholder": "E.g., Public Health HIA"},
            {"key": "project_type", "label": "Type", "type": "text", "placeholder": "E.g., Data Analysis Tool, Dashboard, Research Paper"},
            {"key": "description", "label": "What It Does", "type": "textarea", "placeholder": "E.g., AI-powered tool that analyzes public health datasets"},
            {"key": "tech_stack", "label": "Tech Stack", "type": "text", "placeholder": "E.g., Python, Streamlit, Plotly, Ollama"},
            {"key": "impact", "label": "Impact/Results", "type": "textarea", "placeholder": "E.g., Processes 10K+ row datasets, identifies disparities automatically"},
        ],
    },
    "twitter_thread": {
        "label": "🧵 Twitter/X Thread",
        "description": "Educational thread on a public health topic",
        "fields": [
            {"key": "topic", "label": "Topic", "type": "select", "options_source": "topics"},
            {"key": "thread_angle", "label": "Angle/Hook", "type": "textarea", "placeholder": "E.g., 5 things I wish I knew before switching from clinical to public health data"},
            {"key": "num_tweets", "label": "Number of Tweets", "type": "select", "options": ["5", "7", "10"]},
        ],
    },
}