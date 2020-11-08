#Creating an Animal class as the parent/root/base class
class Animal:

    # Initialising the Animal class
    def __init__(self):
        # Creating attributes
        self.alive=True
        self.spine=True
        self.lungs=True
        self.eyes=True

    # Create behaviours as functions
    def breathe(self):
        return "Keep breathing to stay alive"

    def move(self):
        return "Left to right, up and down"

    def eat(self):
        return "Nom, nom, nom"

    def procreate(self):
        return "Find a partner"

# # Instantiate our class i.e create an object
# cat=Animal()
# # Cat as a child of Animal, inherits behaviours and attributes.
# # Abstracted the eat method from out parent class
# print(cat.eat())
