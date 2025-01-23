#Import custom utility functions or classes from the utils module
import utils

#Import the local_host module (presumably to handle local server or hosting logic)
import server

#Import the html_gen module
import html_gen

#Import threading module for creating threads
import threading

#User Interface
class UserInterface:
    def start(self):
        while True:
            try:
                self.url_input = str(input("Enter a URL: "))
                self.url_handler = utils.Url(self.url_input)
                if self.url_handler.check_correct_url():
                    print(f"Address {self.url_input} has been found.")
                    self.process_url()
                    self.hosting_server = server.Local_host(self.generated_image, self.cleaned_url)
                    server_thread = threading.Thread(target=self.hosting_server.start_server, daemon=True)
                    server_thread.start()
                    self.hosting_server.end_server_ui()
                    break
                else:
                    print("Invalid URL.")
            except ValueError:
                print("Invalid input. Please enter a valid URL.")
                continue
    def process_url(self):
        code_generator = utils.Generate_code(self.url_handler.url)
        self.generated_image = code_generator.generate_code()
        self.cleaned_url = self.url_handler.cleaned_url()
        self._utils = utils.Img(self.generated_image, self.cleaned_url)
        self._utils.create_img()
        self._utils.save_img()
        html_generator = html_gen.Html_handler(self.generated_image, self.url_handler.url, self.cleaned_url)
        html_generator.generate_html_structure()
        html_generator.save_html()
#Call
if __name__ == "__main__":
    ui = UserInterface()
    ui.start()