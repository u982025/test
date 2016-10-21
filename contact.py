from phone_number import PhoneNumber
class Contact:
    def __init__ (self, f_name, l_name, company):
        self.first_name = f_name
        self.last_name = l_name
        self.company = company
        self.phone_number = PhoneNumber()

    def add_phone_number(self, number, type):
        self.phone_number.number = number
        self.phone_number.type = type
   
if __name__ == '__main__':
    John = Contact('John', 'Doe', 'FB')
    print John.first_name
