import time 
import random

mode = input("Select one of these two services(Generator, Validator): ")
if(mode == "Generator" or mode == "generator"):
    print("You selected password generator")
    import generate
elif(mode == "Validator" or mode == "validator"):
    print("You selected password validator")
    import validate 
else:
    print("Invalid Command typed!")