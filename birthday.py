from field import Field
from utils import to_timestamp, timestamp_to_date


class Birthday(Field):
    def validate_and_transform(self, birthday):
        if birthday:
            timestamp = to_timestamp(birthday)
            if timestamp:
                return timestamp
            else:
                raise ValueError('Please enter the correct date.')
        else:
            return ''

    # Searching by date of birth is very superficial.    
    def check_availability(self, value: str):
        date = timestamp_to_date(self.value)
        month =  date.strftime('%B')
        splitted_date = str(date).split('-')
        if value in splitted_date or value == month.lower():
            return True