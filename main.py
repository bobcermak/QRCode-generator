# Import custom utility functions or classes from the utils module
import utils

# Import the local_host module (presumably to handle local server or hosting logic)
import server

# Import the html_gen module
import html_gen

#Ui
class Ui:
    def uiAsk(self):
        while True:
            try:
                self.url = str(input("Enter a URL: "))
                _url = utils.Url(self.url)
                if (_url.checkCorrectUrl()):
                    print(f"Address {self.url} has been found, please go to the output folder")
                    _genCode = utils.GenCode(self.url)
                    ourImg = _genCode.generateCode()
                    cleanedUrl = _url.cleanedUrl()
                    _img = utils.Img(ourImg, cleanedUrl)
                    _img.createImg()
                    _img.saveImg()
                    _html = html_gen.Html(ourImg, cleanedUrl) #!!!
                    _html.htmlStructure(ourImg, cleanedUrl)
                    hosting = server.LocalHost(ourImg, cleanedUrl)
                    hosting.startServer()
                else:
                    print("Invalid URL")
            except ValueError:
                print("Invalid input. Please enter a valid URL.")
                continue
#Call
if __name__ == "__main__":
    ui = Ui()
    ui.uiAsk()