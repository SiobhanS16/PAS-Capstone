# from sys import getprofile
# from tokenize import String
# from typing import KeysView
# from xmlrpc.client import Boolean
# from flask_wtf import FlaskForm
# from setuptools import SetuptoolsDeprecationWarning
# from app import app
# from flask import flash
from flask_login import UserMixin
from mongoengine import IntField, FileField, EmailField, StringField, ReferenceField, DateTimeField, CASCADE
from flask_mongoengine import Document
import datetime as dt
# import jwt
# from time import time
# from bson.objectid import ObjectId


class User(UserMixin, Document):
    createdate = DateTimeField(defaultdefault=dt.datetime.utcnow)
    gid = StringField(sparse=True, unique=True)
    gname = StringField()
    gprofile_pic = StringField()
    username = StringField()
    fname = StringField()
    lname = StringField()
    email = EmailField()
    image = FileField()
    prononuns = StringField()

    meta = {
        'ordering': ['lname','fname']
    }
    
class Blog(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    subject = StringField()
    content = StringField()
    tag = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Comment(Document):
    # Line 63 is a way to access all the information in Course and Teacher w/o storing it in this class
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    blog = ReferenceField('Blog',reverse_delete_rule=CASCADE)
    # This could be used to allow comments on comments
    comment = ReferenceField('Comment',reverse_delete_rule=CASCADE)
    # Line 68 is where you store all the info you need but won't find in the Course and Teacher Object
    content = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Survey(Document):
    fluentlang = StringField()
    homelang = StringField()
    classlang = StringField()
    parentlang = StringField()
    familiarity = IntField()
    beauty = IntField()
    melody = IntField()
    softness = IntField()
    orderliness = IntField()
    sweetness = IntField()
    age = IntField()
    gender = StringField()
    ethnicity = StringField()
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 