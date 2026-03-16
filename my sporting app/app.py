import streamlit as st
import time

# ১. টাইটেল
st.title("Partho's Success Match 🏏")

# ২. স্কোর বোর্ড
if 'runs' not in st.session_state:
    st.session_state.runs = 0

st.header(f"স্কোর: {st.session_state.runs} রান")

# ৩. বাটন (ভিডিওর বদলে আমরা সরাসরি এনিমেশন লোড করব)
if st.button('ছক্কা মারুন! 🚀'):
    st.session_state.runs += 6
    st.balloons() # স্ক্রিনে কয়েকশ বেলুন উড়বে
    st.snow()     # তুষারপাত হবে
    st.success("বিশাল ছক্কা! পার্থ, এবার তোমার অ্যাপে ম্যাজিক কাজ করছে!")

st.info("পার্থ, এই বেলুনগুলোই এখন আমাদের এনিমেশন। এটি কোনো লিঙ্কের ওপর নির্ভর করে না, তাই এটি সবসময় কাজ করবে।")
