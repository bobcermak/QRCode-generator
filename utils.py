#Importing the os module to manipulate files
import os

#Importing the qrcode module for generating QR codes
import qrcode

#Importing the requests library to make HTTP requests (e.g., for validating or fetching URLs)
import requests

#Importing urlparse from urllib.parse for parsing URLs into components
from urllib.parse import urlparse

##Classes##
#Url
class Url:
    def __init__(self, url):
        self.url = url
    def checkCorrectUrl(self) -> bool:
        try:
            self.response = requests.get(self.url)
            return self.response.status_code == 200
        except Exception as e:
            print(f"Error while checking URL: {e}")
            return False
    def cleanedUrl(self):
        parsed_url = urlparse(self.url)
        cleaned_url = parsed_url.netloc + parsed_url.path
        converted_url = cleaned_url.strip("/").replace("/", "_").replace(".", "_")
        return converted_url.lstrip("www_")
#Generate code
class GenCode:
    def __init__(self, url):
        self.url = url
    def generateCode(self): #return cleanedUrl()
        img = qrcode.make(self.url)
        return img
#Write img
class Img:
    def __init__(self, img, url):
        self.img = img
        self.url = url
        self.output_path = "./output/images/"
        self.output_path_index = "./output/indexes/"
    def createImg(self):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
    def saveImg(self):
        self.img.save(f"{self.output_path}{self.url}.png")