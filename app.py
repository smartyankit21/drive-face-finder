import streamlit as st
import face_recognition
from googleapiclient.discovery import build

st.title("Find My Photos in Google Drive")

# 1. User Uploads their "Selfie"
uploaded_file = st.file_uploader("Upload a clear photo of your face", type=['jpg', 'png'])

if uploaded_file:
    st.image(uploaded_file, caption="Target Face", width=150)
    
    # 2. Connect to Drive (This triggers the Google Login)
    if st.button("Scan my Google Drive"):
        st.write("Connecting to Drive...")
        # Your Drive Logic here (using the code from our previous chat)
        st.success("Scanning complete! Check the 'Found' folder in your Drive.")