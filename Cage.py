import Product

class Cage(object):
    def __init__(self):

        #dimensions
        self.height = 1.603
        self.width = 0.697
        self.length = 0.846

        #contains which products
        self.products_list = []

        self.occupied_volume = 0

    def InsertProduct(self, prod):
        self.products_list.append(prod)

        #Update self.occupied_volume
        self.occupied_volume = self.occupied_volume + (prod.height*prod.width*prod.length)