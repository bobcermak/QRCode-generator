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
        """
        Initializes the server with the provided image and URL.
        Parameters:
        img (Image): The generated image (QR code).
        url (str): The base URL for generating and saving related files.
        """
        self.host = "127.0.0.1"
        self.port = 5500
        self._utils = utils.Img(img, url)
        self.path = self._utils.output_path_index
        self.html_file = self._utils.url
    def start_server(self) -> None:
        """
        Starts the local HTTP server and opens the generated HTML page in the browser.
        This method serves files from the local directory and opens the 
        HTML page automatically.
        """
        with TCPServer((self.host, self.port), SimpleHTTPRequestHandler) as httpd:
            self.server = httpd
            print(f"Server běží na adrese http://{self.host}:{self.port}")
            try:
                webbrowser.open(f"http://{self.host}:{self.port}/{self.path}{self.html_file}.html")
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer byl zastaven.")
                httpd.shutdown()
    def end_server(self) -> None:
        """
        Prompts the user to press Enter to stop the server.
        This method ensures the user can stop the server manually from the command line.
        """
        input("Stiskněte Enter pro zastavení serveru...\n")
        print("Zastavuji server...")