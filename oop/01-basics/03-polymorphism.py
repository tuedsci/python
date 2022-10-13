# POLYMORPHISM

from pathlib import Path
from typing import ClassVar


# %% Declare a base class and derive two sub-classes
class AudioFile:
    ext: ClassVar[str]

    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath


class Mp3File(AudioFile):
    ext = ".mp3"

    def play(self):
        print(f"Playing {self.filepath} as MP3")


class WavFile(AudioFile):
    ext = ".wav"

    def play(self):
        print(f"Playing {self.filepath} as WAV")


# In the above example, AudioFile is the parent class,
# and it can access the class-level variable ext in the children
# inside __init__()
# Now we can test
m = Mp3File(Path("C:/music/Yesterday.mp3"))
w = WavFile(Path("C/music/Hello.wav"))
m.play()
w.play()
