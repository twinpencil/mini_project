import ttkbootstrap as tb
from  tkinter import messagebox
from emp_db import Employe

class App(tb.Window):

    def __init__(self):
        super().__init__()
        self.title("Employee management")
        self.geometry('920x480')
        self.server = Employe()
        self.current_id = ""

        # creating left frame
        self.left = tb.Frame(self,bootstyle="success")
        self.left.grid(row=0, sticky='ew', column=0)

        # ID
        self.id_l = tb.Label(self.left,text="ID:", bootstyle="success inverse", font=("Helvetica", 14))
        self.id_l.grid(row=0, sticky='ew', column=0, pady=(90,10), padx=(10,20))

        self.id_ipt = tb.Entry(self.left)
        self.id_ipt.grid(row=0, sticky='ew', column=1, padx=(10,20), pady=(90,10))


        # Name
        self.name_l = tb.Label(self.left,text="Name:", bootstyle="success inverse", font=("Helvetica", 14))
        self.name_l.grid(row=1, sticky='ew', column=0, pady=10, padx=(10,20))

        self.name_ipt = tb.Entry(self.left)
        self.name_ipt.grid(row=1, sticky='ew', column=1, padx=(10,20), pady=10)


        # Role
        self.role_l = tb.Label(self.left,text="Role:", bootstyle="success inverse", font=("Helvetica", 14))
        self.role_l.grid(row=2, sticky='ew', column=0, pady=10, padx=(10,20))

        self.role_ipt = tb.Entry(self.left)
        self.role_ipt.grid(row=2, sticky='ew', column=1, padx=(10,20), pady=10)

        # Gender
        self.gender_l = tb.Label(self.left,text="Gender:", bootstyle="success inverse", font=("Helvetica", 14))
        self.gender_l.grid(row=3, sticky='ew', column=0, pady=10, padx=(10,20))

        self.gender_ipt = tb.Combobox(self.left, bootstyle='success', values=['Male', 'Female'], state='readonly')
        self.gender_ipt.set('Male')
        self.gender_ipt.grid(row=3, sticky='ew', column=1, padx=(10,20), pady=10)

        
        # Status
        self.status_l = tb.Label(self.left,text="Status:", bootstyle="success inverse", font=("Helvetica", 14))
        self.status_l.grid(row=4, sticky='ew', column=0, pady=10, padx=(10,20))

        self.status_ipt = tb.Entry(self.left)
        self.status_ipt.grid(row=4, sticky='ew', column=1, padx=(10,20), pady=10)


        # Button 
        self.add_btn = tb.Button(self.left, bootstyle='primary', text="Add Employee", command=self.add_employer)
        self.add_btn.grid(row=5, columnspan=2, padx=(10,20), pady=(40,10), sticky='ew')
        
        # New employe 
        self.new_btn = tb.Button(self.left, bootstyle='light', text="Update", command=self.update_server)
        self.new_btn.grid(row=6, columnspan=2, padx=(10,20), pady=(40,10), sticky='ew')


        # Rigth frame
          # creating left frame
        self.right = tb.Frame(self,bootstyle="success")
        self.right.grid(row=0,column=1)

        # table 
        self.table = tb.Treeview(self.right, columns=("name", "Role", "Gender", "Status"), bootstyle='success', height=27)

        # heading
        self.table.heading("#0", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("Role", text="Role")
        self.table.heading("Gender", text="Gender")
        self.table.heading("Status", text="Status")

        # configuring
        self.table.column('#0', width=40)
        self.table.column('name', width=150, anchor='center')
        self.table.column('Role', width=150, anchor='center')
        self.table.column('Gender', width=150, anchor='center')
        self.table.column('Status', width=150, anchor='center')

        self.table.grid(row=0,column=0, columnspan=2)

        # button 
        self.update_btn = tb.Button(self.right, bootstyle='light', text="Update Employee", command=self.update_employe)
        self.update_btn.grid(padx=(80,20), pady=5, row=1,column=0, sticky='we')
        
        self.delete_btn = tb.Button(self.right, bootstyle='danger', text="Delete Employee", command=self.delete_employe)
        self.delete_btn.grid(padx=(20,80), pady=5, row=1,column=1, sticky='we')

        self.table.bind('<Button-1>', self.get_current_id)
        self.update_table()

    def add_employer(self):
        employe = self.get()
        for e in employe:
            if e == '':
                messagebox.showerror("Error !", "Error!\nForm can't be empy")
                return None
        if not self.server.is_exist(employe[0]):
            self.server.insert(*employe)
            self.update_table()
            return None
        
        messagebox.showwarning("Warnings", "Warnigns!\nEmployee Already exits !")
        
        

    def get(self):
        id = self.id_ipt.get().upper()
        name = self.name_ipt.get()
        role = self.role_ipt.get()
        gender = self.gender_ipt.get()
        status = self.status_ipt.get()
        return (id, name, role, gender ,status)
    
    def update_table(self):
        employees = self.server.fetch_all()
        self.table.delete(*self.table.get_children())
        for employee in employees:
            id = employee[0]
            self.table.insert(
            parent="",
            index='end',
            iid=id,
            text=employee[0],
            values=employee[1:]
        )
    
    def get_current_id(self, event=None):
        self.current_id = self.table.identify_row(event.y)
    
    def delete_employe(self):
        id = self.current_id
        
        if id != '':
            self.server.delete(id)
            self.update_table()

    def update_employe(self):
        id = self.current_id
        if id == "":
            return None
        
        # Updating employee
        emp = self.server.fetch_by_id(id)

        self.id_ipt.delete(0, 'end')
        self.id_ipt.insert(0, emp[0])
        
        self.name_ipt.delete(0, 'end')
        self.name_ipt.insert(0, emp[1])

        self.role_ipt.delete(0, 'end')
        self.role_ipt.insert(0, emp[2])

        self.gender_ipt.set(emp[3])
        self.status_ipt.delete(0, 'end')
        self.status_ipt.insert(0, emp[4])
    
    def update_server(self):
        emp = self.get()
        for e in emp:
            if e == '':
                messagebox.showerror("Error !", "Error!\nForm can't be empy")
                return None
        self.server.update(*emp)
        self.update_table()



if __name__ == '__main__':
    t = App()
    t.mainloop()