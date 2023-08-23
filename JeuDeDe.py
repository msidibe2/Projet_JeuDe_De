# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:25:11 2020
 
@author: moussa
"""
import random

def jeu_de_de():
    score1=0 #score du joueur 1
    score2=0 #score du joueur 2
    faces =[1,2,3,4,5,6]  #La liste qui contient les issues possibles
    fin_jeu = False
    while(fin_jeu == False): #Tant que score1 <= 50 ou score2 <= 50
        issue_joueur1=random.randint(1, 6) 
        if score1 >= 50:
            print('Joueur 1 gagne , son score est {} \n'.format(score1))
            fin_jeu = True
        elif score2 >= 50:
            print('Joueur 2 gagne, son score est {} \n'.format(score2))
            fin_jeu = True
        if(issue_joueur1 in faces): #si le nombre saisi par le joueur 1 est dans la liste des issues
            if(issue_joueur1!=1): 
                if(issue_joueur1%2==0): #si le nombre saisi par le joueur 1 est pair
                    score1+=1 
                elif(issue_joueur1==3):#si le nombre saisi par l'utilisateur 1 egal a 3
                    score1*=2  
                elif(issue_joueur1==5):#si le nombre saisi par l'utilisateur 1 egal a 5
                    score1=score1-2  
 
            else:  #si le joueur1 obtient la face numero 1 alors il passe le tour au joueur2
                
                while(score2<=50):
                    issue_joueur2=random.randint(1, 6)
                    if(issue_joueur2 in faces): 
                        if(issue_joueur2!=1):
                            if(issue_joueur2%2==0):#si le nombre saisi par le joueur 2 est pair
                                score2+=1 
                            elif(issue_joueur2==3):#si le nombre saisi par l'utilisateur 2 egal a 3
                                score2*=2  #le score 2 sera multiplier par 2
                            elif(issue_joueur2==5):#si le nombre saisi par l'utilisateur 2 egal a 5
                                score2=score2-2 
       
                            print('Le joueur2 a la main  \n') 
                        else: 
                            break      
jeu_de_de()
