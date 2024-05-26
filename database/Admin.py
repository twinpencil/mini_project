import sqlite3 

# ORM Admin

class Admin:
    def __init__(self):
        # initialising Database and database cursor
        self.conn = sqlite3.connect("./database.db")
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Admin" (
            "id" INTEGER	PRIMARY KEY AUTOINCREMENT,
            "username"	TEXT NOT NULL,
            "password"	TEXT NOT NULL
        );
        ''')
        self.conn.commit()
    
    def insert(self, username, password):
        self.cursor.execute( "INSERT INTO Admin( username, password) VALUES(?,?)",(username, password))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM Admin")
        return self.cursor.fetchall()
    
    def fetch_by_id(self, id):
        self.cursor.execute("SELECT * FROM Admin WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def is_exist(self, id):
        self.cursor.execute("SELECT COUNT(*) FROM Admin WHERE id = ? ",(id,))
        return self.cursor.fetchone()[0] > 0
    
    def delete(self, id):
        self.cursor.execute("DELETE FROM Admin WHERE id = ?", (id,))
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()