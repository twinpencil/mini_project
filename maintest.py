import tkinter as tk
import customtkinter as cutk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from PIL import Image,ImageTk
from CTkMenuBar import *
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time
#from database import Employe

app = cutk.CTk()

color1 = "#315041" #green
color2 = "#3CD37A" #green fath
color3 = "#FE7101" #ORANGE
color4 = "#547D69" #SELVER

app.title('ProManager')
app.iconbitmap('employee.ico')
app.geometry("1150x450")
app.config(bg=color1)
app.resizable(False,False)

font1 = ('Arial',20,'bold')
font2 = ('Arial',12,'bold')

####LOGIN####
users ={'admin':'admin'}
def login():
    username = user_entry.get()
    password = password_entry.get()
    if username in users and users[username]==password:
        login_frame.pack_forget()
        main_frame.pack(fill='both',expand=True)
    else:
        time.sleep(0.5)
        messagebox.showerror("Login Failed", "Invalid username or password")
####sign up####
def signup():
    username = user_entry.get()
    password = password_entry.get()
    if username in users:
        messagebox.showerror("Sign Up Failed", "Username already exists")
    else:
        time.sleep(0.5)
        users[username] = password
        messagebox.showinfo("Sign Up Successful", "You can now log in with your new informations")
####REPORT####
def show_report():
    main_frame.pack_forget()
    time.sleep(0.5)
    report_frame.pack(fill='both',expand=True)
####BACK TO MAIN####
def back_to_main():
    about_us_frame.pack_forget()
    report_frame.pack_forget()
    time.sleep(0.5)
    main_frame.pack(fill='both',expand=True)
####LOG OUT####
def log_out():
    if messagebox.askyesno("Log out","Are you sure you want to lougout ?"):
        login_frame.pack(fill='both',expand=True)
        time.sleep(0.5)
        main_frame.pack_forget()
        user_entry.delete(0,END)
        password_entry.delete(0,END)
####ABOUT####
def about_us():
    main_frame.pack_forget()
    time.sleep(0.5)
    about_us_frame.pack(fill='both',expand=True)
####EXPORT####
def export(a):
    if a == "txt":
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files","*.txt")])
        if file_path:
            with open(file_path,'w') as f : 
                for item in tree.get_children():
                    values = tree.item(item,'values')
                    text = ', '.join(values) # Concatenate values into a string
                    f.write(text +'\n')
    elif a == "pdf":
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            c = canvas.Canvas(file_path, pagesize=letter)  # Generate a PDF document
            y_position = 750  # Initial vertical position for the first line
            for item in tree.get_children():
                values = tree.item(item, 'values')
                text = ', '.join(values)
                c.drawString(100, y_position, text)  # Write the text to the PDF
                y_position -= 12  # Move down by 12 units 
            c.save()
