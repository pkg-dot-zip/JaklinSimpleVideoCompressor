from dataclasses import dataclass

@dataclass
class CompressSettings:
    """Contains settings for compressing all source files. Settings are optional if None by default."""
    fps: int = None
    video_bitrate: int = None
    audio_bitrate: int = None
    should_mute: bool = False # TODO: Implement.
    format_to_convert_to: str = None
