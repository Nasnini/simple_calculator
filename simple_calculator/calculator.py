class Calculations:
    def __init__(self):
        pass


    #Addition Function
    def add(self, *args):
        sum = 0
        for num in args:
            number = int(num)
            sum += number
        return sum



    #Multiplication Function
    def multiply(self, *args):
        product = 1
        for num in args:
            number = int(num)
            product *= number
        return product
