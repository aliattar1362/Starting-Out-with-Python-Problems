def main():
    # Get total square feet in a tract of land
    t_s = int(input("Enter the total square feet in a tract: "))
    # One acres of land is euqal of 43560 square feet
    A = 43560 
    # Calculate Number of Acres
    n_a = t_s / A
    print(format(n_a,',.0f'))

main()