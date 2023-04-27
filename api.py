# This module handles API requests and responses
from textdistance import levenshtein as edit_distance
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from wit import Wit
import pyaudio

class API:
    def __init__(self, api_key):
        self.client = Wit(api_key)

    def record_audio(self, duration, filename):
        sample_rate = 16000
        device_name = 'MacBook Pro Microphone'

        # Initialize PyAudio
        pa = pyaudio.PyAudio()

        # Find the device index
        device_index = None
        for idx in range(pa.get_device_count()):
            info = pa.get_device_info_by_index(idx)
            if info['name'] == device_name:
                device_index = idx
                break

        if device_index is None:
            print("Error: Unable to find the specified device.")
            return

        # Start recording
        stream = pa.open(format=pyaudio.paInt16,
                         channels=1,
                         rate=sample_rate,
                         input=True,
                         input_device_index=device_index,
                         frames_per_buffer=1024)

        print("Recording...")

        audio_frames = []

        for _ in range(0, int(sample_rate / 1024 * duration)):
            data = stream.read(1024)
            audio_frames.append(np.frombuffer(data, dtype=np.int16))

        # Stop recording
        stream.stop_stream()
        stream.close()
        pa.terminate()

        audio = np.hstack(audio_frames)
        write(filename, sample_rate, audio)

        print("Recording finished.")

    def transcribe_audio(self, audio_file):
        with open(audio_file, 'rb') as f:
            response = self.client.speech(f, {'Content-Type': 'audio/wav'})
        try:
            return response['text']
        except KeyError:
            return "No speech detected"

    def compare_transcriptions(self, transcribed_text, correct_answer):
        distance = edit_distance(transcribed_text, correct_answer)
        if len(transcribed_text) == 0 and len(correct_answer) == 0:
            similarity = 1.0
        else:
            similarity = 1 - distance / \
                max(len(transcribed_text), len(correct_answer))
        return similarity

    def list_devices():
        print(sd.query_devices())
