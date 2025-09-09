from enum import Enum

import compress_settings
from compress_settings import VideoCompressSettings


class Quality(Enum):
    CATASTROPHIC = 0
    TERRIBLE = 1
    BARELY_WATCHABLE = 2
    MWEH = 3
    TOLERABLE = 4
    COULD_BE_WORSE = 5

    def get_readable_name(self) -> str:
        return str(self.value) + ' - ' + self.name.replace('_', ' ').title()

    @staticmethod
    def get_from_readable_name(string: str):
        raise NotImplementedError


def get_video_settings(quality: Quality) -> compress_settings.VideoCompressSettings:
    if quality == Quality.CATASTROPHIC:
        return VideoCompressSettings(fps=10,
                                     video_bitrate=200,
                                     audio_bitrate=200)
    elif quality == Quality.TERRIBLE:
        return VideoCompressSettings(fps=20,
                                     video_bitrate=1000,
                                     audio_bitrate=1000)
    elif quality == Quality.BARELY_WATCHABLE:
        return VideoCompressSettings(fps=30,
                                     video_bitrate=1200)
    elif quality == Quality.MWEH:
        return VideoCompressSettings(fps=40,
                                     video_bitrate=2000)
    elif quality == Quality.TOLERABLE:
        return VideoCompressSettings(fps=60,
                                     video_bitrate=3000)
    elif quality == Quality.COULD_BE_WORSE:
        return VideoCompressSettings(fps=60,
                                     video_bitrate=4000)
    raise NotImplementedError
