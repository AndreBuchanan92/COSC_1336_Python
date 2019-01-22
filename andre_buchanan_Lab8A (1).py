#condition primer for number of invalid entries
count = 0 

while count < 3: 
    #ask for a number of miles
    miles = float(input('How many miles would you like to convert? '))
    if miles < 0:
        print('Error: no negative numbers permitted.')
        count += 1

    else:
        #reset counter
        count = 0
        while count < 3:
            #ask for temp to convert Fahrenheit to Celsius
            F = float(input('How many degrees Fahrenheit would you like to convert? '))
            if F > 1000:
                print('Error: Cannot be above 1000 degrees.')
                count += 1

            else:
                #reset counter
                count = 0
                while count < 3:
                    #ask for number of gallons to convert to liters
                    G = float(input('How many gallons would you like to convert? '))
                    if G < 0:
                        print('Error: no negative numbers permitted.')
                        count += 1
                        
                    else:
                        #reset counter
                        count = 0
                        while count < 3:
                            #ask for pounds to convert to kilograms
                            lbs = float(input('How many pounds would you like to convert? '))
                            if lbs < 0:
                                print("Error: no negative numbers permitted.")
                                count += 1
                            
                            else:
                                #reset counter
                                count = 0
                                while count < 3:
                                    #ask for inches to convert to centimeters
                                    inches = float(input('How many inches would you like to convert? '))
                                    if inches < 0:
                                        print('Error: no negative numbers permitted.')
                                        count += 1
                                
                                    else:
                                        count += 1
                                        #convert input into new format
                            
                                        #calculate km from given number of miles
                                        km = miles*1.6
                                        #calculate Celsius from Fahrenheit
                                        C = (F-32) * (5/9)
                                        #convert Gallons to Liters
                                        L = G/3.9
                                        #convert pounds to kg
                                        kg = lbs/.45
                                        #convert cm to inches
                                        cm = inches * 2.25

                                        #Ask the user for their name and email
                                        name = str(input('Please enter your name: '))
                                        email = str(input('Please enter your email: '))
                                        
                                        #if email does not contain @, ask for a valid entry
                                        symbol = '@'
                                        while symbol not in email:
                                            print('Your email must contain the @ symbol.')
                                            email = input('Please make a valid entry: ')
                                        else:
                                            print()


                                        #print results and display user's name
                                        print('Thank you', name, '. Here are your conversions.')
                                        print()
                                        print('The number of kilometers is: ', format(km, '.2f'))
                                        print('That number in Celsius is', format(C, '.2f'), 'Degrees')
                                        print('The number of liters is: ', format(L, '.2f'))
                                        print('The nuber of kilograms is: ', format(kg, '.2f'))
                                        print('The number of centimeters is: ', format(cm, '.2f'))
                                        count = 4

if count <= 3:
    print("Too many invalid entries. Program terminated.")
else:
    print('Goodbye.')
