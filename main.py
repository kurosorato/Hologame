from tkinter import *
from tkinter import Tk
import random

(Hauteur, Largeur) = (720, 1080)
root: Tk = Tk()
root.title("Game")
game = Canvas(root, height=Hauteur, width=Largeur, bg='black')
root.minsize(1080, 720)
root.maxsize(1080, 720)
game.pack()

guilarg = Largeur // 3
guihaut1 = 600
guihaut2 = 400
hitboxplayer = 18

right = False
left = False
up = False
click = False
Mort = False

holo = PhotoImage(file="holo.png")


class Gameroot:
    def __init__(self):
        self.zone = guilarg, guihaut2, guilarg * 2, guihaut1
        self.optionlarg = Largeur // 9
        self.case = 650
        self.case1 = "Start"
        self.case2 = "Items"
        self.case3 = "Exit"
        self.scorenum = 0
        self.possourisX = 0
        self.possourisY = 0
        self.framebotan = 0
        self.framewatame = 0
        self.framewatame2 = 0
        self.option()
        self.combatzone()
        self.score()
        self.meilleurscore()
        self.Backgroundbotan()
        self.Backgroundwatame()
        self.titacbackground()

    # definit la zone de jeu
    def combatzone(self):
        game.create_rectangle(self.zone, outline="white",tag="zone")

    def combatzonemort(self):
        game.delete("player")
        #game.create_rectangle(self.zone, outline="white", fill="black")
        game.create_text(guilarg+100, guihaut2 + 100 , text="Votre score: {}".format(self.scorenum),
                         fill="white", font="Arial 15 bold", tag="score", anchor="w")


    # cree les 3 cases avec les options
    def option(self):
        game.create_rectangle(self.optionlarg * 2, self.case, self.optionlarg * 3, self.case + 30, outline="white")
        game.create_rectangle(self.optionlarg * 4, self.case, self.optionlarg * 5, self.case + 30, outline="white")
        game.create_rectangle(self.optionlarg * 6, self.case, self.optionlarg * 7, self.case + 30, outline="white")

        game.create_text((self.optionlarg * 2 + self.optionlarg * 3) // 2, self.case + 15, text=self.case1,
                         fill="white", font="Arial 20 bold")
        game.create_text((self.optionlarg * 4 + self.optionlarg * 5) // 2, self.case + 15, text=self.case2,
                         fill="white", font="Arial 20 bold")
        game.create_text((self.optionlarg * 6 + self.optionlarg * 7) // 2, self.case + 15, text=self.case3,
                         fill="white", font="Arial 20 bold")

        # permet de cliquer sur les cases

    def boutonclickable(self):
        game.delete("click")

        # Case 1
        if (self.optionlarg * 2) <= self.possourisX <= self.optionlarg * 3 and \
                self.case <= self.possourisY <= self.case + 30:

            game.create_rectangle(self.optionlarg * 2, self.case, self.optionlarg * 3, self.case + 30,
                                  outline="gray", tag="click")
            niveau.active = True
            niveau.start()

        # case 2

        elif (self.optionlarg * 4) <= self.possourisX <= self.optionlarg * 5 and \
                self.case <= self.possourisY <= self.case + 30:

            game.create_rectangle(self.optionlarg * 4, self.case, self.optionlarg * 5, self.case + 30,
                                  outline="gray", tag="click")


        # case 3
        elif (self.optionlarg * 6) <= self.possourisX <= self.optionlarg * 7 and \
                self.case <= self.possourisY <= self.case + 30:

            game.create_rectangle(self.optionlarg * 6, self.case, self.optionlarg * 7, self.case + 30,
                                  outline="gray", tag="click")
            self.quiter()

    # affiche le score
    def score(self):
        game.delete("score")
        game.create_text(10, 20, text="score: {}".format(self.scorenum),
                         fill="white", font="Arial 15 bold", tag="score", anchor="w")

    # charge et affiche le meilleur score
    def meilleurscore(self):
        try:
            f = open("meilleurscore.txt", "r")
            mscore = f.read()

            game.create_text(10, 50, text="Meilleur score: {}".format(mscore),
                             fill="white", font="Arial 15 bold", tag="mscore", anchor="w")
            f.close()
        except:
            f = open("meilleurscore.txt", "x")
            f.write("0")

    # met sur True quand on click
    def click(self, event):
        global click
        click = True

    # met sur False quand on lache le click
    def resetclick(self, event):
        global click
        click = False

    # permet de quitter l'appli
    def quiter(self):
        global click
        if click:
            f = open("meilleurscore.txt", "r")
            mscore = int(f.read())
            if mscore <= self.scorenum:
                f.close()
                f = open("meilleurscore.txt", "w")
                f.write(str(self.scorenum))
            f.close()
            game.delete("all")
            quiter()

    # traque la position de la souris
    def positionsouris(self, event):
        self.possourisX, self.possourisY = event.x, event.y
        self.boutonclickable()

    # gere la vitesse des gif
    def titacbackground(self):
        global Mort
        self.framebotan += 1
        self.Backgroundbotan()
        if Mort == False:
            self.framewatame += 1
            self.Backgroundwatame()
        if Mort == True:
            self.framewatame2 += 1
            self.Backgroundwatame2()
        game.after(70, self.titacbackground)

    # gere les gif et leurs images
    def Backgroundbotan(self):
        if self.framebotan <= 7:
            self.botan = PhotoImage(file="Botan.gif", format="gif -index {}".format(self.framebotan))
            game.create_image(400, 350, image=self.botan)
        else:
            self.framebotan = 0

    def Backgroundwatame(self):
        if self.framewatame <= 7:
            self.watame = PhotoImage(file="watame.gif", format="gif -index {}".format(self.framewatame))
            game.create_image(700, 350, image=self.watame, tag="watame")
        else:
            self.framewatame = 0

    def Backgroundwatame2(self):
        game.delete('watame')
        if self.framewatame2 <= 3:
            self.watame2 = PhotoImage(file="watame2.gif", format="gif -index {}".format(self.framewatame2))
            game.create_image(700, 350, image=self.watame2)
        else:
            self.framewatame2 = 3


