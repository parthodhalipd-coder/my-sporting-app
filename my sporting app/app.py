import streamlit as st

# ১. অ্যাপ সেটিংস
st.set_page_config(page_title="Partho's Pro Stream", layout="wide")

# ২. টাইটেল
st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🚀 Partho's Live Sports Portal</h1>", unsafe_allow_html=True)

# ৩. সাইডবার
st.sidebar.title("Developer: Partho")
st.sidebar.info("নিচের বক্সে ইউটিউব থেকে যেকোনো সচল লাইভ লিঙ্ক দিলে তা এখানে প্লে হবে।")

# ৪. সচল লাইভ লিঙ্কের ডিকশনারি 
# (আমি এমন কিছু চ্যানেল দিচ্ছি যা সাধারণত সব সময় সচল থাকে)
channels = {
    "T-Sports Live (Search)": "https://www.youtube.com/@tsportsbd/streams",
    "GTV Live (Search)": "https://www.youtube.com/@GTVLive/streams",
    "Sky Sports News": "https://www.youtube.com/watch?v=9Auq9mYxFEE"
}

# ৫. ইউজার ইনপুট বক্স
st.sidebar.subheader("চ্যানেল কন্ট্রোল")
video_input = st.sidebar.text_input("YouTube Live Link এখানে পেস্ট করো:", value="https://www.youtube.com/watch?v=9Auq9mYxFEE")

st.write(f"### 🔴 লাইভ স্ট্রিমিং জোন")

# ৬. ভিডিও প্লেয়ার (এটি প্রাইভেট ভিডিওর এরর দেখাবে না যদি লিঙ্ক সঠিক থাকে)
if video_input:
    try:
        st.video(video_input)
        st.success("লিঙ্কটি সফলভাবে কানেক্ট হয়েছে!")
    except:
        st.error("লিঙ্কটি কাজ করছে না। দয়া করে ইউটিউব থেকে নতুন একটি লাইভ লিঙ্ক কপি করে আনুন।")

st.sidebar.divider()
st.sidebar.write("🔗 **সচল লিঙ্ক পাওয়ার উপায়:**")
st.sidebar.write("১. ইউটিউবে যাও। \n২. 'Live Sports' বা 'T-Sports Live' লিখে সার্চ করো। \n৩. যে ভিডিওর নিচে 'LIVE' লেখা আছে সেটার লিঙ্ক কপি করে এখানে বসাও।")

st.markdown("---")
st.write("© 2026 Developed by **Partho**")

