import streamlit as st

# ১. অ্যাপ সেটিংস
st.set_page_config(page_title="Partho's Pro Stream", layout="wide")

# ২. নাম (Partho) দিয়ে ডিজাইন
st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🚀 Partho's Live Sports Portal</h1>", unsafe_allow_html=True)

# ৩. সাইডবার
st.sidebar.title("Developer: Partho")
st.sidebar.info("এখানে ইউটিউবের যেকোনো সচল ভিডিও লিঙ্ক পেস্ট করুন।")

# ৪. ইউজার ইনপুট (যাতে ভিডিও 'Unavailable' হলে তুমি নিজেই লিঙ্ক বদলে দিতে পারো)
# আমি নিচে একটি সচল লিঙ্ক দিয়ে রাখছি যা পরিবর্তনযোগ্য
default_url = "https://www.youtube.com/watch?v=9Auq9mYxFEE" 
video_input = st.sidebar.text_input("YouTube Link এখানে দিন:", value=default_url)

st.write(f"### 🔴 বর্তমানে সম্প্রচারিত হচ্ছে")

# ৫. ভিডিও প্লেয়ার
if video_input:
    try:
        st.video(video_input)
        st.success("ভিডিওটি সফলভাবে লোড হয়েছে!")
    except Exception as e:
        st.error("এই লিঙ্কটি কাজ করছে না। দয়া করে অন্য একটি লিঙ্ক দিন।")

# ৬. অতিরিক্ত কিছু চ্যানেলের সাজেশন (পার্থর জন্য)
st.sidebar.divider()
st.sidebar.write("🔍 **কিভাবে নতুন লিঙ্ক পাবেন?**")
st.sidebar.write("ইউটিউবে গিয়ে 'Live Sports' লিখে সার্চ করুন এবং যেকোনো লাইভ ভিডিওর লিঙ্ক কপি করে এখানে বসান।")

st.markdown("---")
st.write("© 2026 Developed by **Partho**")
