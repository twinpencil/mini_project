import tkinter as tk
import customtkinter as cutk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


app = cutk.CTk()

color1 = "#ACE1AF"
color2 = "#B0EBB4"
color3 = "#BFF6C3"
color4 = "#E0FBE2"
color5 = "#FEFAF6"

app.title('MANAGEMENT DES EMPLOYEES')
app.geometry("900x420")
app.config(bg=color5)
app.resizable(False,False)

font1 = ('Arial',20,'bold')
font2 = ('Arial',12,'bold')

id_label = cutk.CTkLabel(app,font=font1,text='ID',text_color=color1,bg_color=color5)
id_label.place(x=20,y=20)

id_entrey = cutk.CTkEntry(app,font=font1,text_color='#000',fg_color=color1,border_color='#0C9295',border_width=2,width=180,bg_color=color5)
id_entrey.place(x=100,y=20)

name_label = cutk.CTkLabel(app,font=font1,text='ID',text_color=color1,bg_color=color5)
name_label.place(x=20,y=80)

name_entry = cutk.CTkEntry(app,font=font1,text_color='#000',fg_color=color1,border_color='#0C9295',border_width=2,width=180,bg_color=color5)
name_entry.place(x=100,y=80)

role_label = cutk.CTkLabel(app,font=font1,text='ID',text_color=color1,bg_color=color5)
role_label.place(x=20,y=140)

role_entry = cutk.CTkEntry(app,font=font1,text_color='#000',fg_color=color1,border_color='#0C9295',border_width=2,width=180,bg_color=color5)
role_entry.place(x=100,y=140)

gender_label = cutk.CTkLabel(app,font=font1,text='ID',text_color=color1,bg_color=color5)
gender_label.place(x=20,y=200)

options = ['Homme','femme']
var1 = StringVar()

gender_options = cutk.CTkComboBox(app,
                font=font1,
                text_color='#000',
                fg_color=color1,
                dropdown_hover_color='#0C9295',
                button_color='#0C9295',
                button_hover_color='#0C9295',
                border_color='#0C9295',
                width=180,variable=var1,

                corner_radius=15,
                bg_color=color5,
                values=options,
                state="readonly")
gender_options.set('Male')
gender_options.place(x=100,y=200)

status_label = cutk.CTkLabel(app,font=font1,text='ID',text_color=color1,bg_color=color5)
status_label.place(x=20,y=260)

status_entry = cutk.CTkEntry(app,font=font1,text_color='#000',fg_color=color1,border_color='#0C9295',bg_color=color5,border_width=2,width=180)
status_entry.place(x=100,y=260)

add_button = cutk.CTkButton(app,font=font1,
                            text_color=color1,
                            text='ajouter employe',
                            fg_color=color5,
                            hover_color='#00850B',
                            bg_color=color5,
                            cursor ='hand2',
                            corner_radius=15,
                            border_width=2,
                            border_color='white',
                            width=260 )
add_button.place(x=20,y=310)

clear_button = cutk.CTkButton(app,font=font1,
                            text_color=color1,
                            text='ajouter employe',
                            fg_color=color5,
                            hover_color='#00850B',
                            bg_color=color5,
                            cursor ='hand2',
                            corner_radius=15,
                            width=260 )
clear_button.place(x=20,y=360)

update_button = cutk.CTkButton(app,font=font1,
                            text_color=color1,
                            text='ajouter employe',
                            fg_color=color5,
                            hover_color='#00850B',
                            bg_color=color5,
                            cursor ='hand2',
                            corner_radius=15,
                            width=260 )
update_button.place(x=300,y=360)

delete_button = cutk.CTkButton(app,font=font1,
                            text_color=color1,
                            text='ajouter employe',
                            fg_color=color5,
                            hover_color='#00850B',
                            bg_color=color5,
                            cursor ='hand2',
                            corner_radius=15,
                            width=260 )
delete_button.place(x=580,y=360)




app.mainloop()