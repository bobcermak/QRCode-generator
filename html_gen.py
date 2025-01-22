# Import the html module, which provides functions for handling HTML entities and escaping text
import html

# Import custom utility library
import utils

#HTML
class Html:
    def __init__(self, img, fullUrl):
        self.img = img
        self.fullUrl = fullUrl
    def html_structure(self, img, url):
        _utils = utils.Img(img, url)
        our_url = _utils.url
        path_index = _utils.output_path_index
        path_img = _utils.output_path_rel
        path_url = _utils.url
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QRCode</title>
</head>
<body style="display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: Arial, sans-serif; text-align: center;">
    <div style="text-align: center;">
        <h1>QRCode</h1>
        <img src="{path_img}{path_url}.png" alt="QRCode" width="400" height="400" style="display: block; max-width: 100%; height: auto; margin: 0; padding: 0;">
        <a href="{self.fullUrl}" target="_blank">{self.fullUrl}</a>
        <p>The QR code has been downloaded to the <a href="{path_img}" target="_blank">{path_img}</a> folder.</p>
    </div>
</body>
</html>
"""
        with open(f"{path_index}{our_url}.html", "w") as file:
            file.write(f"{html_content}")