####LIGHT AND DARK MODE####
light_mode_color = {
    #color1 = "#315041" #green
    #color2 = "#3CD37A" #green fath
    #color3 = "#FE7101" #ORANGE
    #color4 = "#547D69"
    "bg": "#5D2A42", # white
    "hover_color": "#FFDCCC", # light green
    "text": "#FB6376", # black
    "delete_fg": "#FA5E23", # orange-red
    "silver":"silver"
}
dark_mode_color = {
    "bg":"#315041", #dark bleu
    "hover_color" :"#3CD37A",
    "text":"white",
    "delete_fg" : "orange",
    "silver":"silver"
} 
mode = "dark"
def change_colors():
    global mode
    colors = light_mode_color if mode == "light" else dark_mode_color
    app.config(bg=colors["bg"])

    for frame in [about_us_frame,login_frame,main_frame,report_frame]:
        frame.configure(bg_color=colors["bg"],fg_color = colors["bg"])

    for label in [about,text,login_label,user_label,password_label,id_label,name_label,role_label,gender_label,status_label,report_label]:
        label.configure(text_color=colors["text"],bg_color = colors["bg"])

    for entry in [user_entry,password_entry,id_entry,name_entry,role_entry,status_entry]:
        entry.configure(fg_color= colors["text"],text_color= colors["bg"],bg_color = colors["bg"],border_color = colors["text"])

    for button in [clear_button,update_button,report_button,back_button]:
        button.configure(fg_color = colors["bg"],text_color = colors["hover_color"],hover_color = colors["text"],bg_color = colors["bg"],border_color = colors["text"])

    for button2 in [signup_button,delete_button]:
        button2.configure(fg_color = colors["delete_fg"],text_color = colors["text"],hover_color = colors["silver"],bg_color = colors["bg"],border_color = colors["delete_fg"])

    for button3 in [login_button,add_button]:
        button3.configure(fg_color = colors["bg"],text_color = colors["text"],hover_color = colors["silver"],bg_color = colors["bg"],border_color = colors["bg"])
    #for tree in [tree,report_tree]:
    #   style = ttk.Style(app)
    # style.configure('Treeview',font= font2 , foreground = colors["tree_fg"],background = colors["tree_bg"],fieldbackground=colors["tree_bg"])
    # style.map('Treeview',background = [('selected',colors["tree_selected_bg"])],foreground=[('selected',colors["tree_selected_fg"])])
def light(): 
    global mode
    mode = "light"
    change_colors()
def dark():
    global mode
    mode = "dark"
    change_colors()
def switch():
    if mode == 'light':
        dark()
    else:
        light()
################ABOUT FRAME################
about_us_frame = cutk.CTkFrame(app,bg_color=color1,fg_color=color1)
####about label####
about = cutk.CTkLabel(about_us_frame,text="About",font=font1)
about.pack(pady=20)
text = cutk.CTkLabel(about_us_frame,text="This Python project, titled 'Management des Employées,' serves as a management tool for employee data.\n \n Developed by Mohammed Benyamna and Davida Berto, the application provides features for user authentication,\n\n employee profile management, and reporting functionalities.\n\n It utilizes the tkinter library for the graphical user interface and aims to streamline employee management processes for businesses and organizations.",font=font2,text_color="white")
text.pack(pady=40)
back_button = cutk.CTkButton(about_us_frame,font=font1,
                            text_color=color2,text="<<< Back To Main",
                            fg_color=color1,
                            cursor='hand2',corner_radius=0,
                            border_color='white',
                            border_width=2,
                            hover_color='white',
                            width=260,command=back_to_main)
back_button.pack(pady=80)
################LOGIN FRAME################
login_frame =cutk.CTkFrame(app,bg_color=color1,fg_color=color1)
login_frame.pack(fill='both',expand=True)
########LOGIN LABEL########
login_label = cutk.CTkLabel(login_frame,text='LOGIN' , font=font1,text_color="white",bg_color=color1)
login_label.place(x=500,y=50)
########USER LABEL########
user_label = cutk.CTkLabel(login_frame,text='Username',
                            font=font1,text_color='white',
                            bg_color=color1)
user_label.place(x=450,y=150)
########USER ENTRY########
user_entry = cutk.CTkEntry(login_frame,font=font1,
                            text_color='black',fg_color='white',
                            bg_color=color1)
user_entry.place(x=600,y=150)
########PASSWORD LABEL########
password_label = cutk.CTkLabel(login_frame,text='Password',
                            font=font1,text_color='white',bg_color=color1)
password_label.place(x=450,y=200)
########PASSWORD ENTRY########
password_entry = cutk.CTkEntry(login_frame,font=font1,
                            text_color='black',
                            fg_color='white',
                            bg_color=color1,show="*")
password_entry.place(x=600 , y=200)
########LOGIN BUTTON########
login_button = cutk.CTkButton(login_frame,text='Login',
                            font=font1,
                            text_color="white",
                            fg_color=color2,
                            bg_color=color1,
                            cursor="hand1",
                            command=login)
