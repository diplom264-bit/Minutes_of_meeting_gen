import streamlit as st
import os
import json
from src.transcription import AudioTranscriber
from src.mom_generator import MoMGenerator

# Page config
st.set_page_config(
    page_title="MoM Generator v2",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Minutes of Meeting Generator v2")
st.markdown("Upload an audio file to automatically generate structured meeting minutes")

# API Key input
api_key = st.text_input("OpenRouter API Key", type="password", value="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")

if not api_key:
    st.warning("Please enter your OpenRouter API key to continue")
    st.stop()

# File upload
uploaded_file = st.file_uploader(
    "Choose an audio file", 
    type=['mp3', 'wav', 'm4a', 'mp4', 'mpeg', 'mpga', 'webm']
)

if uploaded_file is not None:
    # Save uploaded file temporarily
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File uploaded: {uploaded_file.name}")
    
    if st.button("Generate Minutes of Meeting"):
        try:
            with st.spinner("Transcribing audio..."):
                # Initialize transcriber
                transcriber = AudioTranscriber(model_size="base")
                transcript = transcriber.transcribe_audio(temp_path)
            
            st.success("✅ Transcription completed!")
            
            # Show transcript
            with st.expander("View Transcript"):
                st.text_area("Raw Transcript", transcript, height=200)
            
            with st.spinner("Generating Minutes of Meeting..."):
                # Generate MoM
                mom_generator = MoMGenerator(api_key)
                mom_result = mom_generator.generate_mom(transcript)
            
            if "error" in mom_result:
                st.error(f"Error generating MoM: {mom_result['error']}")
                if "raw_response" in mom_result:
                    st.text_area("Raw Response", mom_result["raw_response"])
            else:
                st.success("✅ Minutes of Meeting generated!")
                
                # Display structured MoM
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📋 Meeting Overview")
                    st.write(f"**Title:** {mom_result.get('meeting_title', 'N/A')}")
                    st.write(f"**Date:** {mom_result.get('date', 'N/A')}")
                    
                    st.subheader("👥 Attendees")
                    attendees = mom_result.get('attendees', [])
                    if attendees:
                        for attendee in attendees:
                            st.write(f"• {attendee}")
                    else:
                        st.write("No attendees specified")
                
                with col2:
                    st.subheader("🎯 Key Decisions")
                    decisions = mom_result.get('key_decisions', [])
                    if decisions:
                        for decision in decisions:
                            st.write(f"• {decision}")
                    else:
                        st.write("No key decisions recorded")
                    
                    st.subheader("💬 Discussion Points")
                    discussions = mom_result.get('discussion_points', [])
                    if discussions:
                        for point in discussions:
                            st.write(f"• {point}")
                    else:
                        st.write("No discussion points recorded")
                
                st.subheader("✅ Action Items")
                action_items = mom_result.get('action_items', [])
                if action_items:
                    for item in action_items:
                        st.write(f"**Task:** {item.get('task', 'N/A')}")
                        st.write(f"**Assignee:** {item.get('assignee', 'N/A')}")
                        st.write(f"**Deadline:** {item.get('deadline', 'N/A')}")
                        st.write("---")
                else:
                    st.write("No action items recorded")
                
                # Download JSON
                json_str = json.dumps(mom_result, indent=2)
                st.download_button(
                    label="📥 Download MoM as JSON",
                    data=json_str,
                    file_name=f"mom_{uploaded_file.name.split('.')[0]}.json",
                    mime="application/json"
                )
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)

# Sidebar with info
with st.sidebar:
    st.header("ℹ️ About")
    st.write("This application uses:")
    st.write("• **Whisper** for audio transcription")
    st.write("• **Deepseek** via OpenRouter for MoM generation")
    
    st.header("📋 Supported Formats")
    st.write("• MP3, WAV, M4A")
    st.write("• MP4, MPEG, MPGA")
    st.write("• WebM")
    
    st.header("🚀 Usage")
    st.write("1. Enter your OpenRouter API key")
    st.write("2. Upload an audio file")
    st.write("3. Click 'Generate Minutes of Meeting'")
    st.write("4. Download the structured results")