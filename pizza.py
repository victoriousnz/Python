import math

def main():
    people = int(input("How many people are eating?"))
    eat = float(input("How many slices will they eat?"))
    slices = int(input("How many slices per pizza?"))
    
    eaten_slices = people * eat
    pizzas = math.ceil(eaten_slices / slices)
    all_slices = pizzas * slices
    leftovers = all_slices - eaten_slices
    print("For", people, "people, you will need", pizzas, "pizzas and you will have", leftovers, "slices left over.")

main()