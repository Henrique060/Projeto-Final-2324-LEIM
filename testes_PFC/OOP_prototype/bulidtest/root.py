import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
    
import logging
#from guiv3_alergias import AlergyApp
from guiv3_1_alergias import AlergyApp
from guiv3_principios import PrincipiosAPP
from guiv3_outros import OutrosAPP
from haystack.document_stores import InMemoryDocumentStore
from bulid_test import logic_load_dataset_bulid
from loading import LoadingScreen

class AppController:

    def __init__(self, session, firebase, db, user_id):
        self.root = ctk.CTkToplevel()
        load = LoadingScreen(self.root)
        #self.med_name = 'Brufen'
        # import loadingscreen

        self.session = session
        self.firebase = firebase
        self.db = db
        self.user_id = user_id
        
        self.root.title("BulID")
        
        self.root.geometry("0x0+500+100")
        # Initialize the model
        self.dataset, self.bulid = logic_load_dataset_bulid()
        load.destroy()

        self.current_app = None
        self.root.resizable(False, False)
        self.show_alergy_app()  # Call the method with parentheses

    def show_alergy_app(self):
        if self.current_app:  # Check if current_app exists before destroying it
            self.current_app.destroy()
        self.current_app = AlergyApp(self.root, self.bulid, self.dataset, self.session, self.db, self.user_id, self)
        self.current_app.pack(fill="both", expand=True)

    def show_principios_app(self):
        if self.current_app:  # Check if current_app exists before destroying it
            self.current_app.destroy()
        self.current_app = PrincipiosAPP(self.root, self.bulid, self.dataset, self.session, self.db, self.user_id, self)
        self.current_app.pack(fill="both", expand=True)
        

    def show_outros_app(self):
        if self.current_app:  # Check if current_app exists before destroying it
            self.current_app.destroy()
        self.current_app = OutrosAPP(self.root, self.bulid, self.dataset, self.session, self.db, self.user_id, self)
        self.current_app.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()

