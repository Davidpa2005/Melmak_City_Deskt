import sqlite3
from tkinter import * 

#import sign_in_func
#import reservar_func

#Crear pantalla inicio
root1 = Tk()

# Crear la conexion con la base de datos
con = sqlite3.connect("datos.db")
cursor = con.cursor()

# Crear variable para saber si esta registrado
is_reg = False

# Funcion de inciar sesion
def submit():
 
    id=id_var.get()
    password=passw_var.get()
    

    #Verificar el inicio de sesion
    cursor.execute("SELECT id FROM datos;")
    ids = cursor.fetchall()

    # Verificar si esta registrado un id
    for checking_id in ids:
        is_reg = False
        if checking_id[0] == id:
            is_reg = True
            print("Su id esta registrado.")
            
            cursor.execute("SELECT password FROM datos WHERE id = ?;", (id,))
            password_taken = cursor.fetchall()
            password_taken_1 = password_taken[0]
            
            if password_taken_1[0] == password:
                print("Has Entrado")
            else:
                print("Contraseña Incorrecta")


    print("The name is : " + id)
    print("The password is : " + password)

    id_var.set("")
    passw_var.set("")


#Configurar la pantalla principal
root1.title("Melmak City")
root1.geometry("500x350")
root1.resizable(False, False)
root1.configure(bg="#D0D6D7")


#Variables para el inicio de sesion
id_var = StringVar()
passw_var = StringVar()


#Escribir Pagina de Inicio de Sesion
login_text = Label(root1, text="Login", font=("Arial Bold", 25), bg="#D0D6D7").pack()


#Datos de inicio de sesion
label_id = Label(root1, text="Introduce Id", font=("Arial Bold", 14), bg="#D0D6D7").pack()
enter_id = Entry(root1, font=("Arial Bold", 12)
, width=12, textvariable=id_var).pack()

label_password = Label(root1, text="Introduce Contraseña"
, font=("Arial Bold", 14), bg="#D0D6D7").pack()
enter_password = Entry(root1, font=("Arial Bold", 12)
, width=14, show="*", textvariable=passw_var).pack()

#Boton para iniciar sesion
coger_datos = Button(root1, text="Iniciar Sesion", command=submit).pack()


#Boton para reservar
#reservar_button = Button(root1, text="Reserva Pista",command=reservar_func
#, font=("Arial Bold", 12)).pack()


#Boton para registrarse
#sign_in_button = Button(root1, text="Registrarse", command=sign_in_func
#, font=("Arial Bold", 12)).pack()


#Boton para salir
salir_button = Button(root1, text="Salir", command=quit
, font=("Arial Bold", 12)).pack()


root1.mainloop()

