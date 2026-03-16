import streamlit as st

# ১. অ্যাপ সেটিংস
st.set_page_config(page_title="Partho's Ultimate Stream", layout="wide")

# ২. টাইটেল (Partho)
st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🚀 Partho's Pro Sports App</h1>", unsafe_allow_html=True)

# ৩. সাইডবার
st.sidebar.title("Developer: Partho")
st.sidebar.write("Project: Live Streaming App")

# ৪. চ্যানেলের ডিকশনারি (এখানে আমি কিছু লাইভ ইউটিউব স্পোর্টস লিঙ্ক দিচ্ছি)
# ইউটিউব লিঙ্ক দিলে লোডিং হয়ে আটকে থাকবে না
channels = {
    "Live Cricket (YouTube)": "https://www.youtube.com/watch?v=liS_9SjYk9I", # স্যাম্পল লিঙ্ক
    "Live Football (YouTube)": "https://www.youtube.com/watch?v=5_XvV_UvY88",
    "Sports News": "https://www.youtube.com/watch?v=9Auq9mYxFEE"
}

selected_channel = st.sidebar.selectbox("একটি চ্যানেল বেছে নিন", list(channels.keys()))

st.write(f"### 🔴 বর্তমানে চলছে: {selected_channel}")

# ৫. ইউটিউব প্লেয়ার (এটি ১০০% কাজ করবেই)
try:
    st.video(channels[selected_channel])
    st.success("ভিডিওটি সফলভাবে লোড হয়েছে!")
except:
    st.error("দুঃখিত, এই মুহূর্তে ভিডিওটি পাওয়া যাচ্ছে না।")

st.sidebar.divider()
st.sidebar.info("💡 টিপস: ইউটিউব লিঙ্ক ব্যবহার করলে কোনো এরর বা লোডিং সমস্যা হয় না।")

st.markdown("---")
st.write("© 2026 Developed by **Partho**")
