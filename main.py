import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import subprocess
import os

class VideoCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Compression Application")
        self.root.geometry("400x400")

        self.label = tk.Label(root, text="Select a video file to compress:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Video", command=self.select_video)
        self.select_button.pack(pady=10)

        # CRF Quality Slider.
        self.crf_label = tk.Label(root, text="Select CRF Quality (0-51):")
        self.crf_label.pack(pady=10)

        self.crf_value = tk.IntVar(value=23)  # Instance variable to hold the CRF value

        self.crf_slider = tk.Scale(root, from_=0, to=51, orient=tk.HORIZONTAL, length=300, variable=self.crf_value)
        self.crf_slider.pack(pady=10)

        # Combobox format selection.
        self.output_format = ttk.Combobox(root, values=["mp4", "webm", "avi", "mov"], state="readonly")
        self.output_format.set("mp4")  # Default value
        self.output_format.pack(pady=10)

        self.compress_button = tk.Button(root, text="Compress Video", command=self.compress_video)
        self.compress_button.pack(pady=10)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.webm")])
        if self.video_path:
            messagebox.showinfo("Selected Video", f"Selected: {self.video_path}")

    def compress_video(self):
        if hasattr(self, 'video_path'):
            output_format = self.output_format.get()
            output_path = os.path.splitext(self.video_path)[0] + f"_compressed.{output_format}"

            # Set the appropriate codec based on the selected format
            if output_format == "mp4":
                codec = "libx264"
            elif output_format == "webm":
                codec = "libvpx"
            elif output_format == "avi":
                codec = "mpeg4"
            elif output_format == "mov":
                codec = "libx264"
            else:
                messagebox.showerror("Error", "Unsupported format selected.")
                return

            command = [
                'ffmpeg',
                '-i', self.video_path,
                '-vcodec', codec,
                '-crf', str(self.crf_value.get()),
                output_path
            ]

            try:
                subprocess.run(command, check=True)
                messagebox.showinfo("Success", f"Video compressed successfully!\nSaved as: {output_path}")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"An error occurred during compression:\n{e}")
        else:
            messagebox.showwarning("No Video Selected", "Please select a video file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoCompressorApp(root)
    root.mainloop()