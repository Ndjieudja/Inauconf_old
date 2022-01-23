# !/usr/bin/env/python3.5
# --*-- encoding: utf8 --*--

# In this place we are puting all necessary to handly event of different windows to 
# to diplay rusultin app like edit test app

from tkinter import *
from shuffle import*


class Windows (Tk):
    def __init__(self, doc=str()):
        Tk.__init__(self)
        self.doc = doc
        self.geometry("700x600")
        self.title('Inauconf')

        self.can = Canvas(self, width=700, height=600, bg='green')
        self.lab = Label(self, text=self.doc, width = 500, height = 400, bg="white")
        self.lab.pack()
        self.entry = Text(self.can, width=700)
        self.entry.configure(width=20)
        self.button = Button(self.can, text='Go', command=None)

        scrol = Scrollbar(self.can, command = self.view)
        scrol.pack(expand = YES, fill = Y)

        self.can.pack()
        self.mainloop()
        self.quit()

    def view(self):
        for string in self.doc:
            if string == "\n":
                scroll_width = len(self.doc[:string])

        return scroll_width


"Widget composite associant un champ d'entrée avec une boîte de liste"
class ComboBox(Frame):

    def __init__(self, boss, item='', items=[], command ='', width =10, listSize =5):
        Frame.__init__(self, boss)
        # constructeur de la classe parente
        # (<boss> est la réf. du widget 'maître')
        self.items =items
        # items à placer dans la boîte de liste
        self.command =command
        # fonction à invoquer après clic ou <enter>
        self.item =item
        # item entré ou sélectionné
        # Champ d'entrée :
        self.entree =Entry(self, width =width)
        # largeur en caractères
        self.entree.insert(END, item)
        self.entree.bind("<Return>", self.sortieE)
        self.entree.pack(side =TOP)
        # Boîte de liste, munie d'un 'ascenseur' (scroll bar) :
        cadreLB =Frame(self)
        # cadre pour l'ensemble des 2
        self.bListe =Listbox(cadreLB, height =listSize, width =width-1)
        scrol =Scrollbar(cadreLB, command =self.bListe.yview)
        self.bListe.config(yscrollcommand =scrol.set)
        self.bListe.bind("<ButtonRelease-1>", self.sortieL)
        self.bListe.pack(side =LEFT)
        scrol.pack(expand =YES, fill =Y)
        cadreLB.pack()

        # Remplissage de la boîte de liste avec les items fournis :

        for it in items:
            self.bListe.insert(END, it)
            #Widgets complémentaires, widgets c

    def sortieL(self, event =None):

        # Extraire de la liste l'item qui a été sélectionné :
        index =self.bListe.curselection()

        # renvoie un tuple d'index
        ind0 =int(index[0])

        # on ne garde que le premier
        self.item =self.items[ind0]

        # Actualiser le champ d'entrée avec l'item choisi :
        self.entree.delete(0, END)
        self.entree.insert(END, self.item)

        # Exécuter la commande indiquée, avec l'item choisi comme argument :
        self.command(self.item)

    def sortieE(self, event =None):
        # Exécuter la commande indiquée, avec l'argument-item encodé tel quel :
        self.command(self.entree.get())

    def get(self):
        # Renvoyer le dernier item sélectionné dans la boîte de liste
        return self.item


class ScrolledText(Frame):
    """Widget composite, associant un widget Text et une barre de défilement"""
    
    def __init__(self, baseFont ="Times", width =50, height =25):
        Frame.__init__(self, bd =2, relief =SUNKEN)
        self.text =Text(self, font =baseFont, bg ='ivory', bd =1,
        width =width, height =height)
        scroll =Scrollbar(self, bd =1, command =self.text.yview)
        self.text.configure(yscrollcommand =scroll.set)
        self.text.pack(side =LEFT, expand =YES, fill =BOTH, padx =2, pady =2)
        scroll.pack(side =RIGHT, expand =NO, fill =Y, padx =2, pady =2)

    def importFichier(self, fichier, encodage ="Utf8"):
        "insertion d'un texte dans le widget, à partir d'un fichier"

        of =open(fichier, "r", encoding =encodage)
        lignes =of.readlines()
        of.close()
        for li in lignes:
            self.text.insert(END, li)

    def chercheCible(event=None):
        "défilement du texte jusqu'à la balise <cible>, grâce à la méthode see()"
        index = st.text.tag_nextrange('cible', '0.0', END)
        st.text.see(index[0])
        
        ### Programme principal : fenêtre avec un libellé et un 'ScrolledText' ###
        fen =Tk()
        lib =Label(fen, text ="Widget composite : Text + Scrollbar",
        font ="Times 14 bold italic", fg ="navy")
        lib.pack(padx =10, pady =4)
        st =ScrolledText(fen, baseFont="Helvetica 12 normal", width =40, height =10)
        st.pack(expand =YES, fill =BOTH, padx =8, pady =8)
        
        # Définition de balises, liaison d'un événement <clic du bouton droit> :
        st.text.tag_configure("titre", foreground ="brown",
        font ="Helvetica 11 bold italic")
        st.text.tag_configure("lien", foreground ="blue",
        font ="Helvetica 11 bold")
        st.text.tag_configure("cible", foreground ="forest green",
        font ="Times 11 bold")
        st.text.tag_bind("lien", "<Button-3>", chercheCible)
        titre ="""Le Corbeau et le Renard par Jean de la Fontaine, auteur français\n"""
        auteur ="""Jean de la Fontaine écrivain français (1621-1695) célèbre pour ses Contes en vers, et surtout ses Fables, publiées de 1668 à 1694."""
        
        # Remplissage du widget Text (2 techniques) :
        st.importFichier("CorbRenard.txt", encodage ="Latin1")
        st.text.insert("0.0", titre, "titre")
        st.text.insert(END, auteur, "cible")
        
        # Insertion d'une image :
        photo =PhotoImage(file= "penguin.gif")
        st.text.image_create("6.14", image =photo)
        
        # Ajout d'une balise supplémentaire :
        st.text.tag_add("lien", "2.4", "2.23")
        fen.mainloop()


if __name__ == '__main__':

    def changeCoul(col):
        fen.configure(background = col)

    def changeLabel():
        lab.configure(text = combo.get())

    couleurs = ('navy', 'royal blue', 'steelblue1', 'cadet blue','lawn green', 'forest green', 'yellow', 'dark red',\
    'grey80','grey60', 'grey40', 'grey20', 'pink')

    # test to diplaye cript doc iin Label   
    e = EncriptAll()
    with open('shuffle.py', 'r') as file:
            cript = e.cript(file.read())

    wind = Windows(cript)
    '''fen =Tk()
    combo =ComboBox(fen, item ="néant", items =couleurs, command =changeCoul,width =15, listSize =6)
    combo.grid(row =1, columnspan =2, padx =10, pady =10)
    bou = Button(fen, text ="Test", command =changeLabel)
    bou.grid(row =2, column =0, padx =8, pady =8)
    lab = Label(fen, text ="Bonjour", bg ="ivory", width =15)
    lab.grid(row =2, column =1, padx =8)
    fen.mainloop()
    '''

