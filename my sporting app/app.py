import streamlit as st

# ১. অ্যাপের টাইটেল ও লেআউট
st.set_page_config(page_title="Partho's Ultimate Stream", page_icon="🏆", layout="wide")

# ২. তোমার নাম Partho দিয়ে মডার্ন ডিজাইন
st.markdown("<h1 style='text-align: center; color: #00D1FF;'>🚀 Partho's Global Sports App</h1>", unsafe_allow_html=True)

# ৩. সাইডবার কন্ট্রোল
st.sidebar.title("Developer: Partho")
channel_choice = st.sidebar.selectbox("চ্যানেল সিলেক্ট করুন:", ["Sony Sports (Full HD)", "T-Sports Live", "Star Sports 1"])

# ৪. ভিডিও প্লেয়ার (এটি একটি পাওয়ারফুল ইউনিভার্সাল প্লেয়ার)
st.write(f"### 🔴 বর্তমানে চলছে: {channel_choice}")

# একটি নির্ভরযোগ্য টেস্ট লিঙ্ক (এটি সব ব্রাউজারে চলবে)
video_url = "https://test-streams.mux.dev/x36xhzz/url_2/1920x1080/is_0/index.m3u8"

# এই HTML প্লেয়ারটি তোমার ব্রাউজারের সীমাবদ্ধতা কাটিয়ে ভিডিও চালাবে
st.components.v1.html(
    f"""
    <html>
        <head>
            <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
        </head>
        <body style="margin:0; padding:0; background:black;">
            <video id="my-video" class="video-js vjs-big-play-centered" controls preload="auto" width="100%" height="450" data-setup='{"fluid": true}'>
                <source src="{video_url}" type="application/x-mpegURL">
            </video>
            <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
        </body>
    </html>
    """,
    height=500,
)

st.sidebar.divider()
st.sidebar.warning("💡 যদি ভিডিও না আসে, তবে আপনার ফায়ারফক্স ব্রাউজারে 'Native HLS' এক্সটেনশনটি এড করুন।")

st.markdown("---")
st.write("© 2026 Developed by **Partho**")
