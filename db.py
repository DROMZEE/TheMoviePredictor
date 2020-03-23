from pymongo import MongoClient


class DB:
    def __init__(self, database_name):
        self.client = MongoClient('localhost', 27017)
        self.database_name = database_name

    def reset(self):
        self.client.drop_database(self.database_name)

    def bulk_insert(self, collection, object_list):
        object_dict = [vars(x) for x in object_list]
        self.client[self.database_name][collection].insert_many(
            object_dict)
