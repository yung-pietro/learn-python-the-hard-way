#sets cars value to 100
cars = 100
#sets space_in_a_car value to integer 4
space_in_a_car = 4
#sets drivers to integer 30
drivers = 30
#sets passengers to 90
passengers = 90
#subtracts one variable by another
cars_not_driven = cars - drivers
#sets one variable to another
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
