import pathlib
from enum import Enum


class SourceType(Enum):
    VIDEO = "video"
    IMAGE = "image"
    AUDIO = "audio"


video_types = [".mp4", ".webm", ".avi"]
image_types = [".jpg", ".jpeg", ".png", ".webp"]
audio_types = [".mp3", ".wav", ".aiff"]


def calc_source_type(extension: str) -> SourceType | None:
    """Returns enum with type of source file. Returns none if invalid."""

    # The 'endswith()' method takes in tuples, not lists, according to SO.
    video_tuple = tuple(video_types)
    image_tuple = tuple(image_types)
    audio_tuple = tuple(audio_types)

    if extension.endswith(video_tuple):
        return SourceType.VIDEO
    elif extension.endswith(image_tuple):
        return SourceType.IMAGE
    elif extension.endswith(audio_tuple):
        return SourceType.AUDIO
    return None

class SourceFile:
    def __init__(self, filepath: pathlib.Path):
        self.filepath = filepath
        self.extension = filepath.suffix.lower()
        self.name = filepath.stem
        self.type = calc_source_type(self.extension)

        # Do this last.
        self.is_valid = is_valid_source(self)

def is_valid_source(source: SourceFile):
    """Returns true if source is valid."""
    if source.type is None:
        return False
    return True