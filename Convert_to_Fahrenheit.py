input_celsius = input('What is the temperature outside in Celsius °C: ')
try:
    celsius = float(input_celsius)
    fahrenheit = ((celsius * (9/5)) + 32)
    print(f'The temperature outside is {fahrenheit:.0f}°F')
except:
    print('Please enter a number and try again.')
