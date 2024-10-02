# shoppinglist.py
shoppinglist = []

#Funktion add_item
def add_item():
    item = input("Welche Artikel sollen in die Liste rein?: ")
    print(f"Folgendes wurde zu der Liste hinzugefügt: {item}")
    shoppinglist.append(item)

add_item()

# show_shoppinglist
def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufsliste: ")
    else:
        print("Die Einkaufsliste ist leer")

show_shoppinglist()