import streamlit as st

# 這裡放所有您想在首頁顯示的內容
st.title("歡迎來到吳承翰的 3D GIS 專案！")
st.write("這是一個使用 Streamlit 建立的3D互動式地圖應用程式。")

# 直接將 照片的 URL 傳給 st.image()
image_url = "https://media.tenor.co/cRs4lnEWw48AAAAd/everknight-evernight.gif"
st.image(image_url)
