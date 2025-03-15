import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

from VideoFormatHandler import VideoFormatHandler


class VideoCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jaklin Video Compressor")

        # Set a theme
        style = ttk.Style()
        style.theme_use("clam")

        # Video.
        self.create_video_selection()
        self.create_crf_quality_slider()
        self.create_frame_rate_combobox()
        self.create_output_format_combobox()
        self.create_resolution_field()

        # Audio.
        self.create_audio_bitrate_combobox()

        self.create_video_compress_button()

        # Call update_idletasks to ensure proper sizing
        self.root.update_idletasks()

        # Optionally, you can set a minimum size
        self.root.minsize(400, 300)


    def create_video_compress_button(self):
        self.compress_button = tk.Button(self.root, text="Compress Video", command=self.compress_video)
        self.compress_button.grid(row=7, column=0, columnspan=2, pady=10)

    def create_video_selection(self):
        self.label = tk.Label(self.root, text="Select a video file to compress:")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.select_button = tk.Button(self.root, text="Select Video", command=self.select_video)
        self.select_button.grid(row=1, column=0, columnspan=2, pady=10)

    def create_crf_quality_slider(self):
        crf_label = tk.Label(self.root, text="CRF Quality (0-51):")
        crf_label.grid(row=2, column=0, sticky=tk.W, padx=10)

        self.crf_value = tk.IntVar(value=23)
        self.crf_slider = tk.Scale(self.root, from_=0, to=51, orient=tk.HORIZONTAL, length=200, variable=self.crf_value)
        self.crf_slider.grid(row=2, column=1, padx=10)

    def create_output_format_combobox(self):
        format_label = tk.Label(self.root, text="Format:")
        format_label.grid(row=3, column=0, sticky=tk.W, padx=10)

        self.output_format = ttk.Combobox(self.root, values=VideoFormatHandler.video_file_formats, state="readonly")
        self.output_format.set("mp4")
        self.output_format.grid(row=3, column=1, padx=10)

    def create_frame_rate_combobox(self):
        frame_rate_label = tk.Label(self.root, text="Frame Rate (fps):")
        frame_rate_label.grid(row=4, column=0, sticky=tk.W, padx=10)

        self.frame_rate = ttk.Combobox(self.root, values=["12", "24", "30", "60"], state="readonly")
        self.frame_rate.set("60")
        self.frame_rate.grid(row=4, column=1, padx=10)

    def create_resolution_field(self):
        resolution_label = tk.Label(self.root, text="Video Resolution (%):")
        resolution_label.grid(row=5, column=0, sticky=tk.W, padx=10)

        self.resolution_entry = tk.Entry(self.root)
        self.resolution_entry.insert(0, "100")
        self.resolution_entry.grid(row=5, column=1, padx=10)

    def create_audio_bitrate_combobox(self):
        audio_bitrate_label = tk.Label(self.root, text="Audio Bitrate (kbps):")
        audio_bitrate_label.grid(row=6, column=0, sticky=tk.W, padx=10)

        self.audio_bitrate = ttk.Combobox(self.root, values=["64", "96", "128", "192", "256"], state="readonly")
        self.audio_bitrate.set("192")
        self.audio_bitrate.grid(row=6, column=1, padx=10)

    def select_video(self):
        filetypes = [("Video Files", f"*.{ext}") for ext in VideoFormatHandler.video_file_formats]
        self.video_path = filedialog.askopenfilename(title="Select Video File", filetypes=filetypes)
        if self.video_path:
            messagebox.showinfo("Selected Video", f"Selected: {self.video_path}")

    def compress_video(self):
        if hasattr(self, 'video_path'):
            output_format = self.output_format.get()
            output_path = os.path.splitext(self.video_path)[0] + f"_compressed.{output_format}"

            # Set the appropriate codec based on the selected format
            codec = VideoFormatHandler.get_codec(output_format)
            if codec is None:
                messagebox.showerror("Error", "Unsupported format selected.")
                return

            # Get the resolution percentage from the entry field
            resolution_percentage = self.resolution_entry.get()
            if not resolution_percentage.isdigit() or not (1 <= int(resolution_percentage) <= 100):
                messagebox.showerror("Error", "Please enter a valid percentage (1-100).")
                return
            scale = int(resolution_percentage) / 100.0

            command = [
                'ffmpeg',
                '-y', # This forces overwriting the file; no user input in terminal.
                '-i', self.video_path,
                '-vcodec', codec,
                '-crf', str(self.crf_value.get()), # CRF Quality.
                '-r', self.frame_rate.get(), # Framerate.
                '-b:a', f"{self.audio_bitrate.get()}k",  # Set the audio bitrate.
                '-vf', f'scale=iw*{scale}:ih*{scale}',  # Scale (resolution).
                output_path
            ]

            # Progress window.
            progress_window = tk.Toplevel(self.root)
            progress_window.title("Compressing Video")
            progress_window.geometry("300x100")
            progress_label = tk.Label(progress_window, text="Compressing video, please wait...")
            progress_label.pack(pady=10)

            # Progress bar in window.
            progress_bar = ttk.Progressbar(progress_window, mode='indeterminate')
            progress_bar.pack(pady=10, fill=tk.X, padx=20)
            progress_bar.start()

            def run_compression():
                try:
                    subprocess.run(command, check=True)
                    messagebox.showinfo("Success", f"Video compressed successfully!\nSaved as: {output_path}")
                except subprocess.CalledProcessError as e:
                    messagebox.showerror("Error", f"An error occurred during compression:\n{e}")
                finally:
                    progress_bar.stop()
                    progress_window.destroy()

            threading.Thread(target=run_compression).start()

        else:
            messagebox.showwarning("No Video Selected", "Please select a video file first.")

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("resources/favicon.ico") # Made with Icon Kitchen! :)
    app = VideoCompressorApp(root)
    root.mainloop()