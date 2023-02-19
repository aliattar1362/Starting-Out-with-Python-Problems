def main():
    # Ask the user to enter the temperature in Celisus
    C = int(input("Enter the temperature in Celisus: "))
    # Formula to convert Celisus to Fahrenheit
    # C is temperature in Celisus, F is temperature in Fahrenheit
    F = (9/5)*C+32
    # Displaye the temperature in Fahrenheit
    print("The temperature in Farenheit is", format(F,".0f"))
main()