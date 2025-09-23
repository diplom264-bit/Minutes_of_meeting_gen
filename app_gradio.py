import gradio as gr
import json
import os
from transcribe import transcribe_audio
from llm import generate_mom
from docx_utils import create_mom_docx

def process_audio(audio_file, use_saved_transcript):
    """Process audio file and generate Minutes of Meeting"""
    
    if use_saved_transcript:
        transcript = "Thank you very much. This is the arm of Springfield meeting agenda for August 12, 2025. Committee of a whole starting at 1pm Exactly. I'm mayor Patrick Tarrien. All council is present."
        status = "✅ Using saved transcript for testing"
    else:
        if audio_file is None:
            return "❌ Please upload an audio file", "", "", None
        
        try:
            transcript = transcribe_audio(audio_file)
            status = "✅ Transcription completed!"
        except Exception as e:
            return f"❌ Transcription error: {str(e)}", "", "", None
    
    try:
        mom_data = generate_mom(transcript)
        docx_filename = "meeting_minutes.docx"
        create_mom_docx(mom_data, docx_filename)
        json_output = json.dumps(mom_data, indent=2)
        
        return (
            status + " ✅ Minutes of Meeting generated!",
            transcript,
            json_output,
            docx_filename
        )
        
    except Exception as e:
        return f"❌ Error generating MoM: {str(e)}", transcript, "", None

# Create simple Gradio interface
demo = gr.Interface(
    fn=process_audio,
    inputs=[
        gr.Audio(label="Upload Audio File", type="filepath"),
        gr.Checkbox(label="Use saved transcript (testing mode)", value=False)
    ],
    outputs=[
        gr.Textbox(label="Status"),
        gr.Textbox(label="📄 Transcript", lines=8),
        gr.Textbox(label="📋 Minutes of Meeting (JSON)", lines=8),
        gr.File(label="📥 Download DOCX")
    ],
    title="📝 Minutes of Meeting Generator",
    description="Upload an audio file to generate structured meeting minutes"
)

if __name__ == "__main__":
    demo.launch()