from pymongo import MongoClient
from flask import Flask, send_file
import threading
import middlefunctions

client = None

app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(client)

@app.route('/logo')
def logo():
    return send_file("./Ngrok/logo.png")

@app.route('/put_user')
def put_user():

    threading.Thread(target=middlefunctions.put_user(client)).start()


    return "Completed"




def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = (
        "mongodb+srv://wymotiv:motivteam1234@cluster0.krumakm.mongodb.net/"
    )

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["Motiv"]


# This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#     # Get the database
#     dbname = get_database()
#     collection_name = dbname["Posts"]

#     item_1 = {
#         "sport_type": "football",
#         "data": {
#             "Touchdowns": 10
#         }
#     }

#     item_2 = {
#         "sport_type": "golf",
#         "data": {
#             "Putts": 8
#         }
#     }

#     collection_name.insert_many([item_1, item_2])

if __name__ == '__main__':
    client = get_database()

    app.run(debug=True)
