# OOPS - Object Oriented Programming System

class User:
    id = 1
    f_name = ""
    l_name = ""

a = User()
a.f_name = "Yuga"
a.l_name = "Praveen"

print(a.id, a.f_name, a.l_name)

# Constructor
class User1:
    id = 1
    f_name = ""
    l_name = ""

    def __init__(self, id, f_name, l_name):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self):
        return str(self.id) + " " + self.f_name + " " + self.l_name

a = User1(1, "Yuga", "Praveen")
print(a.id, a.f_name, a.l_name)
print(a)