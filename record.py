from name import Name
from birthday import Birthday
from phone import Phone
from utils import timestamp_to_date, get_current_date


class Record:
    def __init__(self, name, birthday = ''):
        self.__name = ''
        self.__birthday = ''
        self.__phones = []
        self.name = name
        self.birthday = birthday

    @property
    def name(self):
        return self.__name
    
    @property
    def birthday(self):
        return self.__birthday
    
    @property
    def phones(self):
        return self.__phones

    @name.setter
    def name(self, value):
        self.__name = Name(value)

    @birthday.setter
    def birthday(self, value):
        self.__birthday = Birthday(value)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, date): # This is not a mandatory function, but a duplicate birthday setter
        self.birthday = date

    def days_to_birthday(self):
        if self.birthday:
            birthday_date = timestamp_to_date((self.birthday.value))
            current_date = get_current_date()
            current_year = current_date.year
            next_birthday = birthday_date.replace(year=current_year)
            if next_birthday < current_date:
                next_birthday = birthday_date.replace(year=current_year + 1)
            return (next_birthday - current_date).days
        else:
            return None

    def remove_phone(self, phone):
        filtred_array = list(filter(lambda el: el.value != phone, self.phones))
        if len(filtred_array) != len(self.phones):
            self.phones = filtred_array
        else:
            raise ValueError()

    def edit_phone(self, old_phone, new_phone):
        _index = None
        for index, el in enumerate(self.phones):
            if el.value == old_phone:
                _index = index
                break
        if _index is None:
            raise ValueError('The phone you want to change was not found')
        else:
            _new_Phone = Phone(new_phone)
            self.phones[_index] = _new_Phone

    def find_phone(self, phone):
        for el in self.phones:
            if phone == el.value:
                return el
            
    def find_in_record(self, value):
        is_exist_in_name = self.name.check_availability(value)

        if is_exist_in_name:
            return self
        
        is_exist_in_phone = self.birthday.check_availability(value)

        if is_exist_in_phone: 
            return self
        
        for phone in self.phones:
            is_exist_in_phone = phone.check_availability(value)
            if is_exist_in_phone:
                return self
        
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}{f', birthday: {timestamp_to_date(self.birthday.value)}' if timestamp_to_date(self.birthday.value) else ''}"
