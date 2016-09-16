class tovar(object):
    def __init__(self,name,price,date1):
        self.name = name
        self.price = price
        self.date1 = date1

    def __str__(self):
        return self.name + " " + self.price + " " + self.date1