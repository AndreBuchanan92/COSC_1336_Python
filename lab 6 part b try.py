#this program calculates and saves students avg grades
#so they can be recalled later


#there are 12 students who need this calculation
try:
    for students in range(12):
        #initialize accumulator
        total = 0.0
        #ask student's name
        name = input('Please state your first and last name: ')
        #ask for the number of tests taken
        num_tests = int(input('How many tests taken: '))
        if num_tests < 0:
            num_tests = int(input('Please enter a valid number of tests: '))
        #for each test taken ask for the grade they recieved
        for test in range(num_tests):
            #ask for the student's grade
            grade = int(input('Enter your grade: '))
            if grade < 0 or grade > 100:
                grade = int(input('Please enter a valid grade: '))
            total += grade

        #get average of the grades
        avg_grade = total / num_tests
        #open grades.txt file
        save_grades = open('grades.txt', 'w')
        #write grades to the grades.txt file
        save_grades.write(name)
        save_grades.write(str(format(avg_grade, '.1')))
        print('Your average grade is', format(avg_grade, '.1f'))

    #close file
    save_grades.close()

    
except ValueError:
    print()
    print('ERROR: Please type a valid entry.')
    
except IOError:
    print()
    print('ERROR: File cannot be found. Please give correct file name.')

except:
    print()
    print('An Error has occured.')



#open grades.txt
save_grades = open('grades.txt', 'r')

#display the saved grades
print('These are the saved grades:')
print(save_grades.read())

#close it
save_grades.close()






    
