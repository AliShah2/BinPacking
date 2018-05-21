class Product(object):

    def __init__(self, h, w, l):

        # set dimensions
        self.height = h
        self.width = w
        self.length = l

        # placed in a cage?
        self.in_a_cage = False