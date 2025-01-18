import utils
#Ui
class Ui:
    def uiAsk(self):
        while True:
            try:
                self.url = str(input("Enter a URL: "))
                _url = utils.Url()
                if (_url.checkCorrectUrl(self.url)):
                    print(f"Address {self.url} has been found, please go to the output folder")
                    _genCode = utils.GenCode()
                    _img = utils.Img()
                    ourImg = _genCode.generateCode(self.url)
                    cleanedUrl = _url.cleanedUrl(self.url)
                    _img.createImg()
                    _img.saveImg(ourImg, cleanedUrl)
            except ValueError:
                print("Invalid input. Please enter a valid URL.")
                continue 
#Call
ui = Ui()
ui.uiAsk()