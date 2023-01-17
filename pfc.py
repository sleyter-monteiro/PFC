import random

while True:
    joueur = input("Quel est votre nom ?")

    start_jeu = input("Bonjour " + joueur + " Tu veux jouer au jeu du pierre, feuille, ciseau ? (O/n)")
    if start_jeu != "o":
        print("Une prochaine fois peut-être")
        break
    
    for manche in range(1, 4):
        print(f"manche {manche}")

        choix = ["pierre", "feuille", "ciseaux"]               

        choix_pc = random.choice(choix)

        points_joueur = 0
        points_pc = 0

        choix_joueur = input("Choissisez pierre, feuille ou ciseaux :")

        if choix_joueur in choix:
            if choix_joueur == choix_pc:
                print("Egalité !")
                
            elif choix_joueur == "pierre" and choix_pc == "ciseaux":
                print("Vous avez gagné cette manche")
                points_joueur += 1
                
            elif choix_joueur == "feuille" and choix_pc == "pierre":
                print("Vous avez gagné cette manche")
                points_joueur += 1  
                
            elif choix_joueur == "ciseaux" and choix_pc == "feuille":
                print("Vous avez gagné cette manche")
                points_joueur += 1    
                
            else: 
                print("Vous avez perdu cette manche")
                points_pc += 1
                print("Choix du pc :" + choix_pc)
                
        else:
            print("Choix non valide")
            
    score_final_joueur = int(points_joueur)
    score_final_pc = int(points_pc)      
            
    print("Vous avez " + str(score_final_joueur) + " points et le pc a " + str(score_final_pc) + " points")

    if score_final_joueur > score_final_pc:
        print("Vous avez gagné !")
    
    elif score_final_joueur == score_final_pc:
        print("Egalité !")        
            
    else:
        print("C'est perdu !")   
        
    rejouer = input("Voulez-vous rejouer ? (o/n)")
    if rejouer != "o":
        print("Au revoir !")
        break                      