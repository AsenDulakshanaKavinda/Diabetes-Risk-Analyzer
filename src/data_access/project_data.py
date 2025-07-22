import sys
import pandas as pd
import numpy as np
from typing import Optional
from src.logger import logging

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import ProjectException

class ProjectData:
    """
    a class to export MongoDB records as pandas DataFrame
    """

    def __init__(self) -> None:
        """
        initializes the MongoDb client connection
        """

        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise ProjectException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Exports and entire MongoDB collection a pandas DataFrame.
        Parameters:
        collection_name: str - the name of the MongoDB collection to export
        database_name: Optional[str] - name of the database (optional). defaults to DATABASE_NAME

        Returns:
        pd.DataFrame - DataFrame containing the collection data, with '_id' column removed and 'na' values replaced with NaN.
        """

        try:
            # access specified collection from the default or specified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            # convert collection data to DataFrame and preprocess
            logging.info("Fetching data from MongoDB")
            df = pd.DataFrame(list(collection.find()))
            logging.info(f"data fetched with len: {len(df)}")

            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"], axis=1)
            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            raise ProjectException(e, sys)



















