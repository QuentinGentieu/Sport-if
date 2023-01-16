from tkinter import *  #On importe le module 
import tkinter as tk #On importe tk de tkinter
import time #Importation du module time 
from random import * #Importation du module random

listHautDuCorps = ["Pompes", "Gainage", "Position haute Statique", "Abdos groupe", "Corde a sauter", "Marche de l'ours", "Burpees"] #Creation d'une liste pour les exercices du haut du corps
listBasDuCorps = ["Releve de bassin", "Fire hydrant", "Squat bulgare", "Chaise", "Extension de mollets", "Fente sautee", "Pistol"] #Creation d'une liste pour les exercices du bas du corps
listToutLeCorps = ["Ciseaux", "Jumping Jack", "Leve de genou", "Reverse Snow Angel", "Saut etoile", "Super Wo Man", "V-Ups"] #Creation d'une liste pour les exercices de tout le corps

def raise_frame(frame): #fonction pour changer de frame
    frame.tkraise() #Le fait de passer d'une frame a une autre


def exoFacileHaut(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps 
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=pompesPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=gainagePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=tablePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=adbosGroupePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=cordeASauterPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=390, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=marcheDeLoursPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=burpeesPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=330, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listHautDuCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=21) #On set le temps sur 21secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=5): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(21500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants
              

    textHautDuCorpsF = Label(Exercice, text='Exercice facile du haut du corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire  
    textExoChangeHautDuCorpsF.place(x=100, y=200) #Place du Label pour afficher les exos qu'il faut faire chaque tour 
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste 
    textTempsChangeHautDuCorpsF.place(x=110, y=390) #Place du Label pour afficher les le temps qu'il reste
    textTourRestantHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le nombre de tour restant  
    textTourRestantHautDuCorpsF.place(x=510, y=390) #Place du Label pour afficher le nombre de tour restant 
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70) #Creation est place du bouton pour commencer la seance 
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100) #Place du bouton de retour en arriere


def exoMediumHaut(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=pompesPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=gainagePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=tablePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=adbosGroupePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=cordeASauterPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=390, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=marcheDeLoursPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=burpeesPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=330, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listHautDuCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=41) #On set le temps sur 41secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=8): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(41500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants

                
    textHautDuCorpsF = Label(Exercice, text='Exercice moyen du haut du corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire 
    textExoChangeHautDuCorpsF.place(x=100, y=200) #Place du Label pour afficher les exos qu'il faut faire chaque tour
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste 
    textTempsChangeHautDuCorpsF.place(x=110, y=390) #Place du Label pour afficher les le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le nombre de tour restant
    textTourRestantHautDuCorpsF.place(x=510, y=390) #Place du Label pour afficher le nombre de tour restant
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70) #Creation est place du bouton pour commencer la seance
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100) #Place du bouton de retour en arriere

def exoHardHaut(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=pompesPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=gainagePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=tablePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=adbosGroupePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=cordeASauterPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=390, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=marcheDeLoursPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=burpeesPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=330, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listHautDuCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=61) #On set le temps sur 61secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=12): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(61500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants

    textHautDuCorpsF = Label(Exercice, text='Exercice dur du haut du corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire  
    textExoChangeHautDuCorpsF.place(x=100, y=200)#Place du Label pour afficher les exos qu'il faut faire chaque tour
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste 
    textTempsChangeHautDuCorpsF.place(x=110, y=390)#Place du Label pour afficher les le temps qu'il reste
    textTourRestantHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le nombre de tour restant 
    textTourRestantHautDuCorpsF.place(x=510, y=390)#Place du Label pour afficher le nombre de tour restant
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70)#Creation est place du bouton pour commencer la seance
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100) #Place du bouton de retour en arriere

