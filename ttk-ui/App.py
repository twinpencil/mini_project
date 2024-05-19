import ttkbootstrap as tb

class App(tb.Window):

    def __init__(self):
        super().__init__()
        self.title("Employee management")
        self.geometry('920x480')

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
        self.add_btn = tb.Button(self.left, bootstyle='primary', text="Add Employee")
        self.add_btn.grid(row=5, columnspan=2, padx=(10,20), pady=(40,10), sticky='ew')
        
        # New employe 
        self.new_btn = tb.Button(self.left, bootstyle='light', text="New Employee")
        self.new_btn.grid(row=6, columnspan=2, padx=(10,20), pady=(10,40), sticky='ew')

if __name__ == '__main__':
    t = App()
    t.mainloop()