class Obstacle:
    def __init__(self, pos, name, ouverture, distance, vitesse,):
        self.vectvitesse = pos
        self.distance = distance
        self.ouverture = ouverture
        self.name = name
        self.condition = True
        self.vitessefleche = vitesse
        self.damage = 20
        self.fleches()
        self.tictac()

    # le dessin des fleches
    def fleches(self):
        game.delete(self.name)
        game.create_line(self.vectvitesse, guihaut2, self.vectvitesse, guihaut2 + self.distance,
                         width=5, arrow='last', arrowshape=(10, 10, 10), fill='cyan', tag=self.name)

        game.create_line(self.vectvitesse, guihaut1, self.vectvitesse, guihaut2 + self.distance + self.ouverture,
                         width=5, arrow='last', arrowshape=(10, 10, 10), fill='cyan', tag=self.name)

    # pour savoir si le joueur est entrer en collision avec les fleches si oui retirer de la vie
    def collision2(self):
        if self.vectvitesse + 3 >= player.position1 and player.position1 >= self.vectvitesse - 3:
            if player.position2 <= guihaut2 + self.distance:
                player.pointvie += self.damage
                player.vie()
            if player.position2 >= guihaut2 + self.distance + self.ouverture:
                player.pointvie += self.damage
                player.vie()

    # permet de peplacer les fleches
    def deplacement2(self):
        self.vectvitesse -= self.vitessefleche
        self.fleches()

    # suprime les fleches qui sont sortie de la zone de combat
    def suprime(self):
        if self.vectvitesse <= guilarg:
            game.delete(self.name)
            self.condition = False

    # horloge d'action
    def tictac(self):
        if self.condition == True:
            self.collision2()
            self.deplacement2()
            self.suprime()
            game.after(16, self.tictac)


