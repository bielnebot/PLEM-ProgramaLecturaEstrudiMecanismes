class Força:
    def __init__(self,nom,anclatge):
        self.nom = nom
        self.anclatge = anclatge
        self.idSolid = anclatge.idSolidOnPertany

    def __str__(self):
        return "Força (torsor en eixos globals) anomenada {}. Aplicada al punt {}, sòlid {}.".format(self.nom,self.anclatge.nom,self.idSolid)
