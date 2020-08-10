import librosa


class Song:
    def __init__(self, path):
        """Creates a Song object.
        """

        self.waveform = None
        self.sr = None

        self.load_track(path)
        self.process_song()

        # Features
        self.tempo = None
        self.beat_frames = None

        self.detect_tempo()

    def load_track(self, path):
        """Loads a song based on a file path.
        """

        self.waveform, self.sr = librosa.load(path)

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

        


beat = Song("data/examplesong.wav")
print(round(beat.tempo, 0))
