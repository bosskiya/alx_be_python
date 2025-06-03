#usr/bin/env python3

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Attempt to convert temperature input to float
        temperature = float(temp_input)

        if unit_input == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius:.2f}°C.")
        elif unit_input == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit:.2f}°F.")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value.")
        print("Error:", e)

if __name__ == "__main__":
    main()
