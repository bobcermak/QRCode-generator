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
    """
    Handles the local server setup, image generation, and launching
    the HTML page for displaying QR code and URL information.
    """
    def __init__(self, img, url):
        self.host = "127.0.0.1"
        self.port = 5500
        self._utils = utils.Img(img, url)
        self.path = self._utils.output_path_index
        self.html_file = self._utils.url
    """
    Initializes the server with the provided image and URL.
    Parameters:
    img (Image): The generated image (QR code).
    url (str): The base URL for generating and saving related files.
    """
    def start_server(self) -> None:
        with TCPServer((self.host, self.port), SimpleHTTPRequestHandler) as httpd:
            self.server = httpd
            print(f"Server is running at http://{self.host}:{self.port}")
            try:
                webbrowser.open(f"http://{self.host}:{self.port}/{self.path}{self.html_file}.html")
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer stopped.")
                httpd.shutdown()
    """
    Starts the local HTTP server and opens the generated HTML page in the browser.
    This method serves files from the local directory and opens the 
    HTML page automatically.
    """
    def end_server_ui(self) -> None:
        input("Press Enter to stop the server...\n")
        print("Stopping server...")
    """
    Prompts the user to press Enter to stop the server.
    This method ensures the user can stop the server manually from the command line.
    """