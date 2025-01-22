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
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <link rel="icon" sizes="256x357" href="../assets/qrcode-logo.jpg"/>
    <title>QRCode</title>
    <style>
        body {{
            height: 100vh;
            height: 100dvh;
            margin: 0;
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #1e3a8a, #4ade80);
            display: flex;
            justify-content: center;
            align-items: center;
            color: #ffffff;
        }}

        .container {{
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 1em;
            padding: 2em;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            text-align: center;
            max-width: 31.25em;
            width: 80%;
        }}

        h1 {{
            margin: 0;
            font-size: 2.5em;
            color: #f9fafb;
        }}

        img {{
            display: block;
            max-width: 100%;
            height: 100%;
            object-fit: cover;
            margin: 1.25em auto;
            border: 0.1875em solid #ffffff;
            border-radius: 0.625em;
        }}

        a {{
            color: #4ade80;
            font-weight: bold;
            text-decoration: none;
            text-align: center;
            word-wrap: break-word;
        }}

        a:hover {{
            color: #a7f3d0;
            text-decoration: underline;
        }}

        p {{
            margin-top: 1.25em;
            font-size: 1em;
        }}

        @media (max-width: 768px) {{
            h1 {{
                font-size: 2em;
            }}

            p {{
                font-size: 0.9em;
            }}

            img {{
                width: 80%;
            }}
        }}

        @media (max-width: 480px) {{
            .container {{
                padding: 1.5em;
            }}

            h1 {{
                font-size: 1.8em;
            }}

            p {{
                font-size: 0.8em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>QRCode</h1>
        <img src="{path_img}{path_url}.png" alt="QRCode" width="400" height="400">
        <a href="{self.fullUrl}" target="_blank">{self.fullUrl}</a>
        <p>The QR codes have been downloaded to the <a href="{path_img}" target="_blank">{path_img}</a>.</p>
    </div>
</body>
</html>
"""
        with open(f"{path_index}{our_url}.html", "w") as file:
            file.write(f"{html_content}")