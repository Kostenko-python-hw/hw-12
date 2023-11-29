from field import Field
from utils import sanitize_phone_number


class Phone(Field):
    def validate_and_transform(self, phone):
        int(sanitize_phone_number(phone))
        sunitized_phone = sanitize_phone_number(phone)
        if len(sunitized_phone) != 10:
            raise ValueError('The phone number must be 10 characters long.')
        else:
            return sunitized_phone
        
    def check_availability(self, value: str):
        return value in self.value