from car import Car


class Tesla(Car):
    def __init__(self, number_of_wheels, number_of_windows, number_of_seats):
        Car.__init__(self, 
                    number_of_wheels = number_of_wheels, 
                    number_of_windows = number_of_windows, 
                    number_of_seats = number_of_seats)
        self.autodrive = True
        self.gas_tank = 0 # gallons