#Import custom utility functions or classes from the utils module
import utils

#Import the local_host module (presumably to handle local server or hosting logic)
import server

#Import the html_generate module
import html_generate

#Import threading module for creating threads
import threading

#User Interface
class UserInterface:
    def start(self) -> None:
        """
        Starts the user interface loop where the user is prompted to enter a URL.
        If the URL is valid, it processes the URL, generates a QR code, and starts the server.
        If the URL is invalid, it prompts the user to enter a valid one.
        """
        while True:
            try:
                self.url_input = str(input("Zadejte URL: "))
                self.url_handler = utils.Url(self.url_input)
                if self.url_handler.check_correct_url():
                    print(f"Adresa {self.url_input} byla nalezena.")
                    self.process_url()
                    self.hosting_server = server.Local_host(self.generated_image, self.cleaned_url)
                    server_thread = threading.Thread(target=self.hosting_server.start_server, daemon=True)
                    server_thread.start()
                    self.hosting_server.end_server()
                    break
                else:
                    print("Špatná URL.")
            except ValueError:
                print("Neplatný vstup. Zadejte platnou URL.")
                continue
    def process_url(self) -> None:
        """
        Processes the URL by generating a QR code for the given URL, cleaning the URL,
        and creating the corresponding HTML files. This method calls necessary functions
        from the utils and html_generate modules to generate and save the image and HTML content.
        """
        code_generator = utils.Generate_code(self.url_handler.url)
        self.generated_image = code_generator.generate_code()
        self.cleaned_url = self.url_handler.cleaned_url()
        self._utils = utils.Img(self.generated_image, self.cleaned_url)
        self._utils.create_img()
        self._utils.save_img()
        html_generator = html_generate.Html_handler(self.generated_image, self.url_handler.url, self.cleaned_url)
        html_generator.generate_html_structure()
        html_generator.save_html()
#Call
if __name__ == "__main__":
    ui = UserInterface()
    ui.start()