"""
Content Strategy — AI-powered personal branding content generator.

Built for Brook Eshete, MD, MPH — Johns Hopkins Bloomberg School of Public Health.
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

from src.content_types import CONTENT_TYPES, TOPICS, AUDIENCES, LENGTHS, TONES
from src.prompts import build_prompt
from src.ai_service import check_ollama_available, generate_content, regenerate_content
from src.profile import PROFILE

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Content Strategy — Personal Brand",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1A1A2E 0%, #0D7377 100%);
        padding: 1.5rem 2rem;
        border-radius: 0.5rem;
        color: white;
        margin-bottom: 1.5rem;
    }
    .main-header h1 { margin: 0; font-size: 1.8rem; }
    .main-header p { margin: 0.3rem 0 0; opacity: 0.85; }
    .content-output {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.5rem;
        padding: 1.5rem;
        white-space: pre-wrap;
        font-family: inherit;
        line-height: 1.7;
    }
</style>
""", unsafe_allow_html=True)

# ─── Session State ──────────────────────────────────────────────────────────────
if "current_content" not in st.session_state:
    st.session_state.current_content = ""
    st.session_state.current_prompt = ""
    st.session_state.history = []
    st.session_state.selected_type = "linkedin_post"

# ─── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ✍️ Content Strategy")
    st.markdown("---")

    ollama_ok = check_ollama_available()
    if ollama_ok:
        st.success("🟢 AI connected")
    else:
        st.warning("🔴 AI unavailable")
        st.caption("Start Ollama for content generation")

    st.markdown("---")

    st.markdown("#### 👤 Profile")
    st.markdown(f"**{PROFILE['full_title']}**")
    st.caption(PROFILE["summary"][:120] + "...")
    if st.button("View Full Profile"):
        st.markdown(f"**Name:** {PROFILE['name']}")
        st.markdown(f"**Website:** {PROFILE['website']}")
        st.markdown(f"**Skills:** {', '.join(PROFILE['skills']['data_analysis'] + PROFILE['skills']['visualization'])}")
        st.markdown(f"**Focus:** {', '.join(PROFILE['target_roles'][:3])}")

    st.markdown("---")

    st.markdown("#### 📜 History")
    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history)):
            type_label = CONTENT_TYPES.get(item["type"], {}).get("label", item["type"])
            if st.button(f"{type_label}", key=f"hist_{i}"):
                st.session_state.current_content = item["content"]
                st.rerun()
    else:
        st.caption("No content generated yet")

    st.markdown("---")
    st.caption("Built by **Brook Eshete, MD, MPH**")

# ─── Main Content ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>✍️ Content Strategy Generator</h1>
    <p>AI-powered personal branding content for public health professionals</p>
</div>
""", unsafe_allow_html=True)

# ─── Content Type Selection ────────────────────────────────────────────────────
st.markdown("### What type of content?")

type_cols = st.columns(3)
selected_type = st.session_state.get("selected_type", "linkedin_post")

for i, (key, val) in enumerate(CONTENT_TYPES.items()):
    with type_cols[i % 3]:
        is_selected = selected_type == key
        if st.button(
            val["label"],
            key=f"type_{key}",
            use_container_width=True,
            type="primary" if is_selected else "secondary",
        ):
            st.session_state.selected_type = key
            st.rerun()

email_type = st.session_state.get("selected_type", "linkedin_post")
type_config = CONTENT_TYPES[email_type]
st.caption(f"_{type_config['description']}_")

# ─── Common Fields ──────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### Settings")

col1, col2, col3 = st.columns(3)
with col1:
    audience = st.selectbox("Target Audience", AUDIENCES, index=0)
with col2:
    tone = st.selectbox("Tone", TONES, index=0)
with col3:
    length = st.selectbox("Length", LENGTHS, index=1)

# ─── Content-Specific Fields ────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### Details")

form_fields = {}
cols = st.columns(2)
for i, field in enumerate(type_config["fields"]):
    with cols[i % 2]:
        if field["type"] == "text":
            form_fields[field["key"]] = st.text_input(
                field["label"],
                placeholder=field.get("placeholder", ""),
                key=f"input_{field['key']}",
            )
        elif field["type"] == "textarea":
            form_fields[field["key"]] = st.text_area(
                field["label"],
                placeholder=field.get("placeholder", ""),
                height=100,
                key=f"input_{field['key']}",
            )
        elif field["type"] == "select":
            options = TOPICS if field.get("options_source") == "topics" else field.get("options", [])
            form_fields[field["key"]] = st.selectbox(
                field["label"],
                options,
                key=f"input_{field['key']}",
            )

# ─── Generate ───────────────────────────────────────────────────────────────────
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    generate_btn = st.button("✨ Generate Content", type="primary", use_container_width=True, disabled=not ollama_ok)
with col2:
    tweak = st.text_input("Tweak instructions (optional)", placeholder="E.g., make it shorter, add data points...", key="tweak_input")
    regenerate_btn = st.button("🔄 Regenerate", use_container_width=True, disabled=not ollama_ok or not st.session_state.current_content)

if generate_btn:
    filled_fields = {k: v for k, v in form_fields.items() if v}
    if not filled_fields:
        st.warning("Please fill in at least a few fields before generating.")
    else:
        prompt = build_prompt(email_type, filled_fields, tone, audience, length)
        st.session_state.current_prompt = prompt
        with st.spinner("Generating content..."):
            try:
                content = generate_content(prompt)
                st.session_state.current_content = content
                st.session_state.history.append({
                    "type": email_type,
                    "content": content,
                    "fields": filled_fields,
                    "tone": tone,
                    "audience": audience,
                    "length": length,
                })
            except Exception as e:
                st.error(f"Error generating content: {e}")
        st.rerun()

if regenerate_btn and st.session_state.current_content:
    with st.spinner("Regenerating..."):
        try:
            content = regenerate_content(st.session_state.current_prompt, tweak)
            st.session_state.current_content = content
            if st.session_state.history:
                st.session_state.history[-1]["content"] = content
        except Exception as e:
            st.error(f"Error regenerating: {e}")
    st.rerun()

# ─── Output ─────────────────────────────────────────────────────────────────────
if st.session_state.current_content:
    st.markdown("### Generated Content")
    st.markdown(f'<div class="content-output">{st.session_state.current_content}</div>', unsafe_allow_html=True)

    st.code(st.session_state.current_content, language=None)
    st.caption("Copy the text above to paste into your content platform.")