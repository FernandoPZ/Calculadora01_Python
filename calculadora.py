# Proyecto de practica (Calculadora basica)
# Hecho por Fernando Pérez S.

from tkinter import Button, Tk, Frame,Entry,END #Importacion de la libreria

ventana = Tk() 							#Definicion de la ventana
ventana.geometry('275x345')				#Definicion del tamaño de la ventana ("ancho"X"alto")
ventana.config(bg="grey")				#Definicion del color de fondo de la ventana
ventana.iconbitmap(bitmap='calc.ico')	#Definicion del icono
ventana.resizable(0,0)					#Definicion de cambio de tamaño de la ventana
ventana.title('Calculadora')			#Definicion del nombre de la ventana

#Efecto de los botones
class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self, master=master, **kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

i=0
def obtener(dato):
	global i
	i+=1
	Resultado.insert(i, dato)

def operacion():
	global i
	ecuacion = Resultado.get()
	if i !=0:
		try:
			result = str(eval(ecuacion))
			Resultado.delete(0,END)
			Resultado.insert(0,result)
			longitud = len(result)
			i = longitud
		except:
			result = '3RR0R'
			Resultado.delete(0,END)
			Resultado.insert(0,result)
	else:
		pass

def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last=None)
		i-=1

def borrar_todo():
	Resultado.delete(0, END)

#Ventana general
frame = Frame(ventana, bg='grey',
					   relief="raised")
frame.grid(column=0,
		   row=0,
		   padx=6,
		   pady=3)

#Display
Resultado = Entry(frame,bg='#D0FFFF',		#Color
						width=21,			#Tamaño
						relief='groove',	#Estilo
						font='Consolas 16',	#Fuente
						justif='right')		#Alineacion
Resultado.grid(columnspan=4,	#Area
			   row=0,			#Fila
			   pady=3,
			   padx=1,
			   ipadx=1,
			   ipady=1)

#Fila 1
#Boton [C]
BotonC = HoverButton(frame, text="C",						#Simbolo
							command=lambda: borrar_uno(),	#Valor
							height=2,						#Alto
							width=13,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="red",			#Color secundario
							bg='#BB0000',					#Color principal
							anchor="center")				#Orientacion
BotonC.grid(column=2,		#Columna
			columnspan=2,	#Area
			row=1,			#Fila
			pady=2,			#Tamaño en vertical
			padx=2)			#Tamaño en horizontal
#Boton [CA]
BotonCA = HoverButton(frame, text="CA",						#Simbolo
							 command=lambda: borrar_todo(),	#Valor
							 height=2,						#Alto
							 width=13,						#Ancho
							 borderwidth=2,					#Borde
							 font=('Consolas',13,'bold'),	#Fuente
							 relief="raised",				#Estilo
							 activebackground="red",		#Color secundario
							 bg='#BB0000',					#Color principal
							 anchor="center")				#Orientacion
BotonCA.grid(column=0,		#Columna
			 columnspan=2,	#Area
			 row=1,			#Fila
			 pady=2,		#Borde vertical
			 padx=2)		#Borde horizontal

