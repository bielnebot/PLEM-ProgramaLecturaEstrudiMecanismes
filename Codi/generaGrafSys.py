import networkx as nx
import matplotlib.pyplot as plt
import math
import diccionariEdges

def generaGraf(sistema):
    edge_labels = {}
    labels = {}
    llMembresMassa = {}
    llEnllaçActuador = {}
    llEnllaç = {}
    llForcesAplicades = {}
    g = nx.Graph()
    
    # els nodes
    for soli in sistema["membres"]:
        # afegim nodes
        nom = sistema["idToNomMembres"][soli]
        g.add_node(nom, idSolid = sistema["membres"][soli].id)
        # SI TENEN MASSA
        if abs(sistema["membres"][soli].massa) > 0.0001:
            llMembresMassa[sistema["membres"][soli].id] = sistema["membres"][soli].nomSolid
        # ara els labels
        labels[sistema["membres"][soli].nomSolid] = sistema["membres"][soli].nomSolid+"\n (id = "+str(sistema["membres"][soli].id)+")"

    # SI TENEN ACTUADOR
    for act in sistema["actuadors"]:
        id1,id2 = sistema["actuadors"][act].idSolid1, sistema["actuadors"][act].idSolid2
        llEnllaçActuador[(id1,id2)] = sistema["actuadors"][act].nom
        llEnllaçActuador[(id2,id1)] = sistema["actuadors"][act].nom

    # SI TENEN ENLLAÇ
    for enlla in sistema["enllaços"]:
        if sistema["enllaços"][enlla].tipus != "Enllaç fix":
            llEnllaç[(sistema["enllaços"][enlla].idSolid1,sistema["enllaços"][enlla].idSolid2)] = sistema["enllaços"][enlla].nom
            llEnllaç[(sistema["enllaços"][enlla].idSolid2,sistema["enllaços"][enlla].idSolid1)] = sistema["enllaços"][enlla].nom
            
    # SI TENEN FORÇA
    for força in sistema["forces"]:
        llForcesAplicades[sistema["forces"][força].idSolid] = sistema["forces"][força].nom

    print("ENLLAÇ:    ",llEnllaç,"\n")    
    print("MASSA:     ",llMembresMassa,"\n")
    print("ACTUADIR:   ",llEnllaçActuador,"\n")
    print("FORCES:     ",llForcesAplicades,"\n")

# enllaç ---> "e"
# pes ------> "p"
# actuador -> "a"
# força ----> "f"

    combinacionsMembres = diccionariEdges.rangeNodes(sistema["general"]["nreMembres"])
    print(combinacionsMembres)
    # diccEnllaçosParaula = {}

    for membreOrigen,segonMembre in combinacionsMembres:
        nomOrigen = sistema["membres"][membreOrigen].nomSolid
        nomSegon = sistema["membres"][segonMembre].nomSolid
        paraula = ""
        termesMembreOrigen = {}
        if (membreOrigen,segonMembre) in llEnllaç:
            paraula += "e"
            enlla = llEnllaç[(membreOrigen,segonMembre)] # el nom (clau del dicc sistema)
            termesMembreOrigen["e"] = enlla+" ("+str(sistema["enllaços"][enlla].nreF)+" F i "+str(sistema["enllaços"][enlla].nreM)+" M)"
        if (membreOrigen in llMembresMassa and nomSegon == "Bancada") or (segonMembre in llMembresMassa and nomOrigen == "Bancada"):
            paraula += "p"
            termesMembreOrigen["p"] = "pes"
        if (membreOrigen,segonMembre) in llEnllaçActuador:
            paraula += "a"
            termesMembreOrigen["a"] = llEnllaçActuador[(id1,id2)]
        if(membreOrigen in llForcesAplicades and nomSegon == "Bancada") or (segonMembre in llForcesAplicades and nomOrigen == "Bancada"):
            paraula += "f"
            if nomOrigen != "Bancada":
                termesMembreOrigen["f"] = llForcesAplicades[membreOrigen]
            else:
                termesMembreOrigen["f"] = llForcesAplicades[segonMembre]

        if paraula != "":
            g.add_edge(sistema["idToNomMembres"][membreOrigen],sistema["idToNomMembres"][segonMembre], realcions = termesMembreOrigen)
            edge_labels[(sistema["idToNomMembres"][membreOrigen],sistema["idToNomMembres"][segonMembre])] = diccionariEdges.diccToStr(termesMembreOrigen)
       
        # diccEnllaçosParaula[(membreOrigen,segonMembre)] = paraula           
    # print("final",diccEnllaçosParaula)

       
    pos = calculaPuntsCercle(sistema["membres"])
    plt.figure(figsize=(10.0, 6.0)) # per fixar la mida de la finestra

    # nodes i edges
    nx.draw_networkx(g,pos,with_labels=False,node_size= 1000,alpha = 0.9,linewidths = 3,width = 2,node_color = "g",edge_color ="gray")
    # lebels nodes
    nx.draw_networkx_labels(g,pos,labels,font_family = "serif",font_weight ="bold")
    # labels edges
    nx.draw_networkx_edge_labels(g,pos,edge_labels,font_family = "serif",label_pos=0.5)
    
    plt.axis('off')
    plt.savefig("fitxerGraf.pdf")
    # plt.show()
    return g


def calculaPuntsCercle(dMembres):
    # les distribueix en un cercle
    d = {}
    nreMembres = len(dMembres)
    increment = 2*math.pi/nreMembres
    i = 0
    fact = 0.2
    for mem in dMembres:
        d[dMembres[mem].nomSolid] = (fact*math.cos(i*increment)+10, fact*math.sin(i*increment)+10)
        i += 1
    return d
