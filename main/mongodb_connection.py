import os
import sys
import collections

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.dbcreation import DBCreation
from commons.generic_constants import GenericConstants
from pymongo import MongoClient


class MongoDBConnection():
    def __init__(self, *args):
        self.connection = MongoClient(GenericConstants.BASE_URL)
        self.DB = self.connection["DB2"]
        self.tables = []
        
        if "DB2" in self.connection.list_database_names():
            self.connection.drop_database("DB2")

        print("Connected to ==>", self.connection)


if __name__ == "__main__":
    cmd_args = sys.argv
    connection_obj = MongoDBConnection(*cmd_args[1:])
    db_obj = DBCreation(connection_obj)
    db_obj.extract_files()


