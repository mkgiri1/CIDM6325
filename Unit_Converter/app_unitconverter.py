# Mukesh Giri - Unit Conversion App using Python
"""
This app provides following conversions:
1>	Temperature: Celsius to Fahrenheit, Fahrenheit to Celsius, 2>	Area : Square Foot to Square Meter, Square Meter to Square Foot
3>	Volume : US Gallon to Liter, Liter to US Gallon, 4>	Weight: Pound to Kilogram, Kilogram to Pound
"""
# Build Options for requireed conversions
with open("convs.txt", 'w') as file:
    pass


def print_option():
    print("-"*85)
    print("1. Temerature Conversion 2. Area Conversion 3. Volume Conversion""\n""4. Weight Conversion 5. History 6. Exit")
    print("-"*85)

# 1 Temperature COnversion Function


def temp_conversion():
    print("************************\nTemperature Conversion")

    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))
    with open("convs.txt", 'a') as file:
        file.write('%.2f Celsius is: %0.2f Fahrenheit' %
                   (celsius, fahrenheit) + "\n")

    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))
    with open("convs.txt", 'a') as file:
        file.write('%.2f Fahrenheit is: %0.2f Celsius' %
                   (fahrenheit, celsius) + "\n")

# 2 Area COnversion Function


def area_conversion():

    print("************************\nArea Conversion")
    sqfoot = float(input("Enter area in Square Foot:"))
    sqmeter = sqfoot * .0929
    print('Your entered dimensions of %.2f sqfoot is %0.2f sqmeter' %
          (sqfoot, sqmeter))
    with open("convs.txt", 'a') as file:
        file.write('Your entered dimensions of %.2f sqfoot is %0.2f sqmeter' %
                   (sqfoot, sqmeter) + "\n")

    sqmeter = float(input("Enter area in Square Meter:"))
    sqfoot = sqmeter/.0929
    print('Your entered dimensions of %.2f sqmeter is %0.2f sqfoot' %
          (sqmeter, sqfoot))
    with open("convs.txt", 'a') as file:
        file.write('Your entered dimensions of %.2f sqmeter is %0.2f sqfoot' %
                   (sqmeter, sqfoot) + "\n")

# 3 Volume COnversion Function


def vol_conversion():
    print("************************\nVolume Conversion")
    usgallon = float(input("Enter number of US Gallons: "))

    liter = usgallon * 3.785

    print('Volume of %.2f usgallon is %0.2f liter' %
          (usgallon, liter))
    with open("convs.txt", 'a') as file:
        file.write('Volume of %.2f usgallon is %0.2f liter' %
                   (usgallon, liter) + "\n")

    liter = float(input("Enter number of Liters: "))
    usgallon = liter/3.785

    print('Volume of %.2f liter is %0.2f usgallon' %
          (liter, usgallon))
    with open("convs.txt", 'a') as file:
        file.write('Volume of %.2f liter is %0.2f usgallon' %
                   (liter, usgallon) + "\n")

# 4 Weight COnversion Function


def weight_conversion():
    print("************************\nWeight Conversion")
    kgs = float(input("Enter number of Kilograms: "))
    lbs = kgs * 2.205
    print(kgs, "kgs =", lbs, "pounds")

    print('Your entered weight of %.2f kgs is %0.2f lbs' %
          (kgs, lbs))
    with open("convs.txt", 'a') as file:
        file.write('Your entered weight of %.2f kgs is %0.2f lbs' %
                   (kgs, lbs) + "\n")

    lbs = float(input("Enter number of Pounds: "))
    kgs = lbs/2.205
    #print(lbs, "lbs =", kgs, "Kilograms")
    print('Your entered weight of %.2f lbs is %0.2f kgs' %
          (lbs, kgs))
    with open("convs.txt", 'a') as file:
        file.write('Your entered weight of %.2f lbs is %0.2f kgs' %
                   (lbs, kgs) + "\n")


# Display all the options to end user
print_option()
while True:
    choice = input(
        "Please input a value corresponding to conversion you would like to perform:")
    if choice == '6':
        break
    if choice == '5':
        print("Last 10 conversions\n", ("_"*50))
        with open('convs.txt', 'r') as file:
            for i in (file.readlines()[-10:]):
                print(i)
    if choice == '1':
        temp_conversion()

    if choice == '2':
        area_conversion()

    if choice == '3':
        vol_conversion()

    if choice == '4':
        weight_conversion()
    # Display the error to user
    else:
        print("Input a valid choice, or 6 to exit!")
