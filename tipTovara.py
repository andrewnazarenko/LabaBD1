class tipTovara(object):
    def __init__(self,name,category,id):
        self.name = name
        self.category = category
        self.id = id

    def __str__(self):
        return self.name + " " + self.category + " " + self.id