import http.server
import socketserver
import os
import webbrowser

DEFAULT_PORT = 8009
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    # Port bekérése indításkor
    port_input = input(f"Add meg a portot [{DEFAULT_PORT}]: ").strip()
    if port_input.isdigit():
        PORT = int(port_input)
    else:
        PORT = DEFAULT_PORT

    url = f"http://localhost:{PORT}/"
    print(f"Serving at {url} from {DIRECTORY}")

    # Böngésző megnyitása
    webbrowser.open(url)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
