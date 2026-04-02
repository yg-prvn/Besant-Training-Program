# OOPS - Object Oriented Programming System

class User:
    id = 1
    f_name = ""
    l_name = ""

a = User()
a.f_name = "Yuga"
a.l_name = "Praveen"

# print(a.id, a.f_name, a.l_name)

# Constructor
class User1:
    id = 1
    f_name = ""
    l_name = ""

    # For Private Variables, we'll use getter & setter methods in all programming
    # "__" double underscore means it is private variables, Only possible is access private variables via methods
    __email = ""

    def gerEMail(self):
        return self.__email
    
    def setEMail(self, email):
        self.__email = email

    def __init__(self, id, f_name, l_name, email):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.__email = email

    def __str__(self):
        return str(self.id) + " " + self.f_name + " " + self.l_name + " " + self.__email
    
    def getFName(self):
        return self.f_name
    
a = User1(1, "Yuga", "Praveen", "praveenkpm1103@gmail.com")
print(a.id, a.f_name, a.l_name, a.gerEMail()) # We'll use getter method instead calling an __email variable
print(a)
print(a.getFName())