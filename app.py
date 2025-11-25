#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Python Web App</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }}
                .container {{
                    background: rgba(255, 255, 255, 0.1);
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                }}
                h1 {{ color: #fff; text-align: center; }}
                p {{ font-size: 18px; line-height: 1.6; }}
                .info {{ 
                    background: rgba(255, 255, 255, 0.2);
                    padding: 15px;
                    border-radius: 5px;
                    margin: 10px 0;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Python Web App is Running!</h1>
                <div class="info">
                    <p><strong>Server Hostname:</strong> {hostname}</p>
                    <p><strong>Server IP:</strong> {ip}</p>
                    <p><strong>Status:</strong> ✅ Active and Running</p>
                </div>
                <p style="text-align: center; margin-top: 30px;">
                    Deployed successfully via Ansible!
                </p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        print(f"Request from {self.client_address[0]}: {format % args}")

def run(port=8001):
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Server running on port {port}...")
    print(f"Access it at http://0.0.0.0:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
