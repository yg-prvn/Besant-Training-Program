class Category:
    __type = "Mobile"
    _isAvailable = "Yes"

    # def __init__(self, type, isAvailable):
    #     self.type = type
    #     self.isAvailable = isAvailable

class ProductInfo(Category):
    name = ""

    # def __init__(self, type, isAvailable, name):
    #     super().__init__(type, isAvailable)
    #     self.name = name

    def showValue(self):
        print(self._isAvailable)
        # print(self.__type) # Causes Error

obj = ProductInfo()
obj.showValue()