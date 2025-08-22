
# import the needed packages
from abc import ABC, abstractmethod

# create the class
class vehicle(ABC):
    # initializing the method
    def __init__(self,brand):
        self.brand = brand

    # creating the abstract method
    @abstractmethod
    def doors(self):
        pass

# Creating a child class that uses the abstract method
class car(vehicle):
    def doors(self):
        return 4

#creating an object that uses both the parent and the child class and print results
Car = car('Ford')
print('This {} has {} doors.'.format(Car.brand, Car.doors()))
