def main():
    # Get the number of miles driven 
    miles_driven = int(input("Enter the number of miles driven: "))
    # Get the gallon of used
    used_gallon = int(input("Enter the number of used gallons: "))
    # formula to calculate miles per gallon of a car
    MPG = miles_driven // used_gallon
    print("The miles per gallon of the car is", MPG)
main()