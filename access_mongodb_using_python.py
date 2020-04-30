"""
Author : Nikita Malviya
Date : 05 March 2020

Centralised utility class for all operations to be performed on a mongo database.
"""
from pymongo import MongoClient

class MongoUtils:
    def __init__(self, address="127.0.0.1", port=27017, db_name="", collection_name="",user='',password=''):
        """
        Initialise collection object
        :param address: Database ip
        :param port: Mongo port
        :param db_name: Databse name
        :param collection_name: Collection name
        """
        self.address = address
        self.port = port
        self.db_name = db_name
        self.user = user
        self.password = password
        self.collection_name = collection_name
        self.collection = self.connect_to_db()

    def update_record(self, filter_condition=None, new_value=None):
        """
        Connect to mongo db and update data.
        :param filter_condition: Filter condition
        :param new_value: new value of the selected document
        :return: Return collection as a list
        """
        if filter_condition is None:
            filter_condition = {}
        if new_value is None:
            new_value = {}
        self.collection.update_one(filter_condition, {"$set": new_value})

    def insert_record(self, new_record=None):
        """
        Insert a record in table
        :param new_record: New record to be inserted.
        :return:
        """
        if new_record is None:
            new_record = {}
        self.collection.insert_one(new_record)

    def get_list_from_db(self, filter_condition=None):
        """
        Connect to mongo db and fetch data.
        :param filter_condition: Filter condition
        :return: Return collection as a list
        """
        if filter_condition is None:
            filter_condition = {}
        return list(self.collection.find(filter_condition))

    def connect_to_db(self):
        url = f'mongodb://{self.user}:{ self.password}@{self.address}:{self.port}/?authSource={self.db_name}&authMechanism=SCRAM-SHA-1'
        client = MongoClient(url)
        db = client[self.db_name]
        print(f'Collection {self.db_name} Database: {db.list_collection_names()}')
        collection = db[self.collection_name]
        return collection