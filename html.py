import sys
sys.path.append(r"C:\Users\Bob\Desktop\QRCode\libraries")
import os
import flask

app = Flask(__name__)

@app.route("/tvuj_soubor")
def serve_html():
    return send_from_directory(os.getcwd(), "tvuj_soubor.html")

if __name__ == "__main__":
    app.run(debug=True)