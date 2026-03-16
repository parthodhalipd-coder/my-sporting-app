import streamlit as st
import time
import random

# ১. পেজ সেটআপ
st.set_page_config(page_title="Partho's Live Cricket", layout="wide")

# ২. স্টাইল ও টাইটেল
st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🏏 Partho's Live Cricket Animation</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developer: Partho</p>", unsafe_allow_html=True)

# ৩. এনিমেশন সোর্স (এগুলো সরাসরি কাজ করবে, ব্লক হবে না)
# আমি এখানে Giphy-র সরাসরি ইমেজ লিঙ্ক ব্যবহার করছি
four_anim = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlU9asclnE2bCDe/giphy.webp"
six_anim = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlO4y4YfFq9z8uA/giphy.webp"
out_anim = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKMGpxx6B8XgKqA/giphy.webp"
wait_anim = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKz9H0D8oG5eXUo/giphy.webp"

# ৪. সেশন স্টেট (স্কোর ধরে রাখার জন্য)
if 'runs' not in st.session_state:
    st.session_state.runs = 0
if 'wickets' not in st.session_state:
    st.session_state.wickets = 0

# ৫. ডিসপ্লে এরিয়া
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Live Score")
    score_metric = st.empty()
    status_text = st.empty()

with col2:
    st.subheader("📺 Match Animation")
    anim_placeholder = st.empty()

# ৬. রান ও উইকেট লজিক
event = random.choice(["0", "1", "2", "4", "6", "W"])

if event == "W":
    st.session_state.wickets += 1
    status_text.error("🔴 OUT! উইকেট পড়ে গেল!")
    anim_placeholder.image(out_anim, use_container_width=True)
elif event == "4":
    st.session_state.runs += 4
    status_text.success("🔥 boundary! চার রান!")
    anim_placeholder.image(four_anim, use_container_width=True)
elif event == "6":
    st.session_state.runs += 6
    status_text.success("🚀 SIX! বিশাল ছক্কা!")
    anim_placeholder.image(six_anim, use_container_width=True)
else:
    st.session_state.runs += int(event)
    status_text.info("🏏 খেলা চলছে...")
    anim_placeholder.image(wait_anim, use_container_width=True)

score_metric.metric("Total Score", f"{st.session_state.runs} / {st.session_state.wickets}")

# ৭. অটো-রিফ্রেশ (প্রতি ৫ সেকেন্ডে)
time.sleep(5)
st.rerun()
