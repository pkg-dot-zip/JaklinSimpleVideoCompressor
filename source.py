import pathlib

from source_type import calc_source_type


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
