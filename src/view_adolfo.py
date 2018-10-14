#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

''' Esta es la primera version de la vista, se tiene una base de datos de prueba como
un diccionario, simplemente para probar la funcionalidad de la ventana. 
En la siguiente versión la vista accede a los datos de acuerdo 
al patrón MVC'''
dummy_db = [("26/03/1974", "Rnning",  40,"Muy divertido"),
                 ("16/02/1997", "Kick Boxing", 70,"Muy cansado!" )]

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Fitness App")
        self.set_border_width(10)
        #self.set_default_size(400,400) #A considerar después
        #self.set_resizable(False) #A considerar después

        self.grid = Gtk.Grid(margin=20, column_spacing=10, row_spacing=10)
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        ''' Consideramos por el momento los datos de la columna Fecha como un string, en la versión posterior se
        modifica esto para que acepte datos tipo Date, de igual forma es necesario establecer el tipo de dato 
        para la columna Tiempo.
        	Las posiblidades son las siguientes: 
        		Entero: Se mide en minutos
        		Flotante: Se mide en Horas
        		String: Se escribe la cantidad con letra
        	A considerar en la versión posterior'''
        self.liststore = Gtk.ListStore(str, str, int,str)
        for element in dummy_db:
            self.liststore.append(list(element))

        '''Se establecen las columnas de acuerdo al wireframe, queda pendiente la traducción de las cadenas 
        en el task7'''
        self.treeview = Gtk.TreeView(self.liststore)
        for i, column_title in enumerate(["Date", "Type", "Time","Comment"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        self.add = Gtk.Button(label="_Add", use_underline=True)
        self.remove = Gtk.Button(label="_Remove", use_underline=True)
        self.modify = Gtk.Button(label="_Modify", use_underline=True)
        ''' De igual forma, la traducción de los labels de los botones queda pendiente para el task7'''
        
        self.scrolled_treelist = Gtk.ScrolledWindow(expand=True)
        self.scrolled_treelist.set_size_request(200,500)
        #self.scrolled_treelist.set_vexpand(True)
        self.scrolled_treelist.add(self.treeview)
        
        boxButtons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10, margin=10)
        boxButtons.pack_start(self.add, False, False, 0)
        boxButtons.pack_start(self.modify, False, False, 0)
        boxButtons.pack_start(self.remove, False, False, 0)


        self.grid.add(self.scrolled_treelist)
        self.grid.attach(boxButtons,0,2,3,1)
        
        self.show_all()
    ''' Por el momento, la función que se activa al pulsar un botón no hace nada, en la siguiente versión de la vista
    éste método accede al controlador. '''
    def on_button_clicked(self,widget):
    	print("Button clicked!")
    def _connect(self,controller):
        self.connect("destroy",Gtk.main_quit)
        self.add.connect("clicked",controller.onAddButtonClicked)
        self.remove.connect("clicked",controller.onModifyButtonClicked)
        self.modify.connect("clicked",controller.onRemoveButtonClicked)    