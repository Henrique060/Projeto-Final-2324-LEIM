import customtkinter
import tkinter
from PIL import Image, ImageTk

from bulid_test import ask_question, logic_load_rag

class OutrosAPP(customtkinter.CTkFrame):

    def __init__(self, root, model, dataset, session, db, user_id, controller):
        super().__init__(root)
        self.root = root
        self.dataset = dataset
        self.session = session
        self.db = db
        self.user_id = user_id
        self.controller = controller
        self.model = model


        ## O mesmo dicionario mas por ordem alfabética
        self.condicoes = {
            "Sonolência": False,
            "Náuseas": False,
            "Vómitos": False,
            "Dores de cabeça": False,
            "Dores de estômago": False,
            "Dores musculares": False,
            "Tonturas": False,
            "Menstruação": False,
            "Memória": False,
            "Apetite": False,
            "Peso": False,
            "Pressão arterial": False,
            "Condução": False,
            "Gravidez": False,
            "Amamentação": False,
            "Maquinaria pesada": False,
            "Crianças": False,
            "Idade avançada (idosos)": False,
        }

        self.condicoes_list = []

        # Define the desired width and height of the window
        window_width = 900
        window_height = 700
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate x and y coordinates for centering the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        # Set the geometry of the window
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.configure(fg_color="#AFE9DE")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

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

       
        alergy_label = customtkinter.CTkLabel(master=self,
                                              text="Condição Especial *",
                                              width=80,
                                              height=25,
                                              text_color=self.txt_color,
                                              fg_color=self.bg_color,
                                              bg_color=self.bg_color,
                                              font=("Roboto", 15),
                                              corner_radius=8)
        alergy_label.place(relx=0.1, rely=0.41, anchor=tkinter.CENTER)

        
        self.condicoes_dropdown = customtkinter.CTkOptionMenu(master=self,
                                                           values=list(self.condicoes.keys()),
                                                           width=200,
                                                           height=25,
                                                           text_color=self.txt_color,
                                                           fg_color="white",
                                                           bg_color=self.bg_color,
                                                           command=self.select_condicao)
        self.condicoes_dropdown.place(relx=0.3, rely=0.41, anchor=tkinter.CENTER)

        
        self.condicoes_dropdown_label = customtkinter.CTkLabel(master=self,
                                                               text="",
                                                               width=400,
                                                               height=25,
                                                               text_color=self.txt_color,
                                                               fg_color="white",
                                                               bg_color=self.bg_color,
                                                               font=("Roboto", 15),
                                                               corner_radius=8)
        self.condicoes_dropdown_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        
        clear_button = customtkinter.CTkButton(master=self,
                                               text="Limpar Condições",
                                               width=150,
                                               height=50,
                                               corner_radius=10,
                                               bg_color=self.bg_color,
                                               fg_color=self.btn_color,
                                               text_color=self.txt_color,
                                               command=self.clear_condicoes,
                                               hover_color=self.sel_btn_color)
        clear_button.place(relx=0.7, rely=0.41, anchor=tkinter.CENTER)

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

        """self.output = customtkinter.CTkLabel(master=self,
                                             text="",
                                             width=800,
                                             height=100,
                                             text_color=self.txt_color,
                                             fg_color="white",
                                             bg_color=self.bg_color,
                                             font=("Roboto", 15),
                                             corner_radius=8)
        self.output.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)"""

        self.output = customtkinter.CTkTextbox(master=self,
                                                    width=800,
                                                    height=100,
                                                    text_color=self.txt_color,
                                                    fg_color="white",
                                                    bg_color=self.bg_color,
                                                    font=("Roboto", 15),
                                                    corner_radius=8)
        self.output.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        # Query output labels
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
                                                   text="O <<MEDICAMENTO>> causa interferência com <<CONDIÇÕES>>?",
                                                   width=800,
                                                   height=25,
                                                   text_color=self.txt_color,
                                                   fg_color="white",
                                                   bg_color=self.bg_color,
                                                   font=("Roboto", 15),
                                                   corner_radius=8)
        self.query_output.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)

    def select_condicao(self, selection):
        if selection not in self.condicoes_list:
            self.condicoes_list.append(selection)
            self.update_selected_condicoes_label()

    def update_selected_condicoes_label(self):
        self.condicoes_dropdown_label.configure(text=", ".join(self.condicoes_list))

    def clear_condicoes(self):
        self.condicoes_list = []
        self.update_selected_condicoes_label()

    def submit_med_name(self):
        self.med_name = self.med_entry.get()
        print('Medicamento inserido:', self.med_name)
        return self.med_name

    def submit_condicoes(self):
        print('Condições:', self.condicoes_list)
        return self.condicoes_list

    def button_click(self):
        self.submit_med_name()
        self.submit_condicoes()
        texto = f"O {self.medicamento_place()} causa interferência com {self.condicoes_place()}?"
        self.query_output.configure(text=texto)

        nome_medicamento = self.medicamento_place()
        rag = logic_load_rag(self.dataset, self.model, nome_medicamento)
        response = ask_question(texto, rag)
        print(f"Resposta: {response}")
        self.output.insert("0.0", response) 

    def principios_change_activity(self):
        self.controller.show_principios_app()

    def outros_change_activity(self):
        self.controller.show_outros_app()

    def medicamento_place(self):
        med_name = str(self.submit_med_name())
        return med_name
    
    def condicoes_place(self):
        condicoes = str(self.submit_condicoes())
        return condicoes

    def get_output_text(self):
        output_text = f'Medicamento: {self.medicamento_place()}\Condições: {self.condicoes_place()}'

# Example usage:
# root = customtkinter.CTk()
# app = AlergyApp(root, model, dataset, controller)
# root.mainloop()
