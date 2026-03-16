import streamlit as st
import time
import random

# ১. অ্যাপ সেটিংস
st.set_page_config(page_title="Partho's Cricket Animation", layout="wide")

# ২. নাম (Partho) দিয়ে ডিজাইন
st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🏏 Partho's Live Cricket Animation</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align: center;'>Developer: <b>Partho</b></p>", unsafe_allow_html=True)

# ৩. অ্যানিমেশনের লাইব্রেরি (সরাসরি সচল লিঙ্ক)
# এগুলো GIF লিঙ্ক, তাই কখনো 'Unavailable' দেখাবে না
animations = {
    "four": "https://media.giphy.com/media/l0HlU9asclnE2bCDe/giphy.gif",
    "six": "https://media.giphy.com/media/l0HlO4y4YfFq9z8uA/giphy.gif",
    "out": "https://media.giphy.com/media/3o7TKMGpxx6B8XgKqA/giphy.gif",
    "running": "https://media.giphy.com/media/3o7TKz9H0D8oG5eXUo/giphy.gif"
}

# ৪. মেইন ডিসপ্লে
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Live Scoreboard")
    score_metric = st.empty()
    status_msg = st.empty()

with col2:
    st.subheader("Match View")
    animation_view = st.empty()

# ৫. অটোমেটিক রান করার ফাংশন
def auto_play():
    runs = 0
    wickets = 0
    while True:
        event = random.choice(["1", "2", "4", "6", "W", "0"])
        
        if event == "W":
            wickets += 1
            status_msg.error("🔴 OUT! উইকেট পড়ে গেল!")
            animation_view.image(animations["out"], use_container_width=True)
        elif event == "4":
            runs += 4
            status_msg.success("🔥 boundary! চার রান!")
            animation_view.image(animations["four"], use_container_width=True)
        elif event == "6":
            runs += 6
            status_msg.success("🚀 ছক্কা! বিশাল সিক্স!")
            animation_view.image(animations["six"], use_container_width=True)
        else:
            runs += int(event)
            status_msg.info("🏏 ডট বল বা সিঙ্গেল রান...")
            animation_view.image(animations["running"], use_container_width=True)
        
        score_metric.metric("Score", f"{runs} / {wickets}")
        time.sleep(5) # ৫ সেকেন্ড পরপর আপডেট হবে

# ৬. কন্ট্রোল বাটন
if st.sidebar.button("অটোমেটিক ম্যাচ শুরু করুন"):
    auto_play()
else:
    st.sidebar.info("ম্যাচ শুরু করতে বাটনে ক্লিক করুন।")
