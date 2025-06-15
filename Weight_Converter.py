weight = int(input("Enter your weight : "))
unit = input("Enter weight unit L/l for lbs and K/k for kg :")

if unit.upper() == "L":
    weight = weight * 0.45
    print(f"Your weight is converted in Kg : {weight} kg")

else :
    weight = weight / 0.45
    print(f"Your weight is converted in Lbs : {weight} lbs")