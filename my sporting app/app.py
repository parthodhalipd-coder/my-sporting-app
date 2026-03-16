import streamlit as st

# ১. অ্যাপ সেটিংস (Partho's Pro Stream)
st.set_page_config(page_title="Partho's Live Pro", layout="wide")

# ২. নাম (Partho) দিয়ে ডিজাইন
st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🚀 Partho's Live Sports Portal</h1>", unsafe_allow_html=True)

# ৩. সাইডবার সেটিংস
st.sidebar.title("Developer: Partho")
st.sidebar.markdown(f"**স্ট্যাটাস:** 🟢 অনলাইন")
st.sidebar.divider()

# ৪. ইউজার ইনপুট বক্স - যেখানে তুমি নতুন লিঙ্ক দেবে
st.sidebar.subheader("চ্যানেল কন্ট্রোল")
video_input = st.sidebar.text_input("YouTube Live Link এখানে পেস্ট করো:", value="https://www.youtube.com/watch?v=liS_9SjYk9I")

st.write(f"### 🔴 লাইভ স্ট্রিমিং জোন")

# ৫. ভিডিও প্লেয়ার (এটি প্রাইভেট বা ডেড ভিডিওর এরর হাইড করবে)
# দ্রষ্টব্য: লাইভ লিঙ্কে টোকেন থাকলে সেগুলো মাঝে মাঝে পরিবর্তন করতে হয়।
if video_input:
    # ভিডিও লোড করার চেষ্টা করা হচ্ছে
    try:
        st.video(video_input)
        st.success("ভিডিওটি সফলভাবে লোড হয়েছে।")
    except Exception as e:
        # যদি ভিডিও 'Unavailable' বা 'Private' হয়, এই মেসেজটি দেখাবে
        st.error("দুঃখিত, এই লিঙ্কটি এখন আর সচল নেই। এটি হয়তো প্রাইভেট করা হয়েছে বা ডিলিট করা হয়েছে।")
        st.warning("সমাধান: দয়া করে ইউটিউবে গিয়ে নতুন একটি লাইভ লিঙ্ক কপি করে সাইডবারের বক্সে বসান।")

# ৬. অতিরিক্ত কিছু চ্যানেলের সাজেশন (পার্থর জন্য)
st.sidebar.divider()
st.sidebar.write("🔍 **কিভাবে সচল লিঙ্ক পাবেন?**")
st.sidebar.write("১. ইউটিউবে যাও। \n২. 'Live Sports' বা 'T-Sports Live' লিখে সার্চ করো। \n৩. যে ভিডিওর নিচে 'LIVE' লেখা আছে সেটার লিঙ্ক কপি করে এখানে বসাও।")

st.markdown("---")
st.write("© 2026 Developed by **Partho**")