class Playerroot:
    def __init__(self):
        self.position1 = 500  # horizontal
        self.position2 = 550  # vertical
        self.vectgravite = 5
        self.vectdeplacement = 3
        self.vectsaut = 10
        self.pointvie = 0
        self.barrevie = guilarg * 3 - 20 - guilarg * 2
        self.player()
        self.vie()

    # l'image du joueur et sa position
    def player(self):
        game.delete("player")
        game.create_image(self.position1, self.position2, image=holo, tag="player")
        # hitbox du joueur:
        '''game.create_rectangle(self.position1 - hitboxplayer, self.position2 - hitboxplayer,
                              self.position1 + hitboxplayer, self.position2 + hitboxplayer,
                              outline="purple", tag="player")
'''

    # affiche la vie
    def vie(self):
        game.delete("vie")
        game.create_rectangle(guilarg, guihaut1 + 15, guilarg * 2 - self.pointvie, guihaut1 + 25, fill="red", tag="vie")
        game.create_rectangle(guilarg, guihaut1 + 15, 0, guihaut1 + 25, fill="black")
        game.create_rectangle(guilarg, guihaut1 + 15, guilarg * 2, guihaut1 + 25, outline='white')

    # gere la mort
    def mort(self):
        global Mort
        if self.pointvie >= guilarg:
            niveau.active = False
            Game.combatzonemort()
            Mort = True

    # gere la gravité
    def gravite(self):
        if player.position2 + hitboxplayer < guihaut1:
            player.position2 += player.vectgravite
            player.player()

    # gere la collision contre les murs
    def collision(self):
        if player.position1 - hitboxplayer <= guilarg:  # colision sur la gauche
            player.position1 += self.vectdeplacement
            player.player()
        elif player.position1 + hitboxplayer >= (guilarg * 2):  # colision sur la droite
            player.position1 -= self.vectdeplacement
            player.player()

    # gere la colision contre le plafond
    def collisionplafond(self):
        if player.position2 - hitboxplayer <= guihaut2:  # coision contre le plafond
            player.position2 = guihaut2 + hitboxplayer + 5
            player.player()

    # permet de se deplacer
    def deplacement(self):
        global right
        global left
        if right:
            player.position1 += self.vectdeplacement
            player.player()
        elif left == True:
            player.position1 -= self.vectdeplacement
            player.player()

    # permet de se deplacer vers le haut
    def saut(self):
        global up
        if up == True:
            player.position2 -= self.vectsaut
            player.player()

    # permet le deplacement "smooth"
    def toucheenfoncer(self, event):
        global right
        global left
        global up
        if event.keysym == "Right":
            right = True
        elif event.keysym == "Left":
            left = True
        elif event.keysym == "Up":
            up = True

    # reset les variables de deplacement global au lacher de la touche
    def resettouches(self, event):
        global right
        global left
        global up
        if event.keysym == "Right":
            right = False
        elif event.keysym == "Left":
            left = False
        elif event.keysym == "Up":
            up = False


class Niveau:
    def __init__(self):
        self.frequence = 2000
        self.active = False
        self.starter = False
        self.nom = 10
        self.ouverture = 60
        self.progression = 0
        self.pos = 0
        self.vitesse = 4

    # lance le niveau
    def start(self):
        global click
        if click == True:
            if self.starter == False:
                self.active = True
                self.starter = True
                self.tictacgene()

    # change la difficulter selon la progression sur l'espace entre les fleches
    def difficulter(self):
        if 25 < self.progression < 50:
            self.ouverture = random.randint(40, 50)
        elif 50 < self.progression:
            self.ouverture = random.randint(30, 40)

    # change la vitesse des fleche selon la progression
    def difficultervit(self):
        if 50 < self.progression < 70:
            self.vitesse = 5
        elif 70 < self.progression < 80:
            self.vitesse = 6
        elif 80 < self.progression < 100:
            self.vitesse = 7
        elif 100 < self.progression < 150:
            self.vitesse = 8
        elif 150 < self.progression:
            self.vitesse = 9

    # change la frequence d'aparition des fleches
    def difficultefrequence(self):
        if self.progression == 50:
            self.frequence = 1500
        elif self.progression == 100:
            self.frequence = 1400
        elif self.progression == 200:
            self.frequence = 1300
        elif self.progression == 250:
            self.frequence = 1200

    # genere les fleches
    def generation(self):
        Obstacle(850, "fleche{}".format(self.nom), self.ouverture, self.pos, self.vitesse)

    # gere la position de l'ouverture des fleches sur les Y
    def position(self):
        self.pos = random.randint(0, 200 - self.ouverture)

    # horloge
    def tictacgene(self):
        if self.active == True:
            Game.scorenum += 1
            Game.score()
            self.position()
            self.nom += 1
            self.generation()
            self.progression += 1
            self.difficulter()
            self.difficultervit()
            self.difficultefrequence()
            game.after(self.frequence, self.tictacgene)


# appel ces fonciont toute les 16 ms
def chrono():
    player.gravite()
    player.collision()
    player.collisionplafond()
    player.deplacement()
    player.saut()
    Game.boutonclickable()
    player.mort()
    game.after(16, chrono)  # 16 = 60 fps


# zone de test
def test(event):
    Obstacle(850, "qsd", 50, 100, 10)


Game = Gameroot()
player = Playerroot()
niveau = Niveau()

chrono()  # lance la fonction 1 fois

# assignement des touches
root.bind("<Right>", player.toucheenfoncer)
root.bind("<KeyRelease-Right>", player.resettouches)
root.bind("<Left>", player.toucheenfoncer)
root.bind("<KeyRelease-Left>", player.resettouches)
root.bind("<Up>", player.toucheenfoncer)
root.bind("<KeyRelease-Up>", player.resettouches)
root.bind("<Motion>", Game.positionsouris)
root.bind("<Button-1>", Game.click)
root.bind('<ButtonRelease-1>', Game.resetclick)

root.bind("<t>", test)

def quiter():
    game.destroy()
    root.destroy()

mainloop()
