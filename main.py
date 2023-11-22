from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self._value = value
        
    @property   
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Value must be a string.")
        self._value = new_value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone
    
    @Field.value.setter
    def value(self, new_value):
        self._value = new_value
        self.validate_phone
        
    def validate_phone(self):
        if not self._value.isdigit() or len(self._value) != 10:
           raise ValueError("Phone number must be a 10-digit string.") 

class Birthday(Field):
    def __init__(self, value=None):
        if value is not None:
            try:
                datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Invalid date format")
        super().__init__(value)
    
    @Field.value.setter
    def value(self, new_value):
        if new_value is not None:
            try:
                datetime.strptime(new_value, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        self._value = new_value
        
class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        # Додавання телефону до списку
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        # Видалення телефону зі списку
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        if found_phone:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
            print(f"Phone {old_phone} edited successfully to {new_phone}.")
        else:
            raise ValueError(f"Phone {old_phone} not found. Cannot edit.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def days_to_birthday(self):
        if self.burthday.value:
            today = datetime.today(today.year, self.birthday.valu.month, self.birthday.value.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
            days_left = (next_birthday - today).days
            return days_left
        
    def __str__(self):
        # Перевизначення методу для зручного виведення
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

    
class AddressBook(UserDict):
    def __iter__(self, n=1):
        count = 0
        for key in self.data:
            yield self.data[key]
            count += 1
            if count == n:
                return
            
    def add_record(self, record):
        # Додавання запису до книги
        self.data[record.name.value] = record

    def find(self, name):
        # Пошук запису за іменем
        return self.data.get(name)

    def delete(self, name):
        # Видалення запису за іменем
        if name in self.data:
            del self.data[name]

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

