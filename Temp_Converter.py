while True:
    try:
        celsius = float(input("Enter temp in Celsius: "))
        print(f"{celsius}C is {(9/5)*celsius+32}F")
        fahrenheit = float(input("Enter temp in Fahrenheit: "))
        print(f"{fahrenheit}F is {(fahrenheit-32)*(5/9)}F")
    except:
        print("Invalid input")
