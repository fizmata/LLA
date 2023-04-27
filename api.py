# This module handles API requests and responses
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from wit import Wit
import Levenshtein

class API:
    def __init__(self, api_key):
        self.client = Wit(api_key)

    def record_audio(self, duration, filename):
        sample_rate = 16000
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
        sd.wait()
        write(filename, sample_rate, audio)

    def transcribe_audio(self, audio_file):
        with open(audio_file, 'rb') as f:
            response = self.client.post_speech(f, content_type='audio/wav')
        try:
            return response['text']
        except KeyError:
            return "No speech detected"

    def compare_transcriptions(self, transcribed_text, correct_answer):
        distance = Levenshtein.distance(transcribed_text, correct_answer)
        similarity = 1 - distance / max(len(transcribed_text), len(correct_answer))
        return similarity
