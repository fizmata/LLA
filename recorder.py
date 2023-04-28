#!/usr/bin/env python3
import time
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

samplerate = 44100  # Set the sample rate
channels = 1  # Set the number of channels

q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def record():
    try:
        filename = './tmp.wav'
        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='w', samplerate=samplerate,
                        channels=channels) as file:
            with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
                # print('#' * 80)
                print('recording for 10 seconds...')
                # print('#' * 80)
                time.sleep(10)  # Record for 10 seconds
                while not q.empty():
                    file.write(q.get())
    except Exception as e:
        sys.exit(type(e).__name__ + ': ' + str(e))

    # print('Recording finished: ' + repr(filename))
