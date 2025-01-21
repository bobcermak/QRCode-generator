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
        path_img = _utils.output_path
        path_url = _utils.url
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QRCode</title>
</head>
<body>
    <article>
        <h1>QRCode</h1>
        <img src="{path_img}{path_url}" alt="QRCode" width="400" height="400">
        <a href="{self.fullUrl}" target="_blank">{self.fullUrl}</a>
        <p>The QR code has been downloaded to the <a href="{path_img}" target="_blank">{path_img}</a> folder.</p>
    <article/>
</body>
</html>
"""
        with open(f"{path_index}{our_url}.html", "w") as file:
            file.write(f"{html_content}")