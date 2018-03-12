# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field is required'
    )

    parser.add_argument('store_id',
        type=int,
        required=True,
        help='Every item needs store_id'
    )



    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': "item not found"}, 404 # no need to use else as previous line (if successful) would terminate method


    def post(self, name):
        if ItemModel.find_by_name(name):
        #if next(filter(lambda x: x['name']==name, items), None) is not None:
            return {'message': "An item '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data) # data['price'], data['store_id']

        try:
            #item.insert()
            item.save_to_db()
        except:
            return {"message": "insert method went ballistic :-o"}, 500 #500 Internal Server Error

        return item.json(), 201


    def delete(self, name):
        #if ItemModel.find_by_name(name):
        #    connection = sqlite3.connect('data.db')
        #    cursor = connection.cursor()
        #    query = "DELETE FROM items WHERE name = ?"
        #    cursor.execute(query, (name,))
        #    connection.commit()
        #    connection.close()
        #    #global items
        #    #items = list(filter(lambda x: x['name'] != name, items)) # delete item by stroring filtered out list
        #    return {"message": "item deleted"}
        #return {"message": "item not found"}, 404
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "item deleted"}
        return {"message": "item not found"}, 404

    def put(self, name):
        data = Item.parser.parse_args()
        #item = next(filter(lambda x: x['name'] == name, items), None)
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name,data['price'])

        if item is None:
            item = ItemModel(name, **data) # data['price'], data['store_id']
            #item = {'name': name, 'price': data['price']}
            #items.append(item)
            #try:
            #    updated_item.insert()
            #except:
            #    return {"message": "An error occurred while inserting to DB"}, 500
        else:
            item.price = data['price']
            #try:
            #    updated_item.update()
            #except:
            #    return {"message": "An error occurred while updating DB"}, 500

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
                #    return {'items': items}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # rows = result.fetchall()
        # connection.commit()
        # connection.close()
        # if rows:
        #     items = []
        #     for row in rows:
        #         items.append({"name": row[0], "price": row[1]})
        #     return {"items": items}
        # return {"message": "no items in the database found"}, 404

        #return {'items': [x.json() for x in ItemModel.query.all()]}
        # alternatively
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
