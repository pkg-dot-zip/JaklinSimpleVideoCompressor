import tkinter
from tkinter import Tk, Button
from tkinter.ttk import Combobox

import app_icon_handler
import compressor
import file_dialog_handler
from compress_settings import VideoCompressSettings
from quality_settings import Quality
from source import SourceFile
from source_type import SourceType


class MainWindow:
    """Gui code for our app."""

    def __init__(self):
        self.window = Tk()
        app_icon_handler.set_app_icon(self.window)
        self.window.geometry("400x400")
        self.window.title("Jaklin Compressor")

        self.current_source_file = None

        # The "Select File" row.
        self.fileTextBox = tkinter.Text(self.window, height=1)
        self.fileTextBox['state'] = tkinter.DISABLED # This avoids people being able to type in to the field.
        self.fileTextBox.pack()
        open_file_button = tkinter.Button(self.window, text="Open File", command=self.select_file)
        open_file_button.pack()

        # The "Compress" button.
        self.compress_button = Button(self.window, text="Compress", command=self.on_compress_button_clicked)
        self.compress_button['state'] = tkinter.DISABLED
        self.compress_button.pack()

        # Quality dropdown menu.
        quality_dropdown_values = [q.get_readable_name() for q in Quality]
        self.quality_dropdown = Combobox(self.window, values=quality_dropdown_values)
        self.quality_dropdown.current(max(Quality, key=lambda m: m.value).value) # SO to colleagues that actually know Python.
        self.quality_dropdown.pack()

        # File format conversion menu. # TODO ADD

    def on_compress_button_clicked(self):
        if not self.current_source_file:
            self.select_file()
            return

        settings = VideoCompressSettings(fps=12, video_bitrate=400) # TODO: Do not hardcode, instead make configurable.
        compressor.compress(self.current_source_file, settings)

    def refresh_ui_based_on_source_type(self, s_type: SourceType):
        if s_type == SourceType.IMAGE:
            pass # TODO: Implement.

        elif s_type == SourceType.AUDIO:
            pass # TODO: Implement.

        elif s_type == SourceType.VIDEO:
            pass # TODO: Implement.

        else:
            raise ValueError(f"Invalid source type: {s_type}")

    def select_file(self):
        file_path = file_dialog_handler.select_file_from_file_dialog()
        if file_path is None:
            return

        # Set filename in UI.
        self.fileTextBox['state'] = tkinter.NORMAL
        self.fileTextBox.delete("1.0", tkinter.END)
        self.fileTextBox.insert("1.0", file_path.name)
        self.fileTextBox['state'] = tkinter.DISABLED

        # Store selected file in var.
        self.current_source_file = SourceFile(file_path)
        self.refresh_ui_based_on_source_type(self.current_source_file.type)

        # Make 'compress' button clickable.
        self.compress_button['state'] = tkinter.NORMAL

    def run(self):
        self.window.mainloop()