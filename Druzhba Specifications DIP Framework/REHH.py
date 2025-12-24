import http.server, socketserver, functools, xml.etree.ElementTree as ET, System
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
def start_rehh(location):
    root = System.parse.file.xml(location)
    if __name__ == "__main__":
        Details = True
    else:
        Details = False
    #druzhba's high-tech debug tool lol

    try:
        global httpd
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
            with socketserver.TCPServer(("", PORT), HTML) as httpd:
                if Details: print(f"Serving files from {HTML} at http://localhost:{PORT}")
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    if Details: print(f"\nClosing server on http://localhost:{PORT}")
        elif root.get('loc') == 'thisloc':
            HTML = root.get('html')
            print(HTML)
            with socketserver.TCPServer(("", PORT), HTML) as httpd:
                if Details: print(f"Serving files at http://localhost:{PORT}")
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    if Details: print(f"\nClosing server on http://localhost:{PORT}")
        else:
            System.retEx("You must define if html file is either locate here (thisloc) or in another place (diffloc). Please look at the example XML file provided to build file for hosting.")
    except Exception as e:
        System.retEx(e)
def Stop_rehh():
    httpd.shutdown()
    httpd.server_close()