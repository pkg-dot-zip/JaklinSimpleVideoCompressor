import os
import sys
from tkinter import ttk


class GuiUtil:
    @staticmethod
    def configure_theme():
        style = ttk.Style()
        style.theme_use("clam")

    # Icon made with Icon Kitchen! :)
    @staticmethod
    def configure_window_icon():

        # If the application is 'frozen' (running as an executable).
        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, "resources/favicon.ico")

        # If running in a normal Python environment.
        else:
            icon_path = "resources/favicon.ico"

        return icon_path
