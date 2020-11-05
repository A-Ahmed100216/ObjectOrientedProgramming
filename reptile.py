# Create a child class of the Animal class.

# We will need to first import the Animal class
# The syntax is basic from <file_name> import <class_name>
from animal import Animal

# This will be a child class so we pass the Parent class in the arguments. This immediately tells us that Reptile is a child class of Animal.
class Reptile(Animal):

    # First we initialise
    def __init__(self):
        # the super key word is used to inherit everything from the parent class.
        super().__init__()
        self.cold_blooded = bool
        self.tetrapod = True
        self.heart_chambers = [3,4]
        self.amniotic_eggs = False

    def seek_heat(self):
        return "Cold-blooded"

    def hunt(self):
        return "Hunter"

    def use_venom(self):
        return "Poisonous, be warned"

    def attract_mate_through_scent(self):
        return "Scent of Love"


# # Create an object - instantaite the Reptile class
# lizard=Reptile()
# print(lizard.eat() + " (This functionlity is inherited from the Parent class.)") # Inherits this from the Animal class
# print(lizard.cold_blooded)
#
# print(lizard.use_venom()) # Inherits this from the Reptile class.