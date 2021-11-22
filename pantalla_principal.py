import sqlite3
from tkinter import * 


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




#Crear una pantalla de reserva
def reservar_func():

	#Crear funcion para seleccionar una opcion del radio
	def select():
		text_selection = "Opcion", str(opciones_elegir.get())
		
		
	#Crear nueva pantalla
	root2 = Tk()


	#Configurar pantalla
	root2.title("Reservar")
	root2.geometry("500x350")
	root2.resizable(False, False)
	root2.configure(bg="#D0D6D7")


	#Escibir reserva
	reserva_label = Label(root2, text="¿Que desea reservar?"
	, font=("Arial Bold", 25), bg="#D0D6D7").pack()


	#Crear opciones para elegir que reservar
	opciones_elegir = IntVar()

	radio_basquet = Radiobutton(root2, text="Baloncesto", variable=opciones_elegir
	, value=1, command=select, font=("Arial Bold", 14), bg="#D0D6D7").pack()

	radio_futbol = Radiobutton(root2, text="Futbol", variable=opciones_elegir
	, value=2, command=select, font=("Arial Bold", 14), bg="#D0D6D7").pack()

	radio_skate = Radiobutton(root2, text="Skate", variable=opciones_elegir
	, value=3, command=select, font=("Arial Bold", 14), bg="#D0D6D7").pack()

	radio_kart = Radiobutton(root2, text="Karts", variable=opciones_elegir
	, value=4, command=select, font=("Arial Bold", 14), bg="#D0D6D7").pack()

	label = Label(root2, bg="#D0D6D7").pack()


	root2.mainloop()



# Crear pantalla para el registro
def sign_in():
	root3 = Tk()

	# Funcion para recoger los datos de registro
	def sign_in_submit():
		pers_name_get=pers_name_var.get()
		
		#pers_surname_get=pers_surname_var.get()
		
		#pers_id_get=pers_id_var.get()
		
		#pers_age_get=pers_age_var.get()
		
		#pers_email_get=pers_email_var.get()
		
		#pers_password_get=pers_password_var.get()
		



		#entities = (pers_id_get, pers_name_get, pers_surname_get, pers_age_get, pers_email_get, pers_password_get)
		#cursor.execute("""INSERT INTO datos (id, name, surname, age, email, password)
		#VALUES(?, ?, ?, ?, ?, ?)""", entities)
		#con.commit()

		#id_identificar = (pers_id_get, "", "", "")
		#cursor.execute("""INSERT INTO datos_tarj(id, number, cvc, expiry) VALUES(?, ?, ?, ?)""", id_identificar)
		#con.commit()

		#id_identificar_1 = (pers_id_get, "", "")
		#cursor.execute("""INSERT INTO datos_coche (id, registration, owner) VALUES(?, ?, ?)""", id_identificar_1)
		#con.commit()

		print(pers_name_get)
		#print("Apellido:", pers_surname_get)
		#print("Id:", pers_id_get)
		#print("Edad:", pers_age_get)
		#print("Email:", pers_email_get)
		#print("Contraseña:", pers_password_get)

		pers_name_var.set("")
		"""pers_surname_var.set("")
		pers_id_var.set("")
		pers_age_var.set("")
		pers_email_var.set("")
		pers_password_var.set("")
"""


	
	#Configurar la pantalla
	root3.title("Registrar")
	root3.geometry("500x350")
	root3.resizable(False, False)
	root3.configure(bg="#D0D6D7")


	# Poner todos los espacios para los datos
	pers_name_var = StringVar()
	Label(root3, text="Nombre").pack()
	pers_name = Entry(root3, font=("Arial Bold", 12), width=14
	, textvariable=pers_name_var).pack()
	"""
	pers_surname_var=StringVar()
	Label(root3, text="Apellido").pack()
	pers_surname = Entry(root3, font=("Arial Bold", 14)
	, textvariable=pers_surname_var).pack()
	
	pers_id_var=StringVar()
	Label(root3, text="Id").pack()
	pers_id = Entry(root3, font=("Arial Bold", 14), textvariable=pers_id_var).pack()
	
	pers_age_var=StringVar()
	Label(root3, text="Edad").pack()
	pers_age = Entry(root3, font=("Arial Bold", 14), textvariable=pers_age_var).pack()
	
	pers_email_var=StringVar()
	Label(root3, text="Email").pack()
	pers_email = Entry(root3, font=("Arial Bold", 14), textvariable=pers_email_var).pack()
	
	pers_password_var=StringVar()
	Label(root3, text="Contraseña").pack()
	pers_password = Entry(root3, font=("Arial Bold", 14), show="*",
	 textvariable=pers_password_var).pack()
	"""
	# Boton para registrarse
	sign_in_submit_button = Button(root3, text="Registrar", command=sign_in_submit 
	,font=("Arial Bold", 14)).pack()

	
	root3.mainloop()

	



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
reservar_button = Button(root1, text="Reserva Pista",command=reservar_func
, font=("Arial Bold", 12)).pack()


#Boton para registrarse
sign_in_button = Button(root1, text="Registrarse", command=sign_in
, font=("Arial Bold", 12)).pack()


#Boton para salir
salir_button = Button(root1, text="Salir", command=quit
, font=("Arial Bold", 12)).pack()


root1.mainloop()

