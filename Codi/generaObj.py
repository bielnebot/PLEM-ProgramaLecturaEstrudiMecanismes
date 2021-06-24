import solid
import puntDeSolid
import rectaDeSolid
import enllaç
import actuador
import forces

def generaObjectes(diccionariDades):
    # retorna un diccionari d = {<nom sòlid>: <sòlid>, ...}
    # un diccionari de tot el sistema
  
    dMembres = {}
    idToNom = {}
    for nomSolid in diccionariDades["membres"]:
        idSolid,nrePunts,nreRectes,altreNumero,massa,momentInerica,xCM,yCM = diccionariDades["membres"][nomSolid]
        dMembres[idSolid] = solid.Solid(nomSolid,idSolid,nrePunts,nreRectes,massa,momentInerica,[xCM, yCM])
        idToNom[idSolid] = nomSolid

    dPunts = {0: puntDeSolid.PuntDeSolid("puntZero",0,0,[0,0])} 
    if "punts" in diccionariDades:
        for nomPunt in diccionariDades["punts"]:
            idPunt,idSolid,xCoord,yCoord = diccionariDades["punts"][nomPunt]
            dPunts[idPunt] = puntDeSolid.PuntDeSolid(nomPunt.split(" ")[0],idPunt,idSolid,[xCoord,yCoord])

    dRectes = {}
    if "rectes" in diccionariDades:   
        for nomRecta in diccionariDades["rectes"]:
            idRecta,idSolid,xCoord,yCoord,angle = diccionariDades["rectes"][nomRecta]
            dRectes[idRecta] = rectaDeSolid.RectaDeSolid(nomRecta.split(" ")[0],idRecta,idSolid,[xCoord,yCoord],angle)

    dEnllaços = {}
    if "parells" in diccionariDades:
        for nomEnllaç in diccionariDades["parells"]:
            tipus1, tipus2, idSolid1, idSolid2, idPunt1, idPunt2, c1, c2, c3, c4 = diccionariDades["parells"][nomEnllaç]
            if tipus1 == 1:
                dEnllaços[nomEnllaç] = enllaç.EnllaçFix(nomEnllaç,dMembres[idSolid1])
            elif tipus1 == 2:
                dEnllaços[nomEnllaç] = enllaç.EnllaçArticulacio(nomEnllaç,dPunts[idPunt1],dPunts[idPunt2])
            elif tipus1 == 4:
                dEnllaços[nomEnllaç] = enllaç.EnllaçPrismatic(nomEnllaç,dRectes[idPunt1],dRectes[idPunt2])
            elif tipus1 == 5:
                dEnllaços[nomEnllaç] = enllaç.EnllaçPiuGuia(nomEnllaç,dRectes[idPunt1],dPunts[idPunt2])
            elif tipus1 == 7:
                dEnllaços[nomEnllaç] = enllaç.EnllaçTransmissio(nomEnllaç,dMembres[idSolid1],dMembres[idSolid2],c1,c2)
            else:
                pass

    dActuadors = {}
    if "actuadors" in diccionariDades:
        for nomActuador in diccionariDades["actuadors"]:
            tipus1, tipus2, idSolid1, idSolid2, idPunt1, idPunt2,  c1, c2, c3, c4 = diccionariDades["actuadors"][nomActuador]
            if tipus1 == 3:
                dActuadors[nomActuador] = actuador.ActuadorLineal(nomActuador,dPunts[idPunt1],dPunts[idPunt2])
            else:
                dActuadors[nomActuador] = actuador.ActuadorAngular(nomActuador,dMembres[idSolid1],dMembres[idSolid2])

    dForces = {}
    if "forces" in diccionariDades:
        for nomForça in diccionariDades["forces"]:
            tipus1, tipus2, idSolid1, idSolid2, idPunt1, idPunt2,  c1, c2, c3, c4 = diccionariDades["forces"][nomForça]
            if tipus1 == 1: # Torsor en eixos globals/Torsor en eixos del solid
                dForces[nomForça] = forces.Força(nomForça,dPunts[idPunt1])
            else:
                pass # cal implementar forces entre membres


    return {"general": diccionariDades["general"], "membres": dMembres, "idToNomMembres": idToNom, "punts":dPunts, "rectes":dRectes, "enllaços": dEnllaços, "actuadors": dActuadors, "forces": dForces}



def generaArxiusSolids(diccionariDades,cami):
    # la llista de noms de membres
    with open(preparaCami(cami)+"/nomsMembres.txt","w") as f:
        for idSolid in diccionariDades["membres"]:
            nom = diccionariDades["membres"][idSolid].nomSolid
            f.write(nom+"\n")
            with open(preparaCami(cami)+"/"+nom+"ArxiusPerRepresentar.txt","w") as f_membre:
                for idPunt in diccionariDades["punts"]:
                    if diccionariDades["punts"][idPunt].idSolidOnPertany == idSolid:
    ##                    f.write("P: "+diccionariDades["punts"][idPunt].nom+" "+str(diccionariDades["punts"][idPunt].xCoord)+" "+str(diccionariDades["punts"][idPunt].yCoord)+"\n")
                        f_membre.write("1 "+str(diccionariDades["punts"][idPunt].xCoord)+" "+str(diccionariDades["punts"][idPunt].yCoord)+" 999\n")
                f_membre.write("999 999 999 999\n")
                for idRecta in diccionariDades["rectes"]:
                    if diccionariDades["rectes"][idRecta].idSolidOnPertany == idSolid:
    ##                    f.write("R: "+diccionariDades["rectes"][idRecta].nom+" "+str(diccionariDades["rectes"][idRecta].xCoord)+" "+str(diccionariDades["rectes"][idRecta].yCoord)+" "+str(diccionariDades["rectes"][idRecta].angle)+"\n")
                        f_membre.write("2 "+str(diccionariDades["rectes"][idRecta].xCoord)+" "+str(diccionariDades["rectes"][idRecta].yCoord)+" "+str(diccionariDades["rectes"][idRecta].angle)+"\n")
                

def preparaCami(cami):
    ll = cami.split("/")
    arxiuNoServeix = ll.pop(-1)
    return "/".join(ll)
    
    
def mostraObjectes(dSYS):
    for apartat in dSYS:
        print("\n"+apartat+" = {")
        for clau in dSYS[apartat]:
            print(clau,":   ",dSYS[apartat][clau])
        print("}")
