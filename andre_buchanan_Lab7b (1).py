#this program will allow professors to read entered student names from a file
#using functions that pass lists
#there are 12 student names that will be input

#1. main functions to pass lists
def main():
    students = create_list()
    students = sort_modify_list(students)
    create_file(students)
    convert_list(students)

#2-3. Input a list of 12 student names into a list called 'students'
def create_list():
    students = []
    for num in range(12):                           
        new_name = input ("Please enter a name: ")
        students.append(new_name)
    return (students)

def sort_modify_list(students):
    #4. Put list in alphabetical order
    students.sort()
    #5. Put the list in reverse order
    students.reverse()
    #6. Add the instructor's name to end of list
    instructor_name = input("Please enter instructor's Name: ")
    students.append(instructor_name)
    #7. Add your name to beginning of list
    your_name = input ("Please enter your Name: ")
    students.insert(0, your_name)
    return (students)

#8. Create 'names.txt' and write all the names to it
def create_file(students):
    name_file = open('names.txt', 'a')          
    for item in students:
        name_file.write(item + '\n')
    name_file.close()

    #9. Display what is in 'names.txt'
    print()
    print('Here are the names you have recorded:')
    name_file = open('names.txt', 'r')          
    line = name_file.readline()
    line = line.rstrip()
    print(line)
    while line != '':
        line = name_file.readline()
        line = line.rstrip()
        print (line)
    name_file.close()
    
#10. This file will be made into a tuple
def convert_list(students):                     
    students = tuple(students)

main()
