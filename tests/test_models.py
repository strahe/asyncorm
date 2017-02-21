from model import Model
from fields import (CharField, DateField, IntegerField, ForeignKey,
    ManyToMany, PkField
)


class Publisher(Model):
    name = CharField(max_length=50)


class Book(Model):
    table_name = 'library'
    name = CharField(max_length=50)
    content = CharField(max_length=255, field_name='hhuhuhuh', )
    date_created = DateField(auto_now=True)
    author = ForeignKey(foreign_key='Author', null=True)


class WrongBook(Model):
    table_name = 'library'
    name = CharField(max_length=50)
    content = CharField(max_length=255, field_name='hhuhuhuh', )
    hhuhuhuh = CharField(max_length=25, )
    date_created = DateField(auto_now=True)
    author = ForeignKey(foreign_key='Author', null=True)


class Author(Model):
    na = PkField(field_name='uid')
    name = CharField(max_length=50)
    age = IntegerField()
    publisher = ManyToMany(foreign_key='publisher')