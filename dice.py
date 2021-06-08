import random

def roll_die(sides):
    result = random.randint(1, sides)
    return result
    
def main():
    total = 0
    sides = int(input("How many sides on the dice?"))
    rolls = int(input("How many times do you want to roll?"))

    print("Rolling", rolls, "times...")

    i = 1   
    while i <= rolls:
        number = roll_die(sides)
        print("You got a", number, "!")
        total += number
        i += 1
    
    average = round(total / rolls, 2)
    print("Your total was", total, "and your average was", average)
main()
