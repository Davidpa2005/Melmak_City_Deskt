import sqlite3
from tkinter import * 


# Crear la conexion con la base de datos
con = sqlite3.connect("datos.db")
cursor = con.cursor()


# Crear pantalla para el registro
def sign_in():

	#Crear nueva pantalla
	root3 = Tk()

	# Funcion para recoger los datos de registro
	def sign_in_submit():

		#Coger datos introducidos
		pers_name_get=pers_name_var.get()
		pers_surname_get=pers_surname_var.get()
		pers_id_get=pers_id_var.get()
		pers_age_get=pers_age_var.get()
		pers_email_get=pers_email_var.get()
		pers_password_get=pers_password_var.get()
		

		entities = (pers_id_get, pers_name_get, pers_surname_get, pers_age_get, pers_email_get, pers_password_get)
		cursor.execute("""INSERT INTO datos (id, name, surname, age, email, password)
		VALUES(?, ?, ?, ?, ?, ?)""", entities)
		con.commit()

		id_identificar = (pers_id_get, "", "", "")
		cursor.execute("""INSERT INTO datos_tarj(id, number, cvc, expiry) VALUES(?, ?, ?, ?)""", id_identificar)
		con.commit()

		id_identificar_1 = (pers_id_get, "", "")
		cursor.execute("""INSERT INTO datos_coche (id, registration, owner) VALUES(?, ?, ?)""", id_identificar_1)
		con.commit()

		print("Nombre:", pers_name_get)
		print("Apellido:", pers_surname_get)
		print("Id:", pers_id_get)
		print("Edad:", pers_age_get)
		print("Email:", pers_email_get)
		print("Contraseña:", pers_password_get)

		pers_name_var.set("")
		pers_surname_var.set("")
		pers_id_var.set("")
		pers_age_var.set("")
		pers_email_var.set("")
		pers_password_var.set("")


	
	#Configurar la pantalla
	root3.title("Registrar")
	root3.geometry("500x350")
	root3.resizable(False, False)
	root3.configure(bg="#D0D6D7")


	# Poner todos los espacios para los datos
	pers_name_var = StringVar()
	Label(root3, text="Nombre").pack()
	pers_name = Entry(root3, font=("Arial Bold", 14)
	, textvariable=pers_name_var).pack()
	
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
	
	# Boton para registrarse
	sign_in_submit_button = Button(root3, text="Registrar", command=sign_in_submit 
	,font=("Arial Bold", 14)).pack()

	
	root3.mainloop()

	
sign_in()
