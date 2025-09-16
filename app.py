import streamlit as st
import json
import os
import tempfile
from transcribe import transcribe_audio
from llm import generate_mom

st.title("📝 Minutes of Meeting Generator")

uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav', 'm4a', 'mp4'])

if uploaded_file and st.button("Generate Minutes of Meeting"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name
    
    try:
        with st.spinner("Processing..."):
            transcript = transcribe_audio(temp_path)
            mom_data = generate_mom(transcript)
        
        st.text_area("Transcript", transcript, height=200)
        st.json(mom_data)
        
        os.unlink(temp_path)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
        os.unlink(temp_path)