import streamlit as st
import time

# ১. পেজ সেটআপ
st.set_page_config(page_title="Partho's Code Animation", layout="wide")

st.title("🏏 Partho's Interactive Cricket Dashboard")

# ২. সেশন স্টেট (স্কোর সেভ করার জন্য)
if 'score' not in st.session_state:
    st.session_state.score = 0

# ৩. লেআউট তৈরি
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📊 Live Stats")
    st.metric("Total Score", f"{st.session_state.score}")
    if st.button('রান নিন (Add Run)'):
        st.session_state.score += 1

with col2:
    st.header("🎨 Live Animation")
    # এখানে আমরা কোনো ভিডিও লিঙ্ক দিচ্ছি না, সরাসরি কোড দিয়ে প্রগ্রেস বার এনিমেশন করছি
    progress_bar = st.progress(0)
    status_text = st.empty()

    # এই লুপটি এনিমেশনের মতো কাজ করবে
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    
    st.success("এনিমেশন সাকসেসফুল!")
    # একটি ছোট মজার সারপ্রাইজ
    st.balloons()
