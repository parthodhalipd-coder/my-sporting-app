import streamlit as st

# ১. অ্যাপ সেটিংস
st.set_page_config(page_title="Partho's Live Stream", layout="wide")

# ২. টাইটেল
st.markdown("<h1 style='text-align: center; color: #00D1FF;'>🚀 Partho's Global Sports App</h1>", unsafe_allow_html=True)

# ৩. সাইডবার
st.sidebar.title("Developer: Partho")
channel = st.sidebar.selectbox("চ্যানেল বেছে নিন", ["Demo Sports Channel", "T-Sports", "Star Sports"])

# ৪. ভিডিও লিঙ্ক (সরাসরি একটি সচল লিঙ্ক)
video_url = "https://test-streams.mux.dev/x36xhzz/url_2/1920x1080/is_0/index.m3u8"

st.write(f"### 🔴 বর্তমানে দেখছেন: {channel}")

# ৫. স্ট্রিমিং প্লেয়ার (নতুন মেথড)
# আমরা এখানে HTML5 এর সরাসরি প্লেয়ার ব্যবহার করছি যাতে থার্ড পার্টি সাইট না লাগে
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; background: #000; padding: 10px; border-radius: 10px;">
        <video width="100%" height="450" controls autoplay muted>
            <source src="{video_url}" type="application/x-mpegURL">
            Your browser does not support the video tag.
        </video>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    <script>
      var video = document.getElementsByTagName('video')[0];
      var videoSrc = '{video_url}';
      if (Hls.isSupported()) {{
        var hls = new Hls();
        hls.loadSource(videoSrc);
        hls.attachMedia(video);
      }}
      else if (video.canPlayType('application/vnd.apple.mpegurl')) {{
        video.src = videoSrc;
      }}
    </script>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()
st.sidebar.info("💡 টিপস: ভিডিও না আসলে আপনার ব্রাউজারে Native HLS Playback এক্সটেনশনটি একবার চেক করুন।")

st.markdown("---")
st.write("© 2026 Developed by **Partho**")
