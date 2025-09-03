from tkinter import Tk, Button


class MainWindow:
    """Gui code for our app."""

    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.title("Jaklin Compressor")

        # The "Compress" button.
        button = Button(self.window, text="Compress", command=self.window.quit) # TODO: Run compress command.
        button.pack()

    def run(self):
        self.window.mainloop()