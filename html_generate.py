#Import os to handle file and directory operations
import os

#Import html to handle HTML entities if needed
import html

#Import custom utility library for image handling
import utils

#Classes
#Html handler
class Html_handler:
    def __init__(self, qr_image: utils.Generate_code, full_url: str, base_url: str):
        """
        Initializes the Html_handler class with QR code image, full URL, and base URL for HTML generation.
        Args:
            qr_image (img): The QR code image to be embedded in the HTML.
            full_url (str): The full URL for the QR code.
            base_url (str): The base URL used for saving files and generating paths.
        """
        self.qr_image = qr_image
        self.full_url = full_url
        self._utils = utils.Img(qr_image, base_url)
        self.base_url = self._utils.url
        self.index_output_path = self._utils.output_path_index
        self.image_rel_path = self._utils.output_path_img_rel
        self.index_rel_path = self._utils.output_path_index_rel
        self.url_path = self._utils.url
    def generate_html_structure(self) -> None:
        """
        Generates the HTML content structure, embedding the QR code and providing links.
        The method creates a complete HTML structure including styles, the QR code image, and links to the 
        full URL and relative path to the saved image.
        """
        self.html_content = f"""
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
        <p><b>{self.url_path}</b></p>
        <img src="{self.image_rel_path}{self.url_path}.png" alt="QRCode" width="400" height="400">
        <a href="{self.full_url}" target="_blank">{self.full_url}</a>
        <p>QRCodes naleznete <a href="{self.index_rel_path}" target="_blank">zde</a>.</p>
    </div>
</body>
</html>
"""
    def save_html(self) -> None:
        """
        Saves the generated HTML content to a file in the specified output path.
        If the output directory does not exist, it is created. The HTML file is named based on the base URL.
        """
        if not os.path.exists(self.index_output_path): os.makedirs(self.index_output_path)
        with open(f"{self.index_output_path}{self.base_url}.html", "w") as file: file.write(self.html_content)