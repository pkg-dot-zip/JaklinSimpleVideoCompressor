from source import SourceType

video_types = [".mp4", ".webm", ".avi"]
image_types = [".jpg", ".jpeg", ".png", ".webp"]
audio_types = [".mp3", ".wav", ".aiff"]

def get_file_types(s_type: SourceType) -> list[str]:
    if s_type == SourceType.VIDEO:
        return video_types
    elif s_type == SourceType.AUDIO:
        return audio_types
    elif s_type == SourceType.IMAGE:
        return image_types
    raise ValueError(f"Invalid source type: {s_type}")


def get_valid_filetypes_for_dialog(s_type: SourceType) -> list[str]:
    """Returns a list of strings formatted to be used in a file dialog to limit visible types."""
    copy = get_file_types(s_type).copy()
    for i, e in enumerate(copy):
        copy[i] = "*" + e
    return copy