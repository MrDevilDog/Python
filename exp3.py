basic_salary =int(input("enter the basic salary:"))
dearness_allowance =0.7* basic_salary
travel_allowance =0.3* basic_salary
house_rent_allowance =0.1* basic_salary
grosssalary= basic_salary + dearness_allowance + travel_allowance + house_rent_allowance
print("the gross salary is" ,grosssalary)
