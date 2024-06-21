import customtkinter
import tkinter
from PIL import Image, ImageTk

from bulid_test import ask_question, logic_load_rag

class AlergyApp(customtkinter.CTkFrame):

    def __init__(self, root, model, dataset, session, db, user_id, controller):
        super().__init__(root)
        self.root = root
        self.dataset = dataset
        self.controller = controller
        self.session = session
        self.db = db
        self.user_id = user_id
        self.model = model


        ## O mesmo dicionario mas por ordem alfabética
        self.allergies = {
            "Ácido Acetilsalicílico": False,
            "Amido": False,
            "Benzoatos": False,
            "Carbamazepina": False,
            "Corantes": False,
            "Crustáceos": False,
            "Fenitoína": False,
            "Frutos Secos": False,
            "Glúten": False,
            "Ibuprofeno": False,
            "Lactose": False,
            "Latex": False,
            "Lidocaína": False,
            "Metilisotiazolinona": False,
            "Mostarda": False,
            "Naxoproxeno": False,
            "Ovos": False,
            "Parabenos": False,
            "Penicilina": False,
            "Peixe": False,
            "Sacarina": False,
            "Soja": False,
            "Sulfitos": False,
            "Sulfonamidas": False,
            "Tiomersal": False
        }

        self.alergy_list = []

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

        self.account_button = customtkinter.CTkButton(master=self,
                                                    text="Conta",
                                                    width=100,
                                                    height=50,
                                                    corner_radius=10,
                                                    bg_color=self.bg_color,
                                                    fg_color=self.btn_color,
                                                    text_color="#484848",
                                                    command=None,
                                                    hover_color=self.sel_btn_color)
        self.account_button.place(relx=0.80, rely=0.1, anchor=tkinter.CENTER)

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

        # Labels and dropdown for Alergia
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

        # Dropdown menu for allergies
        self.alergy_dropdown = customtkinter.CTkOptionMenu(master=self,
                                                           values=list(self.allergies.keys()),
                                                           width=200,
                                                           height=25,
                                                           text_color=self.txt_color,
                                                           fg_color="white",
                                                           bg_color=self.bg_color,
                                                           command=self.select_alergy)
        self.alergy_dropdown.place(relx=0.3, rely=0.41, anchor=tkinter.CENTER)

        # Selected allergies display
        self.selected_allergies_label = customtkinter.CTkLabel(master=self,
                                                               text="",
                                                               width=400,
                                                               height=25,
                                                               text_color=self.txt_color,
                                                               fg_color="white",
                                                               bg_color=self.bg_color,
                                                               font=("Roboto", 15),
                                                               corner_radius=8)
        self.selected_allergies_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Clear allergies button
        clear_button = customtkinter.CTkButton(master=self,
                                               text="Clear Allergies",
                                               width=150,
                                               height=50,
                                               corner_radius=10,
                                               bg_color=self.bg_color,
                                               fg_color=self.btn_color,
                                               text_color=self.txt_color,
                                               command=self.clear_allergies,
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
                                                   text="O <<MEDICAMENTO>> contém <<ALERGIA>>?",
                                                   width=800,
                                                   height=25,
                                                   text_color=self.txt_color,
                                                   fg_color="white",
                                                   bg_color=self.bg_color,
                                                   font=("Roboto", 15),
                                                   corner_radius=8)
        self.query_output.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)

    def select_alergy(self, selection):
        if selection not in self.alergy_list and self.session is None:
            self.alergy_list.append(selection)
            self.update_selected_allergies_label()
        
        if selection not in self.alergy_list and self.session is not None:
            self.alergy_list.append(selection)

            

    def update_selected_allergies_label(self):
        self.selected_allergies_label.configure(text=", ".join(self.alergy_list))

    def clear_allergies(self):
        self.alergy_list = []
        self.update_selected_allergies_label()

    def save_allergies_to_firebase(self):
        try:
            self.db.child("users").child(self.user_id).child("allergies").set(self.alergy_list)
            print("Allergies saved to Firebase.")
        except Exception as e:
            print(f"An error occurred: {e}")    

    def submit_med_name(self):
        self.med_name = self.med_entry.get()
        print('Medicamento inserido:', self.med_name)
        return self.med_name

    def submit_alergy(self):
        print('Alergias:', self.alergy_list)
        return self.alergy_list

    def button_click(self):
        self.submit_med_name()
        self.submit_alergy()
        texto = f"O {self.medicamento_place()} contém {self.alergias_place()}?"
        self.query_output.configure(text=texto)
        self.save_allergies_to_firebase()

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
    
    def alergias_place(self):
        alergias = str(self.submit_alergy())
        return alergias

    def get_output_text(self):
        output_text = f'Medicamento: {self.medicamento_place()}\nAlergias: {self.alergias_place()}'

# Example usage:
# root = customtkinter.CTk()
# app = AlergyApp(root, model, dataset, controller)
# root.mainloop()
