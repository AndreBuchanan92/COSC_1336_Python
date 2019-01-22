#Part A
print('Hello, cousin. I cannot understand your measurments! I created this program to help you in the US.')
km = int(input('\nPlease input your kilometers: '))
miles = km / 1.6
if km < 0 :
    print ("Error: please re-enter a positive number.")
else :
    print ('You have gone ', miles ,' miles')

    #Part B
    print ('\nOkay, now lets do temperature')
    celsius = int(input('What is the temperature in celsius? '))
    fahrenheit = (celsius * 9/5) + 32
    if celsius > 1000 :
        print ("Error: please re-enter less than 1000 degrees")
    else:
        print ('The temperature is ', fahrenheit, 'degrees.')

        #Part C
        print ('\nOkay, now lets do liters')
        liters = int(input('How many liters do you have? '))
        gallons = liters / 3.9
        if liters < 0 :
            print ("Error: please re-enter a positive number.")
        else:
            print ('You have ', gallons, 'gallons')

            #Part D
            print ('\nOkay, now lets do kilograms')
            kilogram = int(input('How many kilograms do you have? '))
            lbs = kilogram / .45
            if kilogram < 0 :
                print ("Error: please re-enter a postive number.")
            else:
                print ('You have ', lbs, 'pounds')

                #Part E
                print ('\nOkay, now lets do centimeters')
                cm = int(input('How many centimeters do you have? '))
                inches = cm / 2.54
                if cm < 0 :
                    print("Error: please input a positive number.")
                else: 
                    print ('You have ', inches, 'inches')

             

