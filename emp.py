class Employee:
    def __init__(self, eid, designation):
        self.eid = eid
        self.designation = designation

    def display_info(self):
        print(f"Employee ID: {self.eid}")
        print(f"Designation: {self.designation}")

# Input from user
eid = input("Enter Employee ID: ")
designation = input("Enter Designation: ")

# Create Employee object
employee = Employee(eid, designation)
employee.display_info()
