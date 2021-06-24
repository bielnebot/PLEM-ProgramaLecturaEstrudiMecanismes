class Actuador:
    def __init__(self,nom,tipus,):
        self.nom = nom
        self.tipus = tipus


class ActuadorLineal(Actuador):
    def __init__(self,nom,anclatge1,anclatge2):
        super().__init__(nom,"Lineal")
        self.anclatge1 = anclatge1 # són objectes PuntDeSolid
        self.anclatge2 = anclatge2
        self.idSolid1 = anclatge1.idSolidOnPertany 
        self.idSolid2 = anclatge2.idSolidOnPertany

    def __str__(self):
        return "Actuador LINEAL anomenat {}. Uneix [{}] amb [{}]. Introdueix ? F i ? M.".format(self.nom,self.anclatge1.idSolidOnPertany,self.anclatge2.idSolidOnPertany)

    
class ActuadorAngular(Actuador):
    def __init__(self,nom,solid1,solid2):
        super().__init__(nom,"Angular")
        self.solid1 = solid1
        self.solid2 = solid2
        self.idSolid1 = solid1.id
        self.idSolid2 = solid2.id

    def __str__(self):
        return "Actuador ANGULAR anomenat {}. Uneix [{}] amb [{}]. Introdueix 0 F i 1 M.".format(self.nom,self.solid1.id,self.solid2.id)
