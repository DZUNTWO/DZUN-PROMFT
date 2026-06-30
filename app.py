import streamlit as st
import google.generativeai as genai
import os

st.title("AI Prompt Generator")

api_key = st.text_input("Masukkan Google API Key Anda", type="password")
uploaded_file = st.file_uploader("Upload gambar/video", type=['jpg', 'png', 'mp4'])

if uploaded_file and api_key:
    if st.button("Generate Prompt"):
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Simpan sementara untuk diunggah ke Gemini
        with open("temp_file", "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        file_upload = genai.upload_file("temp_file")
        response = model.generate_content([file_upload, "Buatkan prompt AI yang detail berdasarkan file ini"])
        
        st.write("Hasil Prompt:")
        st.write(response.text)
