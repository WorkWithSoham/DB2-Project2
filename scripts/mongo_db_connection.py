from pymongo import MongoClient

from commons.generic_constants import GenericConstants


class MongoDBConnection:
    def __init__(self):
        self.connection = MongoClient(GenericConstants.BASE_URL)
        self.db = self.connection['DB2']
        if self.db.list_collection_names():
            self.drop_collections()

    def drop_collections(self):
        for col in self.db.list_collection_names():
            self.db[col].drop()

    def create_collection(self, collection_name):
        collection = self.db[collection_name]
        return collection

    def collection_insert_one(self, collection, record):
        pass

    def collection_insert_many(self, collection, record_list):
        collection.insert_many(record_list)


