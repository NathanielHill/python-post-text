from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        post_body = self.rfile.read(int(self.headers['content-length']))

        # data = json.loads(post_body)

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(str("Success!").encode())

    return
