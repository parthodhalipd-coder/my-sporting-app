import streamlit as st
# লাইব্রেরি ইন্সটল করার জন্য টার্মিনালে নিচের কমান্ড দিন:
# pip install streamlit requests
import requests
import re

# ১. অটোমেটিক লাইভ লিঙ্ক খুঁজে বের করার ফাংশন
def get_live_links():
    # এটি একটি পাবলিক আইপিটিভি সোর্স (বাংলাদেশি চ্যানেলসহ)
    url = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/bd.m3u"
    try:
        response = requests.get(url)
        content = response.text
        # Regex ব্যবহার করে চ্যানেলের নাম এবং .m3u8 লিঙ্ক আলাদা করা
        links = re.findall(r'#EXTINF:.*,(.*)\n(http.*m3u8)', content)
        return links
    except Exception as e:
        return []

# ২. অ্যাপের পেজ সেটআপ
st.set_page_config(page_title="লাইভ স্পোর্টস প্রো", layout="wide", page_icon="⚽")

# ৩. সিএসএস (ডিজাইন সুন্দর করার জন্য)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #25d366; color: white; font-weight: bold; }
    .ad-box { background-color: #ffffff; padding: 20px; border-radius: 10px; text-align: center; border: 2px dashed #ff4b4b; margin-bottom: 20px; }
    .premium-card { background-color: #0e1117; color: white; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ৪. অ্যাপের শিরোনাম
st.title("⚽ লাইভ স্পোর্টস ও বিনোদন")
st.write("স্বাগতম! এখান থেকে আপনি সরাসরি খেলা ও টিভি চ্যানেল দেখতে পারবেন।")

# ৫. সাইডবার (চ্যানেল লিস্ট এবং পেমেন্ট বাটন)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/53/53283.png", width=100)
    st.header("💎 প্রিমিয়াম মেম্বারশিপ")
    st.markdown('<div class="premium-card">বিজ্ঞাপন ছাড়া খেলা দেখতে এবং আমাদের সাপোর্ট করতে নিচের বাটনে ক্লিক করুন।</div>', unsafe_allow_html=True)
    
    # আয়ের উপায় ১: বিকাশ পেমেন্ট বাটন
    if st.button("বিকাশ দিয়ে সাপোর্ট করুন"):
        st.success("ধন্যবাদ! আমাদের বিকাশ নাম্বার: 01XXX-XXXXXX (Send Money)")
    
    st.divider()
    
    st.header("📺 চ্যানেল বাছাই করুন")
    with st.spinner('লিঙ্ক লোড হচ্ছে...'):
        channels = get_live_links()
    
    if channels:
        channel_names = [c[0].strip() for c in channels]
        choice = st.selectbox("আপনার প্রিয় চ্যানেলটি সিলেক্ট করুন:", channel_names)
        # সিলেক্ট করা চ্যানেলের লিঙ্কটি বের করা
        selected_link = next(link for name, link in channels if name.strip() == choice)
    else:
        st.error("দুঃখিত! এই মুহূর্তে কোনো লাইভ লিঙ্ক পাওয়া যায়নি।")

# ৬. মূল কন্টেন্ট এরিয়া (ভিডিও প্লেয়ার এবং বিজ্ঞাপন)
col1, col2 = st.columns([3, 1])

with col1:
    if channels:
        st.subheader(f"🔴 এখন দেখছেন: {choice}")
        # ভিডিও প্লেয়ার (HLS/M3U8 সাপোর্ট করে)
        st.video(selected_link)
        st.info("টিপস: ভিডিও প্লে না হলে অন্য একটি চ্যানেল ট্রাই করুন।")
    else:
        st.warning("বাম পাশের মেনু থেকে একটি চ্যানেল সিলেক্ট করুন শুরু করার জন্য।")

with col2:
    # আয়ের উপায় ২: বিজ্ঞাপনের জায়গা
    st.subheader("📢 স্পন্সর")
    st.markdown('''
        <div class="ad-box">
            <p style="color: #ff4b4b; font-weight: bold;">আপনার বিজ্ঞাপন এখানে!</p>
            <p style="font-size: 12px;">প্রতিদিন ৫০০০+ মানুষ এই অ্যাপ ব্যবহার করে।</p>
            <a href="mailto:contact@yourdomain.com">যোগাযোগ করুন</a>
        </div>
    ''', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("🗓️ আজকের খেলার সূচি")
    st.caption("🏏 বাংলাদেশ vs শ্রীলঙ্কা - রাত ৮:০০")
    st.caption("⚽ রিয়াল মাদ্রিদ vs বার্সেলোনা - রাত ১:৩০")

# ৭. ফুটার
st.divider()
st.caption("© ২০২৬ লাইভ স্পোর্টস এআই | সাইবার সিকিউরিটি ল্যাব প্রজেক্ট")