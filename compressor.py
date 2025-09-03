from dataclasses import dataclass

from source import SourceFile

@dataclass
class CompressSettings:
    

def compress(source: SourceFile):
    if not source.is_valid:
        raise Exception("Source is not valid")