from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SimpleHTTPServer

PORT = 10161

class AjaxHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','AJAX.html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        self.wfile.write("Daniils Aleksandrovs-Moisejs, 161REB161")
        return

try:
    server = HTTPServer(('213.175.92.37',PORT), AjaxHandler)
    print 'Started AJAX handler on port', PORT
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
