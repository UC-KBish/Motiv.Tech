from pymongo import MongoClient
from flask import Flask, send_file, request, Response
import threading
import middlefunctions
import searchfunctions

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

@app.route('/put_video1')
def put_video1():

    threading.Thread(target=middlefunctions.put_video1(client)).start()

    return "Completed"

@app.route('/put_video', methods=['POST'])
def put_video():
    return middlefunctions.put_video(client, request)

@app.route('/put_post', methods=['POST'])
def put_post():
    return middlefunctions.put_post(client, request)

@app.route('/test_vid', methods=['GET'])
def test_vid():

    with open('./Tokalytics/Tiktok videos/Tiktok videos/baseball/2.mp4', 'rb') as video_file:
        video_bytes = video_file.read()

    return Response(video_bytes, mimetype='video/mp4')

    with open('./Tokalytics/Tiktok videos/Tiktok videos/baseball/2.mp4', 'rb') as videoFile:
        bytes_data = videoFile.read()

    from io import BytesIO
    file_obj = BytesIO(bytes_data)

    # Send the file with appropriate content type and download headers
    # response = Response(file_obj, content_type='video/mp4')
    # response.headers['Content-Disposition'] = 'attachment; filename=2.mp4'
    return file_obj


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

    collection_name = client["Post"]


    query_id = "6547204e2dabd976c6e05ceb"
    
    
    searchfunctions.query_mlt2(collection_name, query_id)

    

    # app.run() 
    app.run(ssl_context=('localhost.crt', 'localhost.key'), debug=True)


    