from tkinter import *
from tkinter import filedialog
from io import open
from tkinter import font
from tkinter import colorchooser

global ruta         #--Utilizamos la variable global ruta para almacenar los ficheros.
ruta = ""      
global seleccion    #--Utilizamos la variable global seleccion para cortar, copiar y pegar texto seleccionado.
seleccion = False
global etiqueta_contador    #-Variable que nos permite seleccionar más de una etiqueta, para poder cambiar de color mas de una etiqueta, sumandole 1 cada vez que se seleccione un texto.
etiqueta_contador = 0       
#--///FUNCIONES PARA CREAR ARCHIVOS, NUEVO, ABRIR, GUARDAR Y GUARDAR COMO
#--Función para crear un archivo nuevo y vacío.
def nuevo():
    global ruta
    mensaje.set("Nuevo archivo")        #-Mensaje en monitor inferior.
    ruta = ""                               #-Establecemos la variable ruta sin nombre, por si queremos guardar en algún momento.
    texto.delete(0.0, END)                      #-Borramos todo el texto que se encuentre en el editor.
    root.title("Editor de texto")                   #-Ponemos el nombre de la ventana, cada vez que se inicie un archivo nuevo.
#--Función para abrir un archivo guardado.
def abrir():
    global ruta                                       
    ruta = filedialog.askopenfilename(initialdir=".",         #-Indicamos el directorio que abrirá inicialmente, con ".", indicamos que abrirá el directorio en el cual estamos.
                                      title="Abrir un archivo de texto",        #-Título de la ventana de los archivos a abrir.
                                      filetypes = (("Ficheros de texto", "*.txt"),),)   #-Indicamos el tipo de archivo que podemos abrir, todos los que sean .txt.
    if ruta != "":          #-Si la varible ruta tiene nombre entonces...
        with open(ruta, "r") as archivo: #-Abrimos el archivo en modo lectura y le damos el nombre a la variable.
            contenido = archivo.read()          #-Definimos la variable contenido con el archivo abierto anteriormente.
            texto.delete(0.0, END)                  #-Borramos todo el texto que se encuentre en nuestro editor, para dejar la página en blanco para nuestro archivo.
            texto.insert("insert", contenido)           #-Insertmaos nuestro archivo seleccionado anteriormente.
            root.title(ruta + " - Editor del Sr. Toscano")      #-Ponemos nombre en la ventana a nuestro archivo.
            mensaje.set("Archivo abierto correctamente")            #-Mensaje en nuestro monitor inferior.
#-Función guardar.      
def guardar():
    global ruta
    mensaje.set("Guardar archivo")          #-Mensaje en nuestro monitor inferior.
    if ruta != "":                  #-Si la variable ruta tiene nombre.
        contenido = texto.get(0.0, "end-1c")    #-Cogemos el texto del editor.
        with open(ruta, "w+") as fichero:                 #-Cogemos el fichero de dicha ruta y lo abrimos.
            fichero.write(contenido)                        #-Volveremos a guardar, esta vez, el contenido actual.
            mensaje.set("Archivo guardado correctamente")           #-Mensaje del monitor inferior.
    else:
        guardar_como()              #-Llamamos a la función guardar como en el caso que la variable ruta no tenga un nombre definido.
#-Función guardar como.
def guardar_como():
    global ruta
    mensaje.set("Guardar archivo como")
    fichero = filedialog.asksaveasfile(title="Guardar archivo", mode="w", defaultextension=".txt")  #-Creamos un fichero nuevo con filedialog.asksaveasfile()
    if fichero is not None:             #-Comprobamos que el fichero se ha creado correctamente.
        ruta = fichero.name                 #-Establecemos el nombre de la ruta con fichero.name, que nos dice la ruta exacta del fichero.
        contenido = texto.get(0.0, "end-1c")    #-Hacemos los mismo pasos que en la función anterior <guardar()>.
        with open(ruta, "w+") as fichero:
            fichero.write(contenido)
            fichero.close()
            mensaje.set("Archivo guardado correctamente")
    else:                                       #-Si el fichero no se ha creado correctamente, se ha cancelado o similar, entonces imprime mensaje de "guardado cancelado"
        mensaje.set("Guardado cancelado")
        ruta = ""
#--///FUNCIONES DE CORTAR, COPIAR Y PEGAR///
#--Función que nos permite cortar el texto seleccionado.
def cortar():
    global seleccion
    if texto.selection_get():               #-Si tenemos algo en seleccionado en nuestro editor, entonces...
            try:
                seleccion = texto.selection_get()       #-Creamos la variable selección con lo que tenemos seleccionado.
            except TclError:
                return
            texto.delete("sel.first", "sel.last")       #-Borramos toda la selección del texto.
            root.clipboard_clear()                          #-Eliminamos lo que pueda haber en el portapapeles.
            root.clipboard_append(seleccion)                    #-Añadimos nuestra selección al portapapeles, para futuras acciones.
