from dataclasses import dataclass

@dataclass
class VideoCompressSettings:
    """Contains settings for compressing all video source files. Settings are optional if None by default."""
    fps: int = None
    video_bitrate: int = None
    audio_bitrate: int = None
    should_mute: bool = False # TODO: Implement.
    format_to_convert_to: str = None

# TODO: Implement.
@dataclass
class AudioCompressSettings:
    """Contains settings for compressing all audio source files. Settings are optional if None by default."""
    format_to_convert_to: str = None

# TODO: Implement.
@dataclass
class ImageCompressSettings:
    """Contains settings for compressing all image files. Settings are optional if None by default."""
    quality: int = None
    format_to_convert_to: str = None