class Link():
    """This class represent a Link from a website."""

    def __init__(self):
        self._tag = ""
        self._url = ""


    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, val = ""):
        if not type(val) is str:
            raise ValueError(f"The value type must be str. The type of the input value is: {type(val)}")
        else:
            self._tag = val
    

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, val = ""):
        if not type(val) is str:
            raise ValueError(f"The value type must be str. The type of the input value is: {type(val)}")
        else:
            self._url = val
    
