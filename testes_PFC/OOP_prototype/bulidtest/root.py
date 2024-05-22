import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
    
import logging
from guiv3_alergias import AlergyApp
from guiv3_principios import PrincipiosAPP
from guiv3_outros import OutrosAPP
from haystack.document_stores import InMemoryDocumentStore
from bulid_test import logic_load_dataset_bulid


class AppController:

    def __init__(self):
        self.root = ctk.CTkToplevel()
        #self.med_name = 'Brufen'

        self.root.title("BulID")
        
        # Initialize the model
        self.dataset, self.bulid = logic_load_dataset_bulid()


        self.current_app = None
        self.root.resizable(False, False)
        self.show_alergy_app()  # Call the method with parentheses

    def show_alergy_app(self):
        if self.current_app:  # Check if current_app exists before destroying it
            self.current_app.destroy()
        self.current_app = AlergyApp(self.root, self.bulid, self.dataset, self)
        self.current_app.pack(fill="both", expand=True)

    def show_principios_app(self):
        if self.current_app:  # Check if current_app exists before destroying it
            self.current_app.destroy()
        self.current_app = PrincipiosAPP(self.root, self)
        self.current_app.pack(fill="both", expand=True)
        

    def show_outros_app(self):
        if self.current_app:  # Check if current_app exists before destroying it
            self.current_app.destroy()
        self.current_app = OutrosAPP(self.root, self)
        self.current_app.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    controller = AppController()
    controller.run()
