print("------------Employee Salary Management System---------")
employees = {
    "EMP101":"Pranjal",
    "EMP102":"Paramita",
    "EMP103":"Pragnya",
    "EMP104":"Prachi",
    "EMP105":"Priyanshi"
}
for i in range(3):
    print(f"\nLogin ")
    name=input("Enter your name:")
    emp_id=input("Enter your empid:")
    if emp_id in employees and employees[emp_id]==name:
        print("\nAuthentication Successful")
        
        salary=float(input("Enter your salary for one day:-"))
        working_day=int(input("Enter how many days you have worked:-"))
        monthly_salary=salary*working_day
        print("The total salary for this month is: ",monthly_salary)
        if working_day>25:
            overtime=(working_day-25)*salary*1.5
        else:
            overtime=0


        print("\n--Performance Levels:")
        print("1.Excellent (20% increment)")
        print("2.Good (10% increment)")
        print("3.Average (5% increment)")
        choice=int(input("Enter performance choice (1/2/3): "))
        if choice==1:
            increment=monthly_salary*0.20
        elif choice==2:
            increment=monthly_salary*0.10
        elif choice==3:
            increment=monthly_salary*0.05
        else:
            increment=0
            print("Invalid choice! no increment applied.")
        inc_salary=monthly_salary+increment+overtime
        if inc_salary>50000:
            tax = inc_salary*0.10
        else:
            tax=0
        final_salary=inc_salary-tax
        print("\n-----Salary Details-----")
        print("Employee Name:-",name)
        print("Monthly salary :",monthly_salary)
        print("Overtime pay:",overtime)
        print("Increment amount:",increment)
        print("Tax deducted:",tax)
        print("Final salary:",final_salary)
    else:
        print("Not accesible! due to invalid name or emp_id")