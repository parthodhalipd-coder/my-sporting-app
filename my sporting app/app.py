import streamlit as st

# ১. অ্যাপের টাইটেল ও লেআউট
st.set_page_config(page_title="Partho's Global Sports", page_icon="⚽", layout="wide")

# ২. নাম (Partho) দিয়ে ডিজাইন
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏆 Partho's Global Sports App</h1>", unsafe_allow_html=True)

# ৩. স্পোর্টস চ্যানেলের ডিকশনারি (নাম এবং কাজ করে এমন সম্ভাব্য লিঙ্ক)
# দ্রষ্টব্য: লাইভ লিঙ্কে টোকেন থাকলে সেগুলো মাঝে মাঝে পরিবর্তন করতে হয়।
channels = {
    "Sony Sports (Sample)": "https://test-streams.mux.dev/x36xhzz/url_2/1920x1080/is_0/index.m3u8",
    "T-Sports": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/bd.m3u",
    "Star Sports": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/in.m3u"
}

# ৪. সাইডবার ডিজাইন
st.sidebar.title("📺 চ্যানেল গ্যালারি")
st.sidebar.write("ডেভেলপার: **Partho**")
selected_channel = st.sidebar.selectbox("একটি চ্যানেল বেছে নিন", list(channels.keys()))

# ৫. সরাসরি স্ট্রিমলিট ভিডিও প্লেয়ার (এটি অনেক বেশি স্টেবল)
st.write(f"### 🔴 বর্তমানে দেখছেন: {selected_channel}")

# চ্যানেলের লিঙ্ক সেট করা
video_url = channels[selected_channel]

# এরর হ্যান্ডলিং সহ ভিডিও প্লেয়ার
try:
    st.video(video_url)
    st.success("ভিডিওটি সফলভাবে লোড হয়েছে।")
except Exception as e:
    st.error("ভিডিওটি এই মুহূর্তে লোড করা যাচ্ছে না। দয়া করে অন্য চ্যানেল চেষ্টা করুন বা লিঙ্ক আপডেট করুন।")

st.sidebar.divider()
st.sidebar.info("💡 টিপস: ভিডিও না আসলে আপনার ব্রাউজারে HLS Player এক্সটেনশনটি ব্যবহার করুন।")

st.markdown("---")
st.write("© 2026 Developed by **Partho**")
