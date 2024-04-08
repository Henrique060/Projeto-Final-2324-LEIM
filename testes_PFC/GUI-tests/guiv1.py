import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  

class GUI:
    width = 700
    height = 650
    window_size = f"{width}x{height}"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bul.Id v1")
        self.window.geometry(f"{self.window_size}")
        self.window.resizable(False, False)
        
        self.image = Image.open("testes_PFC\GUI-tests\pharmacy.png")
        image = self.image.resize((100, 100))
        image_res = ImageTk.PhotoImage(image)
        label_image = tk.Label(self.window, image=image_res, bg='#AFE9DE')
        label_image.place(x=500, y=0) 

        ## BACKGROUND
        self.window.configure(bg='#AFE9DE')
        
        ## TITLE
        self.title = tk.Label(self.window, text="Bul.Id", font=("Calibri", 60), 
                              anchor="w", justify="left", fg="#656866", bg='#AFE9DE', padx=25)
        self.title.grid(row=0, column=0, sticky="nw")


        ## MEDICAMENTO FIELD
        # Texto 
        self.title_medicamento = tk.Label(self.window, text="Medicamento *",
                                        font=("Calibri", 20), anchor="w", justify="left", fg="#656866", bg='#AFE9DE', padx=25).place(x=0, y=125)
        # Entry
        self.entry_medicamento = tk.Entry(self.window, font=("Calibri", 20), width=30).place(x=240, y=125)
       
       ## ALERGIA FIELD
        # Texto
        self.title_alergia = tk.Label(self.window, text="Alergias *",
                                        font=("Calibri", 20), anchor="w", justify="left", fg="#656866", bg='#AFE9DE', padx=25).place(x=0, y=175)
        # Entry
        self.entry_alergia = tk.Entry(self.window, font=("Calibri", 20), width=46).place(x=25, y=225)

        ## PRINCIPIO FIELD
        # Texto
        self.title_principio = tk.Label(self.window, text="Principios Ativos/Excipientes a Detetar *",
                                        font=("Calibri", 20), anchor="w", justify="left", fg="#656866", bg='#AFE9DE', padx=25).place(x=0, y=275)
        # Entry
        self.entry_principio = tk.Text(self.window, font=("Calibri", 20), width=46, height=3).place(x=25, y=325)

        ## OUTPUT FIELD
        # Texto
        self.title_output = tk.Label(self.window, text="Informação Resultante",
                                        font=("Calibri", 20), anchor="w", justify="left", fg="#656866", bg='#AFE9DE', padx=25).place(x=0, y=435)
        # Entry
        self.entry_output = tk.Text(self.window, font=("Calibri", 20), width=46, height=3, state="disabled").place(x=25, y=485)




       

        ## LOOP
        self.window.mainloop()

if __name__ == "__main__":
    gui = GUI()
    
