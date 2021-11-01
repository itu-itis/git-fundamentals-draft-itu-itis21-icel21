def asal(sayi):

    for i in range(2,sayi):

        if(sayi%i==0):

            return False #asal değil
        else:
            pass
    return True #asal

def ekokbul(a,b):
    aliste = list()#sadece a'nın asal bölenleri
    bliste = list()#sadece b'nin asal bölenleri
    ortakbolen = list()#ortak asal bölenler
    x = 2
    ekok = 1
    while (x <= a or x <= b):
        if a%x == 0 and b%x == 0 and asal(x):
            ortakbolen.append(x)
            a /= x
            b /= x
        elif a%x == 0 and b%x != 0 and asal(x):
            aliste.append(x)
            a /= x
        elif a%x != 0 and b%x == 0 and asal(x):
            bliste.append(x)
            b /= x
        else:
            x += 1

    for i in bliste:
        aliste.append(i)
    for i in ortakbolen:
        aliste.append(i)

    for i in aliste:
        ekok *= i
    print("İki sayinin ekoku = ",ekok)
a = int(input("1. Sayinizi Girin:"))
b = int(input("2. Sayinizi Girin:"))
ekokbul(a,b)