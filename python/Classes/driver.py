from car import Car
from tesla import Tesla


my_car = Car(number_of_wheels = 4, number_of_windows = 4, number_of_seats = 5)
print("My car has " + str(my_car.number_of_wheels) + " wheels.")
print("My car has " + str(my_car.number_of_windows) + " windows.")
print("My car has " + str(my_car.number_of_seats) + " seats.")
print("Autodrive status: " + str(my_car.autodrive))



your_car = Car(number_of_wheels = 4, number_of_windows = 2, number_of_seats = 2)
print("\nYour car has " + str(your_car.number_of_wheels) + " wheels.")
print("Your car has " + str(your_car.number_of_windows) + " windows.")
print("Your car has " + str(your_car.number_of_seats) + " seats.")
print("Autodrive status: " + str(your_car.autodrive))

my_tesla = Tesla(number_of_wheels = 4, number_of_windows = 4, number_of_seats = 5)
print("\nMy tesla has " + str(my_tesla.number_of_wheels) + " wheels.")
print("My tesla has " + str(my_tesla.number_of_windows) + " windows.")
print("My tesla has " + str(my_tesla.number_of_seats) + " seats.")
print("Autodrive status: " + str(my_tesla.autodrive))
print("My tesla has " + str(my_tesla.gas_tank) + " gas containers left")

your_merc = Merc(number_of_wheels = 4, number_of_windows = 4, number_of_seats = 5)
print("\nYour merc has " + str(your_merc.number_of_wheels) + " wheels")
print("Your merc has " + str(your_merc.number_of_windows) + " windows")
print("Your merc has " + str(your_merc.number_of_seats) + " seats")
print("Autodrive status: " + str(your_merc.autodrive))
print("Your merc has " + str(your_merc.gas_tank) + " gas containers left")