def iPikk(x:str)->bool:
    """Funktsioon tagastab True, kui iPikk on 11 sümbolid
    :param str x: Inimese isikukood
    :rtype: bool
    """
    y=False
    if len(x)==11:
        y=True 
    return y

def ksugu(x:str)->str:
    """Kui esimene täht on [1,2,3,4,5,6], siis määrame sugu
    :param str x: Inimese isikukood
    :rtype: str
    """
    xlist=list(map(int,x))
    if xlist[0] in [1,3,5]:
        sugu="Mees"
    elif xlist[0] in [2,4,6]:
        sugu="Naine"
    else:
        sugu="Viga"
    return sugu

def ksupa(x:str)->str:
    xlist=list(x)
    if xlist[0] in ["1","2"]:
        aasta="18"+xlist[1]+xlist[2]
    elif xlist[0] in ["3","4"]:
        aasta="19"+xlist[1]+xlist[2] 
    else:
        if int(xlist[1]+xlist[2])<=23:
            aasta="20"+xlist[1]+xlist[2]
        else:
            aasta="Viga"

    ku=xlist[3]+xlist[4]
    if int(ku) in range(1,13):
        kuu=ku
    else:
        kuu="Viga"

    pa=xlist[5]+xlist[6]
    if int(pa) in range(1,32):
        paev=pa
    else:
        paev="Viga"
    if aasta=="Viga" or kuu=="Viga" or paev=="Viga":
        sun="Viga"
    else:
        sun=aasta+"."+kuu+"."+paev
    return sun

def khaiga(x:str)->str:
    xlist=list(x)
    hai=xlist[7]+xlist[8]+xlist[9]
    if int(hai) in range(1,11): 
        haigla="Kuressaare Haigla"
    elif int(hai) in range(11,20): 
        h="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif int(hai) in range(21,221):
        haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif int(hai) in range(221,271): 
        haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif int(hai) in range(271,371):
        haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif int(hai) in range(371,421): 
        haigla="Narva Haigla"
    elif int(hai) in range(421,471):
        haigla="Pärnu Haigla"
    elif int(hai) in range(471,491):
        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif int(hai) in range(491,521):
        haigla="Järvamaa Haigla (Paide)"
    elif int(hai) in range(521,571):
        haigla="Rakvere, Tapa haigla"
    elif int(hai) in range(571,601):
        haigla="Valga Haigla"
    elif int(hai) in range(601,651): 
        haigla="Viljandi Haigla"
    elif int(hai) in range(651,701):
        haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        haigla="Viga"
    return haigla

def karv(x:str)->str:
    xlist=list(map(int,x))
    astme1=[1,2,3,4,5,6,7,8,9,1]
    astme2=[3,4,5,6,7,8,9,1,2,3]
    arv=0
    for i in range(10):
        arv+=xlist[i]*astme1[i]
    if arv%10==0:
        arv=0
        for i in range(10):
            arv+=xlist[i]*astme2[2]
        arv=arv-(arv//11)*11
    else:
        arv=arv-(arv//11)*11
    if arv==xlist[10]:
        x="Kontrollnumber on korras"
    else:
        x="Viga"
    return x

def ikood(x: str)->str:
    print(f"See on {ksugu(x)} ta on sündinud {ksupa(x)}, tema sünnikoht on {khaiga(x)}")

def ars(x:list)->list:
    xlist=list(x)
    xlist.sort()
    return xlist

def arg(x:list)->list:
    naised=[]
    mehed=[]
    for kood in x:
        kood_=list(kood)
        if int(kood_[0])%2==0:
            naised.append(kood)
        else: 
            mehed.append(kood)
    naised.extend(mehed)
    x=naised
    return x
