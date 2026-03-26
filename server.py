from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            with open('settings.json', 'w') as f:
                f.write(data.decode())
            self.send_response(200)
            self.end_headers()
        elif self.path == '/load':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            try:
                with open('settings.json', 'r') as f:
                    self.wfile.write(f.read().encode())
            except FileNotFoundError:
                self.wfile.write(b'{}')

print("Server starting on http://192.168.1.241:8000...")
HTTPServer(('0.0.0.0', 8000), MyHandler).serve_forever()

