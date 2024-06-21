## build a simple loading screen in custom Tkinter

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import time

class LoadingScreen(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Loading")
        
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Set window width and height
        window_width = 300
        window_height = 150
        
        # Calculate x and y coordinates for centering the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        # Set the geometry of the window
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.resizable(False, False)
        
        self.label = tk.Label(self, text="Loading...", font="Arial 20")
        self.label.pack(pady=20)
        
        self.progress = ctk.CTkProgressBar(self, width=200, height=20)
        self.progress.pack(pady=10)
        self.progress.start()
        
        ## Update the window to reflect changes
        self.update()
        self.update_idletasks()

    

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    loading = LoadingScreen(root)
    root.mainloop()