def llegeixPAM(nom):
    with open(nom,"r") as fitxerPAM:
        apartats = {}
        apartatActual = ""
        for linia in fitxerPAM:
            linia = depurarLinia(linia)
            if linia == []:
                linia = ["***","res"]
##            print(linia)
            if linia[0] == "***":
                apartatActual = linia[1]
                if apartatActual == "general":
                    pass
                else:
                    continue # perquè salti a la següent iteració del for i no executi el codi de sota sobre una linia títol d'apartat

#########################################################
#                COMPROVACIÓ APARTAT
#########################################################

# ----------------------- GENERAL ------------------------
            if apartatActual == "general":
                if "general" not in apartats:
                    apartats["general"] = {"nom":linia[3],"altreNumero":int(linia[4])}
                else:
                    apartats["general"]["nreMembres"] = int(linia[0])
                    apartats["general"]["nreParells"] = int(linia[1])
                    apartats["general"]["nreForces"] = int(linia[2])
                    apartats["general"]["nreActuadors"] = int(linia[3])
                    apartats["general"]["nreTotalPunts"] = int(linia[4])
                    apartats["general"]["nreTotalRectes"] = int(linia[5])
                    apartats["general"]["presenciaGravetat"] = int(linia[6])
                    apartats["general"]["g"] = float(linia[7])

# ----------------------- MEMBRES ------------------------
            elif apartatActual == "membres":
                if "membres" not in apartats:
                    nom,nrePunts,nreRectes,altreNumero = linia[0][1:],linia[1],linia[2],linia[3]
                    linia = depurarLinia(fitxerPAM.readline())
                    massa,Ig,G1,G2=linia
                    apartats["membres"] = {nom: [1, int(nrePunts),int(nreRectes),int(altreNumero),float(massa),float(Ig),float(G1),float(G2)]}
#                                        {nom: [id_del_Sòlid nrePunts, nreRectes, altreNumero, massa, Ig, G1, G2]}
                    comptador = 1
                else:
                    comptador +=1 # que correspon a id_del_Sòlid
                    nom = linia[0][len(str(comptador)):]
                    nrePunts,nreRectes,altreNumero = linia[1],linia[2],linia[3]
                    linia = depurarLinia(fitxerPAM.readline())
                    massa,Ig,G1,G2=linia
                    apartats["membres"][nom] = [comptador, int(nrePunts),int(nreRectes),int(altreNumero),float(massa),float(Ig),float(G1),float(G2)]

# ----------------------- PUNTS ------------------------
            elif apartatActual == "punts":
                if "punts" not in apartats:
                    linia = depurarMenys(linia)
                    apartats["punts"] = {linia[0][1:]+" del sòlid "+linia[1]:[1, int(linia[1]), float(linia[2]), float(linia[3])]}
#                                       {<nom del punt>    <sòlid al que pertany>:  [sòlid al que pertany, xCoord, yCoord]}
                    comptador = 1
                else:
                    linia = depurarMenys(linia)
                    comptador += 1
                    nom = linia[0][len(str(comptador)):]
                    apartats["punts"][nom+" del sòlid "+linia[1]] = [comptador, int(linia[1]), float(linia[2]), float(linia[3])]

# ----------------------- RECTES ------------------------                
            elif apartatActual == "rectes":
                if "rectes" not in apartats:
                    linia = depurarMenys(linia)
                    nom,nreSolid,x,y = linia[0][1:],linia[1],linia[2],linia[3]
                    angle = fitxerPAM.readline() # es podria posar depurarLinia(fitxerPAM.readline())
                    apartats["rectes"] = {nom+" del sòlid "+nreSolid: [1, int(nreSolid), float(x), float(y), float(angle)]}
#                                        {<nom de la recta>    <sòlid al que pertany>:  [sòlid al que pertany, xCoord, yCoord, angle]}
                    comptador = 1
                else:
                    linia = depurarMenys(linia)
                    comptador += 1
                    nom = linia[0][len(str(comptador)):]
                    nreSolid,x,y = linia[1:]
                    angle = fitxerPAM.readline()
                    apartats["rectes"][nom+" del sòlid "+nreSolid] = [comptador, int(nreSolid), float(x), float(y), float(angle)]
# ----------------------- PARELLS ------------------------            
            elif apartatActual == "parells":
                if "parells" not in apartats:
                    nom = linia[0][1:]
                    tipus1,tipus2,id1,id2,anc1,anc2 = linia[1:]
                    c1,c2,c3,c4 = depurarLinia(fitxerPAM.readline())
                    apartats["parells"] = {nom: [int(tipus1),int(tipus2),int(id1),int(id2),int(anc1),int(anc2),float(c1),float(c2),float(c3),float(c4)]}
                    comptador = 1
                else:
                    linia = depurarMenys(linia)
                    comptador += 1
                    nom = linia[0][len(str(comptador)):]
                    tipus1,tipus2,id1,id2,anc1,anc2 = linia[1:]
                    c1,c2,c3,c4 = depurarLinia(fitxerPAM.readline())
                    apartats["parells"][nom] = [int(tipus1),int(tipus2),int(id1),int(id2),int(anc1),int(anc2),float(c1),float(c2),float(c3),float(c4)]

