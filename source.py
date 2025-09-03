import pathlib
from enum import Enum


class SourceType(Enum):
    VIDEO = "video"
    IMAGE = "image"
    AUDIO = "audio"


video_types = [".mp4", ".webm", ".avi"]
image_types = [".jpg", ".jpeg", ".png", ".webp"]
audio_types = [".mp3", ".wav", ".aiff"]


def calc_source_type(extension: str):
    """Returns enum with type of source file. Returns none if invalid."""

    # The 'endswith()' method takes in tuples, not lists, according to SO.
    video_tuple = tuple(video_types)
    image_tuple = tuple(image_types)
    audio_tuple = tuple(audio_types)

    if extension.lower().endswith(video_tuple):
        return SourceType.VIDEO
    elif extension.lower().endswith(image_tuple):
        return SourceType.IMAGE
    elif extension.lower().endswith(audio_tuple):
        return SourceType.AUDIO
    return None


class SourceFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.extension = pathlib.Path(filepath).suffix.lower()
        self.name = pathlib.Path(filepath).stem
        self.type = calc_source_type(self.extension)
