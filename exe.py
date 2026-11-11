while True:
    try:
        reading = input("Enter the temperature reading in °C (or 'q' to quit): ")
        if reading.lower() == "q":
            break
        temperature = float(reading)

        if temperature < -40 or temperature > 125:
            print("Out of range: readings must be between -40°C and 125°C")
        elif temperature >= 80:
            print("Hot")
        elif temperature <= 20:
            print("Cold")
        else:
            print("Normal")
    except ValueError:
        print("Invalid input: please enter a number")
