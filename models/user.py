import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(50))

    def __init__(self, username, password):
    #def __init__(self, _id, username, password):
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,)) # (element,) makes sure result is a tuple
        # row = result.fetchone() # fetch the first row only
        # if row: # equivalent of 'if row is not None:'
        #     user = cls(*row) # equivalent of cls User(row[0], row[1], row[2])
        # else:
        #     user = None

        # connection.close()
        # return user
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,)) # (element,) makes sure result is a tuple
        # row = result.fetchone() # fetch the first row only
        # if row: # equivalent of 'if row is not None:'
        #     user = cls(*row) # equivalent of cls User(row[0], row[1], row[2])
        # else:
        #     user = None

        # connection.close()
        # return user
        return cls.query.filter_by(id=_id).first()
