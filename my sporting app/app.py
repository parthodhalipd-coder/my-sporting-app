import streamlit as st

# ১. অ্যাপের টাইটেল ও লেআউট
st.set_page_config(page_title="Partho's Stream", page_icon="📺", layout="wide")

# ২. তোমার নাম (Partho) দিয়ে ডিজাইন
st.markdown("<h1 style='text-align: center; color: #1E90FF;'>🚀 Partho's Live App</h1>", unsafe_allow_html=True)

# ৩. সাইডবার ডিজাইন
st.sidebar.title("Owner: Partho")
st.sidebar.write("সাইবার সিকিউরিটি ও স্ট্রিমিং প্রজেক্ট")

# চ্যানেল সিলেকশন
channel = st.sidebar.selectbox("চ্যানেল বেছে নিন", ["Live Sports", "Somoy TV", "Jamuna TV"])

# তোমার নতুন লিঙ্কটি এভাবে বসাও
video_url = "এখানে_তোমার_কপি_করা_লিঙ্কটি_পেস্ট_করো"

st.write(f"### বর্তমানে দেখছেন: {channel}")

# এই প্লেয়ারটি Partho-র অ্যাপে ভালো কাজ করবে
st.markdown(
    f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000; border-radius: 10px;">
        <iframe 
            src="https://p.m3u8play.com/player/index.html?url={video_url}" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            allowfullscreen>
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.write("© 2026 Developed by **Partho**")
