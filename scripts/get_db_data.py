import json
import os
import sys

import pymongo
from bson import json_util

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.mongo_db_connection import MongoDBConnection


class GetDBData:
    def __init__(self, query_option_list):
        if len(query_option_list) == 1:
            self.mongo_db_obj = MongoDBConnection(query_option_list[0])
        else:
            self.mongo_db_obj = MongoDBConnection()

    def get_db_data(self):
        query = {}
        query_1_statement, query_1 = self.get_artist_data()
        query[query_1_statement] = query_1
        query_2_statement, query_2 = self.get_artwork_data()
        query[query_2_statement] = query_2
        query_3_statement, query_3 = self.get_artwork_data_filter_price()
        query[query_3_statement] = query_3
        self.write_query_outputs(query)

    def get_artist_data(self):
        query_1_statement = "Get Data of all Artist"
        artist_collection = self.mongo_db_obj.db['Artist']
        data = list(artist_collection.find({}).sort("aID", pymongo.ASCENDING))
        return query_1_statement, data

    def get_artwork_data(self):
        query_2_statement = "Get Data of all Artwork"
        artwork_collection = self.mongo_db_obj.db['Artwork']
        data = list(artwork_collection.find({}))
        return query_2_statement, data

    def get_artwork_data_filter_price(self):
        query_3_statement = "Get all artists details whose artworks price is greater than equal to 20000"
        artist_collection = self.mongo_db_obj.db['Artist']
        data = list(artist_collection.aggregate([
            {"$match":
                {
                    'artwork.price': {
                        '$gte': 20000
                    }
                }
            }
        ]))
        return query_3_statement, data

    @staticmethod
    def write_query_outputs(query):
        i = 1
        for query_statement, query_data in query.items():
            with open(f'output_files/query_{i}', 'w') as f:
                out = f'Query {i}: {query_statement}\n\n\n'
                for data in query_data:
                    out = f'{out}\n{str(json.dumps(json.loads(json_util.dumps(data)), indent=4))}'
                f.write(out)
            i += 1


if __name__ == '__main__':
    cmd_args = sys.argv
    GetDBData(cmd_args[1:]).get_db_data()
