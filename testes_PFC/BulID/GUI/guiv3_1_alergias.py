import customtkinter
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json

from lib.bulid_man.bulid import BulID

class AlergyApp(customtkinter.CTkFrame):
    """ Aba de alergias do Bul.ID. 
    
        Permite ao utilizador inserir o nome de um medicamento e selecionar alergias 
        de modo a detetar se tais estão presentes no medicamento.
        
        Faz gestão das alergias e submissão de dados, carregamento e descarregamento do Firebase.
    """

    def __init__(self, root, model, dataset, session, db, user_id, 
                 firestore_client, doc_ref, controller):
        super().__init__(root)
        self.root = root
        self.dataset = dataset
        self.controller = controller
        self.session = session
        self.db = db
        self.user_id = user_id
        self.model = model
        self.bul_id_interface = BulID()

        self.firestore = firestore_client
        self.doc_ref = doc_ref

        # Inicia-se um dicionário de alergias para modularização
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

        self.alergy_list = [] # Para guardar as alergias selecionadas

        window_width = 900
        window_height = 700
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.configure(fg_color="#AFE9DE")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.bg_color = "#AFE9DE"
        self.txt_color = "#656565"
        self.btn_color = "#FFF3D4"
        self.sel_btn_color = "#FFF598"

        self.setup_ui()

    def setup_ui(self):
        """ Configura a interface gráfica."""
        bul_id = customtkinter.CTkLabel(master=self,
                                        text="Bul.ID",
                                        width=400,
                                        height=100,
                                        text_color="#656866",
                                        fg_color=self.bg_color,
                                        bg_color=self.bg_color,
                                        font=("Roboto", 70))
        bul_id.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)


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
                                                    text="Descarregar Dados",
                                                    width=130,
                                                    height=50,
                                                    corner_radius=10,
                                                    bg_color=self.bg_color,
                                                    fg_color=self.btn_color,
                                                    text_color="#484848",
                                                    command=self.download_button_click,
                                                    hover_color=self.sel_btn_color)
        self.account_button.place(relx=0.90, rely=0.21, anchor=tkinter.CENTER)


        image = customtkinter.CTkImage(Image.open("imgs/pharmacy.png"), size=(100, 100))
        image_label = customtkinter.CTkLabel(master=self,
                                             image=image,
                                             text="",
                                             width=100,
                                             bg_color=self.bg_color,
                                             height=100)
        image_label.place(relx=0.90, rely=0.1, anchor=tkinter.CENTER)


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
        alergy_button.place(relx=0.15, rely=0.21, anchor=tkinter.CENTER)


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
        principles_button.place(relx=0.35, rely=0.21, anchor=tkinter.CENTER)


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
        outros_button.place(relx=0.55, rely=0.21, anchor=tkinter.CENTER)


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
                                              text="Alergia *",
                                              width=80,
                                              height=25,
                                              text_color=self.txt_color,
                                              fg_color=self.bg_color,
                                              bg_color=self.bg_color,
                                              font=("Roboto", 15),
                                              corner_radius=8)
        alergy_label.place(relx=0.1, rely=0.41, anchor=tkinter.CENTER)

        
        self.alergy_dropdown = customtkinter.CTkOptionMenu(master=self,
                                                           values=list(self.allergies.keys()),
                                                           width=200,
                                                           height=25,
                                                           text_color=self.txt_color,
                                                           fg_color="white",
                                                           bg_color=self.bg_color,
                                                           command=self.select_alergy)
        self.alergy_dropdown.place(relx=0.3, rely=0.41, anchor=tkinter.CENTER)

        
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

        
        clear_button = customtkinter.CTkButton(master=self,
                                               text="Limpar Alergias",
                                               width=150,
                                               height=50,
                                               corner_radius=10,
                                               bg_color=self.bg_color,
                                               fg_color=self.btn_color,
                                               text_color=self.txt_color,
                                               command=self.clear_allergies,
                                               hover_color=self.sel_btn_color)
        clear_button.place(relx=0.7, rely=0.41, anchor=tkinter.CENTER)

       
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

        

        self.output = customtkinter.CTkTextbox(master=self,
                                                    width=800,
                                                    height=100,
                                                    text_color=self.txt_color,
                                                    fg_color="white",
                                                    bg_color=self.bg_color,
                                                    font=("Roboto", 15),
                                                    corner_radius=8)
        self.output.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        
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
        """ Adiciona a alergia selecionada à lista de alergias."""
        if selection not in self.alergy_list:
            self.alergy_list.append(selection)
            self.update_selected_allergies_label()
             

    def update_selected_allergies_label(self):
        """ Atualiza a label de lista com as alergias selecionadas."""
        self.selected_allergies_label.configure(text=", ".join(self.alergy_list))
        self.selected_allergies_label.update_idletasks()

    def clear_allergies(self):
        """ Limpa a lista de alergias."""
        self.alergy_list = []
        self.update_selected_allergies_label()

    def save_allergies_to_firebase(self):
        """ Guarda as alergias selecionadas na base de dados Firebase."""
        try:
            self.db.child("users").child(self.user_id).child("allergies").set(self.alergy_list)
            print("Allergies saved to Firebase.")
        except Exception as e:
            print(f"An error occurred: {e}")    

    def submit_med_name(self):
        """ Verifica se o campo de nome do medicamento está preenchido e retorna para uso."""
        if self.med_entry.get() == "":
            messagebox.showerror("Erro", "Por favor insira o nome do medicamento.")
        else:
            self.med_name = self.med_entry.get()
            print('Medicamento inserido:', self.med_name)
            return self.med_name.lower()

    def submit_alergy(self):
        """ Verifica se a lista de alergias está preenchida e retorna para uso."""
        if len(self.alergy_list) == 0:
            messagebox.showerror("Erro", "Por favor selecione pelo menos uma alergia.")
        else:
            print('Alergias:', self.alergy_list)
            return self.alergy_list

    def button_click(self):
        """ Usada para submissão de dados. Vai buscar o nome do medicamento e as alergias,
            constrói o texto da questão e submete à base de dados Firebase.
            
            Inicia o RAG e submete a questão ao modelo.
        """
        self.submit_med_name()
        self.submit_alergy()
        texto = f"O {self.medicamento_place()} contém {self.alergias_place()}?"
        self.query_output.configure(text=texto)

        nome_medicamento = self.medicamento_place()
        self.save_allergies_to_firebase(nome_medicamento)
        
        rag = self.bul_id_interface.logic_load_rag(nome_medicamento)
        response = self.bul_id_interface.ask_question(texto, rag)
        print(f"Resposta: {response}")
        self.output.insert("0.0", response) 
        self.save_processed_information_to_firebase(nome_medicamento, response)

    

    def principios_change_activity(self):
        """ Muda a aba para "princípios"."""
        self.controller.show_principios_app()

    def outros_change_activity(self):
        """ Muda a aba para "outros"."""
        self.controller.show_outros_app()

    def medicamento_place(self):
        """ Retorna o nome do medicamento inserido."""
        med_name = str(self.submit_med_name())
        return med_name
    
    def alergias_place(self):
        """ Retorna a lista de alergias selecionadas."""
        alergias = str(self.submit_alergy())
        return alergias


    def save_allergies_to_firebase(self, medication_name):
        """ Guarda as alergias selecionadas na base de dados Firebase."""
        user_id = self.get_user_id()  
        allergies = self.alergias_place()  
        self.firestore.collection('users').document(user_id).collection('medications').document(medication_name).set({'alergias': allergies}, merge=True)

    def save_processed_information_to_firebase(self, medication_name, response):
        """ Guarda a resposta obtida na base de dados Firebase."""
        user_id = self.get_user_id()  
        self.firestore.collection('users').document(user_id).collection('medications').document(medication_name).set({'resposta_alergias': response}, merge=True)

    def get_user_id(self):
        """ Retorna o ID do utilizador."""
        return self.user_id

    def fetch_data_from_firestore(self):
        """ Busca os dados da base de dados Firestore."""
        user_id = self.get_user_id()
        medications_ref = self.firestore.collection('users').document(user_id).collection('medications')
        medications = medications_ref.stream()
        
        medications_dict = {}
        for med in medications:
            medications_dict[med.id] = med.to_dict()
    
        return medications_dict
            
    def convert_data_to_json(self, data):
        """ Converte os dados para JSON. Utilizado para a exportação de dados vindos do Firestore."""
        return json.dumps(data, indent=4, ensure_ascii=False)
    
    def save_json_to_file(self, json_data, file_path):
        """ Guarda os dados num ficheiro JSON."""
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)
    
    def download_button_click(self):
        """ Função associada ao botão de descarregar dados para obter dados da conta."""
        data = self.fetch_data_from_firestore()
        if data:
            json_data = self.convert_data_to_json(data)
            file_path = f"informação_do_user.json"
            self.save_json_to_file(json_data, file_path)
            messagebox.showinfo("Sucesso", "Os dados foram descarregados com sucesso.")
        else:
            messagebox.showerror("Erro", "Não existem dados para descarregar.")