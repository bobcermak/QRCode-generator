# Import custom utility functions or classes from the utils module
import utils

# Import the local_host module (presumably to handle local server or hosting logic)
import server

# Import the html_gen module
import html_gen

#Ui
class Ui:
    def ui_ask(self):
        while True:
            try:
                self.url = str(input("Enter a URL: "))
                _url = utils.Url(self.url)
                if (_url.check_correct_url()):
                    print(f"Address {self.url} has been found")
                    _gen_code = utils.GenCode(self.url)
                    ourImg = _gen_code.generate_code()
                    cleaned_url = _url.cleaned_url()
                    _img = utils.Img(ourImg, cleaned_url)
                    _img.create_img()
                    _img.save_img()
                    _html = html_gen.Html(ourImg, self.url)
                    _html.html_structure(ourImg, cleaned_url)
                    hosting = server.LocalHost(ourImg, cleaned_url)
                    hosting.start_server()
                else:
                    print("Invalid URL")
            except ValueError:
                print("Invalid input. Please enter a valid URL.")
                continue
#Call
if __name__ == "__main__":
    ui = Ui()
    ui.ui_ask()