#if item in position 0 is greater than 12 or less than 1, error, ask again
#if it is in range assign a word_month accordingly

def main():
    month = int(input('Two digit Month: '))
    while month > 12 or month < 0:
        print('Error: Month cannot be greater than 12 or less than zero.')
        month = int(input('Two digit month: '))
    if month == 1:
        word_month = 'January'
    elif month == 2:
        word_month = 'February'
    elif month == 3:
        word_month = 'March'
    elif month == 4:
        word_month = 'April'
    elif month == 5:
        word_month = 'May'
    elif month == 6:
        word_month = 'June'
    elif month == 7:
        word_month = 'July'
    elif month == 8:
        word_month = 'August'
    elif month == 9:
        word_month = 'September'
    elif month == 10:
        word_month = 'October'
    elif month == 11:
        word_month = 'November'
    else:
        word_month = 'December'

        
    #if item in position 1 is over 31 or under 1, print an error and ask again
    day = int(input('Two digit Day: '))
    while day > 31 or day < 1:
        print('Error: Day cannot be negative or greater than 31.')
        day = int(input('Two digit Day: '))
    #if item in position 2 is not 15, print error, ask again
    year = int(input('Two digit Year: '))
    while year != 15:
        print('Error: The year is 2015. Please make a valid entry.')
        year = int(input('Two digit Year: '))
    #once 15 is input for year, write full year
    full_year = '2015'
    #convert month, day and year to a string
    month = str(month)
    day = str(day)
    year = str(year)
    

    #create a list to hold date values
    print('The date is', month, '/', day, '/', year)
    print('or in long form...')
    print(str(word_month + " " + day + ', ' + full_year))


main()