login_button.place(x=600,y=260)
########SIGN UP BUTTON########
signup_button = cutk.CTkButton(login_frame,text="Sign Up",
                            font=font1,
                            text_color="white",
                            fg_color=color3,
                            bg_color=color1,
                            cursor='hand2',
                            command=signup)
signup_button.place(x=770,y=260)
################MAIN APPLICATION FRAME################
main_frame = cutk.CTkFrame(app, bg_color=color1,fg_color=color1)
########BARE MENU########
menu = CTkMenuBar(main_frame)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Profile")
button_3 = menu.add_cascade("Settings")
button_4 = menu.add_cascade("About")
####DROPDOWN####
#button_1#
dropdown1 = CustomDropdownMenu(widget=button_1)
sub_menu = dropdown1.add_submenu("Export As")
sub_menu.add_option(option=".TXT",command= lambda : export("txt"))
sub_menu.add_option(option=".PDF",command= lambda : export("pdf"))
#button_2#
dropdown2 = CustomDropdownMenu(widget=button_2)
dropdown2.add_option(option="log out",command=log_out)
#button_3#
dropdown3 = CustomDropdownMenu(widget=button_3)
dropdown3.add_option(option="dark mode",command=switch)
dropdown3.add_option(option="light mode",command=switch)
#button_4#
dropdown4 = CustomDropdownMenu(widget=button_4)
dropdown4.add_option(option="About us",command=about_us)
########ID LABEL########
id_label = cutk.CTkLabel(main_frame,font=font1,
                            text='ID : ',
                            text_color="white",
                            bg_color=color1)
id_label.place(x=20,y=40)
########ID ENTRY########
id_entry = cutk.CTkEntry(main_frame,font=font1,
                            text_color="black",
                            fg_color="white",
                            #border_color='black',
                            #border_width=3,
                            corner_radius=0,
                            border_color="white",
                            width=180,
                            bg_color=color1)
id_entry.place(x=100,y=40)
########NAME LABEL########
name_label = cutk.CTkLabel(main_frame,font=font1,
                            text='Name : ',
                            text_color="white",
                            bg_color=color1)
name_label.place(x=20,y=100)
########NAME ENTRY########
name_entry = cutk.CTkEntry(main_frame,font=font1,
                            text_color='black',
                            fg_color="white",
                            #border_color='black',
                            corner_radius=0,
                            #border_width=3,
                            border_color="white",
                            width=180,
                            bg_color=color1)
name_entry.place(x=100,y=100)
########ROLE LABEL########
role_label = cutk.CTkLabel(main_frame,font=font1,
                            text='Role : ',
                            text_color="white",
                            bg_color=color1)
role_label.place(x=20,y=160)
########ROLE ENTRY########
role_entry = cutk.CTkEntry(main_frame,font=font1,
                            text_color='black',
                            fg_color="white",
                            #border_color='black',
                            #border_width=2,
                            corner_radius=0,
                            width=180,
                            border_color="white",
                            bg_color=color1)
role_entry.place(x=100,y=160)
########GENDER LABEL########
gender_label = cutk.CTkLabel(main_frame,font=font1,
                            text='Gender ',
                            text_color="white",
                            bg_color=color1)
