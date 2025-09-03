import pathlib

import ffmpeg
from ffmpeg import Stream

from compress_settings import CompressSettings
from source import SourceFile, SourceType

def get_output_filepath(source: SourceFile) -> pathlib.Path:
    output_path = source.filepath.with_stem(source.filepath.stem + "_compressed").with_suffix(source.extension)
    return output_path

def compress(source: SourceFile, settings: CompressSettings):
    handle_compress(source, settings)

def handle_compress(source: SourceFile, settings: CompressSettings) -> ffmpeg.Stream | None:
    if not source.is_valid:
        raise Exception("Source is not valid")

    if source.type == SourceType.VIDEO:
        return get_compress_video_stream(source, settings)
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
        'fps': settings.fps,
        'format': settings.format_to_convert_to,
    }
    output_params = {k: v for k, v in output_params.items() if v is not None} # Filter out parameters that are None

    stream = ffmpeg.output(audio, video, get_output_filepath(source), **output_params)

    return stream