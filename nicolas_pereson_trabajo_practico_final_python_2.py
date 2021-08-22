from tkinter import * 
from tkinter import ttk
from tkinter import messagebox as mb
from typing import Set
import Conexion_BD
import datetime as dt
import os


class AppBiblioteca:
    #Create main root
    def __init__(self):
        self.root = Tk()
        self.root.geometry('480x400')
        self.root.config(background='red') #No Funciona
        self.root.title('BIBLIOTECA'.center(110))
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(column=0, row=0, padx= 5, pady=5)
        self.notebook.pack(expand='yes', fill= 'both')
        self.connection = Conexion_BD.connectionBD()
        self.connection.crearBD()
        self.frameAdd()
        self.frameSearch()
        self.frameTreeview()
        self.frameLoan()
        self.dateControl()
        self.listBooks()
        self.root.mainloop()

    #Create Frame to add books
    def frameAdd(self):
        self.frame_add = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_add, text = 'Alta')
        self.labelFrame_add = ttk.LabelFrame(self.frame_add, text= 'Alta de Libro')
        self.labelFrame_add.pack(padx=4, pady=4, expand='yes')
        self.label_title_add = ttk.Label(self.labelFrame_add, text='Título').grid(column=0, row=0, padx=5,pady=8)
        self.title_add = StringVar()
        self.entry_title_add = Entry(self.labelFrame_add, textvariable=self.title_add, width=30).grid(column=1, row=0, padx=5, pady=8)
        self.label_author_add = ttk.Label(self.labelFrame_add, text='Autor').grid(column=0, row=1, padx=5,pady=8)
        self.author_add = StringVar()
        self.entry_author_add = Entry(self.labelFrame_add, textvariable=self.author_add, width=30).grid(column=1, row=1, padx=5, pady=8) 
        self.label_edition_add = ttk.Label(self.labelFrame_add, text='Edición').grid(column=0, row=2, padx=5,pady=8)
        self.edition_add = StringVar()
        self.entry_edition_add = Entry(self.labelFrame_add, textvariable=self.edition_add, width=30).grid(column=1, row=2, padx=5, pady=8)
        self.label_print_place_add = ttk.Label(self.labelFrame_add, text='Lugar de Impresión').grid(column=0, row=3, padx=5,pady=8)
        self.print_place_add = StringVar()
        self.entry_print_place_add = Entry(self.labelFrame_add, textvariable=self.print_place_add, width=30).grid(column=1, row=3, padx=5, pady=8)
        self.label_editorial_add = ttk.Label(self.labelFrame_add, text='Editorial').grid(column=0, row=4, padx=5,pady=8)
        self.editorial_add = StringVar()
        self.entry_editorial_add = Entry(self.labelFrame_add, textvariable=self.editorial_add, width=30).grid(column=1, row=4, padx=5, pady=8)
        self.label_translate_add = ttk.Label(self.labelFrame_add, text='¿Está traducido?').grid(column=0, row=5, padx=5,pady=8)
        self.translate_add = StringVar()
        self.translate_options_search = ['Si', 'No']
        self.translate_add_cb = ttk.Combobox(self.labelFrame_add, width= 5, values=self.translate_options_search, textvariable=self.translate_add).grid(column=1, row=5, padx=5, pady=8)
        self.label_page_qty_add = ttk.Label(self.labelFrame_add, text='Cantidad de páginas').grid(column=0, row=6, padx=5,pady=8)
        self.page_qty_add = StringVar()
        self.entry_page_qty_add = Entry(self.labelFrame_add, textvariable=self.page_qty_add, width=30).grid(column=1, row=6, padx=5, pady=8)
        self.button_add = Button(self.labelFrame_add, width=10, text= 'Agregar', font=('Arial',11,'bold'), bg='orange', bd=5, command=self.addBooks)
        self.button_add.grid(column=1, row=9, padx=5,pady=8)

    #Create Frame to search, modify and delete books from database
    def frameSearch(self):
        self.frame_search = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_search, text = 'Consulta de Libros')
        self.labelFrame_search = ttk.LabelFrame(self.frame_search, text= 'Consulta, Modificación y Baja de Libros')
        self.labelFrame_search.pack(padx=4, pady=4, expand='yes')
        self.label_title_search = ttk.Label(self.labelFrame_search, text='Título').grid(column=0, row=0, padx=5,pady=8)
        self.title_search = StringVar()
        self.entry_title_search = Entry(self.labelFrame_search, width=30, textvariable=self.title_search).grid(column=1, row=0, padx=5, pady=8)
        self.label_author_search = ttk.Label(self.labelFrame_search, text='author').grid(column=0, row=1, padx=5,pady=8)
        self.author = StringVar()
        self.entry_author_search = Entry(self.labelFrame_search, width=30, textvariable=self.author).grid(column=1, row=1, padx=5, pady=8) 
        self.label_edition_search = ttk.Label(self.labelFrame_search, text='Edición').grid(column=0, row=2, padx=5,pady=8)
        self.edition_search = StringVar()
        self.entry_edition_search = Entry(self.labelFrame_search, width=30, textvariable=self.edition_search).grid(column=1, row=2, padx=5, pady=8)
        self.label_print_place_search = ttk.Label(self.labelFrame_search, text='Lugar de Impresión').grid(column=0, row=3, padx=5,pady=8)
        self.print_place_search = StringVar()
        self.entry_print_place_search = Entry(self.labelFrame_search, width=30, textvariable=self.print_place_search).grid(column=1, row=3, padx=5, pady=8)
        self.label_editorial_search = ttk.Label(self.labelFrame_search, text='Editorial').grid(column=0, row=4, padx=5,pady=8)
        self.editorial_search = StringVar()
        self.entry_editorial_search = Entry(self.labelFrame_search, width=30, textvariable=self.editorial_search).grid(column=1, row=4, padx=5, pady=8)
        self.label_translate_search = ttk.Label(self.labelFrame_search, text='¿Está traducido?').grid(column=0, row=5, padx=5,pady=8)
        self.translate_options_search = ['Si', 'No']
        self.translate_search_cb = ttk.Combobox(self.labelFrame_search, width= 5, values=self.translate_options_search)
        self.translate_search_cb.grid(column=1, row=5, padx=5, pady=8)
        self.label_page_qty_search = ttk.Label(self.labelFrame_search, text='Cantidad de páginas').grid(column=0, row=6, padx=5,pady=8)
        self.page_qty_search = StringVar()
        self.entry_page_qty_search = Entry(self.labelFrame_search, width=30, textvariable=self.page_qty_search).grid(column=1, row=6, padx=5, pady=8)
        self.state_options_search = ['Disponible', 'Prestado', 'En restauración', 'Con retraso']
        self.label_state_search = ttk.Label(self.labelFrame_search, text='Estado Actual').grid(column=0, row=7, padx=5,pady=8)
        self.book_state_search = ttk.Combobox(self.labelFrame_search, width=27, values=self.state_options_search)
        self.book_state_search.grid(column=1, row=7, padx=5, pady=8)
        self.button_search = Button(self.labelFrame_search, width=15, text= 'Buscar', font=('Arial',9,'bold'), bg='orange', bd=5, command= self.searchBooks)
        self.button_search.grid(column=2, row=0, padx=3,pady=3)
        self.labelFrame_search_action = ttk.LabelFrame(self.frame_search, text= 'Acciones')
        self.labelFrame_search_action.pack(padx=4, pady=4, expand='yes')
        self.button_modify_data = Button(self.labelFrame_search_action, width=15, text= 'Actualizar data', font=('Arial',9,'bold'), bg='orange', bd=5, command= self.modifyBooks)
        self.button_modify_data.grid(column=0, row=0, padx=2,pady=2)
        self.button_delete = Button(self.labelFrame_search_action, width=15, text= 'Borrar', font=('Arial',9,'bold'), bg='orange', bd=5, command=self.deleteBooks)
        self.button_delete.grid(column=2, row=0, padx=2,pady=2)

    #Create Frae to list books from database
    def frameTreeview(self):
        self.frame_treeview = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_treeview, text = 'Listado de Libros')
        self.labelFrame_treeview = ttk.LabelFrame(self.frame_treeview, text = '')
        self.labelFrame_treeview.pack(expand= 'yes', fill= 'both')
        self.treeview = ttk.Treeview(self.labelFrame_treeview)
        self.treeview.pack(padx=4, pady=4, fill='both', expand='yes')
        self.treeview['columns'] = ('id', 'title', 'author', 'cantPag', 'estado') #Defino columnas
        self.treeview.column('#0', stretch=NO, width=0)
        self.treeview.column('id', anchor=CENTER, width=0)
        self.treeview.column('title', anchor=CENTER, width=120)
        self.treeview.column('author', anchor=CENTER, width=100)
        self.treeview.column('cantPag', anchor=CENTER, width=70)
        self.treeview.column('estado', anchor=CENTER, width=80)
        # Define headings
        self.treeview.heading('id', text = 'ID')
        self.treeview.heading('title', text = 'Título', anchor=CENTER)
        self.treeview.heading('author', text = 'Autor', anchor=CENTER)
        self.treeview.heading('cantPag', text = 'Páginas', anchor=CENTER)
        self.treeview.heading('estado', text = 'Estado', anchor=CENTER)
        #Update changes
        self.labelFrame_treeview_action = ttk.LabelFrame(self.frame_treeview, text='Acciones')
        self.labelFrame_treeview_action.pack(padx=4, pady=4, expand='yes', fill='both')
        self.button_update_treeview = Button(self.labelFrame_treeview_action, width=15, font=('Arial',9,'bold'), bg='orange', bd=5,text='Actualizar Cambios', command=self.listBooks)
        self.button_update_treeview.pack(padx=4, pady=4)

    #Create Frame to loans
    def frameLoan(self):
        self.frame_loan = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_loan, text = 'Gestión de Prestamos')
        self.labelFrame_loan = ttk.LabelFrame(self.frame_loan, text = 'Préstamos')
        self.labelFrame_loan.pack(expand='yes', fill = 'both')
        self.title_loan = StringVar()
        self.label_title_loan = ttk.Label(self.labelFrame_loan, text = 'Libro a consultar'). grid(column=0, row=0, padx=4, pady=4)
        self.entry_title_loan = Entry(self.labelFrame_loan, width=30, textvariable=self.title_loan).grid(column=1, row=0)
        self.current_state_loan = StringVar()
        self.label_state_loan = ttk.Label(self.labelFrame_loan, text = 'Estado: ').grid(column=0, row=1, padx=2, pady=2)
        self.entry_state_loan = Entry(self.labelFrame_loan, width=30, textvariable=self.current_state_loan, state='readonly', bg='green', background='yellow').grid(column=1, row=1, padx=2, pady=2)
        self.loan_to_loan = StringVar()
        self.label_loan_to_loan = ttk.Label(self.labelFrame_loan, text = 'Prestado a: ').grid(column=0, row=2, padx=4, pady=4)
        self.entry_loan_to_loan = Entry(self.labelFrame_loan, width=30, textvariable=self.loan_to_loan, state='readonly').grid(column=1, row=2, padx=2, pady=2)
        self.return_date_loan = StringVar()
        self.label_return_date_loan = ttk.Label(self.labelFrame_loan, text = 'Fecha devolución: ').grid(column=0, row=3, padx=4, pady=4)
        self.entry_return_date_loan = Entry(self.labelFrame_loan, width=30, textvariable=self.return_date_loan, state='readonly').grid(column=1, row=3, padx=2, pady=2)
        self.button_check_availability_loan = Button(self.labelFrame_loan, width=20, text= 'Consultar disponibilidad', font=('Arial',9,'bold'), bg='orange', bd=5, command=self.checkAvailability)
        self.button_check_availability_loan.grid(column=2, row=0, padx=2,pady=2)
        self.button_finish_loan = Button(self.labelFrame_loan, width=20, text= 'Finalizar Préstamo', font=('Arial',9,'bold'), bg='orange', bd=5, command=self.finishLoan)
        self.button_finish_loan.grid(column=2, row=1, padx=2,pady=2)
        #Labelframe generate loans
        self.labelFrame_gen_loan = ttk.LabelFrame(self.frame_loan, text = 'Nuevo Préstamo')
        self.labelFrame_gen_loan.pack(expand='yes', fill = 'both')
        self.title_gen_loan = StringVar()
        self.label_title_gen_loan = ttk.Label(self.labelFrame_gen_loan, text = 'Libro a prestar'). grid(column=0, row=0, padx=4, pady=4)
        self.entry_title_gen_loan = Entry(self.labelFrame_gen_loan, width=30, textvariable=self.title_gen_loan).grid(column=1, row=0, padx=4, pady=4)
        self.affiliate_gen_loan = StringVar()
        self.label_affiliate_gen_loan = ttk.Label(self.labelFrame_gen_loan, text = 'Nombre Afiliado: '). grid(column=0, row=1, padx=4, pady=4)
        self.entry_affiliate_gen_loan = Entry(self.labelFrame_gen_loan, width=30, textvariable=self.affiliate_gen_loan).grid(column=1, row=1, padx=4, pady=4)
        self.phone_gen_loan = StringVar()
        self.label_phone_gen_loan = ttk.Label(self.labelFrame_gen_loan, text = 'Teléfono: '). grid(column=0, row=2, padx=4, pady=4)
        self.entry_phone_gen_loan = Entry(self.labelFrame_gen_loan, width=30, textvariable=self.phone_gen_loan).grid(column=1, row=2, padx=4, pady=4)
        self.email_gen_loan = StringVar()
        self.label_email_gen_loan = ttk.Label(self.labelFrame_gen_loan, text = 'E-mail: '). grid(column=0, row=3, padx=4, pady=4)
        self.entry_email_gen_loan = Entry(self.labelFrame_gen_loan, width=30, textvariable=self.email_gen_loan).grid(column=1, row=3, padx=4, pady=4)
        self.start_date_gen_loan = StringVar()
        self.label_start_date_gen_loan = ttk.Label(self.labelFrame_gen_loan, text = 'Fecha inicio'). grid(column=0, row=4, padx=4, pady=4)
        self.entry_start_date_gen_loan = Entry(self.labelFrame_gen_loan, width=10, textvariable=self.start_date_gen_loan).grid(column=1, row=4, padx=4, pady=4)
        self.label_start_date_gen_loan2 = ttk.Label(self.labelFrame_gen_loan, text = 'yyyy-mm-dd', foreground='grey'). grid(column=2, row=4, padx=4, pady=4)
        self.return_date_gen_loan = StringVar()
        self.label_return_date_gen_loan = ttk.Label(self.labelFrame_gen_loan, text = 'Fecha devolución'). grid(column=0, row=5, padx=4, pady=4)
        self.label_return_date_gen_loan2 = ttk.Label(self.labelFrame_gen_loan, text = 'yyyy-mm-dd', foreground='grey'). grid(column=2, row=5, padx=4, pady=4)
        self.entry_return_date_gen_loan = Entry(self.labelFrame_gen_loan, width=10, textvariable=self.return_date_gen_loan).grid(column=1, row=5, padx=4, pady=4)
        self.state_gen_loan = StringVar()
        self.button_generate_loan = Button(self.labelFrame_gen_loan, width=20, text= 'Generar Préstamo', font=('Arial',9,'bold'), bg='orange', bd=5, command=self.generateLoan)
        self.button_generate_loan.grid(column=2 ,row=0, padx=2,pady=2)

    #######      FUNCTIONS       ###########
    #Function to list books in treeview
    def listBooks(self):
        for record in self.treeview.get_children():
            self.treeview.delete(record)
        data = self.connection.toListBooks()
        count=0
        #Insert data 
        for dato in data:
            if count % 2 == 0:
                self.treeview.insert(parent='', index='end', iid=count, text='', values=(dato[0], dato[1], dato[2], dato[7], dato[8]), tags= ('evenrow', ))
            else:
                self.treeview.insert(parent='', index='end', iid=count, text='', values=(dato[0], dato[1], dato[2], dato[7], dato[8]), tags= ('oddrow', ))
            count +=1

    #Button Buscar libro
    def searchBooks(self):
        data = (self.title_search.get(), )
        answer = self.connection.toCheckBooks(data)
        if len(answer) > 0:
            self.author.set(answer[0][0])
            self.edition_search.set(answer[0][1])
            self.print_place_search.set(answer[0][2])
            self.editorial_search.set(answer[0][3])
            self.translate_search_cb.set(answer[0][4])
            self.page_qty_search.set(answer[0][5])
            self.book_state_search.set(answer[0][6])
        else:
            self.author.set('')
            self.edition_search.set('')
            self.print_place_search.set('')
            self.editorial_search.set('')
            self.translate_search_cb.set('')
            self.page_qty_search.set('')
            self.book_state_search.set('')
            mb.showinfo('Informacion','No existe un libro con ese título')

    #Button Agregar libro
    def addBooks(self):
        if self.title_add.get() == '':
            mb.showinfo('Información', 'El libro debe contener un Título')
        else:
            data = (self.title_add.get(), self.author_add.get(), self.edition_add.get(), self.print_place_add.get(), self.editorial_add.get(), self.translate_add.get(), self.page_qty_add.get(), 'Disponible')
            self.connection.toAddBook(data)
            self.title_add.set('')
            self.author_add.set('')
            self.edition_add.set('')
            self.print_place_add.set('')
            self.editorial_add.set('')
            self.translate_add.set('')
            self.page_qty_add.set('')
            mb.showinfo('Información', 'El libro ha sido cargado a la Base de data')

    #Button Actualizar
    def modifyBooks(self):
        title = (self.title_search.get(), )
        control = self.connection.toControlExistence(title)
        if len(control) > 0:
            data = (self.author.get(), self.edition_search.get(), self.print_place_search.get(), self.editorial_search.get(), self.translate_search_cb.get(), self.page_qty_search.get(), self.book_state_search.get(), self.title_search.get())
            self.connection.toModifyBook(data)
            self.title_search.set('')
            self.author.set('')
            self.edition_search.set('')
            self.print_place_search.set('')
            self.editorial_search.set('')
            self.translate_search_cb.set('')
            self.page_qty_search.set('')
            self.book_state_search.set('')
            mb.showinfo('Información', 'Los data del libro han sido modificados')
        else:
            mb.showinfo('Información', 'No existe un libro con ese título')

    #Button Borrar libro
    def deleteBooks(self):
        data = (self.title_search.get(), )
        answer = self.connection.toDeleteBook(data)
        if answer > 0:
            self.title_search.set('')
            self.author.set('')
            self.edition_search.set('')
            self.print_place_search.set('')
            self.editorial_search.set('')
            self.translate_search_cb.set('')
            self.page_qty_search.set('')
            mb.showinfo('Información', 'El libro ha sido eliminado de la Base de data')
        else:
            mb.showinfo('Información', 'No existe un libro con ese título')

    #Button Generar Préstamo
    def generateLoan(self):
        title = (self.title_gen_loan.get(),)
        control = self.connection.toControlExistence(title)
        if len(control) > 0:
            control_estado = self.connection.toControlState(title)
            if control_estado[0][0] == 'Disponible':   
                self.state_gen_loan.set('Prestado')
                data = (self.state_gen_loan.get(), self.affiliate_gen_loan.get(), self.phone_gen_loan.get(), self.email_gen_loan.get(), self.start_date_gen_loan.get(), self.return_date_gen_loan.get(), self.title_gen_loan.get())
                self.connection.toGenerateLoan(data)
                mb.showinfo('Información', 'El préstamo ha sido registrado correctamente')
                self.state_gen_loan.set('')
                self.affiliate_gen_loan.set('')
                self.phone_gen_loan.set('')
                self.email_gen_loan.set('')
                self.start_date_gen_loan.set('')
                self.return_date_gen_loan.set('')
                self.title_gen_loan.set('')
            else:
                mb.showinfo('Información', 'El libro NO está Disponible para su préstamo')
        else:
            mb.showinfo('Información', 'No existe un libro con ese título')
    
    #Button Consultar Disponibilidad
    def checkAvailability(self):
        data = (self.title_loan.get(), )
        answer = self.connection.toCheckAvailability(data)
        if len(answer) > 0:
            self.current_state_loan.set(answer[0][0])
            if answer[0][1] == None:
                self.loan_to_loan.set('') 
            #
            else:
                self.loan_to_loan.set(answer[0][1]) 
            if answer[0][2] == None:
                self.return_date_loan.set('')
            else:
                self.return_date_loan.set(answer[0][2])
        else:
            self.current_state_loan.set('')
            self.loan_to_loan.set('') 
            self.return_date_loan.set('')
            mb.showinfo('Información', 'No existe un libro con ese título')
            
    #Button Finalizar Préstamo
    def finishLoan(self):
        title = (self.title_loan.get(),)
        data = ('', '', '', '', '', 'Disponible', self.title_loan.get())
        control = self.connection.toControlExistence(title)
        if len(control) > 0:
            self.connection.toFinishLoan(data)
            mb.showinfo('Información', '¡El libro se encuentra Disponible nuevamente!')
            self.checkAvailability()
        else:
            mb.showinfo('Información', 'No existe un libro con ese título')

    def dateControl(self):
        data = self.connection.toControlDate()
        today_date = dt.datetime.today()
        format = "%Y-%m-%d"
        for i in data:
            titulo = i[0]
            try:    
                return_date = dt.datetime.strptime(str(i[2]), format)
            except ValueError:
                pass
            if return_date < today_date:
                    tuple = ('Con retraso', titulo)
                    self.connection.toUpdateState(tuple)




os.system('cls')
App = AppBiblioteca()
