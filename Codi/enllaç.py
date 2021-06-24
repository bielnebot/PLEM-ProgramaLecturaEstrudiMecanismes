class Enllaç:
    def __init__(self,nom,tipus,nreF,nreM):
            self.nom= nom
            self.tipus = tipus
            self.nreIncognites = nreF + nreM
            self.nreF = nreF
            self.nreM = nreM


class EnllaçArticulacio(Enllaç):
    def __init__(self,nom,anclatge1,anclatge2):
        super().__init__(nom,"Articulació",2,0)
        self.anclatge1 = anclatge1 # són objectes PuntDeSolid
        self.anclatge2 = anclatge2
        self.idSolid1 = anclatge1.idSolidOnPertany
        self.idSolid2 = anclatge2.idSolidOnPertany

    def __str__(self):
        return "ARTICULACIÓ anomenada {}. Uneix [{}] amb [{}]. Introdueix {} F i {} M.".format(self.nom,self.anclatge1.idSolidOnPertany,self.anclatge2.idSolidOnPertany,self.nreF,self.nreM)


class EnllaçFix(Enllaç):
    def __init__(self,nom,solid):
        super().__init__(nom,"Enllaç fix",0,0) 
        self.quinSolid = solid
        self.idSolid1 = solid.id

    def __str__(self):
        return "Enllaç FIX anomenat {}. Fixa el sòlid [{}]. Introdueix {} F i {} M.".format(self.nom,self.quinSolid.nomSolid,self.nreF,self.nreM)

class EnllaçPrismatic(Enllaç):
    def __init__(self,nom,anclatge1,anclatge2):
        super().__init__(nom,"Prismàtic",1,1)
        self.anclatge1 = anclatge1 # són objectes PuntDeSolid
        self.anclatge2 = anclatge2
        self.idSolid1 = anclatge1.idSolidOnPertany
        self.idSolid2 = anclatge2.idSolidOnPertany

    def __str__(self):
        return "Enllaç PRISMÀTIC anomenat {}. Uneix [{}] amb [{}]. Introdueix {} F i {} M.".format(self.nom,self.anclatge1.idSolidOnPertany,self.anclatge2.idSolidOnPertany,self.nreF,self.nreM)
        
class EnllaçPiuGuia(Enllaç):
    def __init__(self,nom,anclatge1,anclatge2):
        super().__init__(nom,"Piu-guia.",1,0)
        self.anclatge1 = anclatge1 # són objectes PuntDeSolid
        self.anclatge2 = anclatge2
        self.idSolid1 = anclatge1.idSolidOnPertany
        self.idSolid2 = anclatge2.idSolidOnPertany

    def __str__(self):
        return "Enllaç PIU-GUIA anomenat {}. Uneix [{}] amb [{}]. Introdueix {} F i {} M.".format(self.nom,self.anclatge1.idSolidOnPertany,self.anclatge2.idSolidOnPertany,self.nreF,self.nreM)
        
class EnllaçTransmissio(Enllaç):
    def __init__(self,nom,solid1,solid2,tau,angleInicial):
        super().__init__(nom,"Transmissió",0,0) # revisar el (0,0)
        self.quinSolid1 = solid1
        self.quinSolid2 = solid2
        self.idSolid1 = solid1.id
        self.idSolid2 = solid2.id
        self.tau = tau # la relació de transmissió
        self.angleInicial = angleInicial

    def __str__(self):
        return "TRANSMISSIÓ anomenada {}. Uneix [{}] amb [{}]. Relació de transmissió = {}. Angle inicial = {}. Introdueix {} F i {} M.".format(self.nom,self.idSolid1,self.idSolid2,self.tau,self.angleInicial,self.nreF,self.nreM)
