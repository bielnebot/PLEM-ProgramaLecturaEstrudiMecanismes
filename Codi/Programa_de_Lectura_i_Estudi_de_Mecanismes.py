from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
    # FUNCIONS
from llegirPAM import *
from generaObj import *
from generaGrafSys import *
from generaLatexLecturaPAM import *

####################################################

# Part gràfica (GUI)
finestra = Tk()
finestra.title('Programa de lectura i estudi de mecanismes')
finestra.geometry('900x200')
finestra.resizable(False, False)
canvas = Canvas(finestra, width = 900, height = 200)
canvas.pack()

def BuscaRutaPAM():
    ruta = tkinter.filedialog.askopenfilename()
    rutaPAM_entry.delete(0, END)
    rutaPAM_entry.insert(END, ruta)

def BuscaRutaMATLAB():
    ruta = tkinter.filedialog.askopenfilename()
    rutaMATLAB_entry.delete(0, END)
    rutaMATLAB_entry.insert(END, ruta)

def res():
    pass

def funcio_help():
    #Crea una finestra d'ajuda
    help_window = Toplevel(finestra)
    help_window.title("Ajuda")
    help_text = Text(help_window, width=130, height=35, bg="black", fg="skyblue",selectbackground="red")
    help_text.pack()
    help_text.insert(END,"Biel Nebot Cabrera\nbiel.nebot@gmail.com\n\nPrograma de lectura i estudi de mecanismes\nversió 1.1\n\n---------------------------------------------------------------------------------------\n\nPer consultar el funcionament del programa mireu a la carpeta LLEGEIX-ME\n\n--------------------------------------------------------------------------------------\n")


def EXECUTA():
    rutaPAM = rutaPAM_entry.get()
    rutaMATLAB = rutaMATLAB_entry.get()
    print(rutaMATLAB)
    if rutaPAM == "" or rutaMATLAB == "":
        error_falta_ruta()
    else:
        if rutaPAM[-4:] != ".pam":
            error_arxiu_no_pam()
        else:
            nomDelFitxer = rutaPAM
            diccDades = llegeixPAM(nomDelFitxer)
            show(diccDades)
            diccSistema = generaObjectes(diccDades)
            mostraObjectes(diccSistema)
            if on_or_off_Solids.get() == 1:
                # print("Farem solids")
                generaArxiusSolids(diccSistema,rutaMATLAB) # (els arxius .txt)
            if on_or_off_Graf.get() == 1:
                # print("Farem el graf")
                g = generaGraf(diccSistema) # (el graf en .pdf del sistema)
            if on_or_off_LATEX_v1.get() == 1:
                # print("Farem LATEX v1")
                LecturaPAM_to_LaTeX(diccDades) # (el .pdf amb la informació del sistema)
            if on_or_off_LATEX_v2.get() == 1:
                # print("Farem LATEX v2")
                LecturaPAM_to_LaTeX_descodificat(diccDades)
            if on_or_off_LATEX_v3.get() == 1:
                # print("Farem LATEX v3")
                LecturaPAM_to_LaTeX_Dibuixos(diccDades) # (el .pdf amb el graf i els membres dibuixats)   
            # print("End")


on_or_off_Solids = IntVar()
on_or_off_Graf = IntVar()
on_or_off_LATEX_v1 = IntVar()
on_or_off_LATEX_v2 = IntVar()
on_or_off_LATEX_v3 = IntVar()


