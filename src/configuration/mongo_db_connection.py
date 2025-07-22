import os
import sys
import pymongo
import certifi

from src.exception import ProjectException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# load the certificate authority file to avoid timeout errors when connecting to mongodb
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to the nongoDB database.
    Attribures:
    client : MongoClient - a shared MongoClient instance for the class
    database : Database - the specific database instance that MongoDBClient connects to

    Methods:
    __init__(database_name: str) -> None - Initializes the MongoDB connection using the given database name.
    """

    client = None # shared MongoClient instance across all MongoDBClinet instance

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one
        
        Parameters:
        database_name: str - optional name of the MongoDb databse to connect to, default is set by DATABASE_NAME constant

        Raise:
        ProjectException: if there is an issue connecting to MongoDb or if the environment variable for MongoDb URL is not set
        """

        try:
            # Check if a MongoDB client connection has already been established; if not, create a new one
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY) # Retrieve MongoDB URL from environment variables
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")
                # establish a new MongoDB clinet connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            # use the shared MongoClient for this instance
            self.client = MongoDBClient.client
            self.database = self.client[database_name] # Connect to the specified database
            self.database_name = database_name
            logging.info("MongoDB connection successful.")
        except Exception as e:
            # raise a custom exception with traceback details if connection fails
            raise ProjectException(e, sys)

