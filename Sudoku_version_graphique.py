import pygame
from pygame.locals import *
import os
import sys
from Sudoku_solution_version_console import *



def afficher_grille(fenetre,grille,posxy,longueur = 225,Grille_de_base = False):
    """Cette fonction permet l'affichage d'une grille de manière graphique"""


    noir = (0,0,0)
    
    decalx,decaly = posxy
    
    Liste = [round(i*longueur/9) for i in range(10)]
    
    for i in range(len(Liste)):
        if i%3 == 0:
            largeur = round(longueur/(100))
        else:
            largeur = round(longueur/(200)) #Trace les lignes du sudoku
        
        valeur = Liste[i]
        
        pygame.draw.line(fenetre,noir,[decalx+valeur,decaly],[decalx+valeur,decaly+longueur],largeur)
        pygame.draw.line(fenetre,noir,[decalx,decaly+valeur],[decalx+longueur,decaly+valeur],largeur)
    

    for x in range(9):
        for y in range(9):

            if grille[y][x] != 0:
                
                couleur = (0,0,0)
                if Grille_de_base != False:
                    if Grille_de_base[y][x] == 0:
                        couleur = (84,84,84)
                posx = decalx + x * longueur / 9 + longueur /(9*4) #Ajoute les numéros à chaque case du sudoku si celui n'est pas un 0
                posy = decaly + y * longueur / 9 + longueur /(9*7)
                taille_police_ecr = round(longueur / 7)
                affichage_numero(fenetre,grille[y][x],posx,posy,taille_police_ecr,couleur)


def animation_grille(fenetre,grille,valider,numero):
    """Cette fonction permet l'animation de la grille quand elle sera selectionné en prenant en paramètre une grille,la fenetre graphique si la fonction est valider"""

    noir = (0,0,0)

    for i in range(31):
        pygame.draw.line(fenetre,noir,[200,0],[200,20*i],8)
        pygame.draw.line(fenetre,noir,[400,0],[400,20*i],8) 
        pygame.draw.line(fenetre,noir,[0,200],[20*i,200],8)
        pygame.draw.line(fenetre,noir,[0,400],[20*i,400],8)
        pygame.display.flip()
        pygame.time.wait(15)
    Liste = [round(i*600/9) for i in range(10)]
    for i in range(31):
        for p in Liste:
            pygame.draw.line(fenetre,noir,[p,0],[p,20*i],2)#permet l'animation des traits noir horizontaux et verticaux
            pygame.draw.line(fenetre,noir,[0,p],[20*i,p],2)

        pygame.display.flip()
        pygame.time.wait(15)
    
    for x in range(9):
        for y in range(9):
            if grille[y][x] != 0:
                posx =  round(x * 600 / 9 + 600 /(9*4))
                posy =  round(y * 600 / 9 + 600 /(9*7))
                taille_police_ecr = round(600 / 7)
                affichage_numero(fenetre,grille[y][x],posx,posy,taille_police_ecr) #puis affiche les numeros et autres éléments
    
    
    pygame.display.flip()


def affichage_boutons(fenetre,valider,numero):
    """Cette fonction permet l'affichage des boutons reset,gomme et des chiffres quand on joue au sudoku en prenant en paramètre la fenetre graphique si la fonction est valider"""

    noir = (0,0,0)
    rouge = (255,0,0)
    vert = (119,178,85)
    blanc = (255,255,255)
    bleu = (37,70,255)


    police_ecr = pygame.font.Font(None, 35)
    texte = police_ecr.render("reset", True, noir)
    fenetre.blit(texte, (5, 615))

    if valider:
        pygame.draw.line(fenetre,rouge,(75, 637),(95, 617),3)
        pygame.draw.line(fenetre,rouge,(75, 617),(95, 637),3)
    else:
        pygame.draw.rect(fenetre, vert, (72, 614, 25, 25))
        pygame.draw.line(fenetre, blanc,[75,624],[80,634],2) #affichage de la gomme (vert ou rouge si elle est selectionné) et du bouton "echap"
        pygame.draw.line(fenetre, blanc,[80,634],[90,617],2)

    police_ecr = pygame.font.Font(None, 35)
    texte_nb = police_ecr.render("X", True, noir) 
    fenetre.blit(texte_nb, (557, 615))
    

    for i in range(1,10):
        
        if numero == i:
            couleur = bleu #Si un numéro est selectionné un cercle bleu l'entourera
        else:
            couleur = noir
        
        pygame.draw.circle(fenetre,couleur,(77+i*50,626),15,1)

        police_ecr = pygame.font.Font(None, 35)
        texte_nombre = police_ecr.render(str(i), True, noir)#Affichage des chiffres
        fenetre.blit(texte_nombre, (70+i*50, 615))


