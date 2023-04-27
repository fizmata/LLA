import tkinter as tk
from gui import MyApp
from api import API

def main():
    root = tk.Tk()
    api_key = 'YZD2ZA6BSWCKQGKJJZWXAICJTHUV3IXP'
    api = API(api_key)
    app = MyApp(api, root)
    root.mainloop()

if __name__ == "__main__":
    main()
