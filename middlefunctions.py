from pymongo import MongoClient
import json

def put_user(dbname):

    collection_name = dbname["Posts"]

    with open('./User.json') as templateFile:
        template = json.loads(templateFile.read())

    collection_name.insert_one(template)