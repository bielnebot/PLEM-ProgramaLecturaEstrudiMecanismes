def LecturaPAM_to_LaTeX(diccionariDades):
    with open("LecturaPAM.tex","w") as f:
        #------------------- dicc idToNom ---------------------------------------
        idToNom = {}
        for nomSolid in diccionariDades["membres"]:
            idSolid,nrePunts,nreRectes,altreNumero,massa,momentInerica,xCM,yCM = diccionariDades["membres"][nomSolid]
            idToNom[idSolid] = nomSolid

##        print(idToNom)
        #------------------- CAPÇALERA ---------------------------------------
        f.write(r"\documentclass[11pt,a4paper]{article}")
        salta(f)
        f.write(r"\usepackage[top=24.99mm, bottom=24.99mm, left=1mm, right=1mm]{geometry}")
        salta(f)
        f.write(r"\righthyphenmin=62")
        salta(f)
        f.write(r"\begin{document}")
        salta(f)
        f.write(r"\title{\textbf{"+diccionariDades["general"]["nom"]+"}}")
        salta(f)
        f.write(r"\author{Generat amb PLEM}")
        salta(f)
        f.write(r"\date{}")
        salta(f)
        f.write(r"\maketitle")
        salta(f)
        #------------------- GENERAL ---------------------------------------
        f.write(r'\begin{center}')
        salta(f)
        f.write(r"\section*{General}")
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        f.write(r"\begin{center}")
        salta(f)
        f.write(r"\begin{tabular}{l c}")
        salta(f)
        f.write(r"\hline")
        salta(f)
        f.write(r'Nom del mecanisme     & '+diccionariDades["general"]["nom"]+r' \\ \hline')
        salta(f)
        f.write(r'Nre. membres          & '+str(diccionariDades["general"]["nreMembres"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. parells          & '+str(diccionariDades["general"]["nreParells"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. forces           & '+str(diccionariDades["general"]["nreForces"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. actuadors        & '+str(diccionariDades["general"]["nreActuadors"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. total de punts   & '+str(diccionariDades["general"]["nreTotalPunts"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. total de rectes  & '+str(diccionariDades["general"]["nreTotalRectes"])+r' \\ \hline')
        salta(f)
        if diccionariDades["general"]["presenciaGravetat"] == 1:
            f.write(r'Presencia de gravetat & Si \\ \hline')
        else:
            f.write(r'Presencia de gravetat & No \\ \hline')
        salta(f)
        f.write(r'$g$                   & '+str(diccionariDades["general"]["g"])+r' \\ \hline')
        salta(f)
        f.write(r'\end{tabular}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        #------------------- MEMBRES ---------------------------------------
        f.write(r'\begin{center}')
        salta(f)
        f.write(r'\section*{Membres}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        f.write(r'\begin{center}')
        salta(f)
        f.write(r'\begin{tabular}{c c c c c c c}')
        salta(f)
        f.write(r'\hline')
        salta(f)
        f.write(r'&\textbf{Nre. punts} & \textbf{Nre. rectes} & \textbf{massa} & \textbf{Ig} & \textbf{G1} & \textbf{G2} \\ \hline')
        salta(f)
        for nomMembre in diccionariDades["membres"]:
            id_del_Sòlid, nrePunts, nreRectes, altreNumero, massa, Ig, G1, G2 = diccionariDades["membres"][nomMembre]
            f.write(nomMembre+" (id = "+str(id_del_Sòlid)+") & "+str(nrePunts)+" & "+str(nreRectes)+" & "+str(massa)+" & "+str(Ig)+" & "+str(G1)+" & "+str(G2)+r" \\ \hline")
            salta(f)
        f.write(r'\end{tabular}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        if "punts" in diccionariDades:
            #------------------- PUNTS ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Punts}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Solid on pertany} & \textbf{$x$} & \textbf{$y$} \\ \hline')
            salta(f)
            for nomPunt in diccionariDades["punts"]:
                idPunt, solidAlQuePertany, xCoord, yCoord = diccionariDades["punts"][nomPunt]
                f.write(nomPunt.split(" ")[0]+" (id = "+str(idPunt)+") & "+str(solidAlQuePertany)+" & "+str(xCoord)+" & "+str(yCoord)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        if "rectes" in diccionariDades:
            #------------------- RECTES ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Rectes}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Solid on pertany} & \textbf{$x$} & \textbf{$y$} & \textbf{$\alpha$} \\ \hline')
            salta(f)
            for nomRecta in diccionariDades["rectes"]:
                idRecta, solidAlQuePertany, xCoord, yCoord, angle = diccionariDades["rectes"][nomRecta]
                f.write(nomRecta.split(" ")[0]+" (id = "+str(idRecta)+") & "+str(solidAlQuePertany)+" & "+str(xCoord)+" & "+str(yCoord)+" & "+str(angle)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        if "parells" in diccionariDades:
            #------------------- PARELLS ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Parells}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c c c c | c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Tipus 1} & \textbf{Tipus 2} & \textbf{Solid 1} & \textbf{Solid 2} & \textbf{Anc. 1} & \textbf{Anc. 2} & \textbf{$c_{1}$} & \textbf{$c_{2}$} & \textbf{$c_{3}$} & \textbf{$c_{4}$}  \\ \hline')
            salta(f)
            for nomParell in diccionariDades["parells"]:
                tipus1, tipus2, id1, id2, anc1, anc2,  c1, c2, c3, c4 = diccionariDades["parells"][nomParell]
                f.write(nomParell+" & "+str(tipus1)+" & "+str(tipus2)+" & "+str(id1)+" & "+str(id2)+" & "+str(anc1)+" & "+str(anc2)+" & "+str(c1)+" & "+str(c2)+" & "+str(c3)+" & "+str(c4)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        if "forces" in diccionariDades:
        #------------------- FORCES ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Forces}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c c c c | c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Tipus 1} & \textbf{Tipus 2} & \textbf{Solid 1} & \textbf{Solid 2} & \textbf{Anc. 1} & \textbf{Anc. 2} & \textbf{$c_{1}$} & \textbf{$c_{2}$} & \textbf{$c_{3}$} & \textbf{$c_{4}$}  \\ \hline')
            salta(f)
            for nomForça in diccionariDades["forces"]:
                tipus1, tipus2, id1, id2, anc1, anc2,  c1, c2, c3, c4 = diccionariDades["forces"][nomForça]
                f.write(nomForça+" & "+str(tipus1)+" & "+str(tipus2)+" & "+str(id1)+" & "+str(id2)+" & "+str(anc1)+" & "+str(anc2)+" & "+str(c1)+" & "+str(c2)+" & "+str(c3)+" & "+str(c4)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        if "actuadors" in diccionariDades:
            #------------------- ACTUADORS ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Actuadors}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c c c c | c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Tipus 1} & \textbf{Tipus 2} & \textbf{Solid 1} & \textbf{Solid 2} & \textbf{Anc. 1} & \textbf{Anc. 2} & \textbf{$c_{1}$} & \textbf{$c_{2}$} & \textbf{$c_{3}$} & \textbf{$c_{4}$}  \\ \hline')
            salta(f)
            for nomActuador in diccionariDades["actuadors"]:
                tipus1, tipus2, id1, id2, anc1, anc2,  c1, c2, c3, c4 = diccionariDades["actuadors"][nomActuador]
                f.write(nomActuador+" & "+str(tipus1)+" & "+str(tipus2)+" & "+str(id1)+" & "+str(id2)+" & "+str(anc1)+" & "+str(anc2)+" & "+str(c1)+" & "+str(c2)+" & "+str(c3)+" & "+str(c4)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        #------------------- CONFIGURACIÓ ---------------------------------------
        f.write(r'\begin{center}')
        salta(f)
        f.write(r'\section*{Configuracio inicial}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        f.write(r'\begin{center}')
        salta(f)
        f.write(r'\begin{tabular}{c c c c}')
        salta(f)
        f.write(r'\hline')
        salta(f)
        f.write(r'&\textbf{$x$} & \textbf{$y$} & \textbf{$\alpha$} \\ \hline')
        salta(f)
        for config in diccionariDades["configuracio"]:
            x,y,angle = diccionariDades["configuracio"][config]
            f.write(idToNom[int(config.split(" ")[-1])]+" & "+str(x)+" & "+str(y)+" & "+str(angle)+r" \\ \hline")
            salta(f)
        f.write(r'\end{tabular}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
       

        f.write(r"\end{document}")

def LecturaPAM_to_LaTeX_descodificat(diccionariDades):
    with open("LecturaPAM_descodificat.tex","w") as f:
        #------------------- dicc idToNom ---------------------------------------
        if "membres" in diccionariDades:
            idToNom = {0: "-"}
            for nomSolid in diccionariDades["membres"]:
                idSolid,nrePunts,nreRectes,altreNumero,massa,momentInerica,xCM,yCM = diccionariDades["membres"][nomSolid]
                idToNom[idSolid] = nomSolid
        #------------------- dicc idPuntToNom ---------------------------------------
        if "punts" in diccionariDades:
            idPuntToNom = {0: "-"}
            for nomPunt in diccionariDades["punts"]:
                idPunt,solidPertany,xCoord,yCoord = diccionariDades["punts"][nomPunt]
                idPuntToNom[idPunt] = nomPunt.split(" ")[0]
        #------------------- dicc idRectaToNom ---------------------------------------
        if "rectes" in diccionariDades:
            idRectaToNom = {0: "-"}
            for nomRecta in diccionariDades["rectes"]:
                idRecta,solidPertany,xCoord,yCoord, alfa = diccionariDades["rectes"][nomRecta]
                idRectaToNom[idRecta] = nomRecta.split(" ")[0]
        #------------------- dicc idEnllaToNom ---------------------------------------
        idEnllaToNom = {0: "-", 1: "Enll. fix", 2: "Articulacio", 4: "Prismatic", 5: "Piu-guia", 7: "Transmissio"}
        #------------------- dicc idForcToNom ---------------------------------------
        idForcToNom = {(1,1): "Torsor en eixos globals", (1,2): "Torsor en eixos del solid", (2,1): "Molla-amortidor lineal", (3,1): "Molla-amortidor torsional"}
        #------------------- dicc idActuadToNom ---------------------------------------
        idActuadToNom = {(3,1): "Lineal polinomic",
                         (3,2): "Lineal harmonic",
                         (3,3): "Lin. funcio rampa",
                         (3,4): "Lin. funcio Bezier C1",
                         (3,5): "Lin. funcio Bezier C2",
                         (6,1): "Angular polinomic",
                         (6,2): "Angular harmonic",
                         (6,3): "Ang. funcio rampa",
                         (6,4): "Ang. funcio Bezier C1",
                         (6,5): "Ang. funcio Bezier C2",}


        #------------------- CAPÇALERA ---------------------------------------
        f.write(r"\documentclass[11pt,a4paper]{article}")
        salta(f)
        f.write(r"\usepackage[top=24.99mm, bottom=24.99mm, left=1mm, right=1mm]{geometry}")
        salta(f)
        f.write(r"\righthyphenmin=62")
        salta(f)
        f.write(r"\begin{document}")
        salta(f)
        f.write(r"\title{\textbf{"+diccionariDades["general"]["nom"]+"}}")
        salta(f)
        f.write(r"\author{Generat amb PLEM}")
        salta(f)
        f.write(r"\date{}")
        salta(f)
        f.write(r"\maketitle")
        salta(f)
        #------------------- GENERAL ---------------------------------------
        f.write(r'\begin{center}')
        salta(f)
        f.write(r"\section*{General}")
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        f.write(r"\begin{center}")
        salta(f)
        f.write(r"\begin{tabular}{l c}")
        salta(f)
        f.write(r"\hline")
        salta(f)
        f.write(r'Nom del mecanisme     & '+diccionariDades["general"]["nom"]+r' \\ \hline')
        salta(f)
        f.write(r'Nre. membres          & '+str(diccionariDades["general"]["nreMembres"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. parells          & '+str(diccionariDades["general"]["nreParells"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. forces           & '+str(diccionariDades["general"]["nreForces"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. actuadors        & '+str(diccionariDades["general"]["nreActuadors"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. total de punts   & '+str(diccionariDades["general"]["nreTotalPunts"])+r' \\ \hline')
        salta(f)
        f.write(r'Nre. total de rectes  & '+str(diccionariDades["general"]["nreTotalRectes"])+r' \\ \hline')
        salta(f)
        if diccionariDades["general"]["presenciaGravetat"] == 1:
            f.write(r'Presencia de gravetat & Si \\ \hline')
        else:
            f.write(r'Presencia de gravetat & No \\ \hline')
        salta(f)
        f.write(r'$g$                   & '+str(diccionariDades["general"]["g"])+r' \\ \hline')
        salta(f)
        f.write(r'\end{tabular}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        #------------------- MEMBRES ---------------------------------------
        f.write(r'\begin{center}')
        salta(f)
        f.write(r'\section*{Membres}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        f.write(r'\begin{center}')
        salta(f)
        f.write(r'\begin{tabular}{c c c c c c c}')
        salta(f)
        f.write(r'\hline')
        salta(f)
        f.write(r'&\textbf{Nre. punts} & \textbf{Nre. rectes} & \textbf{massa} & \textbf{Ig} & \textbf{G1} & \textbf{G2} \\ \hline')
        salta(f)
        for nomMembre in diccionariDades["membres"]:
            id_del_Sòlid, nrePunts, nreRectes, altreNumero, massa, Ig, G1, G2 = diccionariDades["membres"][nomMembre]
            f.write(nomMembre+" (id = "+str(id_del_Sòlid)+") & "+str(nrePunts)+" & "+str(nreRectes)+" & "+str(massa)+" & "+str(Ig)+" & "+str(G1)+" & "+str(G2)+r" \\ \hline")
            salta(f)
        f.write(r'\end{tabular}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        if "punts" in diccionariDades:
            #------------------- PUNTS ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Punts}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Solid on pertany} & \textbf{$x$} & \textbf{$y$} \\ \hline')
            salta(f)
            for nomPunt in diccionariDades["punts"]:
                idPunt, solidAlQuePertany, xCoord, yCoord = diccionariDades["punts"][nomPunt]
                f.write(nomPunt.split(" ")[0]+" (id = "+str(idPunt)+") & "+idToNom[solidAlQuePertany]+" & "+str(xCoord)+" & "+str(yCoord)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        if "rectes" in diccionariDades:
            #------------------- RECTES ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Rectes}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Solid on pertany} & \textbf{$x$} & \textbf{$y$} & \textbf{$\alpha$} \\ \hline')
            salta(f)
            for nomRecta in diccionariDades["rectes"]:
                idRecta, solidAlQuePertany, xCoord, yCoord, angle = diccionariDades["rectes"][nomRecta]
                f.write(nomRecta.split(" ")[0]+" (id = "+str(idRecta)+") & "+idToNom[solidAlQuePertany]+" & "+str(xCoord)+" & "+str(yCoord)+" & "+str(angle)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        if "parells" in diccionariDades:
            #------------------- PARELLS ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Parells}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c c c | c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Tipus} & \textbf{Solid 1} & \textbf{Solid 2} & \textbf{Anc. 1} & \textbf{Anc. 2} & \textbf{$c_{1}$} & \textbf{$c_{2}$} & \textbf{$c_{3}$} & \textbf{$c_{4}$}  \\ \hline')
            salta(f)
            for nomParell in diccionariDades["parells"]:
                tipus1, tipus2, id1, id2, anc1, anc2,  c1, c2, c3, c4 = diccionariDades["parells"][nomParell]
                if tipus1 == 4:
                    ancoratges = idRectaToNom[anc1]+" & "+idRectaToNom[anc2]
                elif tipus1 == 5:
                    ancoratges = idRectaToNom[anc1]+" & "+idPuntToNom[anc2]
                elif tipus1 == 7:
                    ancoratges = "- & -"
                else:
                    ancoratges = idPuntToNom[anc1]+" & "+idPuntToNom[anc2]
                f.write(nomParell+" & "+idEnllaToNom[tipus1]+" & "+idToNom[id1]+" & "+idToNom[id2]+" & "+ancoratges+" & "+str(c1)+" & "+str(c2)+" & "+str(c3)+" & "+str(c4)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        if "forces" in diccionariDades:
        #------------------- FORCES ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Forces}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c c c | c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Tipus} & \textbf{Solid 1} & \textbf{Solid 2} & \textbf{Anc. 1} & \textbf{Anc. 2} & \textbf{$c_{1}$} & \textbf{$c_{2}$} & \textbf{$c_{3}$} & \textbf{$c_{4}$}  \\ \hline')
            salta(f)
            for nomForça in diccionariDades["forces"]:
                tipus1, tipus2, id1, id2, anc1, anc2,  c1, c2, c3, c4 = diccionariDades["forces"][nomForça]
                if (tipus1, tipus2) == (3,1):
                    
                    ancoratges = "- & -"
                else:
                    ancoratges = idPuntToNom[anc1]+" & "+idPuntToNom[anc2]
                f.write(nomForça+" & "+idForcToNom[(tipus1,tipus2)]+" & "+idToNom[id1]+" & "+idToNom[id2]+" & "+ancoratges+" & "+str(c1)+" & "+str(c2)+" & "+str(c3)+" & "+str(c4)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        if "actuadors" in diccionariDades:
            #------------------- ACTUADORS ---------------------------------------
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\section*{Actuadors}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
            f.write(r'\begin{center}')
            salta(f)
            f.write(r'\begin{tabular}{c c c c c c | c c c c}')
            salta(f)
            f.write(r'\hline')
            salta(f)
            f.write(r'&\textbf{Tipus} & \textbf{Solid 1} & \textbf{Solid 2} & \textbf{Anc. 1} & \textbf{Anc. 2} & \textbf{$c_{1}$} & \textbf{$c_{2}$} & \textbf{$c_{3}$} & \textbf{$c_{4}$}  \\ \hline')
            salta(f)
            for nomActuador in diccionariDades["actuadors"]:
                tipus1, tipus2, id1, id2, anc1, anc2,  c1, c2, c3, c4 = diccionariDades["actuadors"][nomActuador]
                if tipus1 == 6:
                    ancoratges = "- & -"
                else:
                    ancoratges = idPuntToNom[anc1]+" & "+idPuntToNom[anc2]
                f.write(nomActuador+" & "+idActuadToNom[(tipus1,tipus2)]+" & "+idToNom[id1]+" & "+idToNom[id2]+" & "+ancoratges+" & "+str(c1)+" & "+str(c2)+" & "+str(c3)+" & "+str(c4)+r" \\ \hline")
                salta(f)
            f.write(r'\end{tabular}')
            salta(f)
            f.write(r'\end{center}')
            salta(f)
        #------------------- CONFIGURACIÓ ---------------------------------------
        f.write(r'\begin{center}')
        salta(f)
        f.write(r'\section*{Configuracio inicial}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
        f.write(r'\begin{center}')
        salta(f)
        f.write(r'\begin{tabular}{c c c c}')
        salta(f)
        f.write(r'\hline')
        salta(f)
        f.write(r'&\textbf{$x$} & \textbf{$y$} & \textbf{$\alpha$} \\ \hline')
        salta(f)
        for config in diccionariDades["configuracio"]:
            x,y,angle = diccionariDades["configuracio"][config]
            f.write(idToNom[int(config.split(" ")[-1])]+" & "+str(x)+" & "+str(y)+" & "+str(angle)+r" \\ \hline")
            salta(f)
        f.write(r'\end{tabular}')
        salta(f)
        f.write(r'\end{center}')
        salta(f)
       






        f.write(r"\end{document}")



def LecturaPAM_to_LaTeX_Dibuixos(diccionariDades):
    with open("LecturaPAM_Dibuixos.tex","w") as f:
        #------------------- dicc idToNom ---------------------------------------
        idToNom = {}
        for nomSolid in diccionariDades["membres"]:
            idSolid,nrePunts,nreRectes,altreNumero,massa,momentInerica,xCM,yCM = diccionariDades["membres"][nomSolid]
            idToNom[idSolid] = nomSolid

##        print(idToNom)
        #------------------- CAPÇALERA ---------------------------------------
        f.write(r"\documentclass[11pt,a4paper]{article}")
        salta(f)
        f.write(r"\usepackage[top=24.99mm, bottom=24.99mm, left=1mm, right=1mm]{geometry}")
        salta(f)
        f.write(r"\usepackage{graphicx}")
        salta(f)
        f.write(r"\righthyphenmin=62")
        salta(f)
        f.write(r"\begin{document}")
        salta(f)
        f.write(r"\title{\textbf{"+diccionariDades["general"]["nom"]+"}}")
        salta(f)
        f.write(r"\author{Generat amb PLEM}")
        salta(f)
        f.write(r"\date{}")
        salta(f)
        f.write(r"\maketitle")
        salta(f)
        #------------------- GRAF DEL SISTEMA ---------------------------------------
        f.write(r"\begin{center}")
        salta(f)
        f.write(r'\section*{Graf del sistema}')
        salta(f)
        f.write(r"\end{center}")
        salta(f)
        f.write(r"\begin{tabular}{c}")
        salta(f)
        f.write(r"\includegraphics[width=0.9\linewidth]{fitxerGraf} \\")
        salta(f)
        f.write(r"\end{tabular}")
        salta(f)
        f.write(r"\newpage")
        salta(f)
        #------------------- TAULA DE MEMBRES ---------------------------------------
        f.write(r"\begin{center}")
        salta(f)
        f.write(r'\section*{Membres del sistema}')
        salta(f)
        f.write(r"\end{center}")
        salta(f)


        f.write(r"\begin{center}")
        salta(f)

        
              
        nreFiles = membresToFiles(diccionariDades["general"]["nreMembres"])
        llNoms = list(diccionariDades["membres"].keys())
##        print(diccionariDades["general"]["nreMembres"]," membres")
##        print(nreFiles," files")
##        print(llNoms)
        count = 0
        if diccionariDades["general"]["nreMembres"]%2 == 0: # if nre parell de membres
            for fila in range(1,nreFiles+1):
                f.write(r"\begin{tabular}{c|c}")
                salta(f)  
                f.write(r'\includegraphics[scale=0.6]{DibuixosMatlab/'+llNoms[count]+r'} & \includegraphics[scale=0.6]{DibuixosMatlab/'+llNoms[count+1]+r'} \\')
                salta(f)
                f.write(r"\end{tabular}")
                salta(f)
                count += 2
        else:
            for fila in range(1,nreFiles+1):
                if fila == nreFiles:
                    f.write(r"\begin{tabular}{c|c}")
                    salta(f)
                    f.write(r'\multicolumn{2}{c}{\includegraphics[scale=0.6]{DibuixosMatlab/'+llNoms[-1]+r'}} \\')
                    salta(f)
                    f.write(r"\end{tabular}")
                    salta(f)
                else:
                    f.write(r"\begin{tabular}{c|c}")
                    salta(f)
                    f.write(r'\includegraphics[scale=0.6]{DibuixosMatlab/'+llNoms[count]+r'} & \includegraphics[scale=0.6]{DibuixosMatlab/'+llNoms[count+1]+r'} \\')
                    salta(f)
                    f.write(r"\end{tabular}")
                    salta(f)
                count += 2

        
        
        f.write(r"\end{center}")
        salta(f)
        f.write(r"\end{document}")


def salta(f):
    f.write("\n")


def membresToFiles(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return int((n+1)/2)



