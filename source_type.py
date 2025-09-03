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


def get_file_types(s_type: SourceType) -> list[str]:
    if s_type == SourceType.VIDEO:
        return valid_file_types.video_types
    elif s_type == SourceType.AUDIO:
        return valid_file_types.audio_types
    elif s_type == SourceType.IMAGE:
        return valid_file_types.image_types
    raise ValueError(f"Invalid source type: {s_type}")


def get_valid_filetypes_for_dialog(s_type: SourceType) -> list[str]:
    """Returns a list of strings formatted to be used in a file dialog to limit visible types."""
    copy = get_file_types(s_type).copy()
    for i, e in enumerate(copy):
        copy[i] = "*" + e
    return copy
