import librosa


class Song:
    def __init__(self, path):
        """Creates a Song object.
        """

        self.waveform = None
        self.sr = None

        self.load_track(path)

        # Features

        self.tempo = None
        self.beat_frames = None

        self.detect_tempo()

    def load_track(self, path):
        """Loads a song based on a file path.
        """
        self.waveform, self.sr = librosa.load(path)

    def detect_tempo(self):
        """Detects tempo of a track.
        """

        if (self.sr is None) or (self.waveform is None):
            raise ValueError("No song was loaded.")

        self.tempo, self.beat_frames = librosa.beat.beat_track(
            y=self.waveform, sr=self.sr
        )


beat = Song("data/mirage.mp3")
print(beat.tempo)