#Fila 2
#Boton [7]
Boton7 = HoverButton(frame, text="7",						#Simbolo
							command=lambda: obtener(7),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center")				#Orientacion
Boton7.grid(column=0,	#Columna
			row=2,		#Fila
			pady=2,		#Borde vertical
			padx=3)		#Borde horizontal
#Boton [8]
Boton8 = HoverButton(frame, text="8",						#Simbolo
							command=lambda: obtener(8),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center")				#Orientacion
Boton8.grid(column=1,	#Columna
			row=2,		#Fila
			pady=1,		#Borde vertical
			padx=3)		#Borde horizontal
#Boton [9]
Boton9 = HoverButton(frame, text="9",						#Simbolo
							command=lambda: obtener(9),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center")				#Orientacion
Boton9.grid(column=2,	#Columna
			row=2,		#Fila
			pady=1,		#Borde vertical
			padx=1)		#Borde horizontal
#Boton [÷]
BotonDividir = HoverButton(frame, text="÷",						#Simbolo
								  command=lambda: obtener('/'),	#Valor
								  height=2,						#Alto
								  width=5,						#Ancho
								  borderwidth=2,				#Borde
								  font=('Consolas',13,'bold'),	#Fuente
								  relief="raised",				#Estilo
								  activebackground="#6CCCFF",	#Color secundario
								  bg='#00AAD3',					#Color principal
								  anchor="center")				#Orientacion
BotonDividir.grid(column=3,	#Columna
				  row=2,	#Fila
				  pady=1,	#Borde vertical
				  padx=3)	#Borde horizontal

#fila 3
#Boton[4]
Boton4 = HoverButton(frame, text="4",						#Simbolo
							command=lambda: obtener(4),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center")				#Orientacion
Boton4.grid(column=0,	#Columna
			row=3,		#Fila
			pady=1,		#Borde vertical
			padx=1)		#Borde horizontal
#Boton[5]
Boton5 = HoverButton(frame, text="5",						#Simbolo
							command=lambda: obtener(5),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center")				#Orientacion
Boton5.grid(column=1,	#Columna
			row=3,		#Fila
			pady=1,		#Borde vertical
			padx=1)		#Borde horizontal
#Boton[6]
Boton6 = HoverButton(frame, text="6",						#Simbolo
							command=lambda: obtener(6),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center",)				#Orientacion
Boton6.grid(column=2,	#Columna
			row=3,		#Fila
			pady=1,		#Borde vertical
			padx=1)		#Borde horizontal
#Boton[X]
BotonPor = HoverButton(frame, text="X",						#Simbolo
							  command=lambda: obtener('*'),	#Valor
							  height=2,						#Alto
							  width=5,						#Ancho
							  borderwidth=2,				#Borde
							  font=('Consolas',13,'bold'),	#Fuente
							  relief="raised",				#Estilo
							  activebackground="#6CCCFF",	#Color secundario
							  bg='#00AAD3',					#Color principal
							  anchor="center")				#Orientacion
BotonPor.grid(column=3,	#Columna
			  row=3,	#Fila
			  pady=2,	#Borde vertical
			  padx=2)	#Borde horizontal

#Fila 4
#Boton[1]
Boton1 = HoverButton(frame, text="1",						#Simbolo
							command=lambda: obtener(1),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center")				#Orientacion
Boton1.grid(column=0,	#Columna
			row=4,		#Fila
			pady=1,		#Borde vertical
			padx=1)		#Borde horizontal
#Boton[2]
Boton2 = HoverButton(frame, text="2",						#Simbolo
							command=lambda: obtener(2),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center")				#Orientacion
Boton2.grid(column=1,	#Columna
			row=4,		#Fila
			pady=1,		#Borde vertical
			padx=1)		#Borde horizontal
#Boton[3]
Boton3 = HoverButton(frame, text="3",						#Simbolo
							command=lambda: obtener(3),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center",)				#Orientacion
Boton3.grid(column=2,	#Columna
			row=4,		#Fila
			pady=1,		#Borde vertical
			padx=1)		#Borde horizontal
#Boton[-]
BotonMenos = HoverButton(frame, text="-",						#Simbolo
								command=lambda: obtener('-'),	#Valor
								height=2,						#Alto
								width=5,						#Ancho
								borderwidth=2,					#Borde
								font=('Consolas',13,'bold'),	#Fuente
								relief="raised",				#Estilo
								activebackground="#6CCCFF",		#Color secundario
								bg='#00AAD3',					#Color principal
								anchor="center")				#Orientacion
BotonMenos.grid(column=3,	#Columna
				row=4,		#Fila
				pady=2,		#Borde vertical
				padx=2)		#Borde horizontal
#Fila 5
#Boton[.]
BotonPunto = HoverButton(frame, text=".",					#Simbolo
							command=lambda: obtener('.'),	#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center")				#Orientacion
BotonPunto.grid(column=0,	#Columna
				row=5,		#Fila
				pady=1,		#Borde vertical
				padx=1)		#Borde horizontal
#Boton[0]
Boton0 = HoverButton(frame, text="0",						#Simbolo
							command=lambda: obtener(0),		#Valor
							height=2,						#Alto
							width=5,						#Ancho
							borderwidth=2,					#Borde
							font=('Consolas',13,'bold'),	#Fuente
							relief="raised",				#Estilo
							activebackground="#999999",		#Color secundario
							bg='#777777',					#Color principal
							anchor="center",)				#Orientacion
Boton0.grid(column=1,	#Columna
			row=5,		#Fila
			pady=1,		#Borde vertical
			padx=1)		#Borde horizontal
#Boton[=]
BotonIgual = HoverButton(frame, text="=",						#Simbolo
								command=lambda: operacion(),	#Valor
								height=2,						#Alto
								width=5,						#Ancho
								borderwidth=2,					#Borde
								font=('Consolas',13,'bold'),	#Fuente
								relief="raised",				#Estilo
								activebackground="#0FC500",		#Color secundario
								bg='#0B9000',					#Color principal
								anchor="center")				#Orientacion
BotonIgual.grid(column=2,	#Columna
				row=5,		#Fila
				pady=1,		#Borde vertical
				padx=1)		#Borde horizontal
#Boton[+]
BotonMas = HoverButton(frame, text="+",						#Simbolo
							  command=lambda: obtener('+'),	#Valor
							  height=2,						#Alto
							  width=5,						#Ancho
							  borderwidth=2,				#Borde
							  font=('Consolas',13,'bold'),	#Fuente
							  relief="raised",				#Estilo
							  activebackground="#6CCCFF",	#Color secundario
							  bg='#00AAD3',					#Color principal
							  anchor="center")				#Orientacion
BotonMas.grid(column=3,	#Columna
			  row=5,	#Fila
			  pady=2,	#Borde vertical
			  padx=2)	#Borde horizontal

ventana.mainloop()

#Ultima modificacion 14-08-2023 [12:54]