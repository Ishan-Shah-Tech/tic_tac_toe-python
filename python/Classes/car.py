from pickle import FALSE


class Car:
    def __init__(self, number_of_wheels, number_of_windows, number_of_seats):
        self.number_of_wheels = number_of_wheels
        self.number_of_windows = number_of_windows
        self.number_of_seats = number_of_seats
        self.autodrive = False
        self.gas_tank = 10 # gallons