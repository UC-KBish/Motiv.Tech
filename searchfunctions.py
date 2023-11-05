from pymongo import MongoClient
import math

def query(collection, query = {}):
    result = collection.find(query)
    for document in result:
        print(document)

def query_similar(collection, query={}):

    search_query = {
        "$or": [
            {"Description": {"$regex": query.get("Description", ""), "$options": "i"}},
            {"Sport": {"$regex": query.get("Sport", ""), "$options": "i"}}
        ]
    }

    result = collection.find(search_query, {"score": {"$meta": "textScore"}})
    result = result.sort([("score", {"$meta": "textScore"})])

    for doc in result:
        print(f"Document: {doc['_id']}, Score: {doc['score']}")



def query_mlt(collection, query_id):
    post = collection.find_one({"_id": query_id})
    if post:
        description = post.get("description", "")
        sport = post.get("sport", "")
        query_text = f"{description}, {sport}"
    else:
        query_text = ""


    # Define the fields to consider for MLT search
    fields_to_search = ["Description", "Sport"]

    # Build a custom MLT query using the cosine similarity
    mlt_query = {
        "$or": [
            {field: {"$regex": query_text, "$options": "i"}}
            for field in fields_to_search
        ]
    }

    # Find similar documents in the collection
    results = collection.find(mlt_query)

    # You can iterate through the results
    for document in results:
        print(f"Document: {document['_id']}")




def calculate_cosine_similarity(vector1, vector2):
    # Calculate the dot product of the two vectors
    dot_product = sum(x * y for x, y in zip(vector1, vector2))

    # Calculate the magnitude (Euclidean norm) of each vector
    magnitude1 = math.sqrt(sum(x ** 2 for x in vector1))
    magnitude2 = math.sqrt(sum(y ** 2 for y in vector2))

    # Calculate the cosine similarity
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)

def query_mlt2(collection, query_id):
    post = collection.find_one({"_id": query_id})
    if post:
        description = post.get("description", "")
        sport = post.get("sport", "")
        query_text = f"{description}, {sport}"
    else:
        query_text = ""

    # Define the fields to consider for MLT search
    fields_to_search = ["Description", "Sport"]

    # Calculate the TF-IDF vectors for the query
    query_vector = [query_text.count(word) for word in query_text.split()]

    # Find similar documents in the collection and calculate the similarity scores
    results = collection.find()

    for document in results:
        document_text = " ".join([document.get(field, "") for field in fields_to_search])
        document_vector = [document_text.count(word) for word in query_text.split()]

        # Calculate the cosine similarity
        similarity_score = calculate_cosine_similarity(query_vector, document_vector)
        print(f"Document: {document['_id']}, Similarity Score: {similarity_score}")


