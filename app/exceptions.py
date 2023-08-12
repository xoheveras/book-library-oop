"""

Classes of errors handled in this application

"""

class IsNoNumeric(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IsEmptyString(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IsTextSizeExceed(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)