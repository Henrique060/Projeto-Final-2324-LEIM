import customtkinter
import tkinter
from PIL import Image, ImageTk

from bulid_test import ask_question, logic_test_v1

class AlergyApp(customtkinter.CTkFrame):
    def __init__(self, root, controller, model, med_name):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.med_name = med_name
        self.model = model
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
        # Title
        bul_id = customtkinter.CTkLabel(master=self,
                                        text="Bul.ID",
                                        width=400,
                                        height=100,
                                        text_color="#656866",
                                        fg_color=self.bg_color,
                                        bg_color=self.bg_color,
                                        font=("Roboto", 70))
        bul_id.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)

        # Subtitle
        id_title = customtkinter.CTkLabel(master=self,
                                          text="Identificador de Alegias e Intolerâncias em Bulas",
                                          width=400,
                                          height=50,
                                          text_color="#656866",
                                          fg_color=self.bg_color,
                                          bg_color=self.bg_color,
                                          font=("Roboto", 20))
        id_title.place(relx=0.55, rely=0.1, anchor=tkinter.CENTER)

        # Image
        image = customtkinter.CTkImage(Image.open("OOP_prototype/bulidtest/pharmacy.png"), size=(100, 100))
        image_label = customtkinter.CTkLabel(master=self,
                                             image=image,
                                             text="",
                                             width=100,
                                             bg_color=self.bg_color,
                                             height=100)
        image_label.place(relx=0.90, rely=0.1, anchor=tkinter.CENTER)

        # Alergy button
        alergy_button = customtkinter.CTkButton(master=self,
                                                text="Alergias",
                                                width=150,
                                                height=50,
                                                corner_radius=10,
                                                bg_color=self.bg_color,
                                                fg_color=self.btn_color,
                                                text_color="#484848",
                                                command=None,
                                                hover_color=self.sel_btn_color)
        alergy_button.place(relx=0.15, rely=0.2, anchor=tkinter.CENTER)

        # Principles button
        principles_button = customtkinter.CTkButton(master=self,
                                                    text="Princípios",
                                                    width=150,
                                                    height=50,
                                                    corner_radius=10,
                                                    bg_color=self.bg_color,
                                                    fg_color=self.btn_color,
                                                    text_color="#484848",
                                                    command=self.principios_change_activity,
                                                    hover_color=self.sel_btn_color)
        principles_button.place(relx=0.35, rely=0.2, anchor=tkinter.CENTER)

        # Outros button
        outros_button = customtkinter.CTkButton(master=self,
                                                text="Outros",
                                                width=150,
                                                height=50,
                                                corner_radius=10,
                                                bg_color=self.bg_color,
                                                fg_color=self.btn_color,
                                                text_color="#484848",
                                                command=self.outros_change_activity,
                                                hover_color=self.sel_btn_color)
        outros_button.place(relx=0.55, rely=0.2, anchor=tkinter.CENTER)

        # Labels and entry for Medicamento
        med_label = customtkinter.CTkLabel(master=self,
                                           text="Medicamento *",
                                           width=80,
                                           height=25,
                                           text_color=self.txt_color,
                                           fg_color=self.bg_color,
                                           bg_color=self.bg_color,
                                           font=("Roboto", 15),
                                           corner_radius=8)
        med_label.place(relx=0.12, rely=0.3, anchor=tkinter.CENTER)

        self.med_entry = customtkinter.CTkEntry(master=self,
                                                placeholder_text="Nome do Medicamento",
                                                width=800,
                                                height=25,
                                                text_color=self.txt_color,
                                                fg_color="white",
                                                bg_color=self.bg_color,
                                                border_width=0,
                                                corner_radius=10)
        self.med_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

        # Labels and buttons for Alergia
        alergy_label = customtkinter.CTkLabel(master=self,
                                              text="Alergia *",
                                              width=80,
                                              height=25,
                                              text_color=self.txt_color,
                                              fg_color=self.bg_color,
                                              bg_color=self.bg_color,
                                              font=("Roboto", 15),
                                              corner_radius=8)
        alergy_label.place(relx=0.1, rely=0.41, anchor=tkinter.CENTER)

        self.create_alergy_buttons()

        # Submit button
        submit_button = customtkinter.CTkButton(master=self,
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
        submit_button.place(relx=0.5, rely=0.73, anchor=tkinter.CENTER)

        # Result labels
        result_label = customtkinter.CTkLabel(master=self,
                                              text="Informação Resultante",
                                              width=80,
                                              height=25,
                                              text_color=self.txt_color,
                                              fg_color=self.bg_color,
                                              bg_color=self.bg_color,
                                              font=("Roboto", 15),
                                              corner_radius=8)
        result_label.place(relx=0.15, rely=0.8, anchor=tkinter.CENTER)

        self.output = customtkinter.CTkLabel(master=self,
                                             text="",
                                             width=800,
                                             height=100,
                                             text_color=self.txt_color,
                                             fg_color="white",
                                             bg_color=self.bg_color,
                                             font=("Roboto", 15),
                                             corner_radius=8)
        self.output.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


        ## Criar uma zona de output com texto que se adapta ao que é inserido
        self.query_output_label = customtkinter.CTkLabel(master=self,
                                                            text="Questão",
                                                            width=80,
                                                            height=25,
                                                            text_color=self.txt_color,
                                                            fg_color=self.bg_color,
                                                            bg_color=self.bg_color,
                                                            font=("Roboto", 15),
                                                            corner_radius=8)
        self.query_output_label.place(relx=0.1, rely=0.63, anchor=tkinter.CENTER)

        self.query_output = customtkinter.CTkLabel(master=self,
                                                    text="O <<MEDICAMENTO>> contém <<ALERGIA>>?",
                                                    width=800,
                                                    height=25,
                                                    text_color=self.txt_color,
                                                    fg_color="white",
                                                    bg_color=self.bg_color,
                                                    font=("Roboto", 15),
                                                    corner_radius=8)
        self.query_output.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)

    def create_alergy_buttons(self):
        alergy_buttons_info = [
            ("Lactose", 0.15, 0.475, self.lactose),
            ("Ovos", 0.15, 0.575, self.ovos),
            ("Frutos Secos", 0.35, 0.475, self.nuts),
            ("Penicilina", 0.35, 0.575, self.penicilina),
            ("Glúten", 0.55, 0.475, self.gluten),
            ("Soja", 0.55, 0.575, self.soja),
            ("Peixe", 0.75, 0.475, self.fish),
            ("Sulfitos", 0.75, 0.575, self.sulfitos),
        ]

        for (text, relx, rely, command) in alergy_buttons_info:
            button = customtkinter.CTkButton(master=self,
                                             text=text,
                                             width=150,
                                             height=50,
                                             corner_radius=10,
                                             bg_color=self.bg_color,
                                             fg_color="white",
                                             text_color=self.txt_color,
                                             command=command,
                                             hover_color=self.sel_btn_color)
            button.place(relx=relx, rely=rely, anchor=tkinter.CENTER)

    def submit_med_name(self):
        med_name = self.med_entry.get()
        print('Medicamento inserido:', med_name)
        return med_name

    def lactose(self):
        self.alergy_list.append('Lactose')

    def ovos(self):
        self.alergy_list.append('Ovos')

    def nuts(self):
        self.alergy_list.append('Frutos Secos')

    def penicilina(self):
        self.alergy_list.append('Penicilina')

    def gluten(self):
        self.alergy_list.append('Glúten')

    def soja(self):
        self.alergy_list.append('Soja')

    def fish(self):
        self.alergy_list.append('Peixe')

    def sulfitos(self):
        self.alergy_list.append('Sulfitos')

    def submit_alergy(self):
        print('Alergias:', self.alergy_list)
        return self.alergy_list

    def button_click(self):
        self.submit_med_name()
        self.submit_alergy()
        texto = f"O {self.medicamento_place()} contém {self.alergias_place()}?"
        self.query_output.configure(text=texto)
        model_answer = ask_question(texto, self.model)
        self.output.configure(text=model_answer)
        self.update()
        
     
    def principios_change_activity(self):
        self.controller.show_principios_app()

    def outros_change_activity(self):
        self.controller.show_outros_app()

    def medicamento_place(self):
        med_name = str(self.submit_med_name())
        return med_name
    
    def alergias_place(self):
        alergias = str(self.submit_alergy())
        return alergias
    
    def get_output_text(self):
        """ Esta função servirá como responsável por entregar ao modelo
            LLM o texto que foi inserido nos campos de texto. 
        """
        output_text = f'Medicamento: {self.medicamento_place()}\nAlergias: {self.alergias_place()}'
        #output_text(ask_question(output_text), self.root.model)
        #return output_text
    
    
