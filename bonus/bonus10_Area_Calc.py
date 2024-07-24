while True:
    try:
        width = float(input("Enter rectangle width: "))
        length = float(input("Enter rectangle length: "))
        if width == length:
            print("We don't do Squares here...")
            continue

        area = width * length
        print(f"Area of rectangle is {area}")

        again = input("Want to calculate another Rectangle? ")
        if again.lower() in ['yes', 'y']:
            continue
        else:
            print("Comeback soon, ya' hear!")
            break

    except ValueError:
        print("Please enter a number")
        continue
