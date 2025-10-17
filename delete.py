from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# In-memory data storage
data = [
    {
        "name": "Saka Idris", 
        "age": 25,
        "track": "AI Developer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    # Handle DELETE requests
    def do_DELETE(self):
        index = int(self.path.strip("/"))
        deleted_item = data.pop(index)  # Remove from list
        self.send_data(200)
        self.wfile.write(json.dumps({"message": f"Deleted item: {deleted_item}"}).encode('utf-8'))

def run():
    print("Application is running on http://localhost:5000")
    HTTPServer(('localhost', 5000), BasicAPI).serve_forever()


run()