# Labels
rutaPAM1_label = Label(finestra, text="Fitxer").place(x=10, y=10)
rutaPAM2_label = Label(finestra, text=".pam:", font=('TkDefaultFont', 9, 'bold')).place(x=43, y=10)
rutaMATLAB_label = Label(finestra, text="Fitxer de DibuixosMatlab:").place(x=10, y=40)
# Entrys
rutaPAM_entry = Entry(finestra, width=70)
rutaPAM_entry.place(x=89, y=10)
rutaMATLAB_entry = Entry(finestra, width=59)
rutaMATLAB_entry.place(x=155, y=40)
# Buttons
RUTA_PAM_button = Button(finestra, width=4, height=1, text="C:/...", bg="gray", fg="black", command = BuscaRutaPAM).place(x=519, y=7)
RUTA_MATLAB_button = Button(finestra, width=4, height=1, text="C:/...", bg="gray", fg="black", command = BuscaRutaMATLAB).place(x=519, y=37)
executaButton = Button(finestra, width=8, height=2, text="EXECUTA",bg='orange', command = EXECUTA).place(x=700, y=154)
AjudaButton = Button(finestra, width=7, height=1, text="Ajuda",bg='deepskyblue4', fg='white', command = funcio_help).place(x=50, y=120)
#Checkbutton
x1, y1 = 630, 20
checkBu_ArxiusSolids = Checkbutton(finestra, text="Genera els sòlids", variable = on_or_off_Solids, onvalue = 1, offvalue = 0, command=res)
checkBu_ArxiusSolids.place(x=x1, y=y1)
checkBu_ArxiuGraf = Checkbutton(finestra, text="Genera el graf", variable = on_or_off_Graf, onvalue = 1, offvalue = 0, command=res)
checkBu_ArxiuGraf.place(x=x1, y=y1+25)
checkBu_ArxiuGraf = Checkbutton(finestra, text="Genera el document sense descodificar", variable = on_or_off_LATEX_v1, onvalue = 1, offvalue = 0, command=res)
checkBu_ArxiuGraf.place(x=x1, y=y1+50)
checkBu_ArxiuGraf = Checkbutton(finestra, text="Genera el document descodificat", variable = on_or_off_LATEX_v2, onvalue = 1, offvalue = 0, command=res)
checkBu_ArxiuGraf.place(x=x1, y=y1+75)
checkBu_ArxiuGraf = Checkbutton(finestra, text="Genera el document de figures", variable = on_or_off_LATEX_v3, onvalue = 1, offvalue = 0, command=res)
checkBu_ArxiuGraf.place(x=x1, y=y1+100)

canvas.create_rectangle(620, 15, 870, 150,width=2)
Label(finestra, text="Programa de lectura i", font=("TkDefaultFont", 18)).place(x=210, y=95)
Label(finestra, text="estudi de mecanismes", font=("TkDefaultFont", 18)).place(x=210, y=130)
x1, y1 = 500-5,87
r = 15
k = 70 # distancia amb el de sobre
xshiftDD, yshiftDD = 30,17 # x/yshift del primer (DALT DRET)
xshiftDE, yshiftDE = 30,17 # x/yshift del primer (DALT ESQUERRE)
extraY = 35
xshiftBD, yshiftBD = 30,17 # x/yshift del primer (BAIX DRET)
xshiftBE, yshiftBE = 30,17 # x/yshift del primer (BAIX ESQUERRE)

