import streamlit as st
import time
import random
import requests

# ১. অ্যানিমেশন লোড করার ফাংশন
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ২. পেজ সেটিংস
st.set_page_config(page_title="Partho's Live Cricket", layout="wide")

# ৩. এনিমেশন সোর্স (এগুলো কোড ভিত্তিক, তাই ব্লক হবে না)
# এগুলো স্পোর্টস ও ক্রিকেট রিলেটেড এনিমেশন
lottie_cricket = "https://assets5.lottiefiles.com/packages/lf20_m6cu9msc.json"
lottie_celebration = "https://assets2.lottiefiles.com/packages/lf20_kyu7xb1v.json"

st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🏏 Partho's Non-Stop Animation</h1>", unsafe_allow_html=True)

# ৪. সেশন স্টেট
if 'runs' not in st.session_state: st.session_state.runs = 0
if 'wickets' not in st.session_state: st.session_state.wickets = 0

col1, col2 = st.columns([1, 2])

# ৫. ইভেন্ট জেনারেশন
event = random.choice(["0", "1", "2", "4", "6", "W"])
status = "🏏 খেলা চলছে..."
color = "white"

if event == "W":
    st.session_state.wickets += 1
    status = "🔴 OUT! উইকেট পড়ে গেল!"
    color = "red"
elif event == "4" or event == "6":
    st.session_state.runs += int(event)
    status = f"🔥 {event} রান! অসাধারণ শট!"
    color = "green"
else:
    st.session_state.runs += int(event)

# ৬. ডিসপ্লে এরিয়া
with col1:
    st.subheader("📊 Scoreboard")
    st.metric("Total Score", f"{st.session_state.runs} / {st.session_state.wickets}")
    st.markdown(f"<h3 style='color: {color};'>{status}</h3>", unsafe_allow_html=True)

with col2:
    st.subheader("📺 Animation View")
    # এখানে আমরা ভিডিওর বদলে একটি সুন্দর ক্রিকেট গ্রাফিক্স দেখাবো যা সবসময় নড়াচড়া করবে
    st.info("অ্যানিমেশন লোড হচ্ছে... এটি সরাসরি কোড থেকে চলছে।")
    
    # এটি একটি স্ট্যাটিক ইমেজের বদলে নড়াচড়া করা গ্রাফিক্স দেখাবে
    if event == "4" or event == "6":
         st.balloons() # রান হলে স্ক্রিনে বেলুন উড়বে
         st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/l0HlU9asclnE2bCDe/giphy.gif", use_container_width=True)
    elif event == "W":
         st.snow() # আউট হলে তুষারপাত হবে (মজার জন্য)
         st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKMGpxx6B8XgKqA/giphy.gif", use_container_width=True)
    else:
         st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKz9H0D8oG5eXUo/giphy.gif", use_container_width=True)

# অটো-রিফ্রেশ
time.sleep(5)
st.rerun()
