import sqlite3 

class Employe:
    def __init__(self):
        self.conn = sqlite3.connect("./database.db")
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Employe" (
            "id"	TEXT NOT NULL,
            "name"	TEXT NOT NULL,
            "role"	TEXT NOT NULL,
            "gender"	TEXT NOT NULL,
            "status"	TEXT NOT NULL,
            PRIMARY KEY("id")
        );

        ''')
        self.conn.commit()
    
    def insert(self, id, name, role, gender, status):
        self.cursor.execute( "INSERT INTO Employe VALUES(?,?,?,?,?)",(id, name, role, gender, status))
        self.conn.commit()
    
    def update(self, id, name, role, gender, status):
        self.cursor.execute( "UPDATE Employe SET name = ? , role = ? , gender = ? , status =  ? WHERE id = ?",(name, role, gender, status, id))
        self.conn.commit()


    def fetch_all(self):
        self.cursor.execute("SELECT * FROM Employe")
        return self.cursor.fetchall()
    
    def fetch_by_id(self, id):
        self.cursor.execute("SELECT * FROM Employe WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def delete(self, id):
        self.cursor.execute("DELETE FROM Employe WHERE id = ?", (id,))
        self.conn.commit()

if __name__ == '__main__':
    e = Employe()
    e.delete('c2')
    print(e.fetch_by_id("c1"))