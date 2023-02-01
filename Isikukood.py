from OmaModule import *

while True:

    isikukood=input("Palun kirjuta sinu isikukood - ")
    if iPikk(isikukood)==False:
        isikukood=input("Kirjuta õige isikukood! ")
    else:
        print("11 sümbilid")

        sugu=ksugu(isikukood)
        if sugu=="Viga":
            print("Esimene täht ei ole õige")
        else:
            print(sugu)

            sun=ksupa(isikukood)
            if sun=="Viga":
                print("Teine kuni seitmes täth ei ole õige")
            else:
                print(sun)
    print()
