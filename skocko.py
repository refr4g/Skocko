# generisemo trazeni niz
# da li je pogodio
# gledamo koliko puta je pogodio i mesto i znak
# gledamo koliko puta je pogodio samo znak

import random

def generisanje():
    niz=[]
    for i in range(4):
        niz.append((int)(random.random()*6)+1)
    return niz
    
def korisnikunosi():
    niz=[]
    t=input().split(' ')
    for i in t:
        niz.append(int(i))
    return niz

def mestoznak(trazeni, pokusaj):
    br=0
    for i in range(len(trazeni)):
        if(trazeni[i]==pokusaj[i]):
            br=br+1
    return br

def samoznak(trazeni, pokusaj):
    br=0
    A=[0]*6
    B=[0]*6
    for i in range(len(trazeni)):
        if(trazeni[i]!=pokusaj[i]):
            A[trazeni[i]-1]=A[trazeni[i]-1]+1
            B[pokusaj[i]-1]=B[pokusaj[i]-1]+1
        
    for i in range(len(A)):
        br+=min(A[i],B[i])
    return br

trazeni=generisanje()
print(trazeni)
while True:
    pokusaj=korisnikunosi()
    if trazeni==pokusaj:
        print("Pogodili ste, niz je", trazeni)
        exit()
    else:
        mesto=mestoznak(trazeni, pokusaj)
        broj=samoznak(trazeni, pokusaj)
        print("Pokusaj", pokusaj, "i mesto i broj", mesto, "samo broj", broj)

