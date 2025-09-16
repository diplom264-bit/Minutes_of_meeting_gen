import streamlit as st
import json
import os
import tempfile
from transcribe import transcribe_audio
from llm import generate_mom
from docx_utils import create_mom_docx

st.title("📝 Minutes of Meeting Generator")

uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav', 'm4a', 'mp4'])

if uploaded_file and st.button("Generate Minutes of Meeting"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name
    
    try:
        with st.spinner("Processing audio..."):
            transcript = transcribe_audio(temp_path)
            mom_data = generate_mom(transcript)
        
        st.success("✅ Processing completed!")
        
        st.subheader("📄 Transcript")
        st.text_area("Meeting Transcript", transcript, height=200)
        
        st.subheader("📋 Minutes of Meeting")
        with st.expander("View JSON Data", expanded=True):
            st.json(mom_data)
        
        # Generate DOCX for download
        docx_filename = "meeting_minutes.docx"
        create_mom_docx(mom_data, docx_filename)
        
        with open(docx_filename, "rb") as file:
            st.download_button(
                label="📥 Download DOCX",
                data=file.read(),
                file_name=docx_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        
        os.unlink(temp_path)
        if os.path.exists(docx_filename):
            os.unlink(docx_filename)
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        if os.path.exists(temp_path):
            os.unlink(temp_path)