import gradio as gr
import json
import os
import tempfile
from transcribe import transcribe_audio
from llm import generate_mom
from docx_utils import create_mom_docx

def process_audio(audio_file, use_saved_transcript=False):
    """Process audio file and generate Minutes of Meeting"""
    
    if use_saved_transcript:
        # Use saved transcript for testing
        transcript = """Thank you very much. This is the arm of Springfield meeting agenda for August 12, 2025. Committee of a whole starting at 1pm Exactly. I'm mayor Patrick Tarrien. All council is present. And that'll be to my right in descending order. Deputy Mayor Glenn Fuel, Councillors Kaczynski, Miller and Warren. This is in order. So we'll go to the approval of the agenda there. Can I get a mover and a seconder for that, please? Kaczynski and Fuel, any additions or approval of the agenda. Any concerns? I see none. And if I can get a show of hands approval of the agenda. Sorry, Christy, you want me to do something? I just was going to mention that I'd like to remove development agreement discussion from closed meeting. Okay, we all got an email with regards to that. Any concerns from council? I see none. Can I just get a show of hands for approval of the agenda, please? As unanimous and is carried. Approval of the minutes. A mover and a seconder for that, please. Tarian and Warren, any additions or concerns with regards to approval of the minutes for July 8th of 2025? Then I see none. With a show of hands. Those in support. Unanimous and so carried. That's a cell phone. That's a pizza right there. We'll go to the board of revisions 6.1. I'll hand that off to our CEO. So the board of revision is booked for Thursday, November 13th this year to hear appeals for 2026 assessments. We do have. The chair of the board has agreed to serve again pending council's resolution. We also need two council members to sit on the board. Or we need direction from council to find alternate members. If that's what you'd like to see this year instead of council sitting on the board. So just need some time to gather names and make contacts if that's the direction this year. What is your direction there, Council? Just another two members on there. It'll save us some money there. Not considerable amount of money. But is there two volunteers that would want to put their hands up for the Board of Revisions? Councillor Kaczynski and Councillor Warren. But we also have the option of having somebody else there. So if, as long as you're aware of that, then we can. We'll put your names forward. So that'd be councillors Kaczynski and Warren. Thank you for stepping up there, guys. Then we'll go to the approach bylaw. 6.2 it afternoon council. So we've got the approach bylaw back in front of you. After the last meeting. There were some. Some revisions we needed to do regarding mostly offenses and penalties. So Starting on page nine, we revamped the 9.1 or part nine, the offenses. So we've got an outline in there and the types of offenses. If you look into item number 10, we're a notice of contravention and orders to remedy. So what we did is we took out the actual penalties and fines. The. The cost of them. Those are actually covered under the enforcement bylaw. And with that we did look at the minimums and maximums. I think that was a concern from council before being that they might have been a little too stringent. So I believe the minimums are 250 to a maximum of 1000. But then there's other areas that depending on the severity of the offense, if that was the case, there's other areas of which we could take different. Different lines of remedy or penalty. So such as highway traffic act as this is part of the. Within the municipal right of. So we made those changes. Other than that, I don't believe there was any additional changes or comments from the last meeting. So if you have another look at it, any further questions or comments on it, let us know. I. I looked at it there and it addressed the. The. Our concerns there. I forget which counselor was. There was a few counselors that were addressing the. The fact the. The cost and so on like that, but that's just for me. Any other comments from council at all? No, I just stayed up and good with it. Thanks. Well, it's been a little while coming, so it'd be nice to put a check mark on this next little while. So. Okay, I see there's no questions and thank you very much, Blaine for that. Then we'll go to 6.3 and that's the Springfield Police Service update. I'll refer that to our CAO. So as council's aware, as of August 5th of this year, the Springfield Police Service office has been closed. This is due to the fact that both of our remaining employees, Scott and Jesse, have since moved on to the rcmp. And of course we wish them well. But that does leave us with no staff within the department right now. So we did put a notice out onto our social media and website just advising that the office is closed to the public at this time. We provided the relevant non emergency and emergency numbers that people can call. Obviously the RCMP are still active and considered the primary police service in the municipality. So in the event of an emergency, you still call 911 for police, fire or ambulance. So we've provided that update to the Public at this time. We've removed all job postings from the website and any sites that we had posted at the time. You know, the department was going to consist of a chief and two constables. So at this time we're not actively pursuing those postings right now. Just so council has an opportunity to kind of discuss if there's any changes that want to be made. The best time is to do it before there's people in those roles again. So that's the update. I know we've been getting some comments on social media that people wanted more information. So that is the update that we have at this time."""
        status = "✅ Using saved transcript for testing"
    else:
        if audio_file is None:
            return "❌ Please upload an audio file", "", "", None
        
        try:
            # Transcribe audio
            status = "🎵 Transcribing audio..."
            transcript = transcribe_audio(audio_file)
            status = "✅ Transcription completed!"
        except Exception as e:
            return f"❌ Transcription error: {str(e)}", "", "", None
    
    try:
        # Generate MoM
        mom_data = generate_mom(transcript)
        
        # Create DOCX
        docx_filename = "meeting_minutes.docx"
        create_mom_docx(mom_data, docx_filename)
        
        # Format JSON for display
        json_output = json.dumps(mom_data, indent=2)
        
        return (
            status + " ✅ Minutes of Meeting generated!",
            transcript,
            json_output,
            docx_filename
        )
        
    except Exception as e:
        return f"❌ Error generating MoM: {str(e)}", transcript, "", None

# Create Gradio interface
with gr.Blocks(title="📝 Minutes of Meeting Generator") as demo:
    gr.Markdown("# 📝 Minutes of Meeting Generator")
    gr.Markdown("Upload an audio file to generate structured meeting minutes")
    
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                label="Upload Audio File",
                type="filepath",
                sources=["upload"]
            )
            use_saved = gr.Checkbox(
                label="Use saved transcript (for testing without API credits)",
                value=False
            )
            process_btn = gr.Button("Generate Minutes of Meeting", variant="primary")
        
        with gr.Column():
            status_output = gr.Textbox(label="Status", interactive=False)
    
    with gr.Row():
        with gr.Column():
            transcript_output = gr.Textbox(
                label="📄 Transcript",
                lines=10,
                interactive=False
            )
        
        with gr.Column():
            json_output = gr.Textbox(
                label="📋 Minutes of Meeting (JSON)",
                lines=10,
                interactive=False
            )
    
    docx_output = gr.File(label="📥 Download DOCX")
    
    process_btn.click(
        fn=process_audio,
        inputs=[audio_input, use_saved],
        outputs=[status_output, transcript_output, json_output, docx_output]
    )

if __name__ == "__main__":
    demo.launch()