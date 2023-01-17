import random

class Game:
    def __init__(self):
        self.player_name = ""
        self.score = {"user": 0, "computer": 0}
        self.options = ["pierre", "feuille", "ciseaux"]
        
    def start(self):
        self.player_name = input("Entrez votre nom : ")
        play_game = input("Bonjour " + self.player_name + " voulez-vous jouer à pierre-feuille-ciseaux? (o/n)").lower()
        if play_game != "o":
            return
        for round in range(1, 4):
            print(f"Round {round}")
            self.play_round()
        self.display_score()
        play_again = input("Voulez-vous rejouer? (o/n) ").lower()
        if play_again == "o":
            self.start()

    def play_round(self):
        computer_choice = random.choice(self.options)
        user_choice = input("Choisissez pierre, feuille ou ciseaux: ").lower()
        if user_choice in self.options:
            if user_choice == computer_choice:
                print("Egalité!")
            elif user_choice == "pierre" and computer_choice == "ciseaux":
                print("Vous avez gagné ce tour!")
                self.score["user"] += 1
            elif user_choice == "feuille" and computer_choice == "pierre":
                print("Vous avez gagné ce tour!")
                self.score["user"] += 1
            elif user_choice == "ciseaux" and computer_choice == "feuille":
                print("Vous avez gagné ce tour!")
                self.score["user"] += 1
            else:
                print("Vous avez perdu ce tour.")
                self.score["computer"] += 1
            print("Choix de l'ordinateur:", computer_choice)
        else:
            print("Choix non valide.")

    def display_score(self):
        print("Score final:")
        print(self.player_name + ":", self.score["user"])
        print("Ordinateur:", self.score["computer"])
        if self.score["user"] > self.score["computer"]:
            print("Vous avez gagné la partie!")
        elif self.score["user"] < self.score["computer"]:
            print("Vous avez perdu la partie.")
        else:
            print("Partie nulle.")

game = Game()
game.start()
