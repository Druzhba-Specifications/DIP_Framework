import http.server, socketserver, functools, xml.etree.ElementTree as ET, System
from http.server import HTTPServer, BaseHTTPRequestHandler
global Details
# __    __   ____  ____   ____   ____  ____    ____  __
#|  |__|  | /    ||    \ |    \ |    ||    \  /    ||  |
#|  |  |  ||  o  ||  D  )|  _  | |  | |  _  ||   __||  |
#|  |  |  ||     ||    / |  |  | |  | |  |  ||  |  ||__|
#|  `  '  ||  _  ||    \ |  |  | |  | |  |  ||  |_ | __
# \      / |  |  ||  .  \|  |  | |  | |  |  ||     ||  |
#  \_/\_/  |__|__||__|\_||__|__||____||__|__||___,_||__|
#
# Everything you see below is in EXTREME beta, so it has NO GUARANTEE
# of working on your device. Please take Really Easy Http Hosting with
# a grain of salt. Anyway, please actually test and provide feedback!
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML.encode())
def start_rehh(location):
    global HTML
    root = System.parse.file.xml(location)
    if __name__ == "__main__":
        Details = True
    else:
        Details = False
    #druzhba's high-tech debug tool lol
    Details = True
    try:
        PORT = root.find('port').text
        print(PORT)
        if root.find('loc').text == 'diffloc':
            HTML = root.find('html').text
            print(HTML)
            try:
                with open(HTML, 'r') as f:
                    HTML = f.read()
            except Exception as e:
                System.retEx(e)
                if Details: print(f"Serving files from {HTML} at http://localhost:{PORT}")
                try:
                    HTTPServer(("localhost", int(PORT)), SimpleHandler).serve_forever()
                except KeyboardInterrupt:
                    if Details: print(f"\nClosing server on http://localhost:{PORT}")
        elif root.get('loc') == 'webdoc':
            HTML = root.find('html')
            print(HTML)
            if Details == True:
                print(f"Serving files at http://localhost:{PORT}")
            try:
                HTTPServer(("localhost", int(PORT)), SimpleHandler).serve_forever()
            except KeyboardInterrupt:
                if Details: print(f"\nClosing server on http://localhost:{PORT}")
        else:
            System.retEx("You must define if html file is either locate here (thisloc) or on a web place (webloc). Please look at the example XML file provided to build file for hosting.")
    except Exception as e:
        System.retEx(e)