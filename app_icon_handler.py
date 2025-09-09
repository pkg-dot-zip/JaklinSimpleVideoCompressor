import os
import sys

def set_app_icon(tkinter_root):
    tkinter_root.iconbitmap(get_app_icon())

def get_app_icon():
    # 'frozen' (running as an executable)
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(sys._MEIPASS, "resources/favicon.ico")

    # normal Python environment.
    else:
        icon_path = "resources/favicon.ico"

    return icon_path