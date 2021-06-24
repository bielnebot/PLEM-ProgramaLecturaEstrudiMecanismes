class PuntDeSolid:
    def __init__(self,nomPunt,idPunt,idSolidOnPertany,punt):
        self.nom = nomPunt
        self.xCoord = punt[0]
        self.yCoord = punt[1]
        self.idSolidOnPertany = idSolidOnPertany
        self.id = idPunt

    def __str__(self):
        return "{} (∈ sòlid {}) = ({}, {})  (id = {})".format(self.nom,self.idSolidOnPertany,self.xCoord,self.yCoord,self.id)
