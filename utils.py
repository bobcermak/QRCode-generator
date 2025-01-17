import sys
sys.path.append(r"C:\Users\Bob\Desktop\QRCode\libraries")
import qrcode
import requests
from urllib.parse import urlparse

##Classes##
#Url
class Url:
    def checkCorrectUrl(self, url) -> bool:
        self.response = requests.get(url)
        return self.response.status_code == 200
    def cleanedUrl(self):
        parsed_url = urlparse(self.response)
        cleaned_url = parsed_url.netloc + parsed_url.path
        return cleaned_url
#Generate code
class GenCode:
    def generateCode(self, url):
        img = qrcode.make(url)
        return img
#Write img
class WriteImg(Url):
    def writeImg(self, img):
        with open(f'./output/txts/{super().cleanedUrl()}.txt', 'w') as file:
            file.write(f"\nImage saved as: ./output/images/{super().cleanedUrl()}.png")
        img.save(f"./output/images/{super().cleanedUrl()}.png")