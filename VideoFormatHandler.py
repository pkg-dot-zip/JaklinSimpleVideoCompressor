class VideoFormatHandler:
    video_file_formats = [
        "mp4",
        "webm",
        "avi",
        "mov",
        "wmv",
        "mkv",
        "flv",
    ]

    @staticmethod
    def get_codec(output_format):
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