def exoFacileBas(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=releveDeBassinPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=fireHydrantPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=SquatBulgarePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=chaisePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=extensionDeMolletsPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=fenteSauteePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=400, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=pistolPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=400, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listBasDuCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=21) #On set le temps sur 21secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=5): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(21500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants
              

    textHautDuCorpsF = Label(Exercice, text='Exercice facile du bas du corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire   
    textExoChangeHautDuCorpsF.place(x=100, y=200)#Place du Label pour afficher les exos qu'il faut faire chaque tour
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste 
    textTempsChangeHautDuCorpsF.place(x=110, y=390)#Place du Label pour afficher les le temps qu'il reste
    textTourRestantHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le nombre de tour restant 
    textTourRestantHautDuCorpsF.place(x=510, y=390)#Place du Label pour afficher le nombre de tour restant
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70)#Creation est place du bouton pour commencer la seance
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100)#Place du bouton de retour en arriere


def exoMediumBas(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=releveDeBassinPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=fireHydrantPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=SquatBulgarePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=chaisePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=extensionDeMolletsPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=fenteSauteePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=400, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=pistolPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=400, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listBasDuCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=41) #On set le temps sur 21secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=8): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(41500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants
              

    textHautDuCorpsF = Label(Exercice, text='Exercice moyen du bas du corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire  
    textExoChangeHautDuCorpsF.place(x=100, y=200)#Place du Label pour afficher les exos qu'il faut faire chaque tour
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste 
    textTempsChangeHautDuCorpsF.place(x=110, y=390)#Place du Label pour afficher les le temps qu'il reste
    textTourRestantHautDuCorpsF = Label(Exercice, text='')#Creation du Label pour dire le nombre de tour restant 
    textTourRestantHautDuCorpsF.place(x=510, y=390)#Place du Label pour afficher le nombre de tour restant
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70)#Creation est place du bouton pour commencer la seance
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100)#Place du bouton de retour en arriere

def exoHardBas(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=releveDeBassinPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=fireHydrantPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=300, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=SquatBulgarePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=chaisePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=extensionDeMolletsPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=350, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=fenteSauteePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=400, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=pistolPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=400, y=70) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listBasDuCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=61) #On set le temps sur 21secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=12): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(61500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants
              

    textHautDuCorpsF = Label(Exercice, text='Exercice dur du bas du corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire  
    textExoChangeHautDuCorpsF.place(x=100, y=200)#Place du Label pour afficher les exos qu'il faut faire chaque tour
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste 
    textTempsChangeHautDuCorpsF.place(x=110, y=390)#Place du Label pour afficher les le temps qu'il reste
    textTourRestantHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le nombre de tour restant  
    textTourRestantHautDuCorpsF.place(x=510, y=390)#Place du Label pour afficher le nombre de tour restant
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70)#Creation est place du bouton pour commencer la seance
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100)#Place du bouton de retour en arriere

def exoFacileTout(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=ciseauxPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=jumpingJacksPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=leveeDeGenouPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=reverseSnowAngelPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=sautEtoilePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=superWoManPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=vUpsPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=360, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listToutLeCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=21) #On set le temps sur 21secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=5): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(21500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants
              

    textHautDuCorpsF = Label(Exercice, text='Exercice facile de tout le corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire  
    textExoChangeHautDuCorpsF.place(x=100, y=200)#Place du Label pour afficher les exos qu'il faut faire chaque tour
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste 
    textTempsChangeHautDuCorpsF.place(x=110, y=390)#Place du Label pour afficher les le temps qu'il reste
    textTourRestantHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le nombre de tour restant 
    textTourRestantHautDuCorpsF.place(x=510, y=390)#Place du Label pour afficher le nombre de tour restant
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70)#Creation est place du bouton pour commencer la seance
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100)#Place du bouton de retour en arriere


def exoMediumTout(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=ciseauxPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=jumpingJacksPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=leveeDeGenouPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=reverseSnowAngelPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=sautEtoilePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=superWoManPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=vUpsPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=360, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listToutLeCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=41) #On set le temps sur 21secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=8): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(41500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants
              

    textHautDuCorpsF = Label(Exercice, text='Exercice moyen de tout le corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire  
    textExoChangeHautDuCorpsF.place(x=100, y=200)#Place du Label pour afficher les exos qu'il faut faire chaque tour
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste
    textTempsChangeHautDuCorpsF.place(x=110, y=390)#Place du Label pour afficher les le temps qu'il reste
    textTourRestantHautDuCorpsF = Label(Exercice, text='')#Creation du Label pour dire le nombre de tour restant  
    textTourRestantHautDuCorpsF.place(x=510, y=390)#Place du Label pour afficher le nombre de tour restant
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70)#Creation est place du bouton pour commencer la seance
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100)#Place du bouton de retour en arriere

