import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import time

class LoadingScreen(tk.Toplevel):
    """ Demonstra um ecrã de carregamento para que o utilizador tenha contexto de espera. """
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Loading")
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        window_width = 300
        window_height = 150

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.resizable(False, False)
        
        self.label = tk.Label(self, text="Loading...", font="Arial 20")
        self.label.pack(pady=20)
        
        self.progress = ctk.CTkProgressBar(self, width=200, height=20)
        self.progress.pack(pady=10)
        self.progress.start()
        
        self.update()
        self.update_idletasks()

    

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    loading = LoadingScreen(root)
    root.mainloop()