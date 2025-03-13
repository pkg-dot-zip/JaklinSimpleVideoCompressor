import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class VideoCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Compression Application")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Select a video file to compress:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Video", command=self.select_video)
        self.select_button.pack(pady=10)

        self.compress_button = tk.Button(root, text="Compress Video", command=self.compress_video)
        self.compress_button.pack(pady=10)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if self.video_path:
            messagebox.showinfo("Selected Video", f"Selected: {self.video_path}")

    def compress_video(self):
        if hasattr(self, 'video_path'):
            output_path = os.path.splitext(self.video_path)[0] + "_compressed.mp4"
            command = [
                'ffmpeg',
                '-i', self.video_path,
                '-vcodec', 'libx264',
                '-crf', '23',
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