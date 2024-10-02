# shoppinglist.py
shoppinglist = []

#Funktionen definieren
def add_item():
    item = input("Welche Artikel sollen in die Liste rein?: ")
    print(f"Folgendes wurde zu der Liste hinzugefügt: {item}")
    shoppinglist.append(item)

add_item()