
import random
while True:
    a = input("\n\n\nD&D INSTANT DICE\n----------------\nFor maximum roll enter a number between 1 and 100: ")
    a = int(a)
    print(f"\nPress Enter to generate a random number between 1 and {a}: ")
    input()
    print(random.randint(1, a))
    a = input("Continue? y/n: ")
    if a == "y":
        pass
    else:
        print("\nFarewell.")
        exit()