from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        # Валідація формату номера телефону
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit string.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

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


    def __str__(self):
        # Перевизначення методу для зручного виведення
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
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

