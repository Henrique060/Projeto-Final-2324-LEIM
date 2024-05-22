import customtkinter as ctk
import tkinter
from PIL import Image

class PrincipiosAPP(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.root.geometry("900x700")
        self.configure(fg_color="#AFE9DE")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.alergy_list = []

        self.bg_color = "#AFE9DE"
        self.txt_color = "#656565"
        self.btn_color = "#FFF3D4"
        self.sel_btn_color = "#FFF598"

        self.setup_ui()

    def setup_ui(self):
        ## TITLE
        bul_id = ctk.CTkLabel(master=self,
                              text="Bul.ID",
                              width=400,
                              height=100,
                              text_color="#656866",
                              fg_color=self.bg_color,
                              bg_color=self.bg_color,
                              font=("Roboto", 70))
        bul_id.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)

        ## SUBTITLE
        id_title = ctk.CTkLabel(master=self,
                                text="Identificador de Alegias e Intolerâncias em Bulas",
                                width=400,
                                height=50,
                                text_color="#656866",
                                fg_color=self.bg_color,
                                bg_color=self.bg_color,
                                font=("Roboto", 20))
        id_title.place(relx=0.55, rely=0.1, anchor=tkinter.CENTER)

        ## IMAGEM
        image = ctk.CTkImage(Image.open("OOP_prototype/bulidtest/pharmacy.png"), size=(100, 100))
        image_label = ctk.CTkLabel(master=self,
                                   image=image,
                                   text="",
                                   width=100,
                                   bg_color=self.bg_color,
                                   height=100)
        image_label.place(relx=0.90, rely=0.1, anchor=tkinter.CENTER)

        ## BUTTONS
        self.create_button("Alergias", 0.15, 0.2, self.alergias_change_activity)
        self.create_button("Princípios", 0.35, 0.2, None)
        self.create_button("Outros", 0.55, 0.2, self.outros_change_activity)

        ## MEDICAMENTO
        self.create_label("Medicamento *", 0.13, 0.3)
        self.med_entry = self.create_entry("Nome do Medicamento", 0.5, 0.35)

        ## PRINCIPIOS ATIVOS
        self.create_label("Princípio Ativo *", 0.13, 0.4)
        self.principios_entry = self.create_entry("Principio Ativo", 0.5, 0.45)

        ## EXCIPIENTE
        self.create_label("Excipiente", 0.11, 0.5)
        self.excipiente_entry = self.create_entry("Excipiente", 0.5, 0.55)

        ## SUBMIT BUTTON
        submit_button = ctk.CTkButton(master=self,
                                      text="Submeter",
                                      width=150,
                                      height=50,
                                      corner_radius=10,
                                      bg_color=self.bg_color,
                                      fg_color=self.btn_color,
                                      text_color=self.txt_color,
                                      font=("Roboto", 15),
                                      command=self.button_click,
                                      hover_color=self.sel_btn_color)
        submit_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        ## RESULT LABEL
        result_label = ctk.CTkLabel(master=self,
                                    text="Informação Resultante",
                                    width=80,
                                    height=25,
                                    text_color=self.txt_color,
                                    fg_color=self.bg_color,
                                    bg_color=self.bg_color,
                                    font=("Roboto", 15),
                                    corner_radius=8)
        result_label.place(relx=0.15, rely=0.8, anchor=tkinter.CENTER)

        ## OUTPUT
        self.output = ctk.CTkLabel(master=self,
                                   text="",
                                   width=800,
                                   height=100,
                                   text_color=self.txt_color,
                                   fg_color="white",
                                   bg_color=self.bg_color,
                                   font=("Roboto", 15),
                                   corner_radius=8)
        self.output.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    def create_button(self, text, relx, rely, command):
        button = ctk.CTkButton(master=self,
                               text=text,
                               width=150,
                               height=50,
                               corner_radius=10,
                               bg_color=self.bg_color,
                               fg_color=self.btn_color,
                               text_color="#484848",
                               command=command,
                               hover_color=self.sel_btn_color)
        button.place(relx=relx, rely=rely, anchor=tkinter.CENTER)

    def create_label(self, text, relx, rely):
        label = ctk.CTkLabel(master=self,
                             text=text,
                             width=80,
                             height=25,
                             text_color=self.txt_color,
                             fg_color=self.bg_color,
                             bg_color=self.bg_color,
                             font=("Roboto", 15),
                             corner_radius=8)
        label.place(relx=relx, rely=rely, anchor=tkinter.CENTER)

    def create_entry(self, placeholder, relx, rely):
        entry = ctk.CTkEntry(master=self,
                             placeholder_text=placeholder,
                             width=800,
                             height=25,
                             text_color=self.txt_color,
                             fg_color="white",
                             bg_color=self.bg_color,
                             border_width=0,
                             corner_radius=10)
        entry.place(relx=relx, rely=rely, anchor=tkinter.CENTER)
        return entry

    def submit_med_name(self):
        med_name = self.med_entry.get()
        print('Medicamento inserido:', med_name)
        return med_name

    def button_click(self):
        med_name = self.submit_med_name()
        print("Submitted Medication:", med_name)
        # Further logic to handle the entries from self.principios_entry and self.excipiente_entry

    def alergias_change_activity(self):
        self.controller.show_alergy_app()
    
    def outros_change_activity(self):
        self.controller.show_outros_app()
