import pathlib
from dataclasses import dataclass

import ffmpeg
from ffmpeg import Stream

from source import SourceFile, SourceType


@dataclass
class CompressSettings:
    """Contains settings for compressing all source files. Settings are optional if None by default."""
    fps: int = None
    video_bitrate: int = None
    audio_bitrate: int = None
    should_mute: bool = False # TODO: Implement.

def get_output_filepath(source: SourceFile) -> pathlib.Path:
    output_path = source.filepath.with_stem(source.filepath.stem + "_compressed").with_suffix(source.extension)
    return output_path

def compress(source: SourceFile, settings: CompressSettings):
    """Does mild validation, then directs to correct method for the sourceType."""

    if not source.is_valid:
        raise Exception("Source is not valid")

    if source.type == SourceType.VIDEO:
        stream = get_compress_video_stream(source, settings) # TODO: Use this stream.
    elif source.type == SourceType.AUDIO:
        pass
    elif source.type == SourceType.IMAGE:
        pass

    raise Exception("Unknown source type") # Should literally be impossible at this point.


def get_compress_video_stream(source: SourceFile, settings: CompressSettings) -> Stream:
    stream = ffmpeg.input(source.filepath)

    # First handle the audio.
    audio = stream.audio

    # Then handle the video.
    video = stream.video

    # Then set output.
    output_params = {
        'video_bitrate': settings.video_bitrate,
        'audio_bitrate': settings.audio_bitrate,
        'fps': settings.fps
    }
    output_params = {k: v for k, v in output_params.items() if v is not None} # Filter out parameters that are None

    stream = ffmpeg.output(audio, video, get_output_filepath(source), **output_params)

    return stream