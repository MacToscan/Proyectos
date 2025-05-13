import turtle
import time
import pygame
import random

#--Creamos la ventana.
ventana = turtle.Screen()
ventana.title("PONG Arcade")
color_list = ["blue","green","darkgreen","darkolivegreen","burlywood4","cadetblue","darkorange","darkseagreen4","DarkGoldenrod1","DarkGoldenrod4","indianred3","LightSalmon3","NavajoWhite3","tomato3","red3"]
color = random.choice(color_list)
print("Color de la pista de juego: ", color)
ventana.bgcolor(color)
ventana.setup(width=800, height=600)
ventana.tracer(0)
#--Función para cambiar de color la pista.
def color_ventana():
    color_list = ["blue","green","darkgreen","darkolivegreen","burlywood4","cadetblue","darkorange","darkseagreen4","DarkGoldenrod1","DarkGoldenrod4","indianred3","LightSalmon3","NavajoWhite3","tomato3","red3"]
    color = random.choice(color_list)
    print("Color de la pista de juego: ", color)
    ventana.bgcolor(color)
#--Lineas pista de juego
raya = turtle.Turtle()
raya.speed(0)
raya.shape("square")
raya.color("white")
raya.shapesize(stretch_wid=40, stretch_len=0.2)
raya.goto(-5,0)
turtle.penup()
turtle.goto(-5,-70)
turtle.pendown()
turtle.color("white")
turtle.pensize(5)
turtle.circle(75)
turtle.penup()
turtle.goto(390,-175)
turtle.pendown()
turtle.circle(175,-180)
turtle.penup()
turtle.goto(0,0)
turtle.goto(-400,175)
turtle.pendown()
turtle.circle(175,-180)

#-Creamos las palas del juego.
#--Definimos la variable de la "Pala A"
pala_a = turtle.Turtle()
pala_a.speed(0)
pala_a.shape("square")
pala_a.color("white")
pala_a.shapesize(stretch_wid=5, stretch_len=1)
pala_a.penup()
pala_a.goto(-350,0)

#--Definimos la variable de la "Pala B"
pala_b = turtle.Turtle()
pala_b.speed(0)
pala_b.shape("square")
pala_b.color("white")
pala_b.shapesize(stretch_wid=5, stretch_len=1)
pala_b.penup()
pala_b.goto(350,0)

#--Creamos la pelota.
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("black")
pelota.shapesize(1)
pelota.penup()
pelota.goto(0,0)
pelota.mx = 3.2    #-Comando que define cantidad de pixels que se mueve la pelota con cada ciclo en el eje X.
pelota.my = 3.2     #-Comando que define cantidad de pixels que se mueve la pelota con cada ciclo en el eje Y.

#--Creamos contador de puntos.
contador = turtle.Turtle()
contador.speed(0)
contador.color("black")
contador.penup()
contador.goto(0,270)
contador.write("Jugador A: 0    Vs    Jugador B: 0", align="center", font=("Arial", 20, "normal"))

#--Variables de puntaje.
puntaje_a = 0
puntaje_b = 0

#--Pen variable turtle.
pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.fillcolor("white")

#--Crear medidas del botón de reinicio..
boton_x = -170
boton_y = -285
boton_width = 125
boton_height = 40

# Turtle dedicado a dibujar botones (inicio y reinicio)
boton_turtle = turtle.Turtle()
boton_turtle.hideturtle()
boton_turtle.penup()   

# Variable global que guarda las coordenadas actuales del botón
boton_coords = None
def dibujar_boton(texto):
    global boton_coords
   #boton_turtle.clear()
    boton_turtle.goto(boton_x, boton_y)
    boton_turtle.color("black", "white")
    boton_turtle.begin_fill()
    for _ in range(2):
        boton_turtle.forward(boton_width)
        boton_turtle.left(90)
        boton_turtle.forward(boton_height)
        boton_turtle.left(90)
    boton_turtle.end_fill()
    boton_turtle.goto(boton_x + boton_width / 2, boton_y + boton_height / 2 - 10)
    boton_turtle.write(texto, align="center", font=("Arial", 16, "normal"))
    boton_coords = (boton_x, boton_y, boton_x + boton_width, boton_y + boton_height)

