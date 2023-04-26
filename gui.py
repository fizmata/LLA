import tkinter as tk

class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # Define your GUI widgets here
        # self.pack()
        master.title('LLApp')
        
        random_label = tk.Label(master, text='Random')
        random_label.grid(row=0, column=0, padx=5, pady=5)
        random_entry = tk.Entry(master)
        random_entry.grid(row=0, column=1, padx=5, pady=5)

