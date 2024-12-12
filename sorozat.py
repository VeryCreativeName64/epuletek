import random

def fej_iras():
    lista=[]
    for _ in range(7):
        dobas=random.randint(0,1)
        if(dobas==0):
            lista.append("FEJ")
        if(dobas==1):
            lista.append("ÍRÁS")

    return "-".join(lista)
    
def fejek_szama():
    fejek=fej_iras()
    i=0
    db=0
    while(i<len(fejek)):
        if(fejek[i]=="FEJ"):
            db+=1
        i+=1
    
    print("II/D, E")
    print(f"A fejek száma: {db}")
