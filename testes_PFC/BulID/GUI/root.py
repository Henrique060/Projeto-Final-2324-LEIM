import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
    

from GUI.guiv3_1_alergias import AlergyApp
from GUI.guiv3_principios import PrincipiosAPP
from GUI.guiv3_outros import OutrosAPP
from lib.bulid_man.bulid import BulID
from GUI.loading_screen.loading import LoadingScreen

class AppController:
    """ Gere a lógica base, passando elementos de sessão e do modelo, 
        para as classes que dependem desta.
        
        Permite que as abas do Bul.ID sejam iniciadas e controladas.

        Inica sempre o programa na aba de alergias, a aba principal.
    """

    def __init__(self, session, firebase, db, user_id):
        self.root = ctk.CTkToplevel()
        load = LoadingScreen(self.root) # Inicia o loading screen

        self.session = session
        self.firebase = firebase
        self.db = db
        self.user_id = user_id

        self.cred = credentials.Certificate("GUI/bulid_firestore.json")
        self.fb_app = firebase_admin.initialize_app(self.cred)
        self.firestore = firestore.client()
        self.doc_ref = self.firestore.collection("users").document(self.user_id)
        
        self.root.title("BulID")
        self.bul_id_interface = BulID()
        self.root.geometry("0x0+500+100")

        self.dataset, self.bulid = self.bul_id_interface.logic_load_dataset_bulid()
        load.destroy()

        self.current_app = None
        self.root.resizable(False, False)
        self.show_alergy_app()

    def show_alergy_app(self):
        """ Muda a aba para "alergias"."""
        if self.current_app:
            self.current_app.destroy()
        self.current_app = AlergyApp(self.root, self.bulid, self.dataset, self.session, self.db, 
                                     self.user_id, self.firestore, self.doc_ref, self)
        self.current_app.pack(fill="both", expand=True)

    def show_principios_app(self):
        """ Muda a aba para "principios"."""
        if self.current_app:
            self.current_app.destroy()
        self.current_app = PrincipiosAPP(self.root, self.bulid, self.dataset, self.session, self.db, 
                                     self.user_id, self.firestore, self.doc_ref, self)
        self.current_app.pack(fill="both", expand=True)
        

    def show_outros_app(self):
        """ Muda a aba para "outros"."""
        if self.current_app:  
            self.current_app.destroy()
        self.current_app = OutrosAPP(self.root, self.bulid, self.dataset, self.session, self.db, 
                                     self.user_id, self.firestore, self.doc_ref, self)
        self.current_app.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()