gender_label.place(x=20,y=220)
########GENDER COMBOBOX########
options = ['Man','Women']
var1 = StringVar()
gender_options = cutk.CTkComboBox(main_frame,
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
gender_options.set('Man')
gender_options.place(x=100,y=220)
########STATUS LABEL########
status_label = cutk.CTkLabel(main_frame,font=font1,
                            text='Status : ',
                            text_color="white",
                            bg_color=color1)
status_label.place(x=20,y=280)
########STATUS ENTRY########
status_entry = cutk.CTkEntry(main_frame,font=font1,
                            text_color='#000',
                            fg_color="white",
                            #border_color='black',
                            bg_color=color1,
                            border_color="white",
                            #border_width=3,
                            corner_radius=0,
                            width=180)
status_entry.place(x=100,y=280)
########ADD BUTTON########
add_button = cutk.CTkButton(main_frame,font=font1,
                            text_color="white",
                            text='Add Employe',
                            #fg_color=color2,
                            #hover_color='silver',
                            #bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            border_width=2,
                            #border_color=color2,
                            width=260 )
add_button.place(x=20,y=330)
########CLEAR BUTTON########
clear_button = cutk.CTkButton(main_frame,font=font1,
                            text_color=color2,
                            text='Clear',
                            fg_color=color1,
                            hover_color='white',
                            #bg_color=color1,
                            cursor ='hand2',
                            border_color="white",
                            border_width=2,
                            corner_radius=0,
                            width=260 )
clear_button.place(x=20,y=380)
########UPDATE BUTTON########
update_button = cutk.CTkButton(main_frame,font=font1,
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
update_button.place(x=300,y=380)
########DELETE BUTTON########
delete_button = cutk.CTkButton(main_frame,font=font1,
                            text_color="white",
                            text='Delete Employe',
                            fg_color=color3,
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260 )
delete_button.place(x=580,y=380)
########REPORT BUTTON########
report_button = cutk.CTkButton(main_frame,font=font1,
                            text_color=color2,
                            text="Show Report >>>",
                            fg_color=color1,
                            border_color='white',
                            border_width=2,
                            hover_color='white',
                            cursor="hand2",
                            corner_radius=0,
                            width=260,
                            command=show_report)
report_button.place(x=860,y=380)
style =ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview',font=font2,foreground='white',
                            background=color1,fieldbackground=color4,
                            )
style.map('Treeview',background=[('selected',color4)])
tree = ttk.Treeview(main_frame,height=19)
tree['columns'] = ('ID','Name','Role','Gender','Status')
########REPORT COLUMN########
tree.column('#0',width=0,stretch=tk.NO) #hide the default ffirst colomn
tree.column('ID',anchor=tk.CENTER,width=204)
tree.column('Name',anchor=tk.CENTER,width=204)
tree.column('Role',anchor=tk.CENTER,width=204)
tree.column('Gender',anchor=tk.CENTER,width=204)
tree.column('Status',anchor=tk.CENTER,width=204)
########REPORT HEADING########
tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Status',text='Status')
####PLACING####
tree.place(x=375,y=40)
################REPORT FRAME################
report_frame = cutk.CTkFrame(app,bg_color=color1,fg_color=color1)
########REPORT LABEL########
report_label = cutk.CTkLabel(report_frame,font=font1,text="Employee Report",text_color="white",bg_color=color1)
report_label.pack(pady=20)
########REPORT TREE########
report_tree = ttk.Treeview(report_frame,height=15)
report_tree['columns'] = ('ID','Name','Role','Gender','Status')
########REPORT COLUMN########
report_tree.column('#0',width=0,stretch=tk.NO) #hide the default first column
tree.column('ID',anchor=tk.CENTER,width=204)
tree.column('Name',anchor=tk.CENTER,width=204)
tree.column('Role',anchor=tk.CENTER,width=204)
tree.column('Gender',anchor=tk.CENTER,width=204)
tree.column('Status',anchor=tk.CENTER,width=204)
########REPORT HEADING########
report_tree.heading('ID',text='ID')
report_tree.heading('Name',text='Name')
report_tree.heading('Role',text='Role')
report_tree.heading('Gender',text='Gender')
report_tree.heading('Status',text='Status')
####PACKING####
report_tree.pack()
########REPORT HEADING########
back_button = cutk.CTkButton(report_frame,font=font1,
                            text_color=color2,text="<<< Back To Main",
                            fg_color=color1,
                            cursor='hand2',corner_radius=0,
                            border_color='white',
                            border_width=2,
                            hover_color='white',
                            width=260,command=back_to_main)
back_button.pack(pady=20)
#report_frame.pack_forget()
dark()
app.mainloop()