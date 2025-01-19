# Import the html module, which provides functions for handling HTML entities and escaping text
import html

# Import custom utility library
import utils

#HTML
class Html:
    def __init__(self, img, fullUrl):
        self.img = img
        self.fullUrl = fullUrl
    def htmlStructure(self, img, url):
        _utils = utils.Img(img, url)
        ourUrl = _utils.url
        path = _utils.output_path_index
        # content = "<div>QRcode</div>"
        # escaped_content = html.escape(content)
        html_content = f"""
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Kód</title>
</head>
<body>
    <div>Hey<div/>
</body>
</html>
"""
        with open(f"{path}{ourUrl}", "w") as file:
            file.write(f"{html_content}")