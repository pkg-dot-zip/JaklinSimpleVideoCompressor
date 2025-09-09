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
        """
        Returns readable name for combobox usage by returning digit 'x', followed by a hyphen (/ score), and then the name without underscores.
        So that CATASTROPHIC becomes '0 - CATASTROPHIC'.
        """

        return str(self.value) + ' - ' + self.name.replace('_', ' ').title()

    @staticmethod
    def get_from_readable_name(string: str):
        """
        Basically returns the corresponding Quality enum value from readable name retrieved from get_readable_name.
        Assumes the name is formatted correctly so this is bad code.
        """
        return Quality(int(string[0]))

def get_video_settings(quality: Quality) -> compress_settings.VideoCompressSettings:
    if quality == Quality.CATASTROPHIC:
        return VideoCompressSettings(fps=10,
                                     video_bitrate=200 * 1000,
                                     audio_bitrate=500 * 1000)
    elif quality == Quality.TERRIBLE:
        return VideoCompressSettings(fps=20,
                                     video_bitrate=1000 * 1000,
                                     audio_bitrate=1000 * 1000)
    elif quality == Quality.BARELY_WATCHABLE:
        return VideoCompressSettings(fps=30,
                                     video_bitrate=1200 * 1000)
    elif quality == Quality.MWEH:
        return VideoCompressSettings(fps=40,
                                     video_bitrate=2000 * 1000)
    elif quality == Quality.TOLERABLE:
        return VideoCompressSettings(fps=60,
                                     video_bitrate=3000 * 1000)
    elif quality == Quality.COULD_BE_WORSE:
        return VideoCompressSettings(fps=60,
                                     video_bitrate=4000 * 1000)
    raise NotImplementedError
