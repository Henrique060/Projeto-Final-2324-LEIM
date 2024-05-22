## USAR CUSTOM TKINTER

import customtkinter
import tkinter
from PIL import Image, ImageTk



# Submeter nome do medicamento
def submit_med_name():
    #med_name = med_entry.get()
    #output.configure(text=f"Medicamento: {med_name}")
    #print('Medicamento inserido:', med_name)
    #return med_name
    return 





def create_alergia_app():
  from guiv2_alergias import create_window_alergias
  create_window_alergias()

def create_outros_app():
  from guiv2_outros import create_window_outros
  create_window_outros()

def create_principios_app():
      
  ##CORES
  bg_color = "#AFE9DE"
  txt_color = "#656565"
  btn_color = "#FFF3D4"
  sel_btn_color  = "#FFF598"

  ## APP EM SI
  alergy_app = customtkinter.CTkToplevel()
  alergy_app.geometry("900x700")
  # set background color
  alergy_app.config(bg="#AFE9DE")



  ## TITLE
  bul_id = customtkinter.CTkLabel(master=alergy_app,
                                  text="Bul.ID",
                                  width=400,
                                  height=100,
                                  text_color="#656866",
                                  fg_color="#AFE9DE",
                                  bg_color="#AFE9DE",
                                  font=("Roboto", 70))
  bul_id.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)

  ## SUBTITLE
  id_title = customtkinter.CTkLabel(master=alergy_app,
                                    text="Identificador de Alegias e Intolerâncias em Bulas",
                                      width=400,
                                      height=50,
                                      text_color="#656866",
                                      fg_color="#AFE9DE",
                                      bg_color="#AFE9DE",
                                      font=("Roboto", 20))
  id_title.place(relx=0.55, rely=0.1, anchor=tkinter.CENTER)

  ## IMAGEM
  image = customtkinter.CTkImage(Image.open("OOP_prototype/bulidtest/pharmacy.png"),
                                size=(100,100))
  image_label = customtkinter.CTkLabel(master=alergy_app,
                                      image=image,
                                      text="",
                                      width=100,
                                      bg_color="#AFE9DE",
                                      height=100)
  image_label.place(relx=0.90, rely=0.1, anchor=tkinter.CENTER)

  ## BOTÃO ALERGIAS 
  # Tem rounded corners
  alergy_button = customtkinter.CTkButton(master=alergy_app,
                                          text="Alergias",
                                          width=150,
                                          height=50,
                                          corner_radius=10,
                                          bg_color="#AFE9DE",
                                          fg_color="#FFF3D4",
                                          text_color="#484848",
                                          command=create_alergia_app, ## função de login
                                          hover_color="#FFF598")
  alergy_button.place(relx=0.15, rely=0.2, anchor=tkinter.CENTER)

  ## BOTAO PRINCIPIOS
  principles_button = customtkinter.CTkButton(master=alergy_app,
                                              text="Princípios",
                                              width=150,
                                              height=50,
                                              corner_radius=10,
                                              bg_color="#AFE9DE",
                                              fg_color=sel_btn_color,
                                              text_color="#484848",
                                              command=None, ## função de login
                                              hover_color="#FFF598")
  principles_button.place(relx=0.35, rely=0.2, anchor=tkinter.CENTER)

  ## BOTAO OUTROS
  outros_button = customtkinter.CTkButton(master=alergy_app,
                                          text="Outros",
                                          width=150,
                                          height=50,
                                          corner_radius=10,
                                          bg_color="#AFE9DE",
                                          fg_color="#FFF3D4",
                                          text_color="#484848",
                                          command=create_outros_app, ## função de login
                                          
                                          hover_color="#FFF598")
  outros_button.place(relx=0.55, rely=0.2, anchor=tkinter.CENTER)


  ## LABEL MEDICAMENTO
  med_label = customtkinter.CTkLabel(master=alergy_app,
                                      text="Medicamento *",
                                      width=80,
                                      height=25,
                                      text_color=txt_color,
                                      fg_color=bg_color,
                                      bg_color=bg_color,
                                      font=("Roboto", 15),
                                      corner_radius=8)
  med_label.place(relx=0.13, rely=0.3, anchor=tkinter.CENTER)

  # Entrada de medicamento
  med_entry = customtkinter.CTkEntry(master=alergy_app,
                                      placeholder_text="Nome do Medicamento",
                                      width=800,
                                      height=25,
                                      text_color=txt_color,
                                      fg_color="white",
                                      bg_color=bg_color,
                                      border_width=0,
                                      corner_radius=10)
  med_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

  ## LABEL PRINCIPIOS ATIVOS
  principios = customtkinter.CTkLabel(master=alergy_app,
                                      text="Princípio Ativo *",
                                      width=80,
                                      height=25,
                                      text_color=txt_color,
                                      fg_color=bg_color,
                                      bg_color=bg_color,
                                      font=("Roboto", 15),
                                      corner_radius=8)
  principios.place(relx=0.13, rely=0.4, anchor=tkinter.CENTER)

  # Entrada de principios ativos
  principios_entry = customtkinter.CTkEntry(master=alergy_app,
                                      placeholder_text="Principio Ativo",
                                      width=800,
                                      height=25,
                                      text_color=txt_color,
                                      fg_color="white",
                                      bg_color=bg_color,
                                      border_width=0,
                                      corner_radius=10)
  principios_entry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)



  ## LABEL EXCIPIENTE
  excipiente = customtkinter.CTkLabel(master=alergy_app,
                                      text="Excipiente",
                                      width=80,
                                      height=25,
                                      text_color=txt_color,
                                      fg_color=bg_color,
                                      bg_color=bg_color,
                                      font=("Roboto", 15),
                                      corner_radius=8)
  excipiente.place(relx=0.11, rely=0.5, anchor=tkinter.CENTER)

  # Entrada de excipiente
  excipiente_entry = customtkinter.CTkEntry(master=alergy_app,
                                      placeholder_text="Excipiente",
                                      width=800,
                                      height=25,
                                      text_color=txt_color,
                                      fg_color="white",
                                      bg_color=bg_color,
                                      border_width=0,
                                      corner_radius=10)
  excipiente_entry.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)




  ## BOTAO SUBMETER

  submit_button = customtkinter.CTkButton(master=alergy_app,
                                          text="Submeter",
                                          width=150,
                                          height=50,
                                          corner_radius=10,
                                          bg_color=bg_color,
                                          fg_color=btn_color,
                                          text_color=txt_color,
                                          font=("Roboto", 15),
                                          command=None, ## função de login
                                          hover_color=sel_btn_color)
  submit_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


  ## LABEL INFORMAÇÃO RESULTANTE

  result_label = customtkinter.CTkLabel(master=alergy_app,
                                      text="Informação Resultante",
                                      width=80,
                                      height=25,
                                      text_color=txt_color,
                                      fg_color=bg_color,
                                      bg_color=bg_color,
                                      font=("Roboto", 15),
                                      corner_radius=8)
  result_label.place(relx=0.15, rely=0.8, anchor=tkinter.CENTER)

  ## DISPLAY DE OUTPUT

  output = customtkinter.CTkLabel(master=alergy_app,
                                  text="",
                                  width=800,
                                  height=100,
                                  text_color=txt_color,
                                  fg_color="white",
                                  bg_color=bg_color,
                                  font=("Roboto", 15),
                                  corner_radius=8)
  output.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)








  #alergy_app.mainloop()
