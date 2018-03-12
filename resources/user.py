import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = 'username field is required'
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = 'password field is required'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        # prevent creation of registering duplicate users
        if UserModel.find_by_username(data['username']): # literally 'if User.find_by_username(data['username'])' is NOT None'
            return {"message": "this user already exists!"}, 400 # return finishes method execution on this point

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['username'], data['password'],)) # function accepts two arguments, second is a list of arguments

        # connection.commit()
        # connection.close()

        user = UserModel(**data) #**data unpacks as this --> (data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully"}, 201