def reset(fenetre,Grille_de_base,grille,valider,numero):
    """Cette fonction permet de reset une grille de sudoku à son état initiale"""

    blanc = (255,255,255)
    fenetre.fill(blanc)
    afficher_grille(fenetre,grille,(0,0),600,Grille_de_base)
    affichage_boutons(fenetre,valider,numero)

    

def affichage_numero(fenetre,nombre,x,y,taille_police_ecr,couleur = (0,0,0)):
    """Cette fonction permet l'affichage des numéros dans la grille de sudoku en prenant en paramètre la fenetre graphique,des coordonnées et la taille de la police """
        
    police_ecr = pygame.font.Font(None, taille_police_ecr)
    texte_nombre = police_ecr.render(str(nombre), True, couleur)
    fenetre.blit(texte_nombre, (x, y))

def case_bleu(fenetre,x,y):
    """Affiche la case en bleu quand on interragis avec en prenant en paramètre la fenetre graphique et les coordonnées de la case"""

    bleu = (37,70,255)

    x = x*600/9
    y = y*600/9

    pygame.draw.line(fenetre,bleu,[round(x),round(y)],[round(x+600/9),round(y)],6)
    pygame.draw.line(fenetre,bleu,[round(x),round(y)],[round(x),round(y+600/9)],6)
    pygame.draw.line(fenetre,bleu,[round(x+600/9),round(y)],[round(x+600/9),round(y+600/9)],6)
    pygame.draw.line(fenetre,bleu,[round(x),round(y+600/9)],[round(x+600/9),round(y+600/9)],6)

def affichage_quatre_grille(fenetre,grille,nom_fichier,page):
    """Cette fonction permet l'affichage des 4 grilles quand on va démarer le programme en prenant en paramètre la fenetre graphique et le fichiers contenant les grilles"""
    
    blanc = (255,255, 255)
    noir = (0,0,0)
    police_ecr = pygame.font.Font(None, 25)
    
    fenetre.fill(blanc)
    
    pygame.draw.line(fenetre,noir,[0,0],[600,0],15)
    pygame.draw.line(fenetre,noir,[0,0],[0,650],15) #Séparation des 4 grilles
    pygame.draw.line(fenetre,noir,[600,0],[600,650],15)
    pygame.draw.line(fenetre,noir,[0,650],[600,650],15)
    
    
    Liste= [(35,35),(315,35),(35,365),(315,365)]
        
    for i in range(len(Liste)):
        
        if len(grille) > i + page*4:
            afficher_grille(fenetre,grille[i + page*4],Liste[i],250)
            texte = police_ecr.render(nom_fichier[i + page*4], True, noir)
            posx,posy = Liste[i]
            fenetre.blit(texte, (posx+85,posy-20))
    texte = police_ecr.render("p "+str(page+1), True, noir) #Affiche les grilles graphiquement sur une page si il y a 4 grilles maximum dans le fichier grille
    fenetre.blit(texte, (560,620))
    
    pygame.draw.line(fenetre,noir,[50,310],[20,325],8)
    pygame.draw.line(fenetre,noir,[50,340],[20,325],8)


    pygame.draw.line(fenetre,noir,[550,310],[580,325],8)
    pygame.draw.line(fenetre,noir,[550,340],[580,325],8)



