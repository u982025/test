
class Contact:
    def __init__ (self, f_name, l_name, company):
        self.first_name = f_name
        self.last_name = l_name
        self.company = company


if __name__ == '__main__':
    John = Contact('John', 'Doe', 'FB')
    print John.first_name
