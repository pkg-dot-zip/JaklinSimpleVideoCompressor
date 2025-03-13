import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import subprocess
import os
import threading

class VideoCompressorApp:
    video_file_formats = [
        "mp4",
        "webm",
        "avi",
        "mov",
        "wmv",
        "mkv",
        "flv",
        "mpeg",
        "3gp",
        "hevc"
    ]

    def __init__(self, root):
        self.root = root
        self.root.title("Video Compression Application")
        self.root.geometry("400x400")

        # Video.
        self.create_video_selection()
        self.create_crf_quality_slider()
        self.create_frame_rate_combobox()
        self.create_output_format_combobox()
        self.create_resolution_field()

        # Audio.
        self.create_audio_bitrate_combobox()


        self.create_video_compress_button()


    def create_video_compress_button(self):
        self.compress_button = tk.Button(root, text="Compress Video", command=self.compress_video)
        self.compress_button.pack(pady=10)

    def create_video_selection(self):
        self.label = tk.Label(root, text="Select a video file to compress:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Video", command=self.select_video)
        self.select_button.pack(pady=10)

    def create_crf_quality_slider(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        crf_label = tk.Label(frame, text="CRF Quality (0-51):")
        crf_label.pack(side=tk.LEFT)

        self.crf_value = tk.IntVar(value=23)

        self.crf_slider = tk.Scale(frame, from_=0, to=51, orient=tk.HORIZONTAL, length=300, variable=self.crf_value)
        self.crf_slider.pack(side=tk.RIGHT)

    def create_output_format_combobox(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        frame_rate_label = tk.Label(frame, text="Format:")
        frame_rate_label.pack(side=tk.LEFT)

        self.output_format = ttk.Combobox(frame, values=self.video_file_formats, state="readonly")
        self.output_format.set("mp4")
        self.output_format.pack(side=tk.RIGHT)

    def create_frame_rate_combobox(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        frame_rate_label = tk.Label(frame, text="Frame Rate (fps):")
        frame_rate_label.pack(side=tk.LEFT)

        self.frame_rate = ttk.Combobox(frame, values=["12", "24", "30", "60"], state="readonly")
        self.frame_rate.set("60")
        self.frame_rate.pack(side=tk.RIGHT)\

    def create_resolution_field(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        resolution_label = tk.Label(frame, text="Video Resolution (%):")
        resolution_label.pack(side=tk.LEFT)

        self.resolution_entry = tk.Entry(frame)
        self.resolution_entry.insert(0, "100")
        self.resolution_entry.pack(side=tk.RIGHT)

    def create_audio_bitrate_combobox(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        audio_bitrate_label = tk.Label(frame, text="Audio Bitrate (kbps):")
        audio_bitrate_label.pack(side=tk.LEFT)

        self.audio_bitrate = ttk.Combobox(frame, values=["64", "96", "128", "192", "256"], state="readonly")
        self.audio_bitrate.set("192")
        self.audio_bitrate.pack(side=tk.RIGHT)

    def select_video(self):
        filetypes = [("Video Files", f"*.{ext}") for ext in self.video_file_formats]
        self.video_path = filedialog.askopenfilename(title="Select Video File", filetypes=filetypes)
        if self.video_path:
            messagebox.showinfo("Selected Video", f"Selected: {self.video_path}")

    def get_codec(self, output_format):
        if output_format == "mp4":
            return "libx264"
        elif output_format == "webm":
            return "libvpx"
        elif output_format == "avi":
            return "mpeg4"
        elif output_format == "mov":
            return "libx264"
        elif output_format == "wmv":
            return "wmv2"
        elif output_format == "mkv":
            return "libx264"
        elif output_format == "flv":
            return "flv"
        elif output_format == "mpeg":
            return "mpeg2video"
        elif output_format == "3gp":
            return "libx264"
        elif output_format == "hevc":
            return "libx265"
        else:
            return None  # Unsupported format

    def compress_video(self):
        if hasattr(self, 'video_path'):
            output_format = self.output_format.get()
            output_path = os.path.splitext(self.video_path)[0] + f"_compressed.{output_format}"

            # Set the appropriate codec based on the selected format
            codec = self.get_codec(output_format)
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
                '-i', self.video_path,
                '-vcodec', codec,
                '-crf', str(self.crf_value.get()), # CRF Quality.
                '-r', self.frame_rate.get(), # Framerate.
                '-b:a', f"{self.audio_bitrate.get()}k",  # Set the audio bitrate
                '-vf', f'scale=iw*{scale}:ih*{scale}',  # Scale (resolution)
                output_path
            ]

            # Create a Toplevel window for progress indication
            progress_window = tk.Toplevel(self.root)
            progress_window.title("Compressing Video")
            progress_window.geometry("300x100")
            progress_label = tk.Label(progress_window, text="Compressing video, please wait...")
            progress_label.pack(pady=10)

            # Create a progress bar
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
    app = VideoCompressorApp(root)
    root.mainloop()