# ----------------------- FORCES ------------------------            
            elif apartatActual == "forces":
                if "forces" not in apartats:
                    nom = linia[0][1:]
                    tipus1,tipus2,id1,id2,anc1,anc2 = linia[1:]
                    c1,c2,c3,c4 = depurarLinia(fitxerPAM.readline())
                    apartats["forces"] = {nom: [int(tipus1),int(tipus2),int(id1),int(id2),int(anc1),int(anc2),float(c1),float(c2),float(c3),float(c4)]}
                    comptador = 1
                else:
                    linia = depurarMenys(linia)
                    comptador += 1
                    nom = linia[0][len(str(comptador)):]
                    tipus1,tipus2,id1,id2,anc1,anc2 = linia[1:]
                    c1,c2,c3,c4 = depurarLinia(fitxerPAM.readline())
                    apartats["forces"][nom] = [int(tipus1),int(tipus2),int(id1),int(id2),int(anc1),int(anc2),float(c1),float(c2),float(c3),float(c4)]

# ----------------------- ACTUADORS ------------------------            
            elif apartatActual == "actuadors":
                if "actuadors" not in apartats:
                    nom = linia[0][1:]
                    tipus1,tipus2,id1,id2,anc1,anc2 = linia[1:]
                    c1,c2,c3,c4 = depurarLinia(fitxerPAM.readline())
                    apartats["actuadors"] = {nom: [int(tipus1),int(tipus2),int(id1),int(id2),int(anc1),int(anc2),float(c1),float(c2),float(c3),float(c4)]}
                    comptador = 1
                else:
                    linia = depurarMenys(linia)
                    comptador += 1
                    nom = linia[0][len(str(comptador)):]
                    tipus1,tipus2,id1,id2,anc1,anc2 = linia[1:]
                    c1,c2,c3,c4 = depurarLinia(fitxerPAM.readline())
                    apartats["actuadors"][nom] = [int(tipus1),int(tipus2),int(id1),int(id2),int(anc1),int(anc2),float(c1),float(c2),float(c3),float(c4)]


# ----------------------- CONFIGURACIÓ ------------------------            
            elif apartatActual == "configuracio":
                if "configuracio" not in apartats:
                    linia = depurarMenys(linia)
                    nreSolid,x,y,angle = linia
                    apartats["configuracio"] = {"Sòlid número "+nreSolid: [float(x),float(y),float(angle)]}
                else:
                    linia = depurarMenys(linia)
                    nreSolid,x,y,angle = linia
                    apartats["configuracio"]["Sòlid número "+nreSolid] = [float(x),float(y),float(angle)]

# ----------------------- VELOCITATS ------------------------            
            elif apartatActual == "velocitats":
                pass
# ----------------------- GEOMETRIA ------------------------            
            elif apartatActual == "geometria":
                pass
# ----------------------- ANÀLISI ------------------------            
            elif apartatActual == "anàlisi":
                apartats["anàlisi"] = {"altreNumero": linia[0],"tempsDeCàlcul":linia[1], "incrementDeTemos":linia[2]}
# ----------------------- RES ------------------------            
            elif apartatActual == "res":
                pass

        return(apartats)


def depurarLinia(linia):
    linia = linia.strip().split(" ")
    new = [x for x in linia if x != ""]
    return new

def depurarMenys(llista):
    # per quan els números són negatius
    # sinó es salta l'espai
    if "-" in llista[1]: # pel signe menys (PUNTS I RECTES)
        new = [llista[0], llista[1].split("-")[0], "-"+llista[1].split("-")[1]]
        new = new + llista[2:]
        return new
    elif "-" in llista[0]: # per l'apartat CONFIGURACIÓ
        new = [llista[0].split("-")[0], "-"+llista[0].split("-")[1]]
        new = new + llista[1:]
        return new
    elif len(llista) == 3: # pels 0,... (PUNTS, RECTES i CONFIGURACIÓ)
        if "0." in llista[0]:
            new = [llista[0].split("0.")[0], "0."+llista[0].split("0.")[1]]
            new = new + llista[1:]
        elif "0." in llista[1]:
            new = [llista[0], llista[1].split("0.")[0], "0."+llista[1].split("0.")[1]]
            new = new + llista[2:]
        return new
    else:
        return llista


def show(dicc):
    # per fer un print del diccionari i veure l'estructura visualment
    for x in dicc:
            print(x)
            for y in dicc[x]:
                    print("    "+str(y)+" -> "+str(dicc[x][y]))



