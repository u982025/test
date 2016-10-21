import pytest
from address_book import AddressBook


@pytest.fixture
def phonebook():
    address_book = AddressBook()
    address_book.add_from_file()
    return address_book 

def test_address_loaded(phonebook):
    assert len(phonebook.contacts) > 1

def test_first_name(phonebook):
    assert len(phonebook.contacts[0].first_name) > 2

def test_last_name(phonebook):
    assert len(phonebook.contacts[0].last_name) > 2

def test_company(phonebook):
    assert len(phonebook.contacts[0].company) > 20

if __name__ == '__main__':
    print address_book.contacts[0].first_name
