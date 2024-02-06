import unittest

class Phonebook_test(unittest.TestCase):
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def get_number(self, name):
        return self.contacts.get(name, None)

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    class TestPhoneBook(unittest.TestCase):
        def setUp(self):
            self.phone_book = Phonebook()
            self.phone_book.add_contact("Ayo", "123456")
            self.phone_book.add_contact("Mide", "789012")

        def test_add_contact(self):
            self.phone_book.add_contact("Tolulope", "345678")
            self.assertEqual(self.phone_book.get_number("Tolulope"), "345678")

