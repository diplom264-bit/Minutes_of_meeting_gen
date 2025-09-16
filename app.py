import streamlit as st
import json
import os
import tempfile
from transcribe import transcribe_audio
from llm import generate_mom
from docx_utils import create_mom_docx

st.set_page_config(page_title="Minutes of Meeting Generator", page_icon="📝")

st.title("📝 Minutes of Meeting Generator")
st.write("Upload an audio file to generate structured meeting minutes")

# File upload
uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav', 'm4a', 'mp4'])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name
    
    if st.button("Generate Minutes of Meeting"):
        try:
            with st.spinner("Transcribing audio..."):
                transcript = transcribe_audio(temp_path)
            
            st.success("✅ Transcription completed!")
            
            # Display transcript
            st.subheader("📄 Transcript")
            st.text_area("Meeting Transcript", transcript, height=200)
            
            with st.spinner("Generating Minutes of Meeting..."):
                mom_data = generate_mom(transcript)
            
            st.success("✅ Minutes of Meeting generated!")
            
            # Display JSON MoM
            st.subheader("📋 Minutes of Meeting (JSON)")
            with st.expander("View JSON Data", expanded=True):
                st.json(mom_data)
            
            # Generate DOCX
            docx_filename = "meeting_minutes.docx"
            create_mom_docx(mom_data, docx_filename)
            
            # Download button
            with open(docx_filename, "rb") as file:
                st.download_button(
                    label="📥 Download DOCX",
                    data=file.read(),
                    file_name=docx_filename,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            
            # Clean up
            os.unlink(temp_path)
            if os.path.exists(docx_filename):
                os.unlink(docx_filename)
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            os.unlink(temp_path)

# Sidebar with instructions
st.sidebar.header("📋 Setup Instructions")
st.sidebar.write("""
1. Create a `.env` file with your API keys:
   ```
   ASSEMBLYAI_API_KEY=your_key_here
   OPENROUTER_API_KEY=your_key_here
   ```
2. Upload an audio file
3. Click 'Generate Minutes of Meeting'
4. Download the DOCX file
""")