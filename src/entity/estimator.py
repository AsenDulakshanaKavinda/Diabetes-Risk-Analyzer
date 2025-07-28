
import sys

import pandas as pd
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from src.exception import ProjectException
from src.logger import logging

class TargetValueMapping:
    def __init__(self):
        self.yes:int = 0
        self.no:int = 1

    def _asdict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_responese = self._asdict()
        return dict(zip(mapping_responese.values(), mapping_responese.keys()))
        
class ProjectModel:
    def __init__(self, preprocessing_object: Pipeline, trained_model_object: object):
        """
        :param preprocessing_object: Input Object of preprocesser
        :param trained_model_object: Input Object of trained model 
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object
        
    def predict(self, dataframe: pd.DataFrame) -> DataFrame:
        """
        Function accepts preprocessed inputs (with all custom transformations already applied),
        applies scaling using preprocessing_object, and performs prediction on transformed features.
        """
        try:
            logging.info("stating prediction process")
            # 1. apply scaling transformation using the pre-trained preprocessing object
            transformed_feature = self.preprocessing_object.transform(dataframe)

            # 2. perform prediction using the trained model
            logging.info("using the trained model to get predictions")
            predictions = self.trained_model_object.predict(transformed_feature)
            
            return predictions
        except Exception as e:
            logging.error("Error occurred in predict method", exc_info=True)
            raise ProjectModel(e, sys) from e
    
    def __repr__(self):
        return f'{type(self.trained_model_object).__name__}()'
    
    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"














