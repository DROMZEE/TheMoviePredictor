from pymongo import MongoClient



# create a MongoDB client

client = MongoClient('localhost', 27017)
db = client.test_database

db = client['test-database']

# create a MongoDB client
client = MongoClient('localhost', 27017)

series_db = client['SeriesDB']
series_collection = series_db['series']


def insert_document(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id