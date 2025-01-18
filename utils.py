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
    def checkCorrectUrl(self, url) -> bool:
        try:
            self.response = requests.get(url)
            return self.response.status_code == 200
        except Exception as e:
            print(f"Error while checking URL: {e}")
            return False
    def cleanedUrl(self, url):
        parsed_url = urlparse(url)
        cleaned_url = parsed_url.netloc + parsed_url.path
        converted_url = cleaned_url.strip("/").replace("/", "_").replace(".", "_")
        return converted_url.lstrip("www_")
#Generate code
class GenCode:
    def generateCode(self, url): #return cleanedUrl()
        img = qrcode.make(url)
        return img
#Write img
class Img:
    def createImg(self):
        self.output_path = "./output/images/"
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
    def saveImg(self, img, url):
        img.save(f"{self.output_path}{url}.png")