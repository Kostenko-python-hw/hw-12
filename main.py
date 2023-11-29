from collections import UserDict
import pickle
from record import Record

class AddressBook(UserDict):

    def __init__(self):
        self.__current_index = None
        self.__quantity_per_iter = None
        self.current_index = 0
        self.quantity_per_iter = 3
        super().__init__(self)

    @property
    def quantity_per_iter(self):
        return self.__quantity_per_iter

    @quantity_per_iter.setter
    def quantity_per_iter(self, value):
        self.__quantity_per_iter = value

    @property
    def current_index(self):
        return self.__current_index

    @current_index.setter
    def current_index(self, value):
        self.__current_index = value
    
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError(f"Record with name '{record.name.value}' already exists.")
        
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def search(self, value):
        result = set()
        for el in self.data.values():
            record = el.find_in_record(value.lower().strip())
            if record:
                result.add(str(record))
        
        return '\n'.join([str(record) for record in result]) if len(result) > 0 else 'No results found for the query.'
    
    def save_to_file(self, file_path):
        with open(file_path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def restore_from_file(cls, file_path):
        with open(file_path, "rb") as file:
            return pickle.load(file)
        
    def __next__(self):
        if self.__current_index <= len(self.data) - 1:
            list_data = list(self.data.values())
            data = list_data[self.current_index: self.current_index + self.quantity_per_iter]
            self.current_index += self.quantity_per_iter
            return '\n'.join([str(record) for record in data])
        raise StopIteration

    def __iter__(self):
        return self



# book = AddressBook()

# john_record = Record("John")
# john_record.add_phone("1114567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday('16.11.1987')
# book.add_record(john_record)

# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# jane_record.add_phone("1237652931")
# jane_record.add_birthday('10.11.1000')
# book.add_record(jane_record)

# bob_record = Record("Bob")
# bob_record.add_phone("0000000000")
# bob_record.add_phone("9999992002")
# bob_record.add_birthday('01.05.2012')
# book.add_record(bob_record)

# mark_record = Record("Mark")
# mark_record.add_phone("1111111111")
# mark_record.add_birthday('21.03.2002')
# book.add_record(mark_record)

# print('*****book*****')
# print(book.search('november'))

# book.save_to_file('file33')

# restored_book = AddressBook.restore_from_file('file33')
# print('*****restored_book*****')
# print(restored_book.search('november'))
