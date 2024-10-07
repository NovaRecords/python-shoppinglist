shoppinglist = []

def show_shoppinglist():
    if shoppinglist:
        print("\n---------- Einkaufsliste ----------")
        for item in shoppinglist:
                print(item)
    else:
        print("\n----- Ihre Einkaufsliste ist leer -----")

def add_item():
    item = input("\nWelche Artikel soll in die Liste rein?: ")
    print(f"\nFolgendes wurde zu der Liste hinzugefügt: {item}")
    if item:
        shoppinglist.append(item)

def main():
    while True:
        print("\n------------ Einkaufsliste ------------")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        choice = input("\n Bitte treffen Sie ihre Auswahl: ")

        if choice == "1":
             add_item()
        elif choice == "2":
             show_shoppinglist()
        elif choice == "3":
             print("\n Programm wird beendet! Auf Wiedersehen!")
             break
        else:
             print("\n Bitte wählen Sie zwischen 1, 2 oder 3")
             
     #   show_shoppinglist()

if __name__ == "__main__":
    main()