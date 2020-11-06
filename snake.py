# Creating a Snake class. This is a child class of the Reptile class.
# Once again, we must import the parent class
from reptile import Reptile
class Snake(Reptile):

    # Let's initialise the class
    def __init__(self):
        super().__init__()
        self.cold_blooded=True
        self.forked_tongue=True
        self.venom = bool
        self.limbs = False

    # Creating functions for our user Snake class
    def use_tongue_to_smell(self):
        return "I use tongue to taste"

# snakeee= Snake()
# print(snakeee.eat()) # This is inherited from Animal (grandparent XD)
# print(snakeee.amniotic_eggs) # This is inherited from Reptile
# print(snakeee.cold_blooded) # This is inherited from reptile, but defined in Snake.
# print(snakeee.breathe()) # This is inherited from Animal

#  We have double inheritance and eveurthing is encapsulated in fucntions within parent classes.

