import librosa
import io
import pydub
import numpy as np
import soundfile as sf


class Song:
    def __init__(self, filelike):
        """Creates a Song object.
        """

        self.waveform = None
        self.sr = None
        self.bytes = filelike

        self.load_from_filelike(filelike, "wav")
        # self.process_song()

        # Features
        self.tempo = None
        self.beat_frames = None

        self.detect_tempo()

    def load_from_filelike(self, filelike, extension: str):
        """Filelike to librosa."""

        if extension == "mp3":
            a = pydub.AudioSegment.from_mp3(filelike)
        elif extension == "wav":
            a = pydub.AudioSegment.from_wav(filelike)
        else:
            raise ValueError("Wrong extension: Format not supported.")

        # Converting to float32 for librosa
        waveform = np.array(a.get_array_of_samples())

        if a.channels == 2:
            waveform = waveform.reshape((-1, 2)).astype('float32')

        a.export("data/new.mp3", format="mp3")

        self.waveform = waveform
        self.sr = a.frame_rate*2

    def process_song(self):
        """Removes silence at the beginning of the song.
        """

        self.waveform, _ = librosa.effects.trim(self.waveform)

    def detect_tempo(self):
        """Detects tempo of a track.
        """

        if (self.sr is None) or (self.waveform is None):
            raise ValueError("No song was loaded.")

        # Detect tempo
        self.tempo, self.beat_frames = librosa.beat.beat_track(
            y=self.waveform, sr=self.sr
        )


data_song = io.BytesIO(open("data/examplesong.wav", "rb").read())
beat = Song(data_song)
print(round(beat.tempo, 0))

sf.write("data/processedfile.wav", beat.waveform, beat.sr)
