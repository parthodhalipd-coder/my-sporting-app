import streamlit as st
import requests

# ১. বাংলাদেশের চ্যানেলের সোর্স লিঙ্ক
IPTV_URL = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/bd.m3u"

def get_channels():
    try:
        response = requests.get(IPTV_URL)
        lines = response.text.split('\n')
        channels = []
        for i in range(len(lines)):
            if lines[i].startswith('#EXTINF'):
                name = lines[i].split(',')[-1].strip()
                link = lines[i+1].strip()
                channels.append({"name": name, "url": link})
        return channels
    except:
        return []

st.set_page_config(page_title="রাহিব লাইভ টিভি", layout="wide")
st.title("📺 রাহিবের স্পোর্টস ও লাইভ টিভি অ্যাপ")

# ২. চ্যানেল লোড করা
data = get_channels()

if data:
    names = [c['name'] for c in data]
    selected_channel = st.sidebar.selectbox("একটি চ্যানেল বেছে নিন", names)
    
    # বাছাই করা চ্যানেলের লিঙ্ক বের করা
    url = next(item['url'] for item in data if item['name'] == selected_channel)
    
    st.subheader(f"🔴 বর্তমানে দেখছেন: {selected_channel}")
    
    # সরাসরি ভিডিও প্লেয়ার
    st.video(url)
    
    # যদি ভিডিও প্লে না হয় তবে ইউআরএল দেখাবে
    st.info(f"লিঙ্ক কাজ না করলে এখানে কপি করে অন্য প্লেয়ারে ট্রাই করুন: {url}")
else:
    st.error("দুঃখিত, কোনো চ্যানেল পাওয়া যায়নি!")