#--Función que nos permite copiar el texto seleccionado.
def copiar():
    global seleccion
    if texto.selection_get():       #-La misma lógica que en la función cortar exceptuando el borrado del texto seleccionado (selección).
        try:
                seleccion = texto.selection_get()       #-Creamos la variable selección con lo que tenemos seleccionado.
        except TclError:
            return
        root.clipboard_clear()
        root.clipboard_append(seleccion)
#--Función que nos permite pegar el texto seleccionado.
def pegar():                                   # Pegar el texto del portapapeles, .insert("donde esta el cursor", "lo que esta en el portapapeles")
    texto.insert(INSERT, root.clipboard_get())    #-Siempre que se guarde algo en el portapapeles o clipboard, con atajos de teclado o desde el menú editar, se pegará donde decimos.     
#--Función que nos abre en el root el menú desplegable Editar, al clicar con el botón dercho del mouse.
def on_click(event):
    editmenu.post(event.x_root, event.y_root)
#--Función que actualiza el monitor inferior para que cambie el mensaje una vez se haya podido leer.
def actualizar_monitor():
    root.after(10000, actualizar_monitor) 
    mensaje.set("Bienvenido al editor de texto del Sr. Toscano")
#Función padre para cambiar el tipo de fuente, dando el parámetro de esta.
def cambiar_fuente(fuente):
    tipo_fuente = font.Font(font=texto.cget("font"))        #-Establecemos el tipo de fuente para posteriormente sacar el tamaño de la fuente.
    tamaño_fuente = tipo_fuente.cget("size")                     #-Creamos la variable, del tamaño de la fuente.
    texto.config(bd=30, padx=6, pady=4, font=(fuente, str(tamaño_fuente)))     #-Actualizamos el texto del botón de tamaño, para que sea acorde al tamaño seleccionado
    actualizar_boton_fuente()                                             #-Actualizamos el texto del botón de tamaño, para que sea acorde al tamaño seleccionado
    actualizar_boton_fuente()                                                  #-Actualizamos el texto del botón de tipo de fuente, para que sea acorde a la fuente seleccionada.
#--Funciones que cambian la fuente mediante un botón desplegable.
def consolas():
    cambiar_fuente("Consolas")
def arial():
    cambiar_fuente("Arial")
def verdana():
    cambiar_fuente("Verdana")
def times():
    cambiar_fuente("Times")
def menlo():
    cambiar_fuente("Menlo")
#Función padre para cambiar el tamaño de la fuente, dando el parámetro de esta.
def cambiar_tamaño(tamaño):
    fuente_actual = font.Font(font=texto.cget("font"))      #-Obtenemos la fuente actual.
    texto.config(font=(fuente_actual.actual()['family'], tamaño))   #-Cambiamos el tamaño de la fuente respetando esta.
    actualizar_boton_tamaño()                                           #-Actualizamos el texto del botón de tamaño, para que sea acorde al tamaño seleccionado
    actualizar_boton_fuente()                                                 #-Actualizamos el texto del botón de tipo de fuente, para que sea acorde a la fuente seleccionada.
#--Funciones que cambian el tamaño de la fuente mediante un botón desplegable.
def tamaño_10():
    cambiar_tamaño(10)
def tamaño_12():
    cambiar_tamaño(12)
def tamaño_14():
    cambiar_tamaño(14)
def tamaño_16():
    cambiar_tamaño(16)
def tamaño_20():
    cambiar_tamaño(20)
#--Función que actualizaliza el texto del botón de tipo de fuente, para que esté acorde a la fuente seleccionada.
def actualizar_boton_fuente():
    fuente_actual = font.Font(font=texto.cget("font"))  #-Obtenemos fuente actual.
    boton_fuente.config(text = fuente_actual.actual()['family']) #-Cambiamos texto del botón.
#--Función que actualiza el texto del botón del tamaño de la feunte, para que esté acorde al tamaño seleccionado.
def actualizar_boton_tamaño():
    fuente_actual = font.Font(font=texto.cget("font"))    #-Obtenemos fuente actual.
    tamaño_fuente = fuente_actual.cget("size")            #-Obtenemos el tamaño de la fuente.
    boton_tamaño.config(text = str(tamaño_fuente))   #-Cambiamos el texto del botón.
