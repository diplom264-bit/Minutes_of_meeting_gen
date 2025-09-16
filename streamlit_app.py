import streamlit as st
import requests
import json
import tempfile

st.set_page_config(page_title="Minutes of Meeting Generator", page_icon="📝")

st.title("📝 Minutes of Meeting Generator")
st.write("Upload an audio file to generate structured meeting minutes")

uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav', 'm4a', 'mp4'])

if uploaded_file is not None:
    if st.button("Generate Minutes of Meeting"):
        try:
            with st.spinner("Processing audio..."):
                # Send file to API
                files = {'file': uploaded_file.getvalue()}
                response = requests.post('/api/index', data=uploaded_file.getvalue())
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.success("✅ Processing completed!")
                    
                    # Display transcript
                    st.subheader("📄 Transcript")
                    st.text_area("Meeting Transcript", result['transcript'], height=200)
                    
                    # Display JSON MoM
                    st.subheader("📋 Minutes of Meeting (JSON)")
                    with st.expander("View JSON Data", expanded=True):
                        st.json(result['mom'])
                        
                else:
                    st.error(f"❌ Error: {response.json().get('error', 'Unknown error')}")
                    
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

st.sidebar.header("📋 Instructions")
st.sidebar.write("""
1. Upload an audio file (MP3, WAV, M4A, MP4)
2. Click 'Generate Minutes of Meeting'
3. View transcript and structured MoM
4. API processes the file using AI
""")