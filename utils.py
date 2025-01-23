#Import the os module to manipulate files
import os

#Import the qrcode module for generating QR codes
import qrcode

#Import the requests library to make HTTP requests (e.g., for validating or fetching URLs)
import requests

#Import urlparse from urllib.parse for parsing URLs into components
from urllib.parse import urlparse

#Classes
#Url
class Url:
    def __init__(self, url):
        self.url = url
    def check_correct_url(self) -> bool:
        try:
            self.response = requests.get(self.url)
            return self.response.status_code == 200
        except Exception as e:
            print(f"Error while checking URL: {e}")
            return False
    def cleaned_url(self) -> str:
        parsed_url = urlparse(self.url)
        domain = parsed_url.netloc
        path = parsed_url.path[:5]
        query = parsed_url.query[:5]
        cleaned_url = domain + path + query
        converted_url = cleaned_url.strip("/").replace("/", "_").replace(".", "_")
        return converted_url.lstrip("www_")
#Generate code
class Generate_code:
    def __init__(self, url):
        self.url = url
    def generate_code(self):
        img = qrcode.make(self.url)
        return img
#Img
class Img:
    def __init__(self, img, url):
        self.img = img
        self.url = url
        self.output_path_img = "./output/images/"
        self.output_path_index = "./output/indexes/"
        self.output_path_img_rel = "../images/"
        self.output_path_index_rel = "../indexes"
    def create_img(self):
        if not os.path.exists(self.output_path_img):
            os.makedirs(self.output_path_img)

    def save_img(self):
        self.img.save(f"{self.output_path_img}{self.url}.png")