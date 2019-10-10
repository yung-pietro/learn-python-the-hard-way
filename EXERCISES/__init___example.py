#Using a car with characteristics and functionality(methods) as analogy
class Car(object):
    """
    blueprint for a car
    """

    def __init__(self, model, color, company, horsepower, gear=0, max_gears=6):
        self.color = color
        self.company = company
        self.horsepower = horsepower
        self.model = model
        self.gear = gear
        self.max_gears = max_gears

    def start(self):
        #some action
        print("Started!")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("Accelating...")
        # "Accelarator functionality here"

    def change_gear(self, gear_type):
        if self.gear == 0:
            print("neutral")
            if gear_type == 1 or gear_type == -1: # -1 for reverse 0 for neutral
                print("gear changed")
                self.gear = gear
        if gear_type > self.max_gears:
            print("cannot upsift to requested gear")
        # "gear related functionality here"

# now let's make cars using the Car class (objects)

suzuki = Car("Grand Vitara", "black", "Suzuki", 200)
print(suzuki.gear)
suzuki.change_gear(1)
suzuki.change_gear(7)
exit()
audi = Car("A6", "Red", "Audi", 160)
#notice that the attributes follow the same sequence as they are originally defined in the class
# These attributes are then passed to the __init__ function to instantiate the object

# ------------------------  Another Example ------------------------- #

class Rectangle:
    #one could also create this by saying class Rectangle(object): or class Rectangle):
    #absolutely NO difference
    def __init__(self, length, width, unit_cost=0):
        self.length = length
        self.width = width
        self.unit_cost = unit_cost
        #unit_cost = 0 simply sets placeholder value, that remains unless defined during object creation.

    def get_perimeter(self):
        return 2 * (self.length + self.width)
        #can you think of an example where the method would take multiple arguments?
        #What would that look like?

    def get_area(self):
        return self.length * self.width

    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost

# For a plot that measures 120cm x 160 cm and 1cm ^2 = $2000
r = Rectangle(120, 160, 2000)
print("Area of rectangle is %s cm^2" % (r.get_area()))
print("Cost of rectangular field is: $%s " % (r.calculate_cost()))
