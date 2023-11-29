from field import Field


class Name(Field):
    def validate_and_transform(self, value):
         if value.isalpha():
            return value
         else:
            raise ValueError("The name must contain only letters.")
         
    def check_availability(self, value: str):
        return value in self.value.lower()