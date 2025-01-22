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
    <style>
        body {{
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }}

        .container {{
            margin: 0 auto;
            text-align: center;
        }}

        img {{
            display: block;
            max-width: 100%;
            height: auto;
            margin: 0 auto;
            padding: 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>QRCode</h1>
        <img src="{path_img}{path_url}.png" alt="QRCode" width="400" height="400">
        <a href="{self.fullUrl}" target="_blank">{self.fullUrl}</a>
        <p>The QR code has been downloaded to the <a href="{path_img}{path_url}.png" target="_blank">{path_img}{path_url}.png</a>.</p>
    </div>
</body>
</html>
</html>
"""
        with open(f"{path_index}{our_url}.html", "w") as file:
            file.write(f"{html_content}")