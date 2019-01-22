#1. Create two "arrays" that store Fahrenheit and other original values.
Fahrenheit = [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
original_values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#2. Display list of Fah. temps
print('List of Fahrenheit temperatures: ')
print(Fahrenheit)
print('List of other Original Values: ')
print(original_values)

print()
print()

#3. Create tables that show original value & conversion to metric

#Fahrenheit to Celsius
Celsius =  []                           
for item in Fahrenheit:
    Celsius.append(int((item - 32) * 5/9))
F_to_C = [Fahrenheit,
          Celsius]

#miles to kilometers
kilometers =  []                            
for item in original_values:
    kilometers.append(int(item*1.6))
mi_to_km = [original_values,
            kilometers]

#gallons to Litres
Liters =  []                                
for item in original_values:
    Liters.append(int(item*3.9))
g_to_L = [original_values,
          Liters]

#pounds to kilograms
kilograms =  []                         
for item in original_values:
    kilograms.append(int(item*0.45))
lb_to_kg = [original_values,
            kilograms]

#inches to centimeters
centimeters =  []                           
for item in original_values:
    centimeters.append(int(item*2.54))
in_to_cm = [original_values,
            centimeters]

#4. Display the contents of each list and create a table

#show Celsius list
print('Here is the list of temps in Celsuis: ')
print(list(Celsius))
print()
#show Celsuis table
print('Fah\tCel')
print('-------------')
for column in range(12):
    print(F_to_C[0][column], '°F = ', F_to_C[1][column], '°C')
print()

#show kilometers list
print('Here is the list of values converted to kilometers: ')
print(list(kilometers))
print()
#show kilometers table
print('Mi\tKm')
print('-------------')
for column in range(11):
    print(mi_to_km[0][column], 'mi = ', mi_to_km[1][column], 'km')
print()

#show liters list
print('Here is the list of values converted to liters: ')
print(list(Liters))
print()
#show liters table
print('G\tL')
print('-------------')
for column in range(11):
    print(g_to_L[0][column], 'g = ', g_to_L[1][column], 'L')
print()

#show kilograms list
print('Here is the list of values converted to kilograms: ')
print(list(kilograms))
print()
#show kilograms table
print('Lbs\tKg')
print('-------------')
for column in range(11):
    print(lb_to_kg[0][column], 'lb = ', lb_to_kg[1][column], 'kg')
print()

#show centimeters list
print('Here is the list of values converted to centimeters: ')
print(list(centimeters))
print()
#show centimeters table
print('In\tCm')
print('-------------')
for column in range(11):
    print(in_to_cm[0][column], 'in = ', in_to_cm[1][column], 'cm')

