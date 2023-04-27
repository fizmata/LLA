import tkinter as tk
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

if __name__ == "__main__":
    main()
