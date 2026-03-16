import streamlit as st
import time
import random

# ১. পেজ সেটিংস
st.set_page_config(page_title="Partho's Live Cricket", layout="wide")

# ২. টাইটেল ডিজাইন
st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🏏 Partho's Live Cricket Animation</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #white;'>Developer: Partho</p>", unsafe_allow_html=True)

# ৩. এনিমেশন সোর্স (এগুলো সরাসরি কাজ করবে)
animations = {
    "four": "https://media.giphy.com/media/l0HlU9asclnE2bCDe/giphy.gif",
    "six": "https://media.giphy.com/media/l0HlO4y4YfFq9z8uA/giphy.gif",
    "out": "https://media.giphy.com/media/3o7TKMGpxx6B8XgKqA/giphy.gif",
    "waiting": "https://media.giphy.com/media/3o7TKz9H0D8oG5eXUo/giphy.gif"
}

# ৪. লেআউট তৈরি
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Live Scoreboard")
    score_val = st.empty()
    status_text = st.empty()

with col2:
    st.subheader("📺 Match View")
    anim_placeholder = st.empty()

# ৫. সেশন স্টেট (স্কোর ধরে রাখার জন্য)
if 'runs' not in st.session_state:
    st.session_state.runs = 0
if 'wickets' not in st.session_state:
    st.session_state.wickets = 0

# ৬. মেইন রানার (বাটন ছাড়াই চলবে)
# এটি লুপের মাধ্যমে ৫ সেকেন্ড পর পর স্ক্রিন আপডেট করবে
def start_stream():
    event = random.choice(["0", "1", "2", "4", "6", "W"])
    
    if event == "W":
        st.session_state.wickets += 1
        status_text.error("🔴 OUT! উইকেট পড়ে গেল!")
        anim_placeholder.image(animations["out"], use_container_width=True)
    elif event == "4":
        st.session_state.runs += 4
        status_text.success("🔥 boundary! চার রান!")
        anim_placeholder.image(animations["four"], use_container_width=True)
    elif event == "6":
        st.session_state.runs += 6
        status_text.success("🚀 SIX! বিশাল ছক্কা!")
        anim_placeholder.image(animations["six"], use_container_width=True)
    else:
        st.session_state.runs += int(event)
        status_text.info("🏏 ডট বল বা সিঙ্গেল রান...")
        anim_placeholder.image(animations["waiting"], use_container_width=True)
    
    score_val.metric("Score", f"{st.session_state.runs} / {st.session_state.wickets}")

# ৭. অটো-রিফ্রেশ মেকানিজম
# প্রতি ৫ সেকেন্ডে পেজটি নিজে থেকেই আপডেট হবে
start_stream()
time.sleep(5)
st.rerun()
