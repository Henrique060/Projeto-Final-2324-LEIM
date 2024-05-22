## USAR CUSTOM TKINTER

import customtkinter
import tkinter
from PIL import Image, ImageTk


## FUNÇÕES DE INTERAÇÃO COM A GUI

alergy_list = []
lactose_selected = False
ovos_selected = False
penicilina_selected = False
sulfitos_selected = False
peixe_selected = False
soja_selected = False


# Submeter nome do medicamento
def submit_med_name():
    med_name = med_entry.get()
    #output.configure(text=f"Medicamento: {med_name}")
    print('Medicamento inserido:', med_name)
    return med_name

def create_alergia_app():
  from guiv2_alergias import create_window_alergias
  create_window_alergias()

def create_principios_app():
  from guiv2_principios import create_principios_app
  create_principios_app()

# Subemter alergia conforme o texto do botão
def lactose():
    lactose_selected = True
    if lactose_selected:
        alergy_list.append('Lactose')   

def ovos():
    alergy_list.append('Ovos')

def nuts():
    alergy_list.append('Frutos Secos')

def penicilina():
    alergy_list.append('Penicilina')

def gluten():
    alergy_list.append('Glúten')

def soja():
    alergy_list.append('Soja')

def fish():
    alergy_list.append('Peixe')

def sulfitos():
    alergy_list.append('Sulfitos')

def submit_alergy():
    print('Alergias:', alergy_list)
    #output.configure(text=f"Alergias: {alergy_list}")
    return alergy_list

def button_click():
    submit_med_name()
    submit_alergy()


def create_outros_app():
    ##CORES
    bg_color = "#AFE9DE"
    txt_color = "#656565"
    btn_color = "#FFF3D4"
    sel_btn_color  = "#FFF598"

    ## APP EM SI
    alergy_app = customtkinter.CTk()
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
                                                fg_color="#FFF3D4",
                                                text_color="#484848",
                                                command=create_principios_app, ## função de login
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
                                            command=None, ## função de login
                                            
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

    ## LABEL ALERGIA
    cond_label = customtkinter.CTkLabel(master=alergy_app,
                                        text="Condições Especiais *",
                                        width=80,
                                        height=25,
                                        text_color=txt_color,
                                        fg_color=bg_color,
                                        bg_color=bg_color,
                                        font=("Roboto", 15),
                                        corner_radius=8)
    cond_label.place(relx=0.15, rely=0.4, anchor=tkinter.CENTER)

    # Botao Lactose
    gravidez = customtkinter.CTkButton(master=alergy_app,
                                            text="Gravidez",
                                            width=150,
                                            height=50,
                                            corner_radius=10,
                                            bg_color=bg_color,
                                            fg_color="white",
                                            text_color=txt_color,
                                            command=lactose, ## função de login
                                            hover_color=sel_btn_color)
    gravidez.place(relx=0.15, rely=0.475, anchor=tkinter.CENTER)

    # Botao Ovos
    menstruacao = customtkinter.CTkButton(master=alergy_app,
                                            text="Menstruação",
                                            width=150,
                                            height=50,
                                            corner_radius=10,
                                            bg_color=bg_color,
                                            fg_color="white",
                                            text_color=txt_color,
                                            command=None, ## função de login
                                            hover_color=sel_btn_color)
    menstruacao.place(relx=0.15, rely=0.575, anchor=tkinter.CENTER)

    # Botao Frutos Secos
    operacao = customtkinter.CTkButton(master=alergy_app,
                                            text="Operação Maquinaria",
                                            width=150,
                                            height=50,
                                            corner_radius=10,
                                            bg_color=bg_color,
                                            fg_color="white",
                                            text_color=txt_color,
                                            command=None, ## função de login
                                            hover_color=sel_btn_color)
    operacao.place(relx=0.5, rely=0.475, anchor=tkinter.CENTER)

    # Botao Penincilina
    conducao = customtkinter.CTkButton(master=alergy_app,
                                            text="Condução",
                                            width=150,
                                            height=50,
                                            corner_radius=10,
                                            bg_color=bg_color,
                                            fg_color="white",
                                            text_color=txt_color,
                                            command=None, ## função de login
                                            hover_color=sel_btn_color)
    conducao.place(relx=0.5, rely=0.575, anchor=tkinter.CENTER)

    # Botao Glúten

    sonolencia = customtkinter.CTkButton(master=alergy_app,
                                            text="Sonolência",
                                            width=150,
                                            height=50,
                                            corner_radius=10,
                                            bg_color=bg_color,
                                            fg_color="white",
                                            text_color=txt_color,
                                            command=None, ## função de login
                                            hover_color=sel_btn_color)
    sonolencia.place(relx=0.85, rely=0.475, anchor=tkinter.CENTER)

    # Botao Soja

    func_motor = customtkinter.CTkButton(master=alergy_app,
                                            text="F. Motoras",
                                            width=150,
                                            height=50,
                                            corner_radius=10,
                                            bg_color=bg_color,
                                            fg_color="white",
                                            text_color=txt_color,
                                            command=None, ## função de login
                                            hover_color=sel_btn_color)
    func_motor.place(relx=0.85, rely=0.575, anchor=tkinter.CENTER)

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
                                            command=button_click, ## função de login
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
