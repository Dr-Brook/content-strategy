# Content Strategy — Personal Brand Content Generator

AI-powered content strategy tool for public health professionals. Generate LinkedIn posts, blog outlines, content calendars, and more.

Built by **Brook Eshete, MD, MPH** — Johns Hopkins Bloomberg School of Public Health.

## Setup

```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## AI Setup

Requires Ollama with glm-5.1:cloud:
```bash
ollama pull glm-5.1:cloud
ollama serve
```

## Content Types

1. LinkedIn Post — professional post with hashtags
2. Blog Topic — outline with SEO keywords
3. Content Calendar — monthly posting schedule
4. Thought Leadership — opinion piece on a public health trend
5. Portfolio Project — project write-up for portfolio
6. Twitter/X Thread — educational thread

## Deploy

Push to GitHub → connect to [Streamlit Cloud](https://streamlit.io/cloud) → deploy.

## License

MIT