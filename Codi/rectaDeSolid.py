class RectaDeSolid:
    def __init__(self,nomRecta,idRecta,idSolidOnPertany,punt,angle):
        self.nom = nomRecta
        self.xCoord = punt[0]
        self.yCoord = punt[1]
        self.angle = angle
        self.idSolidOnPertany = idSolidOnPertany
        self.id = idRecta

    def __str__(self):
        return "{} (∈ sòlid {})  Punt = ({}, {})  Angle = {}  (id = {})".format(self.nom,self.idSolidOnPertany,self.xCoord,self.yCoord,self.angle,self.id)