#--Creamos el modo de juego en una variable.
game_state = "waiting"
#--Función para realizar el click en el botón.
def click(x, y):
    global game_state
    if boton_coords is not None:
        x1, y1, x2, y2 = boton_coords
        if x1 <= x <= x2 and y1 <= y <= y2:
            if game_state == "waiting":
                # Iniciar el juego
                boton_turtle.clear()
                update_score()
                game_state = "playing"
            elif game_state == "gameover":
                # Reiniciar juego
                reinicio()
                color_ventana()
ventana.onclick(click)

#--Reinicio juego.
def reinicio():
    global puntaje_a, puntaje_b, game_state
    puntaje_a = 0
    puntaje_b = 0
    update_score()
    pelota.goto(0, 0)
    pelota.mx = 1.2
    pelota.my = 1.2
    mensaje_a.clear()
    # Ocultar botón de reinicio
    boton_turtle.clear()
    game_state = "playing"

def iniciar_juego():
    global game_state
    # Mostrar botón de inicio
    dibujar_boton("Iniciar Juego")
    game_state = "waiting"
def update_score():

    contador.clear()
    contador.write("Jugador A: {}    Vs    Jugador B: {}".format(puntaje_a, puntaje_b),
                   align="center", font=("Arial", 20, "normal"))
    
#--Función para generar el sonido en cada rebote.
def sonido_pelota():
    pygame.init()
    pygame.mixer.music.load("boing1.mp3")
    pygame.mixer.music.play()

#--Mensaje Ganador.
mensaje_a = turtle.Turtle()
mensaje_a.speed(0)
mensaje_a.color("black")
mensaje_a.goto(0,0)
mensaje_a.hideturtle()

#--Funciones para subir y bajar las palas.
#Subir Pala A
def pala_a_arriba():
    y = pala_a.ycor()
    y += 20
    pala_a.sety(y)
#Vincular el teclado al movimiento.
ventana.listen()
ventana.onkeypress(pala_a_arriba, "w")
#Bajar Pala A
def pala_a_bajar():
    y = pala_a.ycor()
    y -= 20
    pala_a.sety(y)
#Vincular el teclado al movimiento.
ventana.listen()
ventana.onkeypress(pala_a_bajar, "s")
#Subir Pala B
def pala_b_arriba():
    y = pala_b.ycor()
    y += 20
    pala_b.sety(y)
#Vincular el teclado al movimiento.
ventana.listen()
ventana.onkeypress(pala_b_arriba, "Up")
#Bajar Pala B
def pala_b_bajar():
    y = pala_b.ycor()
    y -= 20
    pala_b.sety(y)
#Vincular el teclado al movimiento.
ventana.listen()
ventana.onkeypress(pala_b_bajar, "Down")

#-Inciamos juego.
iniciar_juego()
#--Loop principal
while True:
    ventana.update()
    if game_state == "playing":
    #Movimientos pelota.
        pelota.setx(pelota.xcor() + pelota.mx)
        pelota.sety(pelota.ycor() + pelota.my)
        #Establecer límites de pista de juego. 
        if pelota.ycor() > 290:
            pelota.sety(290)
            sonido_pelota()         #Cuando llega a la medida de la ventana creada cambia de sentid y reproduce el sonido.
            pelota.my *= -1
        if pelota.ycor() < -290:
            pelota.sety(-290)
            sonido_pelota()
            pelota.my *= -1
        if pelota.xcor() > 390:
            pelota.goto(0,0)            #Si sobrepasa las palas, se suma 1 punto al marcador.
            pelota.mx *= -1
            puntaje_a += 1
            update_score()
            if puntaje_a == 3:
                mensaje_a.write("Ganador Jugador A", align="center", font=("Arial", 40, "normal"))
                game_state = "gameover"
                dibujar_boton("Reiniciar juego")

        if pelota.xcor() < -390:
            pelota.goto(0,0)
            pelota.mx *= -1
            puntaje_b += 1
            update_score()
            if puntaje_b == 3:
                mensaje_a.write("Ganador Jugador B", align="center", font=("Arial", 40, "normal"))
                game_state = "gameover"
                dibujar_boton("Reiniciar juego")
                
        #Choque en palas.
        if pelota.xcor() < -340 and pelota.ycor() < pala_a.ycor() + 50 and pelota.ycor() > pala_a.ycor() - 50:
            sonido_pelota()
            pelota.mx *= -1
        elif pelota.xcor() > 340 and pelota.ycor() < pala_b.ycor() + 50 and pelota.ycor() > pala_b.ycor() - 50:
            sonido_pelota()
            pelota.mx *= -1

