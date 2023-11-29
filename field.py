class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = self.validate_and_transform(value)

    def validate_and_transform(self, _):
        pass

    def __str__(self):
        return str(self.value)


