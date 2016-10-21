
class PhoneNumber:
    def __init__(self):
        self.number = "" 
        self.type = ""       

    def edit_phone_number(self, number, type):
        self.number = number
        self.type = type

if __name__ == '__main__':
    phone1 = PhoneNumber('4089456404', 'home')
    print phone1.number 
