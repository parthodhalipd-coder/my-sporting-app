import streamlit as st
import time
import random

# ১. পেজ সেটিংস
st.set_page_config(page_title="Partho's Live Animation", layout="wide")

st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🏏 Partho's Live Cricket Animation</h1>", unsafe_allow_html=True)

# ২. এনিমেশন সোর্স (এগুলো স্থায়ী লিঙ্ক)
animations = {
    "four": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlU9asclnE2bCDe/giphy.webp",
    "six": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlO4y4YfFq9z8uA/giphy.webp",
    "out": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKMGpxx6B8XgKqA/giphy.webp",
    "waiting": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKz9H0D8oG5eXUo/giphy.webp"
}

# ৩. লেআউট
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Live Score")
    score_display = st.empty()
    status_msg = st.empty()

with col2:
    st.subheader("📺 Match Animation")
    video_display = st.empty()

# ৪. স্কোর কন্ট্রোল
if 'runs' not in st.session_state:
    st.session_state.runs = 0
if 'wickets' not in st.session_state:
    st.session_state.wickets = 0

# ৫. রান করানো
event = random.choice(["0", "1", "2", "4", "6", "W"])

if event == "W":
    st.session_state.wickets += 1
    status_msg.error("🔴 OUT! উইকেট পড়ে গেল!")
    video_display.image(animations["out"], use_container_width=True)
elif event == "4":
    st.session_state.runs += 4
    status_msg.success("🔥 4 Runs! দারুণ বাউন্ডারি!")
    video_display.image(animations["four"], use_container_width=True)
elif event == "6":
    st.session_state.runs += 6
    status_msg.success("🚀 6 Runs! বিশাল ছক্কা!")
    video_display.image(animations["six"], use_container_width=True)
else:
    st.session_state.runs += int(event)
    status_msg.info("🏏 খেলা চলছে...")
    video_display.image(animations["waiting"], use_container_width=True)

score_display.metric("Total Score", f"{st.session_state.runs} / {st.session_state.wickets}")

# ৫ সেকেন্ড পর পর অটো-রিফ্রেশ
time.sleep(5)
st.rerun()
