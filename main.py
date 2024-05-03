#declaración de librerias
import os
import base64

#funcion para crear un archivo o carpeta
def crear():
    os.system("cls") #limpiar consola
    
    #menu de opciones para elegir el modo entre directorio o archivos
    print("¿Que quieres crear?")
    print("1.- Directorio.")
    print("2.- Archivo.")
    opcion = input("Elija la opción que desear realizar: ") #elije la opcion del menu
    
    if (opcion == "1"):
        try:
            ruta = input("Ingrese la ruta para gruardar el directorio (con la carpeta añadida ya): ")
            archivo = os.mkdir(ruta) #creación de la carpeta
            mensaje = "Se ha creado perfectamente el archivo."
        except FileNotFoundError:
            mensaje = "No se ha encontrado la ruta."
        except IOError:
            mensaje = "Ha habido un error en la creación."
        
    elif (opcion == "2"):
        try:
            ruta = input("Ingrese la ruta para gruardar el archivo: ")        
            nombre = input("Elija el nombre del archivo que desea crear, añada extensión correspondiente: ")
            if (os.path.exists(os.path.join(ruta,nombre))):
                mensaje = "El archivo ya existe."
            elif (os.path.exists(ruta)):
                mensaje = "Ya existe el archivo."
            else:
                archivo = open(os.path.join(ruta,nombre), 'w') #creación de un archivo
                archivo.close() #cerramos el archivo
                
                mensaje = "Se ha creado perfectamente el archivo en: " + ruta
            
        except Exception as Error:
            mensaje = "El error que ha sucedidio es "+ Error
    else:
        mensaje = "Carácter no válido."
    
    input("Pulsa una tecla para continuar ...")
    return mensaje
     
#funcion para eliminar archivos o directorios   
def eliminar():
    os.system("cls") #limpiar consola
    
    #menu de opciones para elegir el modo entre directorio o archivos
    print("¿Que quieres eliminar?")
    print("1.- Directorio.")
    print("2.- Archivo.")
    opcion = input("Elija la opción que desear realizar: ") #elije la opcion del menu
    
    if (opcion == "1"):
        ruta = input("Ingrese la ruta para elimiar el directorio (con el directorio que desea eliminar incluido): ")
        
        #comprovación de si existe la ruta elegida por el usuario
        try:
            archivo = os.removedirs(ruta) #eliminación de directorio
            mensaje = "Se ha eliminado perfectamente el directorio."
        except FileNotFoundError:
            mensaje = "El directorio no existe."

    elif (opcion == "2"):
        ruta = input("Ingrese la ruta del del archivo con el archivo: ")
        
        #comprovación de si existe la ruta elegida por el usuario
        try:
            archivo = os.remove(ruta) #eliminación del archivo
            mensaje = "El archivo se ha eliminado correctamente."
        except FileNotFoundError:
            mensaje = "El archivo no existe."
    else:
        mensaje = "Carácter no válido"
    
    input("Pulsa una tecla para continuar ...")
    return mensaje

#funcion para mover directorios o archivos
def mover():
    os.system("cls") #limpiar consola
    
    #menu de opciones para elegir el modo entre directorio o archivos
    print("¿Que desea mover?")
    print("1.- Directorio.")
    print("2.- Archivo.")
    opcion = input("Elija la opción que desea realizar: ") #elije la opcion del menu

    if (opcion == "1"):
        ruta = input("Elija la ruta del directorio que desea mover:")
        
        #comprovación de si existe la ruta elegida por el usuario
        try:
            nueva = input("Elija la ruta donde desea mover el directorio con el directorio movido incluido: ")
            archvo = os.replace(ruta,nueva) #cambiar la ubicación del directorio
            mensaje = "Se ha movido correctamene el archivo."

        except FileNotFoundError:
            mensaje = "La ruta no existe."

    elif (opcion == "2"):
        ruta = input("Elija la ruta del archivo que desea mover:")
        
        #comprovación de si existe la ruta elegida por el usuario
        try:
            nueva = input("Elija la ruta donde desea mover el archivo con el archivo movido incluido: ")
            archivo = os.replace(ruta,nueva) #cambiar la ubicación del archivo
            mensaje = "Se ha movido correctamente el archivo: "
        except FileNotFoundError:
            mensaje = "La ruta no exsiste."
    else:
        mensaje = "Carácter no válido"

    input("Pulsa una tecla para continuar ...")
    return mensaje
    
#funcion para renombrar archivos o directorios
def renombrar():
    os.system("cls") #limpiar consola
    
    #menu de opciones para elegir el modo entre directorio o archivos
    print("¿Que desea renombrar?")
    print("1.- Directorio.")
    print("2.- Archivo.")
    opcion = input("Elija la opción que desear realizar: ") #elije la opcion del menu

    if (opcion == "1"):
        ruta = input("Escriba la ruta del directorio que desea renombrar: ")
        
        #comprovación de si existe la ruta elegida por el usuario
        try:
            nueva = input("Escriba la ruta del directorio que va a substituir el nombre del otro directorio: ")
            archivo = os.rename(ruta,nueva) #renombrar un direcctoiro
            mensaje = "Se ha renombrado correctamente el directorio."
        except FileNotFoundError:
            mensaje = "La ruta del directorio no existe."

    elif (opcion == "2"):
        ruta = input("Elija la ruta del archivo que desea renombrar: ")
        
        #comprovación de si existe la ruta elegida por el usuario
        try:
            nueva = input("Escriba la ruta del archivo que desea substituir el otro archivo: ")
            archivo = os.rename(ruta,nueva) #renombrar un archivo
            mensaje = "Se ha renombrado correctamente el archivo."
        except FileNotFoundError:
            mensaje = "La ruta no existe."
    else:
        mensaje = "Carácter no válido"
    
    return mensaje

