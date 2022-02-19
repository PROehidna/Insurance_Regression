from peewee import *

db = SqliteDatabase('insdb.db')


class Expenses(Model):
    id = PrimaryKeyField(unique=True)
    d1 = TextField()
    insurance = IntegerField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'expenses'
