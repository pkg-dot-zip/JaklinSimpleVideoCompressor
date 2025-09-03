import pathlib
from enum import Enum

import valid_file_types


class SourceType(Enum):
    VIDEO = "video"
    IMAGE = "image"
    AUDIO = "audio"


def calc_source_type(extension: str) -> SourceType | None:
    """Returns enum with type of source file. Returns none if invalid."""

    # The 'endswith()' method takes in tuples, not lists, according to SO.
    video_tuple = tuple(valid_file_types.video_types)
    image_tuple = tuple(valid_file_types.image_types)
    audio_tuple = tuple(valid_file_types.audio_types)

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