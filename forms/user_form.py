import sys
sys.path.append('./datos')
from datos_user import *
from Tkinter import *

def which_selected():
	datos = all_persons()
	print "En %s de %d" % (select.curselection(), len(datos))
	return int(select.curselection()[0])

def add_persons():
	create_person(name = name_var.get(), age = age_var.get())
	set_select()

def update_persons():
	edad = int(age_var.get())
	ide = int(ide_var.get())
	update_person(id_persona = ide, name = name_var.get(), age = edad)
	set_select()

def delete_persons():
	ide = int(ide_var.get())
	delete_person(id_persona = ide)
	set_select()

def load_data():
	datos = all_persons()
	id, name, age = datos[which_selected()]
	ide_var.set(id)
	name_var.set(name)
	age_var.set(age)

def make_windows():
	global name_var, age_var, ide_var, select
	win = Tk()

	frame1 = Frame(win)
	frame1.pack()

	Label(frame1, text="Id").grid(row=1, column=0, sticky=W)
	ide_var= StringVar()

	Label(frame1, text="Nombre").grid(row=1, column=0, sticky=W)
	name_var= StringVar()
	name= Entry(frame1, textvariable=name_var)
	name.grid(row=1, column=1, sticky=W)

	Label(frame1, text="Edad").grid(row=2, column=0, sticky=W)
	age_var = StringVar()
	age = Entry(frame1, textvariable=age_var)
	age.grid(row=2, column=1, sticky=W)

	frame2 = Frame(win)       # Row of buttons
	frame2.pack()
	b1 = Button(frame2,text=" Add  ",command=add_persons)
	b2 = Button(frame2,text="Update",command=update_persons)
	b3 = Button(frame2,text="Delete",command=delete_persons)
	b4 = Button(frame2,text=" Load ",command=load_data)
	b1.pack(side=LEFT); b2.pack(side=LEFT)
	b3.pack(side=LEFT); b4.pack(side=LEFT)

	frame3 = Frame(win)       # select of names
	frame3.pack()
	scroll = Scrollbar(frame3, orient=VERTICAL)
	select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
	scroll.config (command=select.yview)
	scroll.pack(side=RIGHT, fill=Y)
	select.pack(side=LEFT,  fill=BOTH, expand=1)
	return win

def set_select():
	datos = all_persons()
	select.delete(0, END)
	for p in datos:
		select.insert(END, p.name)
