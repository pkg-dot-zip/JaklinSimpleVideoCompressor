import ffmpeg
from ffmpeg import Stream

from compress_settings import VideoCompressSettings
from source import SourceFile
from source_type import SourceType


def get_output_name(source: SourceFile, settings: VideoCompressSettings) -> str:
    new_name = source.filepath.stem + "_compressed"
    new_extension = source.filepath.suffix

    if settings.format_to_convert_to is not None:
        new_extension = settings.format_to_convert_to

    return new_name + new_extension

def compress(source: SourceFile, settings: VideoCompressSettings):
    temp = handle_compress(source, settings)

    if isinstance(temp, Stream):
        ffmpeg.run(temp)

def handle_compress(source: SourceFile, settings: VideoCompressSettings) -> ffmpeg.Stream | None:
    if not source.is_valid:
        raise Exception("Source is not valid")

    if source.type == SourceType.VIDEO:
        return get_compress_video_stream(source, settings)
    elif source.type == SourceType.AUDIO:
        pass
    elif source.type == SourceType.IMAGE:
        pass

    raise Exception("Unknown source type") # Should literally be impossible at this point.


def get_compress_video_stream(source: SourceFile, settings: VideoCompressSettings) -> Stream:
    stream = ffmpeg.input(source.filepath)

    # First handle the audio.
    audio = stream.audio

    # Then handle the video.
    video = stream.video

    if settings.fps is not None:
        ffmpeg.filter(video, 'fps', fps=settings.fps, round='up')

    # Then set output.
    output_params = {
        'video_bitrate': settings.video_bitrate,
        'audio_bitrate': settings.audio_bitrate,
        'format': settings.format_to_convert_to,
    }
    output_params = {k: v for k, v in output_params.items() if v is not None} # Filter out parameters that are None

    stream = ffmpeg.output(audio, video, get_output_name(source, settings), **output_params)

    return stream