def exoHardTout(): #Creation de la fonction pour les exo facile du haut du corps

    def start(t=3): #Creation de la fonction pour le timer avec t regler sur 3
        global i #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        i = 1 #On affecte 1 a "i"
        if i == 1: #Si i est egal a 1 alors on execute 
            textTempsChangeHautDuCorpsF.config(text=str(t)) #On change le texte du label par le temps
            if t > 0: #Si le temps et superieur a 0 alors 
                window.after(1000, start, t - 1) #on dedeuis toutes les 1s 1 à t
            if t == 0: #Si t est egal a 0 alors 
                x = randint(0, 6) #On genere un nombre aleatoire dans x
                if x == 0: #si x est egal a 0 alors              
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener 
                    imageLabel = Label(Exercice, image=ciseauxPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=120) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 1: #si x est egal a 1 alors                    
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=jumpingJacksPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 2:   #si x est egal a 2 alors                  
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=leveeDeGenouPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 3:#si x est egal a 3 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=reverseSnowAngelPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                if x == 4:#si x est egal a 4 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=sautEtoilePhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 5:#si x est egal a 5 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=superWoManPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=380, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée 
                if x == 6:#si x est egal a 6 alors 
                    fondLabel = Label(Exercice, image=fondPhoto) #On place le fond gris pour que il n'y est pas les anciennes image derriere les nouvelles pour les gener
                    imageLabel = Label(Exercice, image=vUpsPhoto) #On place l'image pour aider la personne a faire l'exercice correctement 
                    fondLabel.place(x=300, y=70) #On place le fond en un premier temps pour pas pietiner l'image d'aide au coordonnée  
                    imageLabel.place(x=360, y=100) #On place l'image en un second temps pour aller sur le fond au coordonnée  
                    
                textExoChangeHautDuCorpsF.config(text=listToutLeCorps[x]) #On met l'exercice par rapport au chiffre du ramdom pour l'index de la liste
                start(t=61) #On set le temps sur 21secondes pour l'exerice suivant
                textTempsChangeHautDuCorpsF.config(text=str(t)) #On remt le temps a jour dans le label

    def final(w=12): #Creation de la fonction pour le timer avec t regler sur 3
        global f #On informe de la creation de cette variable et qu'elle est utilisé a l'interieur de la fonction
        f = 1 #On affecte 1 a "f"
        if f == 1: #Si f est egal a 1 alors 
            textTourRestantHautDuCorpsF.config(text=str(w)) #On met le timer a jour 
            if w > 0: #Si w est superier a 0 alors 
                window.after(61500, final, w - 1) #Toutes les 21.5 secondes on enleve 1 
            if w == 0: #Si w est egal a 0 alors
                textTourRestantHautDuCorpsF.config(text="Vous pouvez vous arreter") #On recommande d'arreter la seance pour les debutants
              

    textHautDuCorpsF = Label(Exercice, text='Exercice dur de tout le corps').place(x=300, y=10) #Creation du Label pour la fenetre du menu avec le titre 
    textExoHautDuCorpsF = Label(Exercice, text='Exercice :').place(x=100, y=150) #Creation du Label pour dire l'exerice a faire
    textTempsHautDuCorpsF = Label(Exercice, text='Temps :').place(x=100, y=350) #Creation du Label pour dire le temps qu'il reste 
    textTourRestantHautDuCorpsF = Label(Exercice, text='Tours restants recommandé :').place(x=500, y=350) #Creation du Label pour dire le temps qu'il reste 
    textExoChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire l'exerice a faire  
    textExoChangeHautDuCorpsF.place(x=100, y=200)#Place du Label pour afficher les exos qu'il faut faire chaque tour
    textTempsChangeHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le temps qu'il reste
    textTempsChangeHautDuCorpsF.place(x=110, y=390)#Place du Label pour afficher les le temps qu'il reste
    textTourRestantHautDuCorpsF = Label(Exercice, text='') #Creation du Label pour dire le nombre de tour restant 
    textTourRestantHautDuCorpsF.place(x=510, y=390)#Place du Label pour afficher le nombre de tour restant
    startSeance = Button(Exercice, text="commencer la seance", command=lambda:[start(), final()]).place(x=320, y=70)#Creation est place du bouton pour commencer la seance
    backB5 = Button(Exercice, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente
    backB5.place(x=330, y=100)#Place du bouton de retour en arriere

window = Tk() #creation de la fenetre principal
window.geometry('800x500') #creation de la taille de la fenetre principale
window.resizable(width=False, height=False) #On fait en sorte que on peut pas relger la taille de la fenetre avec la souris

Accueil = Frame(window, padx=22) #creation de la frame d'acceuil
Seance = Frame(window, padx=22) #creation de la frame des seances
Options = Frame(window, padx=22) #creation de la frame d'options-

hautDuCorpsChoix = Frame(window, padx=22) #creation de la frame pour les exos du haut du corps
basDuCorpsChoix = Frame(window, padx=22) #creation de la frame pour les exos du bas du corps
toutLeCorpsChoix = Frame(window, padx=22) #creation de la frame pour les exos du tout le corps

Exercice = Frame(window, padx=22) #Creation de la frame pour les differents exos


for frame in (Accueil, Seance, Options, hautDuCorpsChoix, basDuCorpsChoix, toutLeCorpsChoix, Exercice): #Declaration de toutes les frames
    frame.grid(row=0, column=0, sticky='news') #On grind toutes les frames

mainLabel = Label(Accueil, text='Sport-if(you want)') #Creation du Label pour la fenetre du menu avec le titre 
newSeanceB = Button(Accueil, text='Nouvelle seance', command=lambda:raise_frame(Seance)) #Creation du boutton pour acceder a une nouvelle seance 
optionsB = Button(Accueil, text='Options', command=lambda:raise_frame(Options)) #Creation du boutton pour acceder au menu des options
quitB = Button(Accueil, text='Quitter', command=window.destroy) #Creation du boutton pour quitter la frame principale

chooseLabel = Label(Seance, text='Chosir un domaine') #Creation du label pour le choix de l'exercice
hautDuCorpsB = Button(Seance, text='Haut du corps', bg='#ffc100', padx=50,pady=200, command=lambda:raise_frame(hautDuCorpsChoix)) #Creation du boutton pour la seance de haut du corps
basDuCorpsmB = Button(Seance, text='Bas du corps', bg='#ff7400', padx=50,pady=200, command=lambda:raise_frame(basDuCorpsChoix))  #Creation du boutton pour la seance de bas du corps
toutLeCorpsB = Button(Seance, text='Tout le corps', bg='#ff0000', padx=50 ,pady=200, command=lambda:raise_frame(toutLeCorpsChoix))  #Creation du boutton pour la seance de tout le corps
backB1 = Button(Seance, text='Page precedente', command=lambda:raise_frame(Accueil)) #Creation du boutton pour aller a la page precedente


hautDuCorpsLabel = Label(hautDuCorpsChoix, text="Choisir la difficulte pour les exercices haut du corps") #Creation du label pour le titre des choix pour la difficulte des exos de haut du corps
easyHautDuCorpsB = Button(hautDuCorpsChoix, text='Facile', bg='#ffc100', padx=204, pady=50, command=lambda:[raise_frame(Exercice), exoFacileHaut()]) #Creation du button pour le choix facile de la seance du haut du corps
mediumHautDuCorpsB = Button(hautDuCorpsChoix, text='Moyen', bg='#ff7400', padx=200, pady=50, command=lambda:[raise_frame(Exercice), exoMediumHaut()])  #Creation du button pour le choix medium de la seance du haut du corps
hardHautDuCorpsB = Button(hautDuCorpsChoix, text='Difficile', bg='#ff0000', padx=199, pady=50, command=lambda:[raise_frame(Exercice), exoHardHaut()]) #Creation du button pour le choix difficile de la seance du haut du corps
backB2 = Button(hautDuCorpsChoix, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente


basDuCorpsLabel = Label(basDuCorpsChoix, text="Choisir la difficulte pour les exercices bas du corps") #Creation du label pour le titre des choix pour la difficulte des exos de bas du corps
easyBasDuCorpsB = Button(basDuCorpsChoix, text='Facile', bg='#ffc100', padx=204, pady=50, command=lambda:[raise_frame(Exercice), exoFacileBas()]) #Creation du button pour le choix facile de la seance du bas du corps
mediumBasDuCorpsB = Button(basDuCorpsChoix, text='Moyen', bg='#ff7400', padx=200 ,pady=50, command=lambda:[raise_frame(Exercice), exoMediumBas()])  #Creation du button pour le choix medium de la seance du bas du corps
hardBasDuCorpsB = Button(basDuCorpsChoix, text='Difficile', bg='#ff0000', padx=199 ,pady=50, command=lambda:[raise_frame(Exercice), exoHardBas()]) #Creation du button pour le choix difficile de la seance du bas du corps
backB3 = Button(basDuCorpsChoix, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente


toutLeCorpsLabel = Label(toutLeCorpsChoix, text="Choisir la difficulte pour les exercices tout le corps") #Creation du label pour le titre des choix pour la difficulte des exos de tout le corps
easyToutLeCorpsB = Button(toutLeCorpsChoix, text='Facile', bg='#ffc100', padx=204, pady=50, command=lambda:[raise_frame(Exercice), exoFacileTout()]) #Creation du button pour le choix facile de la seance de tout le corps
mediumToutLeCorpsB = Button(toutLeCorpsChoix, text='Moyen', bg='#ff7400', padx=200 ,pady=50, command=lambda:[raise_frame(Exercice), exoMediumTout()])  #Creation du button pour le choix medium de la seance du tout le corps
hardToutLeCorpsB = Button(toutLeCorpsChoix, text='Difficile', bg='#ff0000', padx=199 ,pady=50, command=lambda:[raise_frame(Exercice), exoHardTout()]) #Creation du button pour le choix difficile de la seance du tout le corps
backB4 = Button(toutLeCorpsChoix, text='Page precedente', command=lambda:raise_frame(Seance)) #Creation du boutton pour aller a la page precedente


optionsLabel = Label(Options, text='Options') #Creation du label pour le titre de la frame pour les options
backB = Button(Options, text='Revenir a l accueil', command=lambda:raise_frame(Accueil)) #Creation du boutton pour aller en arriere dans le menu des options


mainLabel.pack(padx=0, pady=0) #pack du label pour le titre principal
newSeanceB.pack(padx=330, pady=100) #pack du boutton pour acceder au seance disponible

optionsB.pack() #pack du boutton du menu pour acceder au menu des options
quitB.pack(padx=330, pady=110) #pack pour le boutton pour quitter la fenetre principal



fondPhoto = PhotoImage(file="Images/Fond/fond.PNG") #Importation et assignation d'une image pour l'application 

tablePhoto = PhotoImage(file="Images/HautDuCorps/Table.PNG")#Importation et assignation d'une image pour l'application 
pompesPhoto = PhotoImage(file="Images/HautDuCorps/Pompes.PNG")#Importation et assignation d'une image pour l'application 
gainagePhoto = PhotoImage(file="Images/HautDuCorps/Planche.PNG")#Importation et assignation d'une image pour l'application 
adbosGroupePhoto = PhotoImage(file="Images/HautDuCorps/Abdos groupe.PNG")#Importation et assignation d'une image pour l'application 
cordeASauterPhoto = PhotoImage(file="Images/HautDuCorps/Corde a sauter.PNG")#Importation et assignation d'une image pour l'application 
marcheDeLoursPhoto = PhotoImage(file="Images/HautDuCorps/Marche de l'ours.PNG")#Importation et assignation d'une image pour l'application 
burpeesPhoto = PhotoImage(file="Images/HautDuCorps/Burpees.PNG")#Importation et assignation d'une image pour l'application 

chaisePhoto = PhotoImage(file="Images/BasDuCorps/Chaise.PNG")#Importation et assignation d'une image pour l'application 
extensionDeMolletsPhoto = PhotoImage(file="Images/BasDuCorps/Extension de mollets.PNG")#Importation et assignation d'une image pour l'application 
fenteSauteePhoto = PhotoImage(file="Images/BasDuCorps/Fente sautee.PNG")#Importation et assignation d'une image pour l'application 
fireHydrantPhoto = PhotoImage(file="Images/BasDuCorps/Fire hydrant.PNG")#Importation et assignation d'une image pour l'application 
pistolPhoto = PhotoImage(file="Images/BasDuCorps/Pistols.PNG")#Importation et assignation d'une image pour l'application 
releveDeBassinPhoto = PhotoImage(file="Images/BasDuCorps/Releve de bassin.PNG")#Importation et assignation d'une image pour l'application 
SquatBulgarePhoto = PhotoImage(file="Images/BasDuCorps/Squat bulgare.PNG")#Importation et assignation d'une image pour l'application 

ciseauxPhoto = PhotoImage(file="Images/ToutLeCorps/Ciseaux.PNG")#Importation et assignation d'une image pour l'application 
jumpingJacksPhoto = PhotoImage(file="Images/ToutLeCorps/Jumping jack.PNG")#Importation et assignation d'une image pour l'application 
leveeDeGenouPhoto = PhotoImage(file="Images/ToutLeCorps/Levee de genou.PNG")#Importation et assignation d'une image pour l'application 
reverseSnowAngelPhoto = PhotoImage(file="Images/ToutLeCorps/Reverse snow angel.PNG")#Importation et assignation d'une image pour l'application 
sautEtoilePhoto = PhotoImage(file="Images/ToutLeCorps/Saut etoile.PNG")#Importation et assignation d'une image pour l'application 
superWoManPhoto = PhotoImage(file="Images/ToutLeCorps/Super Wo man.PNG")#Importation et assignation d'une image pour l'application 
vUpsPhoto = PhotoImage(file="Images/ToutLeCorps/V ups.PNG")#Importation et assignation d'une image pour l'application 



chooseLabel.pack(padx=0, pady=0) #pack du label pour le titre du choix de la seance
hautDuCorpsB.place(x=30, y=30) #place pour le boutton pour la seance de haut du corps
basDuCorpsmB.place(x=286, y=30) #place pour le boutton pour la seance de bas du corps
toutLeCorpsB.place(x=533, y=30) #place pour le boutton pour la seance de tout le corps


hautDuCorpsLabel.pack() #pack du label pour le choix de la difficulte de la seance du haut du corps
easyHautDuCorpsB.place(x=180, y=30) #place pour le boutton pour la seance de haut du corps
mediumHautDuCorpsB.place(x=180, y=180) #place pour le boutton pour la seance de bas du corps
hardHautDuCorpsB.place(x=180, y=330) #place pour le boutton pour la seance de tout le corps

basDuCorpsLabel.pack() #pack du label pour le choix de la difficulte de la seance du bas du corps
easyBasDuCorpsB.place(x=180, y=30) #place pour le boutton pour la seance de haut du corps
mediumBasDuCorpsB.place(x=180, y=180) #place pour le boutton pour la seance de bas du corps
hardBasDuCorpsB.place(x=180, y=330) #place pour le boutton pour la seance de tout le corps

toutLeCorpsLabel.pack() #pack du label pour le choix de la difficulte de la seance du tout le corps
easyToutLeCorpsB.place(x=180, y=30) #place pour le boutton pour la seance de haut du corps
mediumToutLeCorpsB.place(x=180, y=180) #place pour le boutton pour la seance de bas du corps
hardToutLeCorpsB.place(x=180, y=330) #place pour le boutton pour la seance de tout le corps

optionsLabel.pack() #pack du label pour le menu des options
backB.place(x=670, y=470) #pack du boutton pour retourner a la page precedente
backB1.place(x=670, y=470) #pack du boutton pour retourner a la page precedente
backB2.place(x=670, y=470) #pack du boutton pour retourner a la page precedente
backB3.place(x=670, y=470) #pack du boutton pour retourner a la page precedente
backB4.place(x=670, y=470) #pack du boutton pour retourner a la page precedente

raise_frame(Accueil) #pack des frames

window.mainloop() #main de la fenetre principal

