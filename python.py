# Creating a Python class. This is a child class of the Snake class.
# Once again, we must import the parent class
from snake import Snake
class Python(Snake):

    # Initialise the class
    def __init__(self):
        # Define attributes
        super().__init__()
        self.large = True
        self.two_lungs= True
        self.venom = False

    # Define behaviours
    def digest_large_prey(self):
        return "Hungry"

    def constrict(self):
        return "Squeeze the life"

    def climb(self):
        return "How?! I don't have legs"

    def shed_skin(self):
        return "Out with the old ..."



#  Let's instantaite the class, create an object
pip= Python()
# Inherits from Animal
print(pip.eat())
print(pip.breathe())
# Inherits from Reptile
print(pip.use_venom())
print(pip.tetrapod)
# Inherits from Snake
print(pip.forked_tongue)
print(pip.use_tongue_to_smell())
# Inheirts from Python
print(pip.two_lungs)
print(pip.shed_skin())
