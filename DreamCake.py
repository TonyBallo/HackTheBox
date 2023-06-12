#!/usr/bin/env python3

class DreamCake:
    # Measurements are defined in grams or units
    eggs = 4
    sugar = 300
    milk = 200
    butter = 50
    flour = 250
    baking_soda = 20
    vanilla = 10

    topping = None
    garnish = None


    is_baked = False

    def __init__(self, topping='No topping', garnish='No garnish'):
        self.topping = topping
        self.garnish = garnish

    def bake(self):
        self.is_baked = True

    def is_cake_ready(self):
        return self.is_baked

    def __str__(self):
        return f'''
              eggs amount : {self.eggs}
              sugar amount : {self.sugar}
              milk amount : {self.milk}
              butter amount : {self.butter}
              flour amount : {self.flour}
              baking soda amount : {self.baking_soda}
              vanilla amount : {self.vanilla}

              topping : {self.topping}
              garnish : {self.garnish}
              '''

class Foo():

    def __enter__(self):
        print("Enter...")

    def __exit__(self, type, value, traceback):
        print("...and exit.")





chocolate_cake = DreamCake(topping='Chocolate frosting')

chocolate_cake.bake() # Calls the function to "bake" on the object
is_cake_done = chocolate_cake.is_cake_ready()

print(is_cake_done) # Prints "True" because we called "bake" earlie

print(str(chocolate_cake))

with Foo():
    print("Hello world!")


