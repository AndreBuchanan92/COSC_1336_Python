#Inputs
salary = 2000
print ("Hello. Welcome to the SoftwarePirates Inc. payment system. We are going to calculate your total pay.")
name = input('\nPlease enter your name: ')

tenure = int(input('Please enter your length of time with the company in months: '))

sales = int(input('Please enter your total sales: '))
if sales < 10000 or tenure <= 3 :
    commission= 0
    gross_Pay = commission + salary
    bonus  = 0

elif sales >= 10000 and sales <= 100000 :
    commission= sales * .02
    gross_Pay = commission + salary
    bonus  = 0

elif sales >= 100001 and sales <= 500000 :
    commission= sales * .15
    bonus = 0 + 1000
    gross_Pay = commission + salary + bonus 

elif sales >= 100001 and sales <= 500000 and tenure >= 60 :
    commission= sales * .15
    bonus = 1000 + 1000
    gross_Pay = commission + salary + bonus 
 
    
elif sales >= 500001 and sales <= 1000000 :
    commission= sales * .28
    bonus = 5000
    gross_Pay = commission + salary + bonus

elif sales >= 500001 and sales <= 1000000 and tenure >= 60 :
    commission= sales * .28
    bonus = 5000 + 1000
    gross_Pay = commission + salary + bonus 

elif sales >= 1000000 :
    commission= sales * .35
    bonus = 100000
    gross_Pay = commission + salary + bonus 

elif sales >= 1000000 and tenure >= 60:
    commission= sales * .35
    bonus = 1000 + 100000
    gross_Pay = commission + salary + bonus

vacation = int(input('Please enter how many vacation days you have taken: '))
if vacation <= 3 :
    new_gross_Pay = gross_Pay
    deductions = 0

elif vacation > 3:
    new_gross_Pay = gross_Pay - 200
    deductions = 200



#outputs
print('name: ', name)
print('tenure: ', tenure, 'months')
print('salary: $', format(salary, '.2f'))
print('sales: $', format(sales, '.2f'))
print('bonus: $', format(commission, '.2f'))
print('Additional bonus: $', format(bonus, '.2f'))
print('deductions: $', format(deductions, '.2f'))
print('Total gross paycheck: $', format(new_gross_Pay, '.2f'))
    
    
    
