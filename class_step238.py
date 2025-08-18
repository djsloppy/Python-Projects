
# Creates an Athlete class that will track an athlete's
# name, number assigned to them, and sport
class Athlete:
    name = ""
    number = 0
    sport = ""

# Child class is Driver where they will also have a vehicle
# attribute (car, truck, boat) and a series that they race
# in (NASCAR< IndyCar, F1, etc.)
class Driver(Athlete):
    vehicle = ""
    race_series = ""

# There are collegiete athletes that attend various colleges
# and will have a year they are (Fr., So., Jr., Sr.)
class College(Athlete):
    school = ""
    year = ""
