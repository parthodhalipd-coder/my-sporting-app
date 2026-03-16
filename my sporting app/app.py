import streamlit as st

# ১. অ্যাপ সেটিংস
st.set_page_config(page_title="Partho's Live Stream", layout="wide")

# ২. টাইটেল
st.markdown("<h1 style='text-align: center; color: #00D1FF;'>🚀 Partho's Global Sports App</h1>", unsafe_allow_html=True)

# ৩. সাইডবার
st.sidebar.title("Developer: Partho")
channel = st.sidebar.selectbox("চ্যানেল বেছে নিন", ["Sony Sports", "T-Sports", "Star Sports"])

# ৪. ভিডিও লিঙ্ক (একটি সচল ইউনিভার্সাল লিঙ্ক)
# এই প্লেয়ারটি সব ব্রাউজারে চলবে
video_url = "https://test-streams.mux.dev/x36xhzz/url_2/1920x1080/is_0/index.m3u8"
player_url = f"https://p.m3u8play.com/player/index.html?url={video_url}"

st.write(f"### 🔴 বর্তমানে চলছে: {channel}")

# ৫. আইফ্রেম প্লেয়ার (এরর মুক্ত)
st.components.v1.iframe(player_url, height=500, scrolling=False)

st.sidebar.divider()
st.sidebar.info("💡 টিপস: ভিডিও না আসলে পেজটি একবার রিফ্রেশ করুন।")

st.markdown("---")
st.write("© 2026 Developed by **Partho**")
