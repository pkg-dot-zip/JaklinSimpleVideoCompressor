from tkinter import ttk
import tkinter as tk

class ProgressGuiHandler:
    @staticmethod
    def create_progress_window(app):
        # Progress window.
        progress_window = tk.Toplevel(app.root)
        progress_window.title("Compressing Video")
        progress_window.geometry("300x100")
        progress_label = tk.Label(progress_window, text="Compressing video, please wait...")
        progress_label.pack(pady=10)

        # Progress bar in window.
        progress_bar = ttk.Progressbar(progress_window, mode='indeterminate')
        progress_bar.pack(pady=10, fill=tk.X, padx=20)
        progress_bar.start()

        return progress_window, progress_bar

    @staticmethod
    def stop_progress_window(progress_window, progress_bar):
        progress_bar.stop()
        progress_window.destroy()