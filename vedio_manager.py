import sqlite3

conn = sqlite3.connect('vedios.db')

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Vedios(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   duration TEXT NOT NULL
               )
''')
def list_vedios():
    print("*****************List of Your Vedios********************")
    cursor.execute("SELECT * FROM Vedios")
    for row in cursor.fetchall():
        print(row)
        
        
def add_vedios(name,time):
    cursor.execute("INSERT INTO Vedios (name,duration) VALUES(?,?)",(name,time))
    print("Insert Successfully...")
    conn.commit()
    
def update_vedios(vedio_id,new_name,new_time):
    cursor.execute("UPDATE Vedios SET name = ? , duration = ? WHERE id = ?",
                   (new_name,new_time,vedio_id))
    print("Updated Successfully...")
    conn.commit()

def delete_vedios(vedio_id):
    cursor.execute("DELETE FROM Vedios WHERE id= ?",(vedio_id,))
    print("Vedio Deleted Successfully...")
    conn.commit()
    
def main():
    while True:
        print("\n *****Welcome to Youtube Vedio manager app*****")
        print("1. List All Vedios")
        print("2. Add Vedios")
        print("3. Update Vedios")
        print("4. Delete Vedios")
        print("5. Exit")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            list_vedios()
        elif choice == "2":
            name = input("Enter the vedio name: ")
            time = input("Enter the vedio Duration: ")
            add_vedios(name,time)
        elif choice == "3":
            id = int(input("Enter the vedio ID to Update: "))
            name = input("Enter the vedio name: ")
            time = input("Enter the vedio Duration: ")
            update_vedios(id,name,time)
        elif choice == "4":
            id = int(input("Enter the vedio ID to Delete: "))
            delete_vedios(id)
        elif choice == "5":
            break
        else:
            print("Invalid input")
            
    conn.close()
    
if __name__ =="__main__":
    main()