def interaction_menu_fond(fenetre):
    """Cette fonction permet l'interaction avec le menu en prenant en paramètre la fenetre graphique"""
    
    police_ecr = pygame.font.Font(None, 30)
    grille = []
    noir = (0,0,0)
    blanc = (255,255,255)
    
    chemin = "./grille"
    nom_fichier = os.listdir(chemin)
    
    for fic in nom_fichier:
        
        grille.append(recup_info_grille(fic))
        
    page = 0
    affichage_quatre_grille(fenetre,grille,nom_fichier,page)
    pygame.display.flip()
    
    while True:
    
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            pos = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:

                if event.key == K_RIGHT:
                    
                    if len(grille) > (page+1)*4:
                        page += 1
                    else:
                        page = 0
                    
                if event.key == K_LEFT:
                    if page == 0:
                        page = len(grille)//4
                    else:
                        page -= 1  #Interaction touche :echap,fleche gauche/droite
            
            
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                
                if 20 < pos[0] < 50 and 310 < pos[1] < 340:
                    if page == 0:
                        page = len(grille)//4
                    else:
                        page -= 1
                
                if 550 < pos[0] < 580 and 310 < pos[1] < 340:
                    if len(grille) > (page+1)*4:
                        page += 1
                    else:
                        page = 0 #Permet la naviguation dans les pages de la fenetre
                
            affichage_quatre_grille(fenetre,grille,nom_fichier,page)
            
            if 35 < pos[0] < 285 and 35 < pos[1] < 285: 
                
                pygame.draw.rect(fenetre,blanc,(37, 37, 248,248))
                
                texte = police_ecr.render("Jouer", True, noir)
                fenetre.blit(texte, (135,115))
                
                texte = police_ecr.render("Solutions", True, noir)
                fenetre.blit(texte, (120,185))
                
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    
                    if pos[1] > 160:
                        return (True,grille[page*4],nom_fichier[page*4])
                    else:
                        return (False,grille[page*4],nom_fichier[page*4])
                
                
            if 315 < pos[0] < 565 and 35 < pos[1] < 285 and len(grille) > 1 + page*4:
                
                pygame.draw.rect(fenetre,blanc,(317, 37, 248,248))
                
                texte = police_ecr.render("Jouer", True, noir)
                fenetre.blit(texte, (415,115))
                
                texte = police_ecr.render("Solutions", True, noir)
                fenetre.blit(texte, (405,185))
                
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    
                    if pos[1] > 160:
                        return (True,grille[1+page*4],nom_fichier[page*4])
                    else:
                        return (False,grille[1+page*4],nom_fichier[page*4])
                
                
            if 35 < pos[0] < 285 and 365 < pos[1] < 615 and len(grille) > 2 + page*4:
                
                pygame.draw.rect(fenetre,blanc,(37, 367, 248,248))
                
                texte = police_ecr.render("Jouer", True, noir)
                fenetre.blit(texte, (135,445))
                
                texte = police_ecr.render("Solutions", True, noir)
                fenetre.blit(texte, (120,515))
                
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    
                    if pos[1] > 440:
                        return (True,grille[2+page*4],nom_fichier[page*4])
                    else:
                        return (False,grille[2+page*4],nom_fichier[page*4])
                
            if 315 < pos[0] < 565 and 365 < pos[1] < 615 and len(grille) > 3 + page*4:
                
                pygame.draw.rect(fenetre,blanc,(317, 367, 248,248))
                
                texte = police_ecr.render("Jouer", True, noir)
                fenetre.blit(texte, (415,445))
                
                texte = police_ecr.render("Solutions", True, noir)
                fenetre.blit(texte, (405,515))
                
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    
                    if pos[1] > 440:
                        return (True,grille[3+page*4],nom_fichier[page*4])
                    else:
                        return (False,grille[3+page*4],nom_fichier[page*4]) #l.248-316:permet l'affichage et l'interactrion des boutons solution et jouer quand on passe la souris sur une grille
                
            
            pygame.display.flip()
      
      
def jouer_la_grille(fenetre,Grille_de_base):
        """Cette fonction permet de jouer à une des grilles du sudoku en prenant en paramètre la fenetre graphique et une grille de sudoku"""
    
        valider = False
        numero = 0
        blanc = (255,255,255)
    
        grille = copier_grille(Grille_de_base)
        fenetre.fill(blanc)
        
        
        animation_grille(fenetre,grille,valider,numero) 
        affichage_boutons(fenetre,valider,numero) 
        pygame.display.flip()
        
        while True:
    
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    
                if event.type == MOUSEBUTTONDOWN and event.button == 1: #Permet de selectionner un chiffre et de le mettre dans une case de la grille si il n'y a pas d'autre chiffre dans cette case et aggrandis les traits quand on selectionne un chiffre
                    
                    pos = pygame.mouse.get_pos()
    
                    if pos[1] < 600:
                        x = 0
                        y = 0
    
                        while pos[0] > x:
                            x += 66
    
                        while pos[1] > y:
                            y += 66
    
                        x = (x // 66) -1
                        y = (y // 66) -1
    
                        if numero != 0 and Grille_de_base[y][x] == 0 :
                            grille[y][x] = numero
    
                        if valider and Grille_de_base[y][x] == 0:
                            grille[y][x] = 0
    
                        reset(fenetre,Grille_de_base,grille,valider,numero)
                        case_bleu(fenetre,x,y)
                        pygame.display.flip()
                    else:
    
                        for i in range(1,10):
                            if 60+i*50 < pos[0] < 90+i*50:
                                if numero == i:
                                    numero = 0
                                else:
                                    numero = i
    
                        if 75 < pos[0] < 95:
                            valider = not valider
    
                        if 555 < pos[0] < 595:
                             return
    
                        if pos[0] < 60:
                            grille = copier_grille(Grille_de_base)
                        
                        reset(fenetre,Grille_de_base,grille,valider,numero)
                        pygame.display.flip()
                        
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        return
                    
                    for i in range(1,10): #Permet d'ajouter un chiffre avec les touches du clavier si celui ci est bien un chiffre
                        if event.key == eval("K_"+str(i)) or event.key == eval("K_KP"+str(i)):
                            if x != -1 and y != -1:
    
                                grille[y][x] = i
                                reset(fenetre,Grille_de_base,grille,valider,numero)
                                pygame.display.flip()
                                
                        
    
    
def afficher_solutions(fenetre,nom_grille,Grille_de_base):
        """Cette fonction permet l'affichage des solutions en prenant en paramètre la fenetre graphique,la grille de sudoku et son nom"""
        
        police_ecr = pygame.font.Font(None, 25)
        noir = (0,0,0)
        blanc = (255,255,255)
        
        affichage_quatre_grille(fenetre,[Grille_de_base],["Grille de base"],0)
        
        texte = police_ecr.render("calcul des solutions ...", True, noir) #Affiche un ecran de chargement
        fenetre.blit(texte, (200,315))
        texte = police_ecr.render("veuillez patientez", True, noir)
        fenetre.blit(texte, (205,335))
        pygame.display.flip()
        
        if verif_grille(Grille_de_base) == True:
            Liste_solution = calcul_solutions(Grille_de_base,[])
        else:
            fenetre.fill(blanc)
            affichage_quatre_grille(fenetre,[Grille_de_base],["Grille de base"],0)
            texte = police_ecr.render("Pas de solutions", True, noir)
            fenetre.blit(texte, (200,315))
            texte = police_ecr.render("Appuyez sur n'importe quel touche pour revenir en arrière", True, noir) #Si il y a une solution le programme le renvoie sinon renvoie un message d'erreur et permet de revenir au menu en appuyant sur n'importe quelle touche
            fenetre.blit(texte, (65,335))
            pygame.display.flip()
            
            while True:
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: #Interraction avec fleche directionnelles et echap
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        return
                    if event.type == MOUSEBUTTONDOWN:
                        return
        
        creer_fichier_solution(nom_grille,Liste_solution)
            
        Liste_solution.insert(0,Grille_de_base)
        
        nom_fichier = ["Grille de base"]
        for i in range(1,len(Liste_solution)):
            nom_fichier.append("solution "+str(i))
        
        page = 0
    
        affichage_quatre_grille(fenetre,Liste_solution,nom_fichier,page)
        texte = police_ecr.render("Retour", True, noir)
        fenetre.blit(texte, (270,315))
        pygame.display.flip()
        
        
        
        
        while True:
    
            for event in pygame.event.get(): #Permet de naviguer entre les pages de solutions avec les touches directionelles
    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
    
                    if event.key == K_LEFT:
                        page -= 1
                        if page < 0:
                            page = len(Liste_solution)//4 
    
                    if event.key == K_RIGHT:
                        
                        page += 1
                        if page > len(Liste_solution)//4:
                            page = 0
                    
                    
                    
                    
                    
                    affichage_quatre_grille(fenetre,Liste_solution,nom_fichier,page)
                    texte = police_ecr.render("Retour", True, noir)
                    fenetre.blit(texte, (270,315))
                    pygame.display.flip()
                    
                    if event.key == K_ESCAPE:
                        return
                        
                    
                    
                    
                
                if event.type == MOUSEBUTTONDOWN and event.button == 1: #Permet de naviguer entre les pages de solutions avec les fleches du menu
                    
                    pos = pygame.mouse.get_pos()
                    if 270 < pos[0] < 345 and 315 < pos[1] < 340 :
                        return
                    
                    
                        
                    if 20 < pos[0] < 50 and 305 < pos[1] < 345 :
                        page -= 1
                        if page < 0:
                            page = len(Liste_solution)//4
                            
                    if 550 < pos[0] < 585 and 305 < pos[1] < 345:
                        page += 1
                        if page > len(Liste_solution)//4:
                            page = 0
                    
                    affichage_quatre_grille(fenetre,Liste_solution,nom_fichier,page)
                    texte = police_ecr.render("Retour", True, noir)
                    fenetre.blit(texte, (270,315))
                    pygame.display.flip()

                    
def start():
    """Cette fonction permet de lancer le programme"""

    mapX= 600
    mapY= 650

    blanc = (255,255,255)
    pygame.init()
    fenetre = pygame.display.set_mode((mapX,mapY))#Crée la page
    pygame.display.set_caption("Sudoku")
    
    
    
    while True:
        solutions,Grille_de_base,nom_grille = interaction_menu_fond(fenetre) #Fonctionnement du programme qui permet de jouer ou de trouver la solution d'une grille de sudoku en utilisant les fonctions jouer_la_grille(),afficher_solutions() et autre fonction permettant l'interaction
        
        if solutions == False:
            jouer_la_grille(fenetre,copier_grille(Grille_de_base))
            
        else:
            afficher_solutions(fenetre,nom_grille,copier_grille(Grille_de_base))
    