import sqlite3
from sqlite3.dbapi2 import Cursor

class connectionBD():
    def openDB(self):
        connection = sqlite3.connect('books_DB')
        return connection
    
    def crearBD(self):
        connection = self.openDB()
        try:
            connection.execute("""create table books_DB(
                            codigo integer primary key AUTOINCREMENT,
                            title text,
                            author text,
                            edicion text,
                            lugar text,
                            editorial text,
                            traduccion text,
                            paginas integer,
                            estado text,
                            afiliado text,
                            telefono text,
                            email text,
                            fecha_inicio text,
                            fecha_fin text
                            )""")
            print('Se creo la tabla books_DB')
        except sqlite3.OperationalError:
            print('La tabla books_DB ya fue creada')
    
    def toAddBook(self, data):
        connection = self.openDB()
        cursor = connection.cursor()
        sql = 'insert into books_DB (title, author, edicion, lugar, editorial, traduccion, paginas, estado) values (?,?,?,?,?,?,?,?)'
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
                      
    def toListBooks(self):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = ' select * from books_DB'
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            connection.close()

    def toModifyBook(self, data):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'update books_DB set author=?, edicion=?, lugar=?, editorial=?, traduccion=?, paginas=?, estado=? where title =? '
            cursor.execute(sql, data)
            connection.commit()
            connection.close()
        except:
            connection.close()
    
    def toDeleteBook(self, data):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'delete from books_DB where title = ?'
            cursor.execute(sql, data)
            connection.commit()
            return cursor.rowcount
        finally:
            connection.close()
        
    def toCheckBooks(self, data):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'select author, edicion, lugar, editorial, traduccion, paginas, estado from books_DB where title = ?'
            cursor.execute(sql, data)
            return cursor.fetchall()
        finally:
            connection.close()
    
    def toGenerateLoan(self, data):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'update books_DB set estado=?, afiliado=?, telefono=?, email=?, fecha_inicio=?, fecha_fin=? where title=?'
            cursor.execute(sql, data)
            connection.commit()
            connection.close()
        except:
            connection.close()

    def toCheckAvailability(self, data):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'select estado, afiliado, fecha_fin from books_DB where title = ?'
            cursor.execute(sql, data)
            return cursor.fetchall()
        finally:
            connection.close()

    def toFinishLoan(self, data):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'update books_DB set afiliado=?, telefono=?, email=?, fecha_inicio=?, fecha_fin=?, estado=? where title =? '
            cursor.execute(sql, data)
            connection.commit()
            connection.close()
        except:
            connection.close()

    def toControlExistence(self, title):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'select estado, author, afiliado from books_DB where title = ?'
            cursor.execute(sql, title)
            return cursor.fetchall()
        finally:
            connection.close()
    
    def toControlState(self, data):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'select estado from books_DB where title = ?'
            cursor.execute(sql, data)
            return cursor.fetchall()
        finally:
            connection.close()
    
    def toControlDate(self):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'select title, estado, fecha_fin from books_DB'
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            connection.close()   

    def toUpdateState(self, data):
        try:
            connection = self.openDB()
            cursor = connection.cursor()
            sql = 'update books_DB set estado=? where title =? '
            cursor.execute(sql, data)
            connection.commit()
            connection.close()
        except:
            connection.close()