#--Funciones que cambian el tipo de escritura, (negrita, cursiva) mediante un botón.
def negrita():
    global texto
    bold_font = font.Font(texto, texto.cget("font"))    
    bold_font.configure(weight="bold")                  #-Creamos nuestra fuente en negrita.
    texto.tag_configure("bold", font=bold_font)         #-Creamos una etiqueta llamada "bold", que coge como fuente la anterior creada.
    etiqueta_actual = texto.tag_names("sel.first")      #-Definimos la posición de la etiqueta.
    if "bold" in etiqueta_actual:
        texto.tag_remove("bold", "sel.first", "sel.last")   #-Si el texto seleccionado esta en negrita, entonces borrara el efecto, y volvera a su estado "normal"
    else:
        texto.tag_add("bold", "sel.first", "sel.last")      #-Si por el contrario "bold", no existe, convertira el texto seleccionado en negrita.
#--Hacemos exactamente lo mismo que con la función anterior, para pasar el texto seleccionado a cursiva.
def cursiva():
    global texto
    italic_font = font.Font(texto, texto.cget("font"))
    italic_font.configure(slant="italic")           #-El único punto que cambia con respecto la función anterior es la manera de llamar a "italic", que es mediante "slant" y weight.
    texto.tag_configure("italic", font=italic_font)
    etiqueta_actual = texto.tag_names("sel.first")
    if "italic" in etiqueta_actual:
        texto.tag_remove("italic", "sel.first", "sel.last")
    else:
        texto.tag_add("italic", "sel.first", "sel.last")
def color_fuente():
    global etiqueta_contador
    fuente_actual = font.Font(font=texto.cget("font"))      #-Obtenemos fuente actual.
    tipo_fuente = font.Font(font=texto.cget("font"))            #-Establecemos el tipo de fuente para posteriormente sacar el tamaño de la fuente.
    tamaño_fuente = tipo_fuente.cget("size")                        #-Creamos la variable, del tamaño de la fuente.
    color = colorchooser.askcolor()[1]              #-Le asignamos a la variable color, la paleta de colores por default que viene con colorchooser.
    if color:
        etiqueta = f"select{etiqueta_contador}"       #-Variable etiqueta que va a ser el nombre que le damos al texto seleccionado, más un contador.
        texto.tag_add(etiqueta, "sel.first", "sel.last")   #-Agregamos la etiqueta en toda nuestra selección.     
        texto.tag_config(etiqueta, foreground=color)            #-Configuramos nuestra etiqueta para que el color sea el elegido en la paleta.
        texto.config(font=(fuente_actual.actual()['family'], tamaño_fuente))    #-Dejamos el texto con la misma fuente y el mismo tamaño
        etiqueta_contador += 1   #-Añadimos +1 en el contadoppr para que las etiiquetas sean diferentes y podamos tener más de un color dentro de nuestro edior.
