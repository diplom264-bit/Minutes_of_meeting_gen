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

# Add option to use saved transcript for testing
use_saved = st.checkbox("Use saved transcript (for testing without API credits)")

if use_saved:
    # Use the Springfield meeting transcript
    saved_transcript = """Thank you very much. This is the arm of Springfield meeting agenda for August 12, 2025. Committee of a whole starting at 1pm Exactly. I'm mayor Patrick Tarrien. All council is present. And that'll be to my right in descending order. Deputy Mayor Glenn Fuel, Councillors Kaczynski, Miller and Warren. This is in order. So we'll go to the approval of the agenda there. Can I get a mover and a seconder for that, please? Kaczynski and Fuel, any additions or approval of the agenda. Any concerns? I see none. And if I can get a show of hands approval of the agenda. Sorry, Christy, you want me to do something? I just was going to mention that I'd like to remove development agreement discussion from closed meeting. Okay, we all got an email with regards to that. Any concerns from council? I see none. Can I just get a show of hands for approval of the agenda, please? As unanimous and is carried. Approval of the minutes. A mover and a seconder for that, please. Tarian and Warren, any additions or concerns with regards to approval of the minutes for July 8th of 2025? Then I see none. With a show of hands. Those in support. Unanimous and so carried. That's a cell phone. That's a pizza right there. We'll go to the board of revisions 6.1. I'll hand that off to our CEO. So the board of revision is booked for Thursday, November 13th this year to hear appeals for 2026 assessments. We do have. The chair of the board has agreed to serve again pending council's resolution. We also need two council members to sit on the board. Or we need direction from council to find alternate members. If that's what you'd like to see this year instead of council sitting on the board. So just need some time to gather names and make contacts if that's the direction this year. What is your direction there, Council? Just another two members on there. It'll save us some money there. Not considerable amount of money. But is there two volunteers that would want to put their hands up for the Board of Revisions? Councillor Kaczynski and Councillor Warren. But we also have the option of having somebody else there. So if, as long as you're aware of that, then we can. We'll put your names forward. So that'd be councillors Kaczynski and Warren. Thank you for stepping up there, guys. Then we'll go to the approach bylaw. 6.2 it afternoon council. So we've got the approach bylaw back in front of you. After the last meeting. There were some. Some revisions we needed to do regarding mostly offenses and penalties. So Starting on page nine, we revamped the 9.1 or part nine, the offenses. So we've got an outline in there and the types of offenses. If you look into item number 10, we're a notice of contravention and orders to remedy. So what we did is we took out the actual penalties and fines. The. The cost of them. Those are actually covered under the enforcement bylaw. And with that we did look at the minimums and maximums. I think that was a concern from council before being that they might have been a little too stringent. So I believe the minimums are 250 to a maximum of 1000. But then there's other areas that depending on the severity of the offense, if that was the case, there's other areas of which we could take different. Different lines of remedy or penalty. So such as highway traffic act as this is part of the. Within the municipal right of. So we made those changes. Other than that, I don't believe there was any additional changes or comments from the last meeting. So if you have another look at it, any further questions or comments on it, let us know. I. I looked at it there and it addressed the. The. Our concerns there. I forget which counselor was. There was a few counselors that were addressing the. The fact the. The cost and so on like that, but that's just for me. Any other comments from council at all? No, I just stayed up and good with it. Thanks. Well, it's been a little while coming, so it'd be nice to put a check mark on this next little while. So. Okay, I see there's no questions and thank you very much, Blaine for that. Then we'll go to 6.3 and that's the Springfield Police Service update. I'll refer that to our CAO. So as council's aware, as of August 5th of this year, the Springfield Police Service office has been closed. This is due to the fact that both of our remaining employees, Scott and Jesse, have since moved on to the rcmp. And of course we wish them well. But that does leave us with no staff within the department right now. So we did put a notice out onto our social media and website just advising that the office is closed to the public at this time. We provided the relevant non emergency and emergency numbers that people can call. Obviously the RCMP are still active and considered the primary police service in the municipality. So in the event of an emergency, you still call 911 for police, fire or ambulance. So we've provided that update to the Public at this time. We've removed all job postings from the website and any sites that we had posted at the time. You know, the department was going to consist of a chief and two constables. So at this time we're not actively pursuing those postings right now. Just so council has an opportunity to kind of discuss if there's any changes that want to be made. The best time is to do it before there's people in those roles again. So that's the update. I know we've been getting some comments on social media that people wanted more information. So that is the update that we have at this time."""
    
    if st.button("Generate Minutes of Meeting (Using Saved Transcript)"):
        try:
            st.success("✅ Using saved transcript!")
            
            st.subheader("📄 Transcript")
            st.text_area("Meeting Transcript", saved_transcript, height=200)
            
            with st.spinner("Generating Minutes of Meeting..."):
                mom_data = generate_mom(saved_transcript)
            
            st.success("✅ Minutes of Meeting generated!")
            
            st.subheader("📋 Minutes of Meeting (JSON)")
            with st.expander("View JSON Data", expanded=True):
                st.json(mom_data)
            
            docx_filename = "meeting_minutes.docx"
            create_mom_docx(mom_data, docx_filename)
            
            with open(docx_filename, "rb") as file:
                st.download_button(
                    label="📥 Download DOCX",
                    data=file.read(),
                    file_name=docx_filename,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            
            if os.path.exists(docx_filename):
                os.unlink(docx_filename)
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
else:
    uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav', 'm4a', 'mp4'])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            temp_path = tmp_file.name
        
        if st.button("Generate Minutes of Meeting"):
            try:
                with st.spinner("Transcribing audio..."):
                    transcript = transcribe_audio(temp_path)
                
                st.success("✅ Transcription completed!")
                
                st.subheader("📄 Transcript")
                st.text_area("Meeting Transcript", transcript, height=200)
                
                with st.spinner("Generating Minutes of Meeting..."):
                    mom_data = generate_mom(transcript)
                
                st.success("✅ Minutes of Meeting generated!")
                
                st.subheader("📋 Minutes of Meeting (JSON)")
                with st.expander("View JSON Data", expanded=True):
                    st.json(mom_data)
                
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
                os.unlink(temp_path)

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