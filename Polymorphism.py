
# base class containing attributes of an employee
class Employee:
    name = "Employee 1"
    email = "employee@test.com"
    password = "Password123"
    
    def getEmployeeInfo(self):
            msg = "Name: {}\nEmail: {}".format(self.name, self.email)
            return msg

# child class inheriting from the Employee class
class PermanentEmployee(Employee):
    name = 'Sarah Jones'
    email = 'sarahjones@test.com'
   
    def getPEInfo(self):
        
        password = 'Password123'
        salary = 12.00
        probationaryDate = '12/04/2020'
        regularizationDate = '05/04/2021'
        employeeType = 'Permanent Employee'

        msg = "Salary: {}\nProbationary Date: {}\nRegularization Date: {}\n\n".format(salary, probationaryDate, regularizationDate)
        return msg
        

# child class inheriting from the Employee class
class ContractEmployee(Employee):
    
    name = 'Kelly Roger'
    email = 'kellyroger@test.com'
    
    def getCEInfo(self):
        
        password = 'Password123'
        hourlyPay = 13.00
        startOfContractDate = '11/09/2020'
        endOfContractDate = '07/17/2021'
        employeeType = 'Contract Employee'
        
        msg = "Hourly Pay: {}\nStart Of Contract Date: {}\nEnd Of ContractDate\n\n".format(hourlyPay, startOfContractDate, endOfContractDate)
        return msg
        

if __name__ == "__main__":
    pe = PermanentEmployee()
    print(pe.getEmployeeInfo())
    print(pe.getPEInfo())

    ce = ContractEmployee()
    print(ce.getEmployeeInfo())
    print(ce.getCEInfo())