#--Creamos ventana
root = Tk() 
root.title("Editor de texto")       #Título de la ventana.
root.geometry("640x490+0+0")
#--Menú de gestión de archivos.
menubar = Menu(root)
filemenu = Menu(menubar)
#--Creamos el menú desplegable "cascade".
filemenu.add_command(label="Nuevo", command=nuevo)      #-Vinculamos nuestros labels a las funciones correspondientes.
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()        #-Hacemos una linea separadora de nuestros labels anteriores.
filemenu.add_command(label="Salir", command=root.quit)  #-Utilizamos la propia función .quit de root para salir de la ventana.
menubar.add_cascade(menu = filemenu, label="Archivo")       #-Ponemos el nombre a la pestaña principal.
#--Menú de esdición de texto.
editmenu = Menu(menubar)
#--Creamos el menú desplegable "cascade".
editmenu.add_command(label="Copiar      (Ctrl+c)", command=copiar)     #-Labels del menu Editar, vinculados a las funciones Copiar, Cortar y Pegar.
editmenu.add_command(label="Cortar      (Ctrl+x)", command=cortar)
editmenu.add_command(label="Pegar       (Ctrl+v)", command=pegar)
menubar.add_cascade(menu = editmenu, label="Editar")
#--Añadimos el menú editar "editmenu" en la pantalla al tocar botón derecho del ratón.
root.bind("<2>", on_click)      #-<2> es el botón derecho del ratón, invocamos la función on_click que nos lleva al menú editar.
#--Atajos de teclado para menú editar.
root.bind("<Control-Key-x>", cortar)    #-Creamos los atajos de teclado para cortar, copiar y pegar, aunque no sería necesario porque vienen por default.
root.bind("<Control-Key-c>", copiar)
root.bind("<Control-Key-v>", pegar)
#--Caja de texto central.
texto = Text(root, undo = True, wrap=WORD)       #-Creamos el widget de texto, ponemos wrap=WORD para que al acabarse el ancho de la ventana salte de linea si la palabra no acaba.
#texto.config(bg="white", fg="black",  )
texto.pack(fill="both",  expand= 1)      #-Ocupamos todo el root
#--Barra lateral de depslazamiento vertical.
text_scroll = Scrollbar(texto)
text_scroll.pack(side="right", fill=Y)
text_scroll.config(command=texto.yview)     #-Configuramos la barra lateral a la variable texto con movimiento en Y.
#-Configuramos el texto de nuestro editor.
texto.config(bd=30, padx=6, pady=4,font=("Menlo"), selectbackground="rosy brown", yscrollcommand=text_scroll.set)
#-Configuramos nuestro menú superior, Archivo y Editar, para que se haga presente.
root.config(menu=menubar)
#--Label donde ubicar los botones.
barra = Frame(root)
barra.config(bg="black")
barra.place(x=20, y=5)
#--Boton tipo de fuente.
fuente_actual = font.Font(font=texto.cget("font"))                                  #-Obtenemos fuente actual.
boton_fuente = Menubutton(barra, text = str(fuente_actual.actual()['family']))          #-Creamos MenuButton con el texto de la feunte actual.
boton_fuente.config(fg="black", bg="gray", font=("Menlo", 12, "normal"))                 #-Configuarmos el tipo de botón que queremos.
boton_fuente.pack(side="left")
boton_fuente.menu = Menu(boton_fuente, tearoff=0)                            #-Creamos el menú depslegable del botón
boton_fuente["menu"] = boton_fuente.menu
boton_fuente.menu.add_radiobutton(label="Consolas", command=consolas)           #-Creamos RadioButtons para que solo se pueda quedar seleccionado uno de ellos.
boton_fuente.menu.add_radiobutton(label="Arial", command=arial)
boton_fuente.menu.add_radiobutton(label="Verdana", command=verdana)
boton_fuente.menu.add_radiobutton(label="Times", command=times)
boton_fuente.menu.add_radiobutton(label="Menlo", command=menlo)
#--Definimos el tamaño de la feunte para poder poner el tamaño en el botón.
tamaño_fuente = fuente_actual.cget("size")
#--Botón tamaño fuente.
boton_tamaño = Menubutton(barra, text = str(tamaño_fuente))
boton_tamaño.config(fg="black", bg="gray", font=("Menlo", 12, "normal"))
boton_tamaño.pack(side="left")
boton_tamaño.menu = Menu(boton_tamaño, tearoff=0)                             #-Creamos el menú depslegable del botón
boton_tamaño["menu"] = boton_tamaño.menu
boton_tamaño.menu.add_radiobutton(label="10", command=tamaño_10)                 #-Creamos RadioButtons para que solo se pueda quedar seleccionado uno de ellos
boton_tamaño.menu.add_radiobutton(label="12", command=tamaño_12)
boton_tamaño.menu.add_radiobutton(label="14", command=tamaño_14)
boton_tamaño.menu.add_radiobutton(label="16", command=tamaño_16)
boton_tamaño.menu.add_radiobutton(label="20", command=tamaño_20)
#--Botón color de texto.
imagen = PhotoImage(file="/Users/mactoscano/ConquerBlocks/Python/Ejercicios/Archivos/icon_color2.png")     #-Cargamos la imagen desde su ruta.
boton_color = Button(barra, image= imagen)      #-Creamos el botón, lo situamos en la barra y le damos la imagen anterior como objeto visible.
boton_color.image = imagen                  #-Mantenemos una referéncia a la imagen
#boton_color = Button(barra, text="Color")   #////////-----Si no tienes descargado el icono utiliza este formato.-----///////
boton_color.config(fg="black",bg="gray", font=("Menlo", 12, "bold"), command=color_fuente)
boton_color.pack(side="right")
#--Botón cursiva.
boton_cursiva = Button(barra, text=("K"))           #-Creamos botón, lo situqamos en la barra y le damos el nombre.
boton_cursiva.config(fg="black", bg="gray", font=("Menlo", 12, "italic"), command=cursiva)     #-Le ponemos sus características, en este caso ponemos letra en cursiva.
boton_cursiva.pack(side="right")
#--Botón negrita
boton_negrita = Button(barra, text=("N"))           #-Creamos botón, lo situqamos en la barra y le damos el nombre.
boton_negrita.config(fg="black", bg="gray", font=("Menlo", 12, "bold"), command=negrita)    #-Le ponemos sus características, en este caso ponemos letra en negrita.
boton_negrita.pack(side="right")
#--Texto en monitor inferior.
mensaje = StringVar()
mensaje.set("Bienvenido al editor de texto del Sr. Toscano")
monitor = Label(root, textvar = mensaje)
monitor.config(fg="lightgray", font=("Menlo", 12, "normal"))
monitor.pack(side="left", padx=10)

actualizar_monitor()        #--Actualizamos constantemente el mensaje del monitor inferior cada 10000 ms
root.mainloop()