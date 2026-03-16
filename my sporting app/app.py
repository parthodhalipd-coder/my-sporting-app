import streamlit as st
import time
import random

# ১. পেজ সেটিংস
st.set_page_config(page_title="Partho's Pro Animation", layout="wide")

st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🏏 Partho's Live Cricket Animation</h1>", unsafe_allow_html=True)

# ২. অ্যানিমেশন সোর্স (সরাসরি GIPHY লিঙ্ক যা ব্লক হবে না)
animations = {
    "four": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlU9asclnE2bCDe/giphy.webp",
    "six": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlO4y4YfFq9z8uA/giphy.webp",
    "out": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKMGpxx6B8XgKqA/giphy.webp",
    "waiting": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKz9H0D8oG5eXUo/giphy.webp"
}

# ৩. লেআউট ও সেশন স্টেট
if 'runs' not in st.session_state: st.session_state.runs = 0
if 'wickets' not in st.session_state: st.session_state.wickets = 0

col1, col2 = st.columns([1, 2])

# ৪. ইভেন্ট জেনারেট করা
event = random.choice(["0", "1", "2", "4", "6", "W"])
current_anim = animations["waiting"]
status = "🏏 খেলা চলছে..."

if event == "W":
    st.session_state.wickets += 1
    current_anim = animations["out"]
    status = "🔴 OUT! উইকেট পড়ে গেল!"
elif event == "4":
    st.session_state.runs += 4
    current_anim = animations["four"]
    status = "🔥 4 Runs! দারুণ বাউন্ডারি!"
elif event == "6":
    st.session_state.runs += 6
    current_anim = animations["six"]
    status = "🚀 6 Runs! বিশাল ছক্কা!"
else:
    st.session_state.runs += int(event)

# ৫. ডিসপ্লে (এখানেই আসল পরিবর্তন - Cache busting)
with col1:
    st.subheader("📊 Live Score")
    st.metric("Score", f"{st.session_state.runs} / {st.session_state.wickets}")
    st.write(f"**অবস্থা:** {status}")

with col2:
    st.subheader("📺 Match Animation")
    # লিঙ্কটির শেষে একটি র্যান্ডম নাম্বার যোগ করছি যাতে ব্রাউজার নতুন করে লোড করে
    unique_link = f"{current_anim}?t={time.time()}"
    st.image(unique_link, use_container_width=True)

# ৫ সেকেন্ড পর পর অটো-রিফ্রেশ
time.sleep(5)
st.rerun()
