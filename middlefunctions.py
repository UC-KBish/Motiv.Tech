from pymongo import MongoClient
import json
import base64

def put_user(dbname):

    collection_name = dbname["Posts"]

    with open('./User.json') as templateFile:
        template = json.loads(templateFile.read())

    collection_name.insert_one(template)

def put_video1(dbname):
    collection_name = dbname["Video"]

    with open('./Video.json') as templateFile:
        template = json.loads(templateFile.read())

    with open('./Tokalytics/Tiktok videos/Tiktok videos/baseball/1.mp4', 'rb') as templateFile:
        fileData = templateFile.read()

    template.update({
        "File_Name": "1.mp4",
        "Data": base64.b64encode(fileData).decode('utf-8')
    })

    collection_name.insert_one(template)

def put_video(dbname, request):
    collection_name = dbname["Video"]

    file = request.files['Video']

    with open('./Video.json') as templateFile:
        template = json.loads(templateFile.read())

    template.update({
        "File_Name": "1.mp4",
        "Data": base64.b64encode(file.read()).decode('utf-8')
    })

    collection_name.insert_one(template)

    return "Completed"

def put_post(dbname, request):
    collection_name = dbname["Post"]

    file = request.files['Video']
    description = request.form.get('Description')
    sport = request.form.get('Sport')
    duration = request.form.get('Duration')


    with open('./Posts.json') as templateFile:
        template = json.loads(templateFile.read())

    template.update({
        "Description": description,
        "Sport": sport,
        "Duration": duration,
        "Data": base64.b64encode(file.read()).decode('utf-8')
    })

    print(collection_name.insert_one(template))

    return "Completed"