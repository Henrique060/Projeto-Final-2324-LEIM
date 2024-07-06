import pyrebase
import customtkinter as ctk
import tkinter
from tkinter import messagebox
from GUI.root import AppController
from GUI.loading_screen.loading import LoadingScreen

class Main:
    """ Executa o sistema inteiro do BulID, desde o login até à aplicação principal.

        É aqui que se encontra a lógica do login e do registo.

        A aplicação principal é iniciada na aba "Alergias", caso o login
        seja feito com sucesso.

        Podem ser modificados aqui os parâmetros do Firebase caso necessário.

        Pode ser iniciada a app sem login mas não permite que os dados
        sejam descarragados ou sequer carregados para a base de dados Firebase.
    """
    def __init__(self):
        self.root = ctk.CTkToplevel()
        load = LoadingScreen(self.root)
        self.fireBaseConfig = {
            "apiKey": "AIzaSyDOhQqt7TvCNTUq8HhJdFP4JoMkXM43SVg",
            "authDomain": "bulidtest.firebaseapp.com",
            "projectId": "bulidtest",
            "databaseURL": "https://console.firebase.google.com/project/bulidtest/database/bulidtest-default-rtdb/data/~2F",
            "storageBucket": "bulidtest.appspot.com",
            "messagingSenderId": "516788987739",
            "appId": "1:516788987739:web:23d1791d0b3380b2a9dc7e",
            "measurementId": "G-GE9F8EHH2W"
        }
        self.firebase = pyrebase.initialize_app(self.fireBaseConfig)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.session = None
        self.user_id = None
        load.destroy()
        self.setup_ui()
        

    def setup_ui(self):
        """ Cria a interface gráfica."""
        self.root.geometry("600x600")
        self.root.title("BulID")
        self.root.resizable(False, False)
        self.root.configure(fg_color="#AFE9DE")

        self.bg_color = "#AFE9DE"
        self.btn_color = "#FFF3D4"
        self.sel_btn_color = "#FFF598"
        self.txt_color = "#656565"

        self.help_button = ctk.CTkButton(master=self.root,
                                            text="?",
                                            width=20,
                                            height=20,
                                            corner_radius=10,
                                            font=("Roboto", 16, "bold"),
                                            fg_color=self.btn_color,
                                            text_color=self.txt_color,
                                            command=self.help,
                                            hover_color=self.sel_btn_color)
        self.help_button.place(relx=0.9, rely=0.1, anchor=tkinter.CENTER)
       
        self.bul_id = ctk.CTkLabel(master=self.root,
                                            text="Bul.ID",
                                            width=400,
                                            height=100,
                                            text_color="#656866",
                                            fg_color=self.bg_color,
                                            bg_color=self.bg_color,
                                            font=("Roboto", 80, "bold"))
        
        self.bul_id.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.id_title = ctk.CTkLabel(master=self.root,
                                          text="Identificador de Alegias e Intolerâncias em Bulas",
                                          width=400,
                                          height=50,
                                          text_color="#656866",
                                          fg_color=self.bg_color,
                                          bg_color=self.bg_color,
                                          font=("Roboto", 20, "italic"))
        self.id_title.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)

        self.username = ctk.CTkLabel(master=self.root,
                                  text="E-mail:",
                                  width=80,
                                  height=25,
                                  text_color=self.txt_color,
                                  fg_color=self.bg_color,
                                  font=("Roboto", 16),
                                  corner_radius=8)
        self.username.place(relx=0.21, rely=0.35, anchor=tkinter.CENTER)

        self.password = ctk.CTkLabel(master=self.root,
                                            text="Password:",
                                            width=80,
                                            height=25,
                                            text_color=self.txt_color,
                                            font=("Roboto", 16),
                                            fg_color=self.bg_color,
                                            corner_radius=8)
        self.password.place(relx=0.23, rely=0.55, anchor=tkinter.CENTER)

        self.username_entry = ctk.CTkEntry(master=self.root,
                                                placeholder_text="Inserir e-mail",
                                                width=400,
                                                height=35,
                                                text_color=self.txt_color,
                                                fg_color="white",
                                                border_width=0,
                                                corner_radius=10)
        self.username_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


        self.password_entry = ctk.CTkEntry(master=self.root,
                                                placeholder_text="Inserir password",
                                                width=400,
                                                height=35,
                                                fg_color="white",
                                                text_color=self.txt_color,
                                                show="*",
                                                border_width=0,
                                                corner_radius=10)
        self.password_entry.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


        self.login_button = ctk.CTkButton(master=self.root,
                                                text="Entrar",
                                                width=80,
                                                height=32,
                                                corner_radius=8,
                                                font=("Roboto", 16),
                                                fg_color=self.btn_color,
                                                text_color=self.txt_color,
                                                command=self.log_in, ## função de login
                                                hover_color=self.sel_btn_color)
        self.login_button.place(relx=0.4, rely=0.7, anchor=tkinter.CENTER)


        self.signup_button = ctk.CTkButton(master=self.root,
                                                width=80,
                                                height=32,
                                                text="Registar",
                                                command=self.sign_up,
                                                fg_color=self.btn_color,
                                                font=("Roboto", 16),
                                                corner_radius=8,
                                                text_color=self.txt_color,
                                                hover_color=self.sel_btn_color)
        self.signup_button.place(relx=0.6, rely=0.7, anchor=tkinter.CENTER)

        self.enter_no_login = ctk.CTkButton(master=self.root,
                                        text="Clique para usar sem registo",
                                        width=120,
                                        height=25,
                                        text_color=self.txt_color,
                                        font=("Roboto", 16),
                                        fg_color=self.btn_color,
                                        command=self.enter_no_login,
                                        corner_radius=8,
                                        hover_color=self.sel_btn_color)
        self.enter_no_login.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)



    def sign_up(self):
        """ Gere a lógica de registo.

            Precisa de ser uma password e email válidos já que o campo é de email e password.

            Caso o registo seja bem sucedido, é enviado um email de verificação para o email do utilizador.

            Caso contrário, é mostrada uma mensagem de erro.
        """
        email = self.username_entry.get()
        password = self.password_entry.get()

        if(email == "" or password == ""):
            print("Email or Password is empty")
            messagebox.showinfo("BulID", "Por favor preencha todos os campos")

        if(email != "" and password != ""):
            # Não pode estar vazio o campo e a pass tem 
            #   de ser igual ou maior que 6 caracteres
            if len(password) < 6:
                print("Password too short")
                messagebox.showinfo("BulID", "Password demasiado curta")
                return
            
            else:
                # Regista o user com email e password
                try:
                    token = self.auth.create_user_with_email_and_password(email, password)
                    print("Register Successful")
                    messagebox.showinfo("BulID", "Registo bem sucedido")
                    print(token['idToken'])

                    try:
                        self.auth.send_email_verification(token['idToken'])
                        print("Verification Email Sent")
                        messagebox.showinfo("BulID", "Email de verificação enviado")

                    except Exception as e:
                        print("Verification Email Failed")
                        messagebox.showinfo("BulID", "Email de verificação falhou")
                        print(e)

                except Exception as e:
                    print("Register Failed")
                    print(e)


    def log_in(self):
        """ Gere a lógica de login. 

            Necessita dos tokens de autenticação caso a conta exista, ou seja, caso
            esteja o user registado no programa (e, consequentemente, na base de dados).

            É necessário que estejam preenchidos todos os campos.

            Caso o login seja bem sucedido, o utilizador é redirecionado para a aplicação principal,
            iniciando na aba "ALergias".
        """
        email = self.username_entry.get()
        password = self.password_entry.get()

        if(email == "" or password == ""):
            print("Email or Password is empty")
            messagebox.showinfo("BulID", "Por favor preencha todos os campos")

        if(email != "" and password != ""):
            try:
                # Login com email e password
                self.session = self.auth.sign_in_with_email_and_password(email, password)
                user_info = self.auth.get_account_info(self.session['idToken']) # Obter informação do utilizador com base no seu token
                self.user_id = user_info['users'][0]['localId']
                
                # Verificar se o email está verificado
                if user_info['users'][0]['emailVerified']:
                    print("Email Verified")
                    messagebox.showinfo("BulID", "Login bem sucedido")
                    self.root.destroy()
                    app = AppController(self.session, self.firebase, self.db, self.user_id)
                    
                else:
                    print("Email Not Verified")
                    messagebox.showinfo("BulID", "Email não verificado")
                    

            except Exception as e:
                print("Email Not Verified")
                print(e)
                messagebox.showinfo("BulID", "Conta não encontrada. Por favor registe-se.")

    
    def enter_no_login(self):
        """ Nesta função, o utilizador pode entrar sem fazer login.
            A sessão está definida a "None".
        """
        self.root.destroy()
        app = AppController(self.session, self.firebase, self.db, self.user_id)

    
    def help(self):
        """ Função que mostra uma mensagem de ajuda ao utilizador. """
        messagebox.showinfo("BulID", "Bem-vindo ao BulID, o identificador de alergias e intolerâncias em bulas de medicamentos! \
                            \n Este programa de literacia farmacêutica permite introduzir medicamentos e obter informações diretamente das bulas de forma prática e rápida, \
                            sem que seja necessário lê-las. \n \
                            Registe-se para que as suas pesquisas sejam guardadas e possa aceder sempre que necessitar. É apenas necessário e-mail e password (6+ dígitos). \n \
                            Caso contrário, também pode usar o programa sem registo, sem guardar as suas pesquisas para acesso futuro.")


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    main = Main()
    main.run()