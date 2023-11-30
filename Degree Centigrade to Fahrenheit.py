def c_to_f(centigrade):
    
    fahrenheit = (centigrade * 9/5) + 32
    
    return fahrenheit

centigrade = float(input("Enter the temperature in centigrade: "))

fahrenheit = c_to_f(centigrade)
print(centigrade, "degree centigrade is equal to", fahrenheit, "degree fahrenheit.")
