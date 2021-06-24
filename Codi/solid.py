class Solid:
    def __init__(self,nom,nreIdentificacioPAM,nrePunts,nreRectes,massa,momentInerica,CM):
        self.nomSolid = nom
        self.id = nreIdentificacioPAM
        self.nrePunts = nrePunts
        self.nreRectes = nreRectes
        self.massa = massa
        self.momentInerica = momentInerica
        self.xCM = CM[0]
        self.yCM = CM[1]

    def __str__(self):
        return "Sòlid '{}' -->  {} punts, {} rectes, m = {} kg, I = {} Nm, CM = ({}, {})  (id = {})".format(self.nomSolid,self.nrePunts,self.nreRectes,self.massa,self.momentInerica,self.xCM,self.yCM,self.id)
