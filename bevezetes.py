def adatbekeres():
    nev=input("Játékosnév: ")
    szerep=input("szerepkör: ")

    print("I/A")
    print(f"Játékos neve: {nev}")
    print(f"szerepkör: {szerep}")

    if(szerep=="varázsló"):
        print("I/B")
        print(f"Üdvözlünk {nev}, 2 életed van!")
    
    elif(szerep=="harcos"):
        print("I/B")
        print(f"Üdvözlünk {nev}, 10 életed van!")
    
    else:
        print("I/B")
        print(f"Üdvözlünk {nev}, 8 életed van!")
