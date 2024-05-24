import tkinter as tk
import customtkinter as cutk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from database import Employe


# Databases 
db = Employe.Employe()

# get data from databases
def get_entrie(event=None):
    id = id_entrey.get()
    name = name_entry.get()
    status = status_entry.get()
    role = role_entry.get()
    genre = gender_options.get()
    return (id, name, status, role, genre)

# get data from entries 

def clear_tree(event=None):
    for t in tree.get_children():
        tree.delete(t)

def refresh_database(event=None):
    employes = db.fetch_all()
    clear_tree()
    for employe in employes:
        tree.insert(
            "",
            index='end',
            text="",
            values=employe
        )

# add employe to databases 
def add_employe(event=None):
    print(get_entrie())
    id = id_entrey.get()
    name = name_entry.get()
    status = status_entry.get()
    role = role_entry.get()
    genre = gender_options.get()
    db.insert(id,name, role, genre, status)
    refresh_database()

def clear_entry(event=None):
    id_entrey.delete(0,'end')
    name_entry.delete(0,'end')
    role_entry.delete(0,'end')
    status_entry.delete(0,'end')


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
####fonction#####
#def ajouter_tree():
    # employe = Employe.fetch
####label,entry####
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
                            button_hover_color='#33c155',
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
                            hover_color='silver',
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            border_width=2,
                            #border_color=color2,
                            width=260,
                             command=add_employe )
add_button.place(x=20,y=310)

clear_button = cutk.CTkButton(app,font=font1,
                            text_color=color2,
                            text='Clear',
                            fg_color=color1,
                            hover_color='white',
                            #bg_color=color1,
                            cursor ='hand2',
                            border_color="white",
                            border_width=2,
                            corner_radius=0,
                            width=260,
                             command=clear_entry )
clear_button.place(x=20,y=360)

update_button = cutk.CTkButton(app,font=font1,
                            text_color=color2,
                            text='Update Employe',
                            fg_color=color1,
                            hover_color='white',
                            #bg_color=color1,
                            border_color='white',
                            border_width=2,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260 )
update_button.place(x=300,y=360)

delete_button = cutk.CTkButton(app,font=font1,
                            text_color="white",
                            text='Delete Employe',
                            fg_color=color3,
                            hover_color='silver',
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260 )
delete_button.place(x=580,y=360)
#style
style =ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview',font=font2,foreground='white',background=color1,fieldbackground=color4,borderwidth=8, relief='flat',highlightthickness=6)
style.map('Treeview',background=[('selected',color4)])

tree = ttk.Treeview(app,height=19)
tree['columns'] = ('ID','Name','Role','Gender','Status')

tree.column('#0',width=0,stretch=tk.NO) #hide the default ffirst colomn
tree.column('ID',anchor=tk.CENTER,width=135)
tree.column('Name',anchor=tk.CENTER,width=134)
tree.column('Role',anchor=tk.CENTER,width=134)
tree.column('Gender',anchor=tk.CENTER,width=134)
tree.column('Status',anchor=tk.CENTER,width=134)

#head
tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Status',text='Status')

#PLACE
tree.place(x=375,y=20)
refresh_database()
app.mainloop()