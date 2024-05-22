import customtkinter
import tkinter
from PIL import Image


class OutrosAPP(customtkinter.CTkFrame):
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
        # TITLE
        bul_id = customtkinter.CTkLabel(master=self,
                                        text="Bul.ID",
                                        width=400,
                                        height=100,
                                        text_color="#656866",
                                        fg_color=self.bg_color,
                                        bg_color=self.bg_color,
                                        font=("Roboto", 70))
        bul_id.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)

        # SUBTITLE
        id_title = customtkinter.CTkLabel(master=self,
                                          text="Identificador de Alegias e Intolerâncias em Bulas",
                                          width=400,
                                          height=50,
                                          text_color="#656866",
                                          fg_color=self.bg_color,
                                          bg_color=self.bg_color,
                                          font=("Roboto", 20))
        id_title.place(relx=0.55, rely=0.1, anchor=tkinter.CENTER)

        # IMAGE
        image = customtkinter.CTkImage(Image.open("OOP_prototype/bulidtest/pharmacy.png"), size=(100, 100))
        image_label = customtkinter.CTkLabel(master=self,
                                             image=image,
                                             text="",
                                             width=100,
                                             bg_color=self.bg_color,
                                             height=100)
        image_label.place(relx=0.90, rely=0.1, anchor=tkinter.CENTER)

        # BUTTONS
        self.create_button("Alergias", 0.15, 0.2, self.alergias_change_activity)
        self.create_button("Princípios", 0.35, 0.2, self.principios_change_activity)
        self.create_button("Outros", 0.55, 0.2, self.dummy_function)

        # MEDICAMENTO
        self.create_label("Medicamento *", 0.13, 0.3)
        self.med_entry = self.create_entry("Nome do Medicamento", 0.5, 0.35)

        # ALERGIA
        self.create_label("Condições Especiais *", 0.15, 0.4)

        # Allergy and condition buttons
        self.create_button("Lactose", 0.15, 0.475, lambda: self.add_alergy("Lactose"))
        self.create_button("Ovos", 0.15, 0.575, lambda: self.add_alergy("Ovos"))
        self.create_button("Frutos Secos", 0.5, 0.475, lambda: self.add_alergy("Frutos Secos"))
        self.create_button("Penicilina", 0.5, 0.575, lambda: self.add_alergy("Penicilina"))
        self.create_button("Glúten", 0.85, 0.475, lambda: self.add_alergy("Glúten"))
        self.create_button("Soja", 0.85, 0.575, lambda: self.add_alergy("Soja"))

        # SUBMIT BUTTON
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
        submit_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        # RESULT LABEL
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

        # OUTPUT
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

    def create_button(self, text, relx, rely, command):
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

    def create_label(self, text, relx, rely):
        label = customtkinter.CTkLabel(master=self,
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
        entry = customtkinter.CTkEntry(master=self,
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

    def add_alergy(self, alergy):
        if alergy not in self.alergy_list:
            self.alergy_list.append(alergy)
            print(f'Alergia adicionada: {alergy}')

    def submit_med_name(self):
        med_name = self.med_entry.get()
        print('Medicamento inserido:', med_name)
        return med_name

    def submit_alergy(self):
        print('Alergias:', self.alergy_list)
        return self.alergy_list

    def button_click(self):
        med_name = self.submit_med_name()
        alergias = self.submit_alergy()
        output_text = f'Medicamento: {med_name}\nAlergias: {", ".join(alergias)}'
        self.output.configure(text=output_text)

    def dummy_function(self):
        pass

    def alergias_change_activity(self):
        self.destroy()
        self.controller.show_alergy_app()

    def principios_change_activity(self):
        self.destroy()
        self.controller.show_principios_app()

