import sqlite3
shoppinglist = []

# Verbindung zu sqlite-DB
conn = sqlite3.connect('groceries.db')

# Erstellung von Cursor um sql-Befehl durchzuführen
cursor = conn.cursor()

# Erstellung von Tabellen in groceries.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS groceries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    amount INTEGER NOT NULL,
    price VARCHAR(32) NOT NULL
    )
''')

# CREATE Product
def add_product(name, amount, price):
    cursor.execute('''
    INSERT INTO groceries (name, amount, price) VALUES (?, ?, ?)      
    ''', (name, amount, price))
    conn.commit()
    print(f"{name} wurde zu der Liste hinzugefügt")

# READ Funktion
def show_groceries():
    cursor.execute('SELECT id, name, amount, price FROM groceries')
    groceries = cursor.fetchall()
    for product in groceries:
        print(product)

# UPDATE Function
def update_groceries(id, name, amount, price):
    cursor.execute('''
    UPDATE groceries SET name = ?, amount = ?, price = ?
    WHERE id = ?
    ''', (name, amount, price, id))
    conn.commit()
    print(f"Produkt mit ID {id} aktualisiert.")

# DELETE Function
def delete_groceries(id):
    cursor.execute('''
    DELETE FROM groceries WHERE id = ?              
    ''', (id,))
    conn.commit()
    print(f"Produkt mit ID {id} wurde gelöscht.")

# Main
def main():
    while True:
        print("\n------------ Einkaufsliste ------------")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Produkt aktualisieren")
        print("4. Produkt löschen")
        print("5. Programm beenden")

        choice = input("\n Bitte wählen Sie eine Option (1, 2, 3, 4 oder 5): ")

        if choice == "1":
             print("\nBitte gib neues Produkt ein: ")
             name = input("Produktname: ")
             amount = input("\nMenge: ")
             price = input("\nPreis: ")
             add_product(name, amount, price)
        elif choice == "2":
             show_groceries()
        elif choice == "3":
             print("\nBitte aktualisiere die Daten. Gib ID ein: ")
             id = input("id: ")
             name = input("Produktname: ")
             amount = input("Menge: ")
             price = input("Preis: ")
             update_groceries(id, name, amount, price)
        elif choice == "4":
             print("\nBitte gib die ID des zu löschenden Produkt ein: ")
             id = input("id: ")
             delete_groceries(id)
        elif choice == "5":
             print("\n Programm wird beendet! Auf Wiedersehen!")
             break
        else:
             print("\nUngültige Eingabe! Bitte wählen Sie zwischen 1, 2, 3, 4 oder 5")

if __name__ == "__main__":
    main()