import pytest
def test_load_contact():
    with open('contact.db', 'r') as fh:
       for line in fh:
           fName, lName, company = line.split()
           
