def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


celsius = 0
print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.1f}°F")

celsius = 100
print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.1f}°F")

fahrenheit = 72
print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.1f}°C")