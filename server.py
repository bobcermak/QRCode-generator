# Import libraries for working with the file system and web browsers
import os

# Import library to open a webpage in the browser
import webbrowser

# Import for a simple HTTP server
from http.server import SimpleHTTPRequestHandler

# Import for managing a TCP server
from socketserver import TCPServer

# Import custom utility library
import utils

class Local_host:
    def __init__(self, img, url):
        self.host = "127.0.0.1"
        self.port = 5500
        self._utils= utils.Img(img, url)
        self.path = self._utils.output_path_index
        self.html_file = self._utils.url
    def start_server(self):
        with TCPServer((self.host, self.port), SimpleHTTPRequestHandler) as httpd:
            print(f"Server is running at http://{self.host}:{self.port}")
            webbrowser.open(f"http://{self.host}:{self.port}/{self.path}{self.html_file}.html")
            httpd.serve_forever()