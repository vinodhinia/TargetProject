from flask import Flask
#from flask_mongokit import MongoKit
from mongokit import Connection

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

db = Connection(MONGODB_HOST, MONGODB_PORT)

