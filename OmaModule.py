def iPikk(x:str)->bool:
    """Funktsioon tagastab True, kui iPikk on 11 sümbolid
    :param str x: Inimese isikukood
    :rtype: bool
    """
    y=False
    if x.isdigit() and len(x)==11:
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
        haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif int(hai) in range(21,221):
        haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif int(hai) in range(221,270): 
        haigla=Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)
    #271...370 
    #= Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla
    #371...420 
    #= Narva Haigla
    #421...470 
    #= Pärnu Haigla
    #471...490 
    #= Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla
    #491...520 
    #= Järvamaa Haigla (Paide)
    #521...570 
    #= Rakvere, Tapa haigla
    #571...600 
    #= Valga Haigla
    #601...650 
    #= Viljandi Haigla
    #651...700
    #= Lõuna-Eesti Haigla (Võru), Põlva Haigla 