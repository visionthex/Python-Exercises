input_fahrenheit = input('What is the temperature outside in Fahrenheit °F: ')
try:
    fahrenheit = float(input_fahrenheit)
    celsius = (fahrenheit - 32) * (5 / 9)
    print(f'The temperature outside is {celsius:.0f}°C')
except:
    print('Please enter a number and try again.')