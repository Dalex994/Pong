# Importation of the modules and definition of players' variables

from turtle import *
import turtle as t
joueurAscore=0
joueurBscore=0

 # Field creation and declaration of window variables and instruction screen()
window=t.Screen()
window.title("Jeu de Pong")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

 # Creation of the left raquette
raquettegauche=t.Turtle()
raquettegauche.speed(0)
raquettegauche.shape("square")
raquettegauche.color("white")
raquettegauche.shapesize(stretch_wid=5, stretch_len=1)
raquettegauche.penup()
raquettegauche.goto(-350,0)

 # Creation of the right raquette
raquettedroite=t.Turtle()
raquettedroite.speed(0)
raquettedroite.square("square")
raquettedroite.color("white")
raquettedroite.shapesize(stretch_wid=5, stretch_len=1)
raquettedroite.penup()
raquettedroite.goto(-350,0)

  # Code to creation of the balise
balle=t.Turtle()
balle.speed(0)
balle.shape("circle")
balle.color("red")
balle.penup()
balle.goto(5,5)
ballexdirection=0.2
balleydirection=0.2

   # Code to update the score
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center", font=('Arial',24,'normal'))

    # Code to move the left raquette
def raquettegaucheup():
        y=raquettegauche.ycor()
        y=y+90
        raquettegauche.sety(y)

 # Code to move the right raquette
def raquettedroiteup():
       y=raquettedroite.ycor()
       y=y+90
       raquettedroite.sety(y)

 # Touches de jeu : w,s touches flèches haut et bas
window.listen()
window.onkeypress(raquettegauche-up,'w')
window.onkeypress(raquettegauche-down,'s')
window.onkeypress(raquettedroite-up,'Up')
window.onkeypress(raquettedroite-up,'Down')

while True:
     window.update()

 # Déplacement de la balle
balle.setx(balle.xcor()+ballex-direction)
balle.setx(balle.ycor()+ballex-direction)

  # Limites du terrain
if balle.ycor()>290:
      balle.sety(290)
      balleydirection=balley-direction*-1

if balle.ycor()<-290:
     balle.sety(-290)
     balleydirection=balley-direction*-1

if balle.xcor()>390:
     balle.goto(0,0)
     balle_dx = balle_dx * -1
     joueur_a_score = joueur_a_score + 1
     pen.clear()
     pen.write("Joueur A: {} Joueur B: {}".format(joueur_a_score, joueur_b_score), align="center", font=('Monaco', 24, 'normal'))
     os.system("son_balle_contre mur.wav&")

if balle.xcor()<-390:
     balle.goto(0,0)
     balle_dx = balle_dx * -1
     joueur_b_score = joueur_b_score + 1
     pen.clear()
     pen.write("Joueur A: {} Joueur B: {}".format(joueur_a_score, joueur_b_score), align="center", font=('Monaco', 24, 'normal'))
     os.system("son_balle_contre mur.wav&")

 # Gestion de la collision de la balle avec les raquettes
if (balle.xcor()>340) and (balle.xcor()<350) and (balle.ycor() < raquette_droite.ycor() + 40 and balle.ycor() > raquette_gauche.ycor() -40):
     balle.setx(340)
     balle_dx = balle_dx*-1
     os.system("son_balle_contre_raquette.wav&")

if (balle.xcor()<-340) and (balle.ycor()>-350) and (balle.ycor() +40 and balle.ycor()>raquettegauche.ycor()-40):
     balle.setx(-340)
     balle_dx = balle_dx*-1
     os.system("son_balle_contre_raquette.wav&")
