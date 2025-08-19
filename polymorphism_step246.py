
# Parent class called Volunteer this will track the name, level and hours
class Volunteer:
    name = ""
    level = "Volunteer"
    hours = 10

    # This function will allow us to initialize the class later on in the program.
    def __init__(self, name, level, hours):
        self.name = name
        self.level = level
        self.hours = hours

    # This function will calculate the wages and then print a summary of the volunteer
    def time(self):
        wages = self.hours * 0
        print("\nThank you",self.name,"for your help. You gave us",self.hours,"hours at the",self.level, "level.")

# This is the first child class. It will inherit the attributes from the parent (Volunteer). It will also add other attributes to track (wage and manages)
class Supervisor(Volunteer):
    wage = 0
    level = "Supervisor"
    manages = 0

    # This function will allow us to initialize the class later on in the program.
    def __init__(self, name, level, hours, wage, manages):
        super().__init__(name, level, hours)
        self.wage = wage
        self.manages = manages       

    # This function will calculate the wages and then print a summary of the volunteer    
    def time(self):
        wages = self.hours * self.wage
        print("\nThank you",self.name,"for your help. You gave us",self.hours,"hours at the",self.level, "level.\nYou have earned $",wages,"and manage",self.manages,"volunteers.")

# This is the second child class. It will inherit the attributes from the parent (Volunteer). It will also add other attributes to track (wage, manages and recruits)
class Manager(Volunteer):
    wage = 0
    level = "Manager"
    manages = 0
    recruits = 0

    # This function will allow us to initialize the class later on in the program.
    def __init__(self, name, level, hours, wage, manages, recruits):
        super().__init__(name, level, hours)
        self.wage = wage
        self.manages = manages
        self.recruits = recruits

    # This function will calculate the wages and then print a summary of the volunteer
    def time(self):
        wages = self.hours * self.wage
        print("\nThank you",self.name,"for your help. You gave us",self.hours,"hours at the",self.level, "level.\nYou have earned $",wages,"and manage",self.manages,"volunteers and have recruited",self.recruits,".")

if __name__ == "__main__":

    # Initializes the volunteer and calls for the summary to print
    volunteer = Volunteer("Joe","Volunteer",15)
    volunteer.time()

    # Initializes the supervisor and calls for the summary to print
    supervisor = Supervisor("Sara","Supervisor",38,12,3)
    supervisor.time()

    # Initializes the manager and calls for the summary to print
    manager = Manager("Fred","Manager",45,15,2,15)
    manager.time()
