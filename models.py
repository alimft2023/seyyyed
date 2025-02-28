from peewee import SqliteDatabase,TextField ,Model

db = SqliteDatabase('mft.db')

class Student(Model):
    name = TextField()
    family = TextField()
    
    class Meta:
        database = db 
        db_table ='Student'
        
Student.create_table()