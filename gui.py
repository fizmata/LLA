import tkinter as tk
from api import API

class MyApp(tk.Frame):
    def __init__(self, api, master=None):
        super().__init__(master)
        self.api = api
        self.master = master
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.master.title('Language Learning Assistant')

        # Record button
        self.record_button = tk.Button(self, text='Record', command=self.record_audio)
        self.record_button.grid(row=0, column=0, padx=5, pady=5)
        
        # Save to file button
        self.save_button = tk.Button(self, text='Save to File', command=self.save_results_to_file)
        self.save_button.grid(row=0, column=5, padx=5, pady=5)

        # Transcribed text
        self.transcribed_text = tk.StringVar()
        self.transcribed_label = tk.Label(self, textvariable=self.transcribed_text)
        self.transcribed_label.grid(row=1, column=0, padx=5, pady=5)

        # Correct answer
        self.correct_answer = tk.StringVar()
        self.correct_label = tk.Label(self.master, text="Correct Answer", fg="white", bg="black")
        self.correct_label.grid(row=0, column=2, padx=5, pady=5)
        self.correct_entry = tk.Entry(self.master, textvariable=self.correct_answer, fg="white", bg="black")
        self.correct_entry.grid(row=0, column=3, padx=5, pady=5)

        # Compare button
        self.compare_button = tk.Button(self, text='Compare', command=self.compare_texts)
        self.compare_button.grid(row=3, column=0, padx=5, pady=5)

        # Similarity score
        self.similarity_score = tk.StringVar()
        self.similarity_label = tk.Label(self, textvariable=self.similarity_score)
        self.similarity_label.grid(row=4, column=0, padx=5, pady=5)

    def record_audio(self):
        self.api.record_audio(5, 'recorded_audio.wav')
        transcribed_text = self.api.transcribe_audio('recorded_audio.wav')
        self.transcribed_text.set(transcribed_text)

    def compare_texts(self):
        transcribed_text = self.transcribed_text.get()
        correct_answer = self.correct_answer.get()
        similarity = self.api.compare_transcriptions(transcribed_text, correct_answer)
        similarity_percentage = round(similarity * 100, 2)
        result_text = f"Similarity: {similarity_percentage}%"

        # Display results in a new window
        result_window = tk.Toplevel(self.master)
        result_window.title("Results")
        result_label = tk.Label(result_window, text=result_text)
        result_label.pack(padx=20, pady=20)
        
    def save_results_to_file(self):
        transcribed_text = self.transcribed_text.get()
        correct_answer = self.correct_answer.get()
        similarity = self.api.compare_transcriptions(transcribed_text, correct_answer)
        similarity_percentage = round(similarity * 100, 2)

        with open('results.txt', 'w') as f:
            f.write(f"Transcribed text: {transcribed_text}\n")
            f.write(f"Correct answer: {correct_answer}\n")
            f.write(f"Similarity: {similarity_percentage}%\n")

        print("Results saved to 'results.txt'")


