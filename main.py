import utils
#Ui
class Ui:
    def uiAsk(self):
        while True:
            try:
                self.url = str(input("Enter a URL: "))
                _utilsUrl = utils.Url()
                if (_utilsUrl.checkCorrectUrl(self.url)):
                    print(f"Address {self.url} has been found, please go to the output folder")
                    _genCode = utils.GenCode()
                    _writeImg = utils.WriteImg()
                    ourImg = _genCode.generateCode(self.url)
                    _writeImg.writeImg(ourImg)
            except ValueError:
                print("Invalid input. Please enter a valid URL.")
                continue
#Call
ui = Ui()
ui.uiAsk()