#ARESTES
canvas.create_line((x1+(x1+r))/2,(y1+(y1+r))/2, (x1+xshiftBD+x1+r+xshiftBD)/2, (y1+yshiftBD+extraY+y1+r+yshiftBD+extraY)/2,width=3)# 1r-BD
canvas.create_line((x1+xshiftDD+x1+r+xshiftDD)/2,(y1+yshiftDD+y1+r+yshiftDD)/2, (x1+xshiftBD+x1+r+xshiftBD)/2, (y1+yshiftBD+extraY+y1+r+yshiftBD+extraY)/2,width=3)# DD-BD
canvas.create_line((x1+xshiftDD+x1+r+xshiftDD)/2,(y1+yshiftDD+y1+r+yshiftDD)/2, (x1+x1+r)/2, (y1+k+y1+r+k)/2,width=3)# DD-B
canvas.create_line((x1-xshiftDE+x1+r-xshiftDE)/2,(y1+yshiftDE+y1+r+yshiftDE)/2, (x1+x1+r)/2, (y1+k+y1+r+k)/2,width=3)# DE-B
canvas.create_line((x1-xshiftBE+x1+r-xshiftBE)/2,(y1+yshiftBE+extraY+y1+r+yshiftBE+extraY)/2, (x1+x1+r)/2, (y1+k+y1+r+k)/2,width=3)# BE-B
canvas.create_line((x1+xshiftBD+x1+r+xshiftBD)/2,(y1+yshiftBD+extraY+y1+r+yshiftBD+extraY)/2, (x1-xshiftBE+x1+r-xshiftBE)/2,(y1+yshiftBE+extraY+y1+r+yshiftBE+extraY)/2,width=3)# BE-BD
canvas.create_line((x1-xshiftBE+x1+r-xshiftBE)/2,(y1+yshiftBE+extraY+y1+r+yshiftBE+extraY)/2, (x1-xshiftDE+x1+r-xshiftDE)/2,(y1+yshiftDE+y1+r+yshiftDE)/2,width=3)# BE-DE
canvas.create_line((x1+(x1+r))/2,(y1+(y1+r))/2, (x1-xshiftDE+x1+r-xshiftDE)/2,(y1+yshiftDE+y1+r+yshiftDE)/2,width=3)# 1r-BD

#NODES
canvas.create_oval(x1,y1,x1+r,y1+r,fill="green",width=1)
##k = 70 # distancia amb el de sobre
canvas.create_oval(x1,y1+k,x1+r,y1+r+k,fill="green",width=1)
##xshiftDD, yshiftDD = 30,17 # x/yshift del primer (DALT DRET)
canvas.create_oval(x1+xshiftDD,y1+yshiftDD,x1+r+xshiftDD,y1+r+yshiftDD,fill="green",width=1)
##xshiftDE, yshiftDE = 30,17 # x/yshift del primer (DALT ESQUERRE)
canvas.create_oval(x1-xshiftDE,y1+yshiftDE,x1+r-xshiftDE,y1+r+yshiftDE,fill="green",width=1)
##extraY = 35
##xshiftBD, yshiftBD = 30,17 # x/yshift del primer (BAIX DRET)
canvas.create_oval(x1+xshiftBD,y1+yshiftBD+extraY,x1+r+xshiftBD,y1+r+yshiftBD+extraY,fill="green",width=1)
##xshiftBE, yshiftBE = 30,17 # x/yshift del primer (BAIX ESQUERRE)
canvas.create_oval(x1-xshiftBE,y1+yshiftBE+extraY,x1+r-xshiftBE,y1+r+yshiftBE+extraY,fill="green",width=1)

#############################################################
## Missatges d'error
def error_arxiu_no_pam():
    tkinter.messagebox.showerror("Programa de lectura i estudi de mecanismes", "Cal que el fitxer seleccionat tingui el format .pam")

def error_falta_ruta():
    tkinter.messagebox.showerror("Programa de lectura i estudi de mecanismes", "Falten rutes per afegir.")
#############################################################

##################################################

##nomDelFitxer = 
##nomDelFitxer = 
##nomDelFitxer = 
##nomDelFitxer = 
##nomDelFitxer = 
##nomDelFitxer = 
##nomDelFitxer = 
##nomDelFitxer = input("...")

##diccDades = llegeixPAM(nomDelFitxer)
##show(diccDades)

##diccSistema = generaObjectes(diccDades)
##mostraObjectes(diccSistema)

##generaArxiusSolids(diccSistema) # (els arxius .txt)

##g = generaGraf(diccSistema) # (el graf en .pdf del sistema) 

##LecturaPAM_to_LaTeX(diccDades) # (el .pdf amb la informació del sistema)
##LecturaPAM_to_LaTeX_descodificat(diccDades)
##LecturaPAM_to_LaTeX_Dibuixos(diccDades) # (el .pdf amb el graf i els membres dibuixats)

finestra.mainloop()
