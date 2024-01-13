from abc import ABC, abstractmethod
from typing import Dict, Any

class NewsIndicatorBase(ABC):

    @abstractmethod
    def get_news(self, **kwargs)->Dict[str,Any]:
        pass

    @abstractmethod
    def filter_data(self, data:Dict[str, Any])->list:
        pass

    @abstractmethod
    def clean_data(self, data:Dict[str, Any]):
        pass

    @abstractmethod
    def calculate_sentiment(self)->int:
        pass

    @abstractmethod
    def get_sentiment_for_news(self, data:Dict[str, Any]):
        pass