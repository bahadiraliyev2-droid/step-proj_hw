class MaxSizeException(Exception):
    pass

class InvalidNameException(Exception):
    pass

class Inventory:
    def __init__(self, name, new_size, current_size):
        self.name = name 
        self.new_size = new_size 
        self.current_size = current_size

    def check_name (self, name):
        if name < 0:
          raise InvalidNameException("the name can not be equal or less than 0")
        if name > 100:
          raise InvalidNameException("name cannot be greater than 100")
    def update_size(self, current_size, new_size):
        if new_size < current_size:
         raise MaxSizeException("new size cannot be smaller than current one")

"examples for checking "
name = 50
current_size = 10
new_size = 20
try:
    print(name < 0)
except:
    print("error! 1#")

try:
    print(name > 100)
except:
    print("error 2#")

try:
    print(new_size < current_size)
except:
    print("error 3#")