from Product import Product
from Cage import Cage
import csv


# Global modukle vars
cages = []
products = []

def main():

    # initialize first cage
    cage= Cage()
    cages.append(cage)

    # initialize all products from CSV file and put them in a sorted list
    GetProductsFromCSV()

    # For each cage c
    for c in cages:

            # For each product
            for p in products:

                # #debug
                # print 'Total cage volume: ' + str(c.height*c.length*c.width)
                # print 'Total free volume: ' + str((c.height*c.length*c.width)-c.occupied_volume)
                # print 'Total product volume: ' + str(p.height*p.width*p.length)

                # If product not in a cage already
                if p.in_a_cage is False:
                    # If enough space in the cage to fit in this product
                    if ((c.height*c.length*c.width)-c.occupied_volume) >= (p.height*p.width*p.length):
                        c.InsertProduct(p)
                        p.in_a_cage = True
                    else:
                        cages.append(Cage())

    #Output
    print 'Number of cages used: ' + str(len(cages))
    print 'Cages utilised volumes (Utilised, Utilised%):'
    for c in cages:
        print '     ' + str(c.occupied_volume)+', ' +str(  (c.occupied_volume / (c.height*c.length*c.width))*100 ) + '%'



def GetProductsFromCSV():

    with open('cage_products.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row[0].isdigit():
                for x in range(0, int(row[4])):
                    p = Product( float(row[1])/1000,float(row[2])/1000,float(row[3])/1000)
                    products.append(p)


if __name__ == '__main__':
    main()
