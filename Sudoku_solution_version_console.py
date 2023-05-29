import os
import shutil


def creer_fichier_solution(nom_grille,Liste_solutions):
    """Cette fonction crée un fichier contenant les solutions du sudoku en prenant en paramètre le nom de la grille et la liste des solutions de cette grille"""
    
    nom_dossier = "solutions "+nom_grille
    
    if os.path.exists(nom_dossier):
        print("Un dossier ",nom_dossier," existait déjà et a été supprimé") #écrase le fichier si il existe deja
        shutil.rmtree(nom_dossier)
    os.mkdir(nom_dossier)
    
    
    for i in range(len(Liste_solutions)):
        fichier = open("./"+nom_dossier+"/"+"solutions"+ str(i+1)+".txt", "w") #ajoute les solutions dans le fichier
        for y in Liste_solutions[i]:
            chaine = ''
            for x in y:
                chaine+= str(x)
            chaine+="\n"
            fichier.write(chaine)
        fichier.close()

    return


    
def afficher_solution_console(nom_fichier):
    """Cette fonction permet d'afficher les solutions d'un sudoku en prenant en paramètre le nom du fichier"""
    
    grille = recup_info_grille(nom_fichier)
    if verif_grille(grille) == True:
    
        Liste_solutions = calcul_solutions(grille,[])
    
        for grille in Liste_solutions:
            affichage_console(grille)
    
    else :
        print("la grille contient une erreur et ne possède pas de solution")



def verif_grille(grille):
    """Cette fonction vérifie si une grille de sudoku est valide en prenant en paramètre une grille de sudoku"""
    
    
    
    
    for x in range(9):
        Liste=[i for i in range(1,10)]
        for y in range(9):
            if grille[y][x] in Liste:
                Liste.remove(grille[y][x])
            elif grille[y][x]!=0:
                print("Grille impossible plusieurs fois la même valeur dans une seule ligne")
                return False
                
    for y in range(9):
        Liste=[i for i in range(1,10)]
        for x in range(9):
            if grille[y][x] in Liste:
                Liste.remove(grille[y][x])
            elif grille[y][x]!=0:
                print("Grille impossible plusieurs fois la même valeur dans une seule colonne")
                return False
    
    Liste_carre = [[p,i] for p in range(3) for i in range(3)]
    
    for carre in Liste_carre:
        
        carre_x,carre_y = carre
        
        Liste=[i for i in range(1,10)]
        for x in range(3):
            for y in range(3):
                if grille[carre_y*3+y][carre_x*3+x] in Liste:
                    Liste.remove(grille[carre_y*3+y][carre_x*3+x])
                elif grille[carre_y*3+y][carre_x*3+x]!=0:
                    print("Grille impossible plusieurs fois la même valeur dans un seul carré")#Vérifie que le chiffre ne sois pas déjà dans une ligne/colonne/carré
                    return False





    return True




def recuperer_nom_fichier():
    """Cette fonction permet de récuperer le nom d'un fichier"""

    chemin = "./grille"
    fichier = os.listdir(chemin)

    print("\nVoici la liste des fichiers dans le dossier grille")
    for fic in fichier:
        print(fic)

recuperer_nom_fichier()

def recup_info_grille(nom_fichier):
    """Cette fonction récupère les informations d'un grille dans le fichier en prenant en paramètre son nom et renvoie son contenu"""

    fichier = open("./grille/"+nom_fichier, "r")

    contenu = []
    for ligne in fichier :

        Liste = list(ligne.strip())

        for i in range(len(Liste)):
            Liste[i] = int(Liste[i])

        contenu.append(Liste)
    fichier.close()

    return contenu


def trouver_case_vide(grille):
    """Cette fonction trouve les cases vides d'une grille en prenant en paramètre une grille et renvoie False ou leurs coordonnées en fonction de si il y en a ou pas"""

    Liste = []

    for x in range(9):
        for y in range(9):
            if grille[y][x] == 0:
                return [y,x]
    return False

def est_possible(grille,nombre,coord):
    """Cette fonction renvoie True ou False si un nombre peut etre placer sur une case précise en prenant en paramètre une grille, le nombre ey les coordonées de cette case"""

    posy,posx = coord

    for y in range(9):
        if grille[y][posx] == nombre: #On vérifie si notre nombre est déjà présent dans la ligne
            return False

    for x in range(9):
        if grille[posy][x] == nombre: #On vérifie si notre nombre est déjà présent dans la colonne
            return False

    carre_x = posx//3
    carre_y = posy//3

    for x in range(3):
        for y in range(3):
            if grille[carre_y*3+y][carre_x*3+x] == nombre: #On vérifie si notre nombre est déjà présent dans le carré
                return False

    return True

def copier_grille(grille):
    """Cette fonction crée une copie de la grille en prenant en paramètre une grille pour pouvoir modifier de manière temporaire la grille de sudoku"""
    copie = []
    for ligne in grille:
        copie.append(list(ligne))
    return copie


def calcul_solutions(grille,grille_solutions = []):
    """Cette fonction permet de trouver les solutions et de les renvoyers dans une liste en prenant en paramètre une grille"""

    if len(grille_solutions) >= 10:
        return grille_solutions

    premiere_case_vide = trouver_case_vide(grille)


    if premiere_case_vide == False:
        grille_solutions.append(copier_grille(grille))#si il n'y a plus de cases vide, on ajoute cette grille dans la liste de solution
        return grille_solutions

    for i in range(1,10):
        if est_possible(grille,i,premiere_case_vide):

            y,x = premiere_case_vide
            grille[y][x] = i
            grille_solutions = calcul_solutions(copier_grille(grille),grille_solutions) #On met de manière recursive un chiffre (qui peut etre dans cette case) dans une case et on continu jusqu'à ce qu'il n'y ait plus de cases vide

            grille[y][x] = 0


    return grille_solutions


def affichage_console(grille):
    """Cette fonction permet d'afficher une grille dans la console en prenant en paramètre cette grille"""

    for y in range(9):
        if y%3 == 0:
            print("")
        chaine = ""
        for x in range(9):
            if x%3 == 0:
                chaine += "   "
            else:
                chaine += " | "

            chaine += str(grille[y][x])
        print(chaine)
    print("")