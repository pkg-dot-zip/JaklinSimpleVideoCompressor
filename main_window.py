import pathlib
import tkinter
from pathlib import Path
from tkinter import Tk, Button, filedialog, messagebox

import valid_file_types
from source import SourceType


class MainWindow:
    """Gui code for our app."""

    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.title("Jaklin Compressor")

        # The "Select File" row.
        self.fileTextBox = tkinter.Text(self.window, height=1)
        self.fileTextBox['state'] = tkinter.DISABLED # This avoids people being able to type in to the field.
        self.fileTextBox.pack()
        open_file_button = tkinter.Button(self.window, text="Open File", command=self.select_file)
        open_file_button.pack()

        # The "Compress" button.
        button = Button(self.window, text="Compress", command=self.window.quit) # TODO: Run compress command.
        button.pack()

    def select_file(self):
        file = select_file_from_file_dialog()
        if file is None:
            return
        self.fileTextBox['state'] = tkinter.NORMAL
        self.fileTextBox.delete("1.0", tkinter.END)
        self.fileTextBox.insert("1.0", file.name)
        self.fileTextBox['state'] = tkinter.DISABLED

    def run(self):
        self.window.mainloop()



def select_file_from_file_dialog() -> Path | None:
    filetypes = (
        ('All files', '*.*'),
        ('Video files', valid_file_types.get_valid_filetypes_for_dialog(SourceType.VIDEO)),
        ('Image files', valid_file_types.get_valid_filetypes_for_dialog(SourceType.IMAGE)),
        ('Audio files', valid_file_types.get_valid_filetypes_for_dialog(SourceType.AUDIO)),
    )

    file_path = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if file_path is None:
        return None

    return pathlib.Path(file_path)