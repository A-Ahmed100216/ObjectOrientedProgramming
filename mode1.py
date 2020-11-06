# Uusing __name__ and __main__

print("this is mode 1 --> " + __name__)
#  This print statement will return this is mode 1 --> __main__
#  __name__ is __main__ as this is the main directory we are using.

def main():
    return "from mode 1 function "
    #pass # The pass keyword can be used if we dont want towrite anthing within the funciton just yet.
#  pass helps you pass without erros

# syntax if __name__=="__main__":
#  The if statement checks whether the code is run from the current file.
if __name__ =="__main__":
    main()