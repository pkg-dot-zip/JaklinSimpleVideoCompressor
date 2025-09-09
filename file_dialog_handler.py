import pathlib
from tkinter import filedialog

import source_type


def select_file_from_file_dialog() -> pathlib.Path | None:
    filetypes = (
        ('All files', '*.*'),
        ('Video files', source_type.get_valid_filetypes_for_dialog(source_type.SourceType.VIDEO)),
        ('Image files', source_type.get_valid_filetypes_for_dialog(source_type.SourceType.IMAGE)),
        ('Audio files', source_type.get_valid_filetypes_for_dialog(source_type.SourceType.AUDIO)),
    )

    file_path = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if file_path is None:
        return None

    return pathlib.Path(file_path)