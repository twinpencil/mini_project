import tkinter as tk
import customtkinter as cutk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


app = cutk.CTk()

color1 = "#315041" #green
color2 = "#3CD37A" #green fath
color3 = "#FE7101" #ORANGE
color4 = "#547D69" #SELVER


app.title('MANAGEMENT DES EMPLOYEES')
app.geometry("900x420")
app.config(bg=color1)
app.resizable(False,False)

font1 = ('Arial',20,'bold')
font2 = ('Arial',12,'bold')

id_label = cutk.CTkLabel(app,font=font1,
                        text='ID : ',
                        text_color="white",
                        bg_color=color1)
id_label.place(x=20,y=20)

id_entrey = cutk.CTkEntry(app,font=font1,
                        text_color="black",
                        fg_color="white",
                        #border_color='black',
                        #border_width=3,
                        corner_radius=0,
                        border_color="white",
                        width=180,
                        bg_color=color1)
id_entrey.place(x=100,y=20)

name_label = cutk.CTkLabel(app,font=font1,
                        text='Name : ',
                        text_color="white",
                        bg_color=color1)
name_label.place(x=20,y=80)

name_entry = cutk.CTkEntry(app,font=font1,
                        text_color='black',
                        fg_color="white",
                        #border_color='black',
                        corner_radius=0,
                        #border_width=3,
                        border_color="white",
                        width=180,
                        bg_color=color1)
name_entry.place(x=100,y=80)

role_label = cutk.CTkLabel(app,font=font1,
                        text='Role : ',
                        text_color="white",
                        bg_color=color1)
role_label.place(x=20,y=140)

role_entry = cutk.CTkEntry(app,font=font1,
                        text_color='black',
                        fg_color="white",
                        #border_color='black',
                        #border_width=2,
                        corner_radius=0,
                        width=180,
                        border_color="white",
                        bg_color=color1)
role_entry.place(x=100,y=140)

gender_label = cutk.CTkLabel(app,font=font1,
                            text='Gender ',
                            text_color="white",
                            bg_color=color1)
gender_label.place(x=20,y=200)

options = ['Homme','femme']
var1 = StringVar()

gender_options = cutk.CTkComboBox(app,
                font=font1,
                text_color="black",
                fg_color="white",
                dropdown_hover_color=color2,
                button_color=color2,
                button_hover_color='#0C9295',
                #border_color='#0C9295',
                width=180,variable=var1,
                #corner_radius=15,
                corner_radius=0,
                bg_color=color1,
                values=options,
                border_color="white",
                state="readonly")
gender_options.set('Homme')
gender_options.place(x=100,y=200)

status_label = cutk.CTkLabel(app,font=font1,
                            text='Status : ',
                            text_color="white",
                            bg_color=color1)
status_label.place(x=20,y=260)

status_entry = cutk.CTkEntry(app,font=font1,
                            text_color='#000',
                            fg_color="white",
                            #border_color='black',
                            bg_color=color1,
                            border_color="white",
                            #border_width=3,
                            corner_radius=0,
                            width=180)
status_entry.place(x=100,y=260)

add_button = cutk.CTkButton(app,font=font1,
                            text_color="white",
                            text='Ajouter Employe',
                            fg_color=color2,
                            hover_color='#00850B',
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            border_width=2,
                            #border_color=color2,
                            width=260 )
add_button.place(x=20,y=310)

clear_button = cutk.CTkButton(app,font=font1,
                            text_color=color2,
                            text='Clear',
                            fg_color="white",
                            hover_color='#00850B',
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260 )
clear_button.place(x=20,y=360)

update_button = cutk.CTkButton(app,font=font1,
                            text_color=color2,
                            text='Update Employe',
                            fg_color="white",
                            hover_color='#00850B',
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260 )
update_button.place(x=300,y=360)

delete_button = cutk.CTkButton(app,font=font1,
                            text_color="white",
                            text='Delete Employe',
                            fg_color=color3,
                            hover_color='#00850B',
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260 )
delete_button.place(x=580,y=360)






app.mainloop()