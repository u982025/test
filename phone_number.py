
class PhoneNumber:
    def __init__(self, number, type):
        self.number = number
        self.typ = type        


if __name__ == '__main__':
    phone1 = PhoneNumber('4089456404', 'home')
    print phone1.number 