#función que encripta el contenido del archivo
def encriptar():
    os.system("cls") #limpiar consola
    ruta = input("Introduzca la ruta del archivo que quiere encriptar: ")
    
    #comprovación de si existe la ruta elegida por el usuario
    try:
        with open(ruta, "rb") as archivo:
            leer = archivo.read()
            codificacion = base64.b64encode(leer) #codificar el archivo

        with open(ruta, "wb") as archivo_codificado:
            archivo_codificado.write(codificacion) #reescribir el contenido del archivo para que solo se muestre que este cifrado

        mensaje = "Archivo encriptado correctamente."
        
    except FileNotFoundError:
        mensaje = "El archivo: " + ruta + " no existe."
        
    input("Pulsa una tecla para continuar ...")
    return mensaje

#función que desencripta el contenido del archivo
def desencriptar():
    os.system("cls") #limpiar consola

    try:
        ruta = input("Introduzca la ruta del archivo que quiere encriptar: ")
    #comprovación de si existe la ruta elegida por el usuario
        with open(ruta, "rb") as archivo:
            leer = archivo.read()
            codificacion = base64.b64decode(leer) # decodificar el archivo

        with open(ruta, "wb") as archivo_codificado:
            archivo_codificado.write(codificacion) #reescribir el contenido del archivo para que solo se muestre el contenido decodificado

        mensaje = "Archivo desencriptado correctamente."
        
    except FileNotFoundError:
        mensaje = "El fichero: " + ruta + " no existe"

    return mensaje

#funcion para escribir en un archivo
def introducirtexto():
    os.system("cls") #limpiar consola
    ruta = input("Introduzca la ruta del archivo que quiere escribir: ")
    
    #comprovación de si existe la ruta elegida por el usuario
    try:
        with open(ruta, 'w') as file:
            escritura = input("Introduzca el texto que desea escribir: ")
            file.write(escritura) #reescribir el contenido del archivo para que solo se muestre que este cifrado

        mensaje = "Archivo redactado correctamente en: " + ruta
        
    except FileNotFoundError:
        mensaje = "No existe: " + ruta
    except Exception as error:
        mensaje = "Se ha producido el siguiente error: " + error + "en el fichero: " + ruta
        
    input("Pulsa una tecla para continuar ...")  
    return mensaje

#funcion para printar el contenido
def printar():
    os.system("cls") #limpiar consola
    ruta = input("Introduzca la ruta del archivo que quiere mostrar: ")
    
    try:
        with open(ruta, "r") as archivo:
            leer = archivo.read()
            anuncio = "El contendio del fichero es: \n"
            mensaje = anuncio + leer
    except FileNotFoundError:
        mensaje = "El archivo: " + ruta + " no existe. Intentelo de nuevo."
    except IOError:
        mensaje = "Error en el proceso de lectura del fichero: " +  ruta + " intentelo de nuevo."
    input("Pulsa una tecla para continuar ...")
    return mensaje
    
#funcion esqueleto del programa
def main():
    os.system("cls") #limpiar consola
    mensaje = "" #inicialización de la variable que mostrará el mensaje
    while True:
        #presentación del estudiante
        print("Autor: Aitor Segura")
        print("Curso: ASIR 2023-24.")
        print("Practica: creación, eliminación, renombración, desplazamiento de archivos y carpetas. Encriptación de archivos.")
        print("---------------------------------------------------------------------------------------------------------------")
        print(mensaje,"\n")
        print("0.- Para salir.")
        print("1.- Crear un directorio / archivo.")
        print("2.- Eliminar un directorio / archivo.")
        print("3.- Mover un directorio / archivo.")
        print("4.- Renombrar un directorio / archivo.")
        print("5.- Encriptar el contenido de un archivo.")
        print("6.- Decodificar el contenido de un archivo.")
        print("7.- Escribir en un archivo.")
        print("8.- Mostrar contenido archivo.")
        opc = input("Elija una acción a realizar: ") #elije la opcion del menu
        
    # condiciones que sirven para seleccionar la opción del menu
        if(opc == "1"):
            mensaje = crear()
        elif (opc == "2"):
            mensaje = eliminar()
        elif (opc == "3"):
            mensaje = mover()
        elif(opc == "4"):
            mensaje = renombrar()
        elif (opc == "5"):
            mensaje = encriptar()
        elif (opc == "6"):
           mensaje =  desencriptar()
        elif (opc == "7"):
            mensaje = introducirtexto()
        elif (opc == "8"):
            mensaje = printar()
        elif(opc == "0"):
            break
        else:
            mensaje = "Carácter no válido"
        
        os.system("cls") #limpiamos consola

main() #llamada al esqueleto.
print("Gracias por usar el servicio! HASTA PRONTO!")
