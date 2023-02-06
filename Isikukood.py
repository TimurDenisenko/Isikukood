from OmaModule import *
TrueIsikukood=[] 
No11=[] 
NoNum=[]
NoKn=[] 
NoSug=[] 
NoSun=[] 
NoHai=[]
TrueI=[]
while True:
    isikukood=input("Palun kirjuta sinu isikukood ")
    if iPikk(isikukood)==False:
        print("Isikukood koosneb üheteistkümnest tähemärgist")
        No11.append(isikukood)
        ars(No11)
    else:
        print("11 sümbilid")

        if isikukood.isdigit()==False:
            print("Isikukood peab sisaldama ainult numbreid")
            NoNum.append(isikukood)
            ars(NoNum)
        else:
            print("Moodustatud numbritest")

            arv=karv(isikukood)
            if arv=="Viga":
                print("Üheteistkümnes täht on vale")
                NoKn.append(isikukood)
                ars(NoKn)
            else:
                print(arv)

                sugu=ksugu(isikukood)
                if sugu=="Viga":
                    print("Esimene täht ei ole õige")
                    NoSug.append(isikukood)
                    ars(NoSug)
                else:
                    print(sugu)

                    sun=ksupa(isikukood)
                    if sun=="Viga":
                        print("Viga teise ja seitsmenda tähe vahel")
                        NoSun.append(isikukood)
                        ars(NoSun)
                    else:
                        print(sun)

                        haigla=khaiga(isikukood)
                        if haigla=="Viga":
                            print("Viga kaheksanda ja kümnenda tähe vahel")
                            NoHai.append(isikukood)
                            ars(NoHai)
                        else:
                            print(haigla)
                            ikood(isikukood)
                            TrueIsikukood.append(isikukood)
                            TrueI=arg(TrueIsikukood)
                            print()
    print("Õige isikukoodid - ",TrueI)
    print("Isikukood, kus märkide arv on vale - ",No11)
    print("Isikukood, kus see ei koosne ainult numbritest - ",NoNum)
    print("Isikukood vale kontrollnumbriga - ",NoKn)
    print("Isikukood, kus sooväärtused on valed - ",NoSug)
    print("Vale sünnikuupäevaga kood - ",NoSun)
    print("Isikukood vale sünnikohaga - ",NoHai)
    print()
