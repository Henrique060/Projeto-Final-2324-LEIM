import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  
from bulid_test import logic_test_v1

class GUI:
    width = 700
    height = 650
    window_size = f"{width}x{height}"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bul.Id v1")
        self.window.geometry(f"{self.window_size}")
        self.window.resizable(False, False)
        
        self.image = Image.open("testes_PFC\OOP_prototype\bulidtest\pharmacy.png")
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
        self.entry_medicamento = tk.Entry(self.window, font=("Calibri", 20), width=30)
        self.entry_medicamento.place(x=240, y=125)
        self.entry_medicamento.bind("<Return>", self.medicamento_enter)

        
        
       ## ALERGIA FIELD
        # Texto
        self.title_alergia = tk.Label(self.window, text="Alergias *",
                                        font=("Calibri", 20), anchor="w", justify="left", fg="#656866", bg='#AFE9DE', padx=25).place(x=0, y=175)
        # Entry
        self.entry_alergia = tk.Entry(self.window, font=("Calibri", 20), width=46)
        self.entry_alergia.place(x=25, y=225)
        self.entry_alergia.bind("<Return>", self.alergia_enter)

        ## PRINCIPIO FIELD
        # Texto
        self.title_principio = tk.Label(self.window, text="Principios Ativos/Excipientes a Detetar *",
                                        font=("Calibri", 20), anchor="w", justify="left", fg="#656866", bg='#AFE9DE', padx=25).place(x=0, y=275)
        # Entry
        self.entry_principio = tk.Text(self.window, font=("Calibri", 20), width=46, height=3)
        self.entry_principio.place(x=25, y=325)
        self.entry_principio.bind("<Return>", self.principio_enter)

        ## OUTPUT FIELD
        # Texto
        self.title_output = tk.Label(self.window, text="Informação Resultante",
                                        font=("Calibri", 20), anchor="w", justify="left", fg="#656866", bg='#AFE9DE', padx=25).place(x=0, y=435)
        # Entry
        self.entry_output = tk.Text(self.window, font=("Calibri", 20), width=46, height=3, state="disabled").place(x=25, y=485)

        ## LOOP
        self.window.mainloop()

    def medicamento_enter(self, event):
        return self.entry_medicamento.get()

    def alergia_enter(self, event):
        return self.entry_alergia.get()
    
    def principio_enter(self, event):
         return self.entry_principio.get()
       
    def load_bul_id_logic(self, question):
        logic_test_v1(self.principio_enter)
        

if __name__ == "__main__":
    gui = GUI()
    
