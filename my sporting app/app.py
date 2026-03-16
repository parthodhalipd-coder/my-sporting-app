import streamlit as st

# ১. অ্যাপের টাইটেল ও লেআউট
st.set_page_config(page_title="Partho's Global Sports", page_icon="⚽", layout="wide")

# ২. নাম (Partho) দিয়ে ডিজাইন
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏆 Partho's Global Sports App</h1>", unsafe_allow_html=True)

# ৩. স্পোর্টস চ্যানেলের তালিকা (দেশি ও বিদেশি)
channels = {
    "Sony Sports 1": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/in.m3u", # এক্সাম্পল সোর্স
    "Star Sports": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/in.m3u",
    "T Sports (BD)": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/bd.m3u",
    "GTV (BD)": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/bd.m3u",
    "BeIN Sports": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/qa.m3u",
    "Sky Sports": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/uk.m3u"
}

# ৪. সাইডবার কন্ট্রোল
st.sidebar.title("📺 চ্যানেল গ্যালারি")
st.sidebar.write("ডেভেলপার: **Partho**")
selected_channel = st.sidebar.selectbox("একটি চ্যানেল বেছে নিন", list(channels.keys()))

# ৫. ভিডিও প্লেয়ার (HLS সমর্থিত)
# দ্রষ্টব্য: লাইভ স্ট্রিম অনেক সময় পরিবর্তন হয়, তাই আমরা ডাইনামিক প্লেয়ার ব্যবহার করছি
st.write(f"### 🔴 বর্তমানে দেখছেন: {selected_channel}")

# যেহেতু তুমি ফায়ারফক্স বা ক্রোম ব্যবহার করো, সরাসরি m3u8 লিঙ্কের জন্য এই প্লেয়ারটি ভালো
video_url = "https://test-streams.mux.dev/x36xhzz/url_2/1920x1080/is_0/index.m3u8" # স্যাম্পল সচল লিঙ্ক

st.markdown(
    f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000; border-radius: 12px;">
        <iframe 
            src="https://p.m3u8play.com/player/index.html?url={video_url}" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            allowfullscreen>
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()
st.sidebar.info("💡 টিপস: যদি ভিডিও লোড না হয়, তবে নেটওয়ার্ক ট্যাব চেক করে নতুন লিঙ্ক আপডেট করুন।")

st.markdown("---")
st.write("© 2026 Developed by **Partho** | Sports Enthusiast")
