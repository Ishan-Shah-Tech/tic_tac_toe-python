from car import Car



class Merc(Car):
    def __init__(self, number_of_wheels, number_of_windows, number_of_seats):
        Car.__init__(self, 
    number_of_wheels = 4, number_of_windows = 4, number_of_seats = 5)
        
        
        self.autodrive = False
        self.gas_tank = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 # gallons