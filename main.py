from api import transcribe_file
from recorder import record
from time import sleep
import signal
import subprocess
import threading
import tkinter as tk
<<<<<<< HEAD

def ylr():
    return 'usdsgsgs'

def main():
    root = tk.Tk()
    root.title('LLApp')

    output = tk.Text(root, width=100, height=10)
    output.pack()

    output.insert('1.0', 'Press the Reccord and speak for 10 seconds.\n\nAfterwards please wait for finished recording text to appear.')

    start_button = tk.Button(root, text='Record', command=lambda: (record(), output.delete('1.0', 'end'),
                            output.insert('1.0', 'Recording done. Please wait for transcribe'), root.update(), 
                            output.delete('1.0', 'end'),  output.insert('1.0', transcribe_file('tmp.wav') + '\n\n Press Record to record again'), root.update()) )
    start_button.pack()
    
    root.mainloop()
=======
from gui import MyApp
from api import API
import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

def main():
    root = tk.Tk()
    api_key = 'YZD2ZA6BSWCKQGKJJZWXAICJTHUV3IXP'
    api = API(api_key)
    app = MyApp(api, master=root)
    app.mainloop()
>>>>>>> 9bb8b82eccdceb507684bc0499dc953f0500b32c

if __name__ == "__main__":
    main()
