#-Vamos a crear una ventana donde en ella se pueda escibir una frase y se detecte cuan rápido es tu escritura.
#-Crearemos una lista con varias frases y abrá un botón que seleccione una de ellas al azar.
import tkinter as tk
import random
import time
#--Creamos la ventana principal, con sus parámetros de dimensión, color, título, etc...
ventana = tk.Tk()
ventana.title("Prueba de escritura veloz.")
ventana.geometry("1200x800+120+0")
ventana.configure(bg="lightgray")
#--Creamos un stringVar que es una variable de tipo texto.
texto = tk.StringVar(value="")
#--Creamos una etiqueta donde se escribirá la frase elegida al azar.
etiqueta = tk.Label(ventana, text="Frase a escribir")    #-Creamos un label
etiqueta.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
etiqueta.grid(row=0, column=2, padx=10, pady=10)
#--Etiqueta donde ese escribirá la frase que escribimos simultanaeamente y al acabar cambiará el mensaje de corrección final.
etiqueta1 = tk.Label(ventana, text="")  
etiqueta1.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
etiqueta1.grid(row=2, column=2, padx=10, pady=10)
#--Etiqueta donde mostraremos un reloj, para así tener cierta certeza de que el cálculo de palabras/minuto está bien hecho.
etiqueta2 = tk.Label(ventana, text=(""))
etiqueta2.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
etiqueta2.grid(row=0, column=5, padx=10, pady=10)
#--Etiqueta donde saldrá el mensaje con el cálculo final, tiempo de ejecución y palabras escritas por minuto
etiqueta3 = tk.Label(ventana, text=(""))
etiqueta3.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
etiqueta3.grid(row=3, column=2, padx=10, pady=10)
#--Cuadro de texto donde escribir nuestra frase.
entrada = tk.Entry(ventana, textvariable = texto)       #-El parámetro de texto de nuestra tk.entry es la variable "texto" de tipo tk.StringVar
entrada.config(fg="black", bg="ivory3", font=("Arial", 18, "normal"))
entrada.grid(row=4, column=2, padx=10, pady=10)

#--Creamos lista de frases.
lista_frases = ["Una madre es una manta que siempre te va a tapar", "No por mucho tempranar amanece más madrugo", "Soy más duro que el acero antes roto que doblarme", "Cuando el grajo vuela bajo, hace un frío del carajo"]
#--Función para mostrar el reloj dentro de la ventana.
def actualizar_hora():
    etiqueta2.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)        #-Con .after(1000, función), acualizamos cada 1000 milisegundos la llamada de la función, por lo tanto el reloj se actualiza cada segundo.
actualizar_hora()       #-Invocamos a la función.  
#--Introducimos un mode = "on",para que el inicio del temporizador solo se active una vez al pulsar la primera tecla del teclado al escribir.
mode = "on"  
def inicio_temporizador(event):
    global inicio
    global mode
    if mode == "on":
        inicio = time.time()        #-Inicio temporizador.
        mode = "off"
def fin_temporizador(event):
    if etiqueta.cget("text").strip().lower() == etiqueta1.cget("text").strip().lower():                     #-Establecemos condicional, si la frase está correctamente escrita o no...
        etiqueta3.config(text="Texto escrito correctamente, buen trabajo!")
    else:
        etiqueta3.config(text=("El texto que has escrito no se corresponde con el texto indicado."))
    fin = time.time()               #-Final temporizador.
    tiempo_total = fin - inicio
    palabras_escritas = len(etiqueta1.cget("text").split())
    print("Número de palabras escritas", len(etiqueta1.cget("text").split()))   #-Imprimimos número de palabras escritas por consola.
    velocidad = (palabras_escritas / tiempo_total) * 60
    etiqueta1.config(text=f"Has tardado {tiempo_total:.2f} segundos, {velocidad:.2f} palabras por minuto")

#--Función frase random.        
def frase_random():
    frase = random.choice(lista_frases)     #-Elegimos una frase al azar de nuestra lista de frases.
    etiqueta.config(text=frase)
 #--Creamos función para que al clicar el botón creado salga frase al azar.
def click_boton():         
    frase_random()
#--Creamos botón para activar la frase aleatoria.
boton = tk.Button(ventana, text = "Frase aleatoria")
boton.config(fg="black", bg="gray", font=("Arial", 18, "normal"), command=click_boton)
boton.grid(row=0, column=0, padx=100, pady=10)
#--Función que actualiza constantemente el texto escrito a la etiqueta1
def actualizar_etiqueta(*args):
    etiqueta1.config(text=texto.get())        
texto.trace("w", actualizar_etiqueta)   #-Con .trace("w", función) llamamos a la función al mismo momento que el texto se esté modificando y actualizamos el texto de la etiqueta1. 
#--Vincular teclado.
ventana.bind("<Key>", inicio_temporizador)      #-Vinclamos cualquier tecla del teclado que se presione, e invocamos al inicio del temporizador.
ventana.bind("<Return>", fin_temporizador)      #-Vinculamos la tecla enter con el final de la escritura y así invocamos al final del temporizador.
#--Función de reinicio.
def reinicio():
    global mode             
    mode = "on"                 #-Volvemos a poner el mode = "on", para que al volver a escribir se inicie de nuevo el temporizador
    entrada.delete(0, tk.END)   #-El método .delete borra todo el contenido de nuestra tk.Entry
#--Creamos botón de reinicio.
boton_reinicio = tk.Button(ventana, text = "Reiniciar prueba")
boton_reinicio.config(fg="black", bg="gray", font=("Arial", 18, "normal"), command=reinicio)
boton_reinicio.grid(row=4, column=0, padx=100, pady=10)
#--Mantenemos la ventana abierta.
ventana.mainloop()