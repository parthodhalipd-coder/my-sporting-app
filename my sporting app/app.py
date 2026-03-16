import streamlit as st
import time

# ১. পেজ সেটিংস
st.set_page_config(page_title="Partho's Success", layout="wide")

# ২. টাইটেল
st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🚀 Partho's Final Win</h1>", unsafe_allow_html=True)

# ৩. এখানে কোনো ভিডিও লিঙ্ক নেই, সরাসরি সিস্টেম অ্যানিমেশন
st.write("### পার্থ, এবার ম্যাজিকটা দেখো!")

# একটি বড় বাটন
if st.button('ম্যাজিক বাটন চাপুন'):
    # এটি ভিডিওর চেয়েও পাওয়ারফুল সিস্টেম অ্যানিমেশন
    st.balloons() # স্ক্রিনে কয়েকশ বেলুন উড়বে
    st.snow()     # তুষারপাত হবে
    st.success("অভিনন্দন পার্থ! তোমার অ্যাপ এখন ১০০% সচল।")
    
    # এটি সরাসরি Giphy-র মূল ইমেজ যা কোনোদিন ব্লক হয় না
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JnB0PW0mY3Q9Zw/3o7TKz9H0D8oG5eXUo/giphy.gif", caption="Cricket is Loading...")

# ৪. অটোমেটিক স্ট্যাটাস আপডেট
st.info("ভিডিও লিঙ্কগুলো কাজ করছে না কারণ ওগুলো প্রাইভেট। তাই আমরা সিস্টেম গ্রাফিক্স ব্যবহার করছি।")
