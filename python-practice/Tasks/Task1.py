def check_temperatures(readings):
    valid_temps = []

    for reading in readings:
       
        if reading == 999:
            print("ALERT fire alarm triggered stopping check.")
            break

        
        if reading == -99:
            continue

        print("Normal temp: " + str(reading) + "C")
        valid_temps.append(reading)

    return valid_temps


logs = [22, 24, -99, 25, 28, 999, 26, 23]
result = check_temperatures(logs)
print(result)