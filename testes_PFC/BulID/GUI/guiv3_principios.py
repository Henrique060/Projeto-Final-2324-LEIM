import customtkinter as ctk
import tkinter
from tkinter import messagebox
from PIL import Image
import json

from lib.bulid_man.bulid import BulID

class PrincipiosAPP(ctk.CTkFrame):
    """ Aba de princípios ativos do Bul.ID.
    
        Permite ao utilizador inserir o nome de um medicamento, princípio ativo e excipiente 
        de modo a detetar se tais estão presentes no medicamento.
        
        Faz gestão das alergias e submissão de dados, carregamento e descarregamento do Firebase.
    """

    def __init__(self, root, model, dataset, session, db, user_id, 
                 firestore_client, doc_ref, controller):
        super().__init__(root)
        self.root = root
        self.dataset = dataset
        self.model = model
        self.session = session
        self.db = db
        self.user_id = user_id
        self.controller = controller
        self.root.geometry("900x700")
        self.configure(fg_color="#AFE9DE")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.alergy_list = []

        self.bg_color = "#AFE9DE"
        self.txt_color = "#656565"
        self.btn_color = "#FFF3D4"
        self.sel_btn_color = "#FFF598"

        self.bul_id_interface = BulID()

        self.firestore = firestore_client
        self.doc_ref = doc_ref

        self.setup_ui()

    def setup_ui(self):
        """ Configura a interface gráfica da aba de princípios ativos. """
        bul_id = ctk.CTkLabel(master=self,
                              text="Bul.ID",
                              width=400,
                              height=100,
                              text_color="#656866",
                              fg_color=self.bg_color,
                              bg_color=self.bg_color,
                              font=("Roboto", 70))
        bul_id.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)

        id_title = ctk.CTkLabel(master=self,
                                text="Identificador de Alegias e Intolerâncias em Bulas",
                                width=400,
                                height=50,
                                text_color="#656866",
                                fg_color=self.bg_color,
                                bg_color=self.bg_color,
                                font=("Roboto", 20))
        id_title.place(relx=0.55, rely=0.1, anchor=tkinter.CENTER)

        image = ctk.CTkImage(Image.open("imgs/pharmacy.png"), size=(100, 100))
        image_label = ctk.CTkLabel(master=self,
                                   image=image,
                                   text="",
                                   width=100,
                                   bg_color=self.bg_color,
                                   height=100)
        image_label.place(relx=0.90, rely=0.1, anchor=tkinter.CENTER)

        self.account_button = ctk.CTkButton(master=self,
                                                    text="Descarregar Dados",
                                                    width=130,
                                                    height=50,
                                                    corner_radius=10,
                                                    bg_color=self.bg_color,
                                                    fg_color=self.btn_color,
                                                    text_color="#484848",
                                                    command=self.download_button_click,
                                                    hover_color=self.sel_btn_color)
        self.account_button.place(relx=0.90, rely=0.2, anchor=tkinter.CENTER)

        self.create_button("Alergias", 0.15, 0.21, self.alergias_change_activity)
        self.create_button("Princípios", 0.35, 0.21, None)
        self.create_button("Outros", 0.55, 0.21, self.outros_change_activity)

        self.create_label("Medicamento *", 0.13, 0.3)
        self.med_entry = self.create_entry("Nome do Medicamento", 0.5, 0.35)

        self.create_label("Princípio Ativo *", 0.13, 0.4)
        self.principios_entry = self.create_entry("Principio Ativo", 0.5, 0.45)

        self.create_label("Excipiente", 0.11, 0.5)
        self.excipiente_entry = self.create_entry("Excipiente", 0.5, 0.55)

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

        self.query_output_label = ctk.CTkLabel(master=self,
                                                            text="Questão",
                                                            width=80,
                                                            height=25,
                                                            text_color=self.txt_color,
                                                            fg_color=self.bg_color,
                                                            bg_color=self.bg_color,
                                                            font=("Roboto", 15),
                                                            corner_radius=8)
        self.query_output_label.place(relx=0.1, rely=0.59, anchor=tkinter.CENTER)

        self.query_output = ctk.CTkLabel(master=self,
                                                    text="O <<MEDICAMENTO>> contém o <<PRINCIPIO ATIVO>> e <<EXCIPIENTE>>?",
                                                    width=800,
                                                    height=25,
                                                    text_color=self.txt_color,
                                                    fg_color="white",
                                                    bg_color=self.bg_color,
                                                    font=("Roboto", 15),
                                                    corner_radius=8)
        self.query_output.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

        self.output = ctk.CTkTextbox(master=self,
                                                    width=800,
                                                    height=100,
                                                    text_color=self.txt_color,
                                                    fg_color="white",
                                                    bg_color=self.bg_color,
                                                    font=("Roboto", 15),
                                                    corner_radius=8)
        self.output.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    def create_button(self, text, relx, rely, command):
        """ Cria um botão na interface, de acordo com os parâmetros fornecidos."""
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
        """ Cria uma label na interface, de acordo com os parâmetros fornecidos."""
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
        """ Cria uma entry na interface, de acordo com os parâmetros fornecidos."""
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
        """ Verifica se o campo do medicamento foi preenchido e retorna o valor inserido."""
        if self.med_entry.get() == "":
            messagebox.showerror("Erro", "Por favor preencha o campo do medicamento")
        else:
            med_name = self.med_entry.get()
            print('Medicamento inserido:', med_name)
            return med_name
    
    def submit_principio_name(self):
        """ Verifica se o campo do princípio ativo foi preenchido e retorna o valor inserido."""
        if self.principios_entry.get() == "":
            messagebox.showerror("Erro", "Por favor preencha o campo do princípio ativo")
        else:
            principio_name = self.principios_entry.get()
            print('Principio Ativo: ', principio_name)
            return principio_name
    
    def submit_excipiente_name(self):
        """ Verifica se o campo do excipiente foi preenchido e retorna o valor inserido."""
        if self.excipiente_entry.get() == "":
            return None
        else:
            excipiente_name = self.excipiente_entry.get()
            print('Excipiente inserido:', excipiente_name)
            return excipiente_name

    def button_click(self):
        """ Usada para submissão de dados.

            Precisa de verificar quais os campos preenchidos de modo a conseguir construir
            a interrogação correta para o modelo linguístico.

            Inicia o RAG e submete a questão ao modelo.
        """
        self.submit_med_name()
        self.submit_principio_name()
        self.submit_excipiente_name()

        if self.submit_med_name() == "" or self.submit_principio_name() == "":
            self.output.configure(text="Por favor preencha todos os campos obrigatórios")
            return
        
        if self.submit_excipiente_name() == None:
            texto = f"O medicamento {self.submit_med_name()} contém o princípio ativo {self.submit_principio_name()}?"
            self.query_output.configure(text=texto)
            print(texto)
        else:
            texto = f"O medicamento {self.submit_med_name()} contém o princípio ativo {self.submit_principio_name()} e o excipiente {self.submit_excipiente_name()}?"
            self.query_output.configure(text=texto)
            print(texto)

        nome_medicamento = self.medicamento_place()
        self.save_principios_to_firebase(nome_medicamento)

        rag = self.bul_id_interface.logic_load_rag(nome_medicamento)
        response = self.bul_id_interface.ask_question(texto, rag)

        self.output.insert("0.0", response)
        self.save_processed_information_to_firebase(nome_medicamento, response)




        med_name = self.submit_med_name()
        print("Submitted Medication:", med_name)

    def medicamento_place(self):
        """ Retorna o nome do medicamento inserido pelo utilizador."""
        med_name = str(self.submit_med_name())
        return med_name
    
    def principio_name(self):
        """ Retorna o nome do princípio ativo inserido pelo utilizador."""
        princip_name = str(self.submit_principio_name())
        return princip_name
    
    def excipiente_name(self):
        """ Retorna o nome do excipiente inserido pelo utilizador."""
        excip_name = str(self.submit_excipiente_name())
        return excip_name




    def alergias_change_activity(self):
        """ Muda a atividade para a aba de alergias."""
        self.controller.show_alergy_app()
    
    def outros_change_activity(self):
        """ Muda a atividade para a aba de outros."""
        self.controller.show_outros_app()

    def save_principios_to_firebase(self, medication_name):
        """ Guarda os princípios ativos e excipientes no Firebase."""
        user_id = self.get_user_id()  
        principios = self.principio_name()  
        excipientes = self.excipiente_name()  
        self.firestore.collection('users').document(user_id).collection('medications').document(medication_name).set({'principios': principios}, merge=True)
        self.firestore.collection('users').document(user_id).collection('medications').document(medication_name).set({'excipiente': excipientes}, merge=True)

    def save_processed_information_to_firebase(self, medication_name, response):
        """ Guarda a informação processada no Firebase."""
        user_id = self.get_user_id()  
        self.firestore.collection('users').document(user_id).collection('medications').document(medication_name).set({'resposta_principios': response}, merge=True)

    def get_user_id(self):
        """ Retorna o ID do utilizador."""
        return self.user_id

    def fetch_data_from_firestore(self):
        """ Busca os dados do Firebase."""
        user_id = self.get_user_id()
        medications_ref = self.firestore.collection('users').document(user_id).collection('medications')
        medications = medications_ref.stream()
        
        medications_dict = {}
        for med in medications:
            medications_dict[med.id] = med.to_dict()

        return medications_dict
        
    def convert_data_to_json(self, data):
        """ Converte os dados para JSON."""
        return json.dumps(data, indent=4, ensure_ascii=False)

    def save_json_to_file(self, json_data, file_path):
        """ Guarda os dados num ficheiro JSON."""
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

    def download_button_click(self):
        """ Lida com o clique no botão de descarregamento."""
        if self.get_user_id() == "":
            messagebox.showerror("Erro", "Por favor faça login para descarregar os dados.")
            return
        else:
            data = self.fetch_data_from_firestore()
            if data:
                json_data = self.convert_data_to_json(data)
                file_path = f"informação_do_user.json"
                self.save_json_to_file(json_data, file_path)
                print(f"Data saved to {file_path}")
                messagebox.showinfo("Sucesso", "Os dados foram descarregados com sucesso.")
            else:
                print("No data found for the specified medication.")
