#Import os to handle file and directory operations
import os

#Import webbrowser to open URLs in the default web browser
import webbrowser

#Import for a simple HTTP server that serves files
from http.server import SimpleHTTPRequestHandler

#Import for managing a TCP server to handle client requests
from socketserver import TCPServer

#Import custom utility library for handling images and URLs
import utils

#Local host
class Local_host:
    def __init__(self, img, url):
        self.host = "127.0.0.1"
        self.port = 5500
        self._utils = utils.Img(img, url)
        self.path = self._utils.output_path_index
        self.html_file = self._utils.url
    def start_server(self):
        with TCPServer((self.host, self.port), SimpleHTTPRequestHandler) as httpd:
            self.server = httpd
            print(f"Server is running at http://{self.host}:{self.port}")
            try:
                webbrowser.open(f"http://{self.host}:{self.port}/{self.path}{self.html_file}.html")
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer stopped.")
                httpd.shutdown()
    def end_server_ui(self):
        input("Press Enter to stop the server...\n")
        print("Stopping server...")