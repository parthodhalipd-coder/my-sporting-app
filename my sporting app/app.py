import streamlit as st
import time

# ১. অ্যাপ কনফিগারেশন
st.set_page_config(page_title="Partho's Live Animation", layout="wide")

# ২. এনিমেশন ভিডিওর লিস্ট (এগুলো তুমি গিটহাবে আপলোড করে নাম বদলে নিতে পারো)
# আমি এখানে কিছু স্যাম্পল GIF লিঙ্ক দিচ্ছি যা ভিডিওর মতো কাজ করবে
animation_files = {
    "waiting": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKz9H0D8oG5eXUo/giphy.gif",
    "four": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlU9asclnE2bCDe/giphy.gif",
    "six": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlO4y4YfFq9z8uA/giphy.gif",
    "out": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKMGpxx6B8XgKqA/giphy.gif"
}

st.title("🏏 Partho's Auto-Animation Live Match")

# ৩. ডিসপ্লে এরিয়া
col1, col2 = st.columns([1, 2])
with col1:
    score_placeholder = st.empty()
    status_placeholder = st.empty()

with col2:
    video_placeholder = st.empty()

# ৪. অটোমেটিক ফাংশন (সিমুলেশন)
def run_live_match():
    # এখানে আমরা রিয়েল টাইম স্কোর আপডেট করব
    test_events = ["waiting", "four", "waiting", "six", "out"]
    
    for event in test_events:
        if event == "four":
            status_placeholder.success("🔥 boundary! চার রান!")
            video_placeholder.image(animation_files["four"], use_container_width=True)
        elif event == "six":
            status_placeholder.success("🚀 SIXER! বিশাল ছক্কা!")
            video_placeholder.image(animation_files["six"], use_container_width=True)
        elif event == "out":
            status_placeholder.error("🔴 OUT! উইকেট পড়ে গেল!")
            video_placeholder.image(animation_files["out"], use_container_width=True)
        else:
            status_placeholder.info("🏏 খেলা চলছে...")
            video_placeholder.image(animation_files["waiting"], use_container_width=True)
        
        time.sleep(5) # প্রতি ৫ সেকেন্ডে চেক করবে

if st.button("লাইভ এনিমেশন শুরু করুন"):
    run_live_match()
