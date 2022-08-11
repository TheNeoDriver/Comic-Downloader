from abc import ABC, abstractmethod

class Website(ABC):
    """Class that represents the comic websites"""

    def __init__(self):
        self._name = ""
        self._url = ""


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val = ""):
        if not type(val) is str:
            raise ValueError(f"The value type must be str.\
                The type of the input value is: {type(val)}")
        else:
            self._name = val
    

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, val = ""):
        if not type(val) is str:
            raise ValueError(f"The value type must be str.\
                The type of the input value is: {type(val)}")
        else:
            self._url = val
    
    
    @abstractmethod
    def get_comics_link():
        pass
    

    @abstractmethod
    def get_issues_link():
        pass
    

    @abstractmethod
    def get_images_link():
        pass
