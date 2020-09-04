# Starting out with my initial class 
import random

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000,10000000)):
        self.name = str(name)
        self.weight = int(weight)
        self.price = int(price)
        self.flammability = float(flammability)
        self.identifier = int(identifier)

    def stealability(self):
        # Takes the price divided by the weight and 
        # returns a message if it's stealable or not

        stealable = float(self.price / self.weight)
        
        if stealable <= 0.5:
            return ('{} is not so stealable'.format(self.name))
        
        elif (stealable > 0.5) & (stealable < 1):
            return ('{} is sorta stealable'.format(self.name))
        
        else:
            return('{} is easily stealable'.format(self.name))

    def explode(self):
        # Grabs the falmmablilty times the weight then returns
        # how large the explosion would be

        boom = self.flammability * self.weight

        if boom <= 10:
            return ('fizzle')
        
        elif (boom > 10) & (boom < 50):
            return('...boom')
        
        else:
            return('BABOOM!!!!!!!!')

# My second class, boxing gloves for the side business
class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000,10000000)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return("......It's a glove......")

    def punch(self):
        # takes the weight to see how hard it would punch
        if self.weight < 5:
            return('That tickles')
        
        elif (self.weight > 5) & (self.weight <= 15):
            return('That hurt...')
        
        else:
            return('OUCH!!!!')