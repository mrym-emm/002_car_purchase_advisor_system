class Car:

    # list_car = []

    def __init__(self, car_code = None, car_name = None, car_capacity = 0, car_horsepower = 0, car_weight = 0, car_type = None):

        #Attributes of Car object
        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type

        # Car.list_car.append(self)

    #Returns created object in readeable way, followed initial assignment specifications
    def __str__(self):

        # Return the unit information as a formatted string.
        return f"{self.car_code},{self.car_name},{self.car_capacity},{self.car_horsepower}, {self.car_weight}, {self.car_type}"


    def __repr__(self):

        #Not part of task, but used it so objects appear in list (if needed)
        return f"'{self.car_code},{self.car_name},{self.car_capacity},{self.car_horsepower}, {self.car_weight}, {self.car_type}'"


    def probationary_licence_prohibited_vehicle(self):

        #Return whether the vehicle is a prohibited vehicle for probationary licence drivers
        if ((self.car_horsepower / self.car_weight) * 1000) > 130:
            return True
        return False

    def found_matching_car(self,car_code):

        # Return whether the current vehicle is the one to be found based on a car_code
        if car_code == self.car_code:
            return True
        return False

    def get_car_type(self):

        #Return the car_type of the current car.
        return f"{self.car_type}"



#Test Data

# car_1 = Car("2H2ESDKI", "Perodua Bezza", 5, 70, 940, "FWD")

# car_2 = Car("CRD19Y1V","Mazda MX-5",2,135, 1030,"RWD")

#2.1.2
# print(car_1)
# output: 2H2ESDKI,Perodua Bezza,5,70, 940, FWD


#2.1.3
# print(car_1.probationary_licence_prohibited_vehicle())
# car_1 based on the valuse I put, is not considered probitionary vehicle
# output: False

# print(car_2.probationary_licence_prohibited_vehicle())
# Since the power to mass ratio is > 130 kw
# output: True

#2.1.4
# print(car_1.found_matching_car("2H2ESDKI"))
# Output : True (Since the car_code passed is the same as the car_code of car_1

# print(car_1.found_matching_car("CRD19Y1V"))
# Output: False (car_code passed belongs to car_2)

# 2.1.5
# print(car_1.get_car_type())
# Output: FWD

# print(car_2.get_car_type())
# Output: RWD







