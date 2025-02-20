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
    def __init__(self, url: str):
        """
        Initializes the Url class with a given URL string.
        Args:
            url (str): The URL to be checked and cleaned.
        """
        self.url = url
    def check_correct_url(self) -> bool:
        """
        Checks if the URL is valid by making an HTTP request and checking the response status code.
        Returns:
            bool: True if the URL is reachable and valid, False otherwise.
        """
        try:
            self.response = requests.get(self.url)
            return self.response.status_code == 200
        except requests.exceptions.ConnectionError:
            print("Chyba: Nelze se připojit k internetu.")
            return False
        except Exception as e:
            print(f"Chyba při kontrolování URL: {e}")
            return False
    def cleaned_url(self) -> str:
        """
        Cleans the URL by extracting the domain, path, and query (first 5 characters) and converting it into a safe format.
        Returns:
            str: A cleaned version of the URL suitable for use as a file name.
        """
        parsed_url = urlparse(self.url)
        domain = parsed_url.netloc
        path = parsed_url.path[:5]
        query = parsed_url.query[:5]
        cleaned_url = domain + path + query
        converted_url = cleaned_url.strip("/").replace("/", "_").replace(".", "_")
        return converted_url.lstrip("www_")
#Generate code
class Generate_code:
    def __init__(self, url: str):
        """
        Initializes the Generate_code class with a URL.
        Args:
            url (str): The URL for which the QR code will be generated.
        """
        self.url = url
    def generate_code(self):
        """
        Generates a QR code image from the provided URL.
        Returns:
            img: A QR code image generated from the URL.
        """
        img = qrcode.make(self.url)
        return img
#Img
class Img:
    def __init__(self, img: Generate_code, url: str):
        """
        Initializes the Img class with a generated QR code image and the corresponding URL.
        Args:
            img (img): The generated QR code image.
            url (str): The cleaned URL used for saving the image and related HTML files.
        """
        self.img = img
        self.url = url
        self.output_path_img = "./output/images/"
        self.output_path_index = "./output/indexes/"
        self.output_path_img_rel = "../images/"
        self.output_path_index_rel = "../indexes"
    def create_img(self) -> None:
        """
        Creates the necessary directory to save the image if it does not already exist.
        """
        if not os.path.exists(self.output_path_img): os.makedirs(self.output_path_img)
    def save_img(self) -> None:
        """
        Saves the generated QR code image to the specified file path using the cleaned URL as the file name.
        """
        self.img.save(f"{self.output_path_img}{self.url}.png")