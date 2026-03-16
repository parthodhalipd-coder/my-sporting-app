import streamlit as st
import time

# ১. টাইটেল
st.title("Partho's Live Project 🏏")

# ২. স্কোরবোর্ড
if 'score' not in st.session_state:
    st.session_state.score = 0

col1, col2 = st.columns(2)

with col1:
    st.header("Scoreboard")
    st.metric("Total Runs", st.session_state.score)
    if st.button('Add Run'):
        st.session_state.score += 1

with col2:
    st.header("Match Status")
    # এটি ভিডিও নয়, এটি একটি পাইথন এনিমেশন যা তোমার ব্রাউজারে তৈরি হবে
    with st.spinner('বোলার বল করছে...'):
        time.sleep(1)
    
    # রান হলে ম্যাজিক দেখাবে
    if st.session_state.score > 0:
        st.balloons()
        st.success("অসাধারণ শট! বেলুন উড়ছে দেখো!")

# ৩. একটি ছোট এনিমেশন বক্স
st.info("পার্থ, এই বেলুনগুলোই এখন আমাদের এনিমেশন। এটি সরাসরি পাইথন দিয়ে চলছে।")
