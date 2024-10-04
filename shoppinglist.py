# shoppinglist.py
shoppinglist = []

#Funktion add_item
def add_item():
    item = input("Welche Artikel sollen in die Liste rein?: ")
    print(f"Folgendes wurde zu der Liste hinzugefügt: {item}")
    if item == '':
        None
    else:
        shoppinglist.append(item)

add_item()

# show_shoppinglist
def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufsliste: ")
        for item in shoppinglist:
            print(f"{item}")
    else:
        print("Die Einkaufsliste ist leer")

show_shoppinglist()

# Main function
def main():
    while True:
        print("_____ Einkaufsliste _____")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        choice = input("Bitte treffen Sie die Auswahl: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")

# Run_function
if __name__ == "__main__":
    main()
