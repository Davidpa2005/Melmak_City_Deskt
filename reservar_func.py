import sqlite3
from tkinter import *


# Crear la conexion con la base de datos
con = sqlite3.connect("datos.db")
cursor = con.cursor()


def reservar_func():
	
	#Crear nueva pantalla
	root2 = Tk()

	#Crear funcion para seleccionar una opcion del radio
	def select():
		text_selection = "Opcion", str(opciones_elegir.get())
		
		
	


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

reservar_func()