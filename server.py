from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        return  # disable logging to keep it minimal

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()