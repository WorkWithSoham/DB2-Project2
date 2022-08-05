import os
import sys
import csv
import pandas as pd

from commons.generic_constants import GenericConstants

class DBCreation():
    def __init__(self, connection):
        self.connection = connection

    def extract_files(self):
        for csv_file_name, csv_file_path in GenericConstants.INPUT_FILES_DIRS.items():
            with open(csv_file_path, "r") as csv_file:
                self.connection.tables.append(csv_file_name)
                csv_file_data = csv.DictReader(csv_file)

                new_table = self.connection.DB[csv_file_name]

                new_table.insert_many(csv_file_data)

    
            


                


    

