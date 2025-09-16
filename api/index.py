from http.server import BaseHTTPRequestHandler
import json
import os
import tempfile
import sys
sys.path.append('..')

from transcribe import transcribe_audio
from llm import generate_mom
from docx_utils import create_mom_docx

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/transcribe':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Save uploaded file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
                tmp.write(post_data)
                temp_path = tmp.name
            
            try:
                transcript = transcribe_audio(temp_path)
                mom_data = generate_mom(transcript)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'transcript': transcript,
                    'mom': mom_data
                }).encode())
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            
            finally:
                os.unlink(temp_path)
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Minutes of Meeting Generator API')