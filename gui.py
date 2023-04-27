import tkinter as tk
from api import API

class MyApp(tk.Frame):
    def __init__(self, api, master=None):
        super().__init__(master)
        self.api = api
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title('Language Learning Assistant')

        # Record button
        self.record_button = tk.Button(self.master, text='Record', command=self.record_audio)
        self.record_button.grid(row=0, column=0, padx=5, pady=5)

        # Transcribed text
        self.transcribed_text = tk.StringVar()
        self.transcribed_label = tk.Label(self.master, textvariable=self.transcribed_text)
        self.transcribed_label.grid(row=1, column=0, padx=5, pady=5)

        # Correct answer
        self.correct_answer = tk.StringVar()
        self.correct_label = tk.Label(self.master, text="Correct Answer")
        self.correct_label.grid(row=2, column=0, padx=5, pady=5)
        self.correct_entry = tk.Entry(self.master, textvariable=self.correct_answer)
        self.correct_entry.grid(row=2, column=1, padx=5, pady=5)

        # Compare button
        self.compare_button = tk.Button(self.master, text='Compare', command=self.compare_texts)
        self.compare_button.grid(row=3, column=0, padx=5, pady=5)

        # Similarity score
        self.similarity_score = tk.StringVar()
        self.similarity_label = tk.Label(self.master, textvariable=self.similarity_score)
        self.similarity_label.grid(row=4, column=0, padx=5, pady=5)

    def record_audio(self):
        self.api.record_audio(5, 'recorded_audio.wav')
        transcribed_text = self.api.transcribe_audio('recorded_audio.wav')
        self.transcribed_text.set(transcribed_text)

    def compare_texts(self):
        transcribed_text = self.transcribed_text.get()
        correct_answer = self.correct_answer.get()
        similarity = self.api.compare_transcriptions(transcribed_text,
