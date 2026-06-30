import streamlit as st
import google.generativeai as genai
import tempfile
import os

st.title("AI Prompt Generator")

api_key = st.text_input("Masukkan Google API Key Anda", type="password")
uploaded_file = st.file_uploader("Upload gambar/video", type=['jpg', 'png', 'mp4'])

if uploaded_file and api_key:
    if st.button("Generate Prompt"):
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Menggunakan tempfile agar aman di cloud
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_path = tmp_file.name
            
            # Upload ke Gemini API
            file_upload = genai.upload_file(tmp_path)
            response = model.generate_content([file_upload, "Buatkan prompt AI yang detail berdasarkan file ini"])
            
            st.write("Hasil Prompt:")
            st.write(response.text)
            
            # Hapus file sementara setelah selesai
            os.remove(tmp_path)
            
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
