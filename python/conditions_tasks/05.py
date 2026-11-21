'''Take the temperature in °C and print the advice.
Temperature (°C)
Below 10
10 to 25
26 to 35
Print
Cold, wear a jacket
Pleasant
Warm
Above 35
Very hot, stay hydrated'''

temperature = int(input("Enter temperature in Celsius: "))

if temperature < 10:
    print("Cold, wear a jacket")
elif temperature > 10 and temperature < 25:
    print("Pleasent")
elif temperature > 26 and temperature < 35:
    print("Warm")
else:
    print("Very hot, stay hydrated")



