#vytvoreni tridy Zvira
class Zvire:
    def __init__(self, jmeno:str, druh:str, vaha:int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    
    def __str__(self):
        return (f"{self.jmeno} je {self.druh} a váží {self.vaha} kg.")
    
    def export_to_dict(self):
        slovnik = {"jmeno": self.jmeno, "druh": self.druh, "vaha": self.vaha}
        return slovnik

#vytvoreni tridy Zamestnanec
class Zamestnanec:
    def __init__(self, cele_jmeno:str, rocni_plat:int, pozice:str):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice
    
    def __str__(self):
        return f"Zaměstnanec {self.cele_jmeno} pracuje na pozici {self.pozice} a vydělává {self.rocni_plat} Kč ročně."

    #vrati inicialy zamestnance
    def ziskej_inicialy(self):
       rozdeleno = self.cele_jmeno.split(" ")
       inicialy = rozdeleno[0][0] + "." + rozdeleno[1][0] + "."
       return inicialy

#vytvoreni tridy Reditel (dedicnost od tridy Zamestnanec)
class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno:str, rocni_plat:int, oblibene_zvire:Zvire, pozice:str="Reditel"):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.oblibene_zvire = oblibene_zvire

#vytvoreni tridy Zoo
class Zoo:
    def __init__(self, jmeno:str, adresa:str, reditel: Reditel, zamestnanci:list[Zamestnanec], zvirata:list[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata
    
    #vrati celkovou vahu vsech zvirat v zoo
    def vaha_vsech_zvirat_v_zoo(self):
        celkova_vaha = 0
        for zvire in self.zvirata:
            celkova_vaha += zvire.vaha
        return celkova_vaha

    #vrati, jake jsou mesicni naklady na zamestnance
    def mesicni_naklady_na_zamestnance(self):
        mesicni_naklady_zamestnanci = 0
        for zamestnanec in self.zamestnanci:
            mesicni_naklady_zamestnanci += zamestnanec.rocni_plat/12
        
        reditel = self.reditel
        mesicni_naklady = mesicni_naklady_zamestnanci + reditel.rocni_plat/12
        return mesicni_naklady

#funkce, ktera prevede slovnik se zviraty na seznam objektu tridy Zvire
def slovnik_na_tridu_zvirata(seznam_zvirat):
    seznam_trid = []
    for slovnik in seznam_zvirat:
        seznam_trid.append(Zvire(slovnik["jmeno"], slovnik["druh"], slovnik["vaha"]))
    return seznam_trid

#funkce, ktera prevede slovnik se zamestnanci na seznam objektu tridy Zamestnanec
def slovnik_na_tridu_zamestnanec(seznam_zamestnancu):
    seznam_trid = []
    for slovnik in seznam_zamestnancu:
        seznam_trid.append(Zamestnanec(slovnik["cele_jmeno"], slovnik["rocni_plat"], slovnik["pozice"]))
    return seznam_trid

zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},

]

#prevod seznamu na seznam objetu
seznam_zvirata = slovnik_na_tridu_zvirata(zvirata_dict)

zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

#previd sezanmu na seznam objektu
seznam_zamestnanci = slovnik_na_tridu_zamestnanec(zamestnanci_dict)