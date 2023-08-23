#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:43:48 2020
 
@author: moussa
"""
print("***************************Exo1*********************")
""
print("Qestion 1: liste sans doublon")
l1 = [1, 2, 2, 3, 4, 5, 5, 6, 8, 9]
def Q1(liste):
    listeSansDoublon = []
    y=liste[0]
    for i in range(0, len(liste)):
          if liste[i] != y:
              listeSansDoublon.append(y)
          y = liste[i]     
           
    return listeSansDoublon 
      
print(Q1(l1))

print("\nQuestion 1 cas general")

l2 =[9, 9, 8, 3, 3, 2, 11, 22]
def CasGeneral(liste):
        listeSansDoublon = []
        for x in liste:
            if x not in listeSansDoublon:
                listeSansDoublon.append(x)
                return listeSansDoublon            
print(CasGeneral(l2))
 
print("\nQuestion 2")
l=[[1,2],[3,4]]
def Q2(liste):
       liste_plate = [item for liste in liste for item in liste]   
       return liste_plate
print(Q2(l))
 

print("\nQuestion 3")
def liste_consecutive(liste):
    x=liste[0]
    sortie = []
    for i in range(1, len(liste)):
        if liste[i] == x+1:
            sortie.extend(x)
            sortie.extend(liste[i])
        x=l[i]
        #return sortie
l=[1, 3, 6, 7, 8, 9]
l=[1,3,6,7,8,9]
print(liste_consecutive(l))


print("Question 4 : nombre d'occurence")
liste = [1, 5, 3, 1, 2, 5, 2, 4, 5,1, 9,1, 4, 5, 1]
nbOccurence = dict([(x, liste.count(x)) for x in set(liste)])
print(nbOccurence)
"""
"""
print("\n#Question 5 :\n")
def combinaison():
    combinaison=dict() 
    clef=0    
    couple=[] #liste des couple
    
    for i in range(1,7):
        for j in range(1,7):
            clef=i+j
            couple=[i,j]
            combinaison.update({clef:couple})
            for k in range(1,7):
                for l in range(1,7):
                    if((k+l == clef) and (i!=k) and (j!=l)):
                        couple=[k, l]
                        combinaison[clef].append(couple)
                        
    for cles,valeur in combinaison.items():#affichage des combinaisons
        print(cles,'->',valeur,'\n')
#Appel de la fonction pour tester
combinaison()

print("\n#Question 6\n")
def test_de_primalite(nombre):
    liste_premier = [2] 
    for i in range(3,nombre,2):
        liste_premier.append(i) 
    for i in liste_premier:
        for j in liste_premier:
            if(j%i==0 and i!=j): #le nombre admet un autre diviseur different de lui-meme
                liste_premier.remove(j)
    return liste_premier

print(test_de_primalite(45))
 

print("\n#Question 7\n")
def inverse(dictionnaire):
    dictionnaire_inverse = {}
    valeur = set()                                           
    for  valeur in dictionnaire.values(): 
            for element in valeur: 
                valeur.add(element)
            for key in valeur:
              dictionnaire_inverse[key]=set()
    for values in valeur: 
        for keys in dictionnaire.keys():
            for element in dictionnaire[keys]:
                if values == element :
                    dictionnaire_inverse[values].add(keys)
     
    return dictionnaire_inverse

d = {"departement": {78}, "commune": {140}}
print(inverse(d))

print("\n#Question 8")
print("\t##8. 1\n")
def mot_identique(m1,m2):
   temoin=True 
   for i in m1:
       for j in m2:
           if ((i not in m2) or (j not in m1)): #si la lettre i n'est pas dans m2 et j n'est pas dans m1
                temoin=False
   if(temoin==True):            
          print("Les 2 mots ont les memes lettres")
   else:
        print("Les 2 mots sont différents")

m1='Isty' 
m2='Isty'
mot_identique(m1,m2)  
  
print("\n\t##8. 2\n")
def anagramme(m1,m2):
    flag=False  
    for i in m1: 
        if i in m2: #si la lettre i est dans m2
            flag=True  
        else:
           flag=False  
    if(flag==True):     
        print("Ce sont des anagrammes")
    else:
        print("Ce ne sont pas des anagrammes")

m1='anas' 
m2='sana'
anagramme(m1,m2)   

print("***************************Exo2 *****************")
print("\t#Algo: ") 
"""
fonction hasard(nombreEntre, nombreMystere: entier): bool
  cpt = 0// pour compter le nombre d'essai
  Tant que cpt < 10
     entrez un nombre()
     si nombreEntrez  < nombreMystere alors afficher (entrer un nombre plus grand)
     sinon si nombreEntrez > nombreMystere alors afficher (entrer un nombre plus petit)
     sinon afficher (bravo! vous avez gagné)
  FinTant que
  Si cpt > 9
     afficher (vous n'avez pas gagné en 1à essais)
 """ 

print("\n\t#code: ")
  
import random
def hasard():
    nombre_mystere=random.randint (0,100) #  pour generer le nombre aleatoire entre 0 et 100 
    cpt=0 # variable qui compte le nombre d'essai
    
    while(cpt<10): 
        nombre_entre=int(input('Saisir un nombre entre 0 et 100 :')) 
        cpt=1 
        if( nombre_entre < nombre_mystere):  
            print('{} est inferieur a la valeur proposee'.format( nombre_entre))  
        elif( nombre_entre > nombre_mystere):  
            print('{} est superieur à la valeur proposee'.format( nombre_entre)) #On affiche un message
        else:  
            print('Bravo ! le nombre mystere est {} '.format( nombre_entre))
            break
    else:
        print("\nVous avez depasser le nombre d'essai!") # quand l'utilisateur depasse le nombre d'essai
           
hasard()
 
 
print("***************************Exo3 *****************")

def Joueur1(sc1,des,j1):
    ##joueur1=int(input('saisir un nombre   entre 1 et 6'))
        
    if(j1 !=1):
        if(j1%2==0):
            sc1+=1
        elif(j1==3):
            sc1*=2
        elif(j1==5):
            sc1=sc1-2
    return sc1
    

def Joueur2(score2,des,joueur2):
    #joueur2=int(input('saisir un nombre  entre 1 et 6'))
    
    if(joueur2 in des):
        if(joueur2%2==0):
            score2+=1
        elif(joueur2==3):
            score2=3*2
        elif(joueur2==5):
            score2=score2-2
    return score2

def jeu_de_de():
    score1=0 #score du joueur 1
    score2=0 #score du joueur 2
    des=[1,2,3,4,5,6]  #La liste qui contient les issues
    fin_j = False
    while(fin_j == False): #Tant que score1 <= 50 ou score2 <= 50
        joueur1=random.randint(1, 6) 
        if score1 >= 50:
            print('Joueur 1 gange ,Le score du joueur1 est {} \n'.format(score1))
            fin_j = True
        elif score2 >= 50:
            print('Joueur 2 gangne, Le score du joueur2 est {} \n'.format(score2))
            fin_j = True
        if(joueur1 in des): #si le nombre saisi par le joueur 1 est dans la liste des issues
            if(joueur1!=1): #si le nombre saisi par le joueur 1 est differend de 1
                if(joueur1%2==0): #si le nombre saisi par le joueur 1 est pair
                    score1+=1 
                elif(joueur1==3):#si le nombre saisi par l'utilisateur 1 egal a 3
                    score1*=2  
                elif(joueur1==5):#si le nombre saisi par l'utilisateur 1 egal a 5
                    score1=score1-2  
 
                print('Le joueur1 : a la main \n')                                       
            else: 
                
                while(score2<=50):
                    joueur2=random.randint(1, 6)
                    if(joueur2 in des): 
                        if(joueur2!=1):
                            if(joueur2%2==0):#si le nombre saisi par le joueur 2 est pair
                                score2+=1 
                            elif(joueur2==3):#si le nombre saisi par l'utilisateur 2 egal a 3
                                score2*=2  #le score 2 serat multiplier par 2
                            elif(joueur2==5):#si le nombre saisi par l'utilisateur 2 egal a 5
                                score2=score2-2 
       
                            print('Le joueur2 : a la main  \n') 
                        else: 
                            break      
jeu_de_de()
