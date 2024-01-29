import random
import time

from retailer import Retailer
from car import Car
from order import Order

path = 'data/stock.txt'

class CarRetailer(Retailer):


    def __init__(self, retailer_id=-1, retailer_name=None, carretailer_address=None, carretailer_business_hours=None,
                 carretailer_stock=[]):

        # Attribute from parent class
        super().__init__(retailer_id, retailer_name)

        #Non-parent attributes
        self.carretailer_address = carretailer_address
        self.carretailer_business_hours = carretailer_business_hours
        self.carretailer_stock = carretailer_stock


    def __str__(self):

        # Return the car retailer information as a formatted string.
        return f"{self.retailer_id}, {self.retailer_name}, {self.carretailer_address}, {self.carretailer_business_hours},{self.carretailer_stock}"


    def __repr__(self):

        #Not needed, but in order to print my list of car_retailer objects, this helped

        return f"{self.retailer_id}, {self.retailer_name}, {self.carretailer_address}, {self.carretailer_business_hours},{self.carretailer_stock}"


    def load_current_stock(self, path):

        # Load the current stock of the car retailer according to the retailer_id from
        # the stock.txt file and store the car_codes of the Cars in a list; this list should
        # be saved to carretailer_stock

        car_codes = []

        #Open stock file
        stock = open(path, 'r')

        #Basically this part parses each line from the txt file and so I can further use it further
        for line in stock:

            #removes any trailing spaces
            line = line.strip()

            #turn line into a list
            line_split = line.split(",")

            #seperate line into retailer_info and car_info
            retailer_info = line_split[0:5]
            car_info = line_split[5:len(line_split)]

            #for below use
            retailer_id = retailer_info[0]

            if retailer_id == self.retailer_id:

                #car_code for respective car in car_info appears at index 0,6,12 and so on.
                car_code_index = list(range(0, len(car_info), 6))
                for index in car_code_index:
                    car_code = car_info[index].strip(" '[]")
                    car_codes.append(car_code)

        stock.close()

        #As per instruction, this will store the relevant car_code to their respective CarRetailer
        self.carretailer_stock = car_codes

        #Just to test if it works
        # return car_codes


    def is_operating(self, cur_hour):

        #Return a boolean value to indicate whether the car retailer is currently operating (i.e., within working hours)

        #Based on my txt file, the business hours will appear like (12.0, 14.5).
        #The below code basically cleans it up and put it in a list
        clean_bus_time = self.carretailer_business_hours.strip("()")
        list_clean_bus_time = clean_bus_time.split(",")

        #Temporary list to put in the business hours, and will convert them to floar since theyre currently strings
        temp_list = []

        for i in list_clean_bus_time:
            temp_list.append(float(i))

        open_time = temp_list[0]
        close_time = temp_list[1]

        #To check if shop is opened in comparison to cur_hour
        if open_time <= cur_hour <= close_time:
            return True

        return False


    def get_all_stock(self):

        # Returns the information of all available cars currently in stock at the car retailer

        car_objects = []

        #What I attempt to do is parse each line from current txt file, and store them into variables. Used a lot of try & exceptions to avoid error, and interruption.
        #Uses similar logic as load_current_stock in terms of parsing

        try:

            stock = open(path, 'r')

            for line in stock:
                line = line.strip()
                line_split = line.split(",")
                retailer_info = line_split[0:5]
                car_info = line_split[5:len(line_split)]
                retailer_id = retailer_info[0]

                if retailer_id == self.retailer_id:
                    car_object_index = list(range(0, len(car_info)))

                    #The car_info that is retrieved isn't in the format I wanted so have to clean it up
                    for index in car_object_index:
                        car_object = car_info[index].strip(" '[]")
                        car_objects.append(car_object)

            stock.close()

            #Initiate list so I can append individual car. However, this is still string format
            list_car_objects = []

            #Used try here to handle the exceptions I received which were IndexError & UnboundLocalError
            #The below code allows a individual car variable to be created, and if theres none, it wont stop, and will just create the necesary.
            #But this code may not be the best because it's not dynamic
            try:
                first_car = car_objects[:6]
                list_car_objects.append(first_car)

                second_car = car_objects[6:12]
                list_car_objects.append(second_car)

                third_car = car_objects[12:18]
                list_car_objects.append(third_car)

                fourth_car = car_objects[18:24]
                list_car_objects.append(fourth_car)

                fifth_car = car_objects[24:30]
                list_car_objects.append(fifth_car)

                sixth_car = car_objects[30:36]
                list_car_objects.append(sixth_car)

            except IndexError:
                pass

            final_list_car_objects = []

            #The below code will take each car item in the list_car_objects, parse them and pass it tru the Car class.
            #Which will then create a car object and will be appended to the final_list_car_objects

            try:

                for car in list_car_objects:

                    car_code = car[0]
                    car_name = car[1]
                    car_capacity = car[2]
                    car_horsepower = car[3]
                    car_weight = car[4]
                    car_type = car[5]

                    ind_car_obj = Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)

                    final_list_car_objects.append(ind_car_obj)

            except IndexError:
                pass

            try:
                return final_list_car_objects

            except UnboundLocalError:
                pass

        except TypeError:
            pass


    def get_postcode_distance(self, postcode):

        #Return the absolute difference of the postcode input by the user and that
        # of the car retailer. You need to extract the postcode from
        # carretailer_address first.

        #The below code parses the address and since the postcode is at the same place,
        # it would work regardless of the length of address

        #Put the address in reverse. Ex: Shah Alam 40150 will become 05104 malA hahS
        retailer_address_reverse = self.carretailer_address[::-1]
        retailer_postcode_reverse = retailer_address_reverse[0:5]

        #Reverse it again so postcode in correct order
        retailer_postcode_not_reverse = int(retailer_postcode_reverse[::-1])
        absolute_postcode_difference = abs(postcode - retailer_postcode_not_reverse)

        return absolute_postcode_difference


    def remove_from_stock(self, car_code):


        # Remove a car from the current stock at the car retailer. The car stock
        # should be consistent with the stock.txt file. A boolean value should be
        # returned to indicate whether the removal is successful.

        #By using the get_all_stock() method, I'm able to get the stock of all cars according to the car retailer
        cars_from_retailer = self.get_all_stock()

        #placeholder list to put a car objects in the list before changing it into string
        new_list = []

        #iterates through all cars available in the car retailer's stock
        for car in cars_from_retailer:

            #Initially, if the car code in the list matches the car_code to be removed, then I would delete it from the list
            #However, after testing, my txt file would have empty lists in the string, and as progressing, I would get an error
            #Doing the opposite, would avoid the error, and my stock.txt format would not look weird
            if car.car_code != car_code:
                new_list.append(car)
            string_new_list = "".join(str(new_list))

            #My approach is to extract all information again from the current stock file, and re-write it with the updated info
            stock = open(path, 'r')

            #Placeholder to hold the updated info
            updated_list_to_write = []


            #Same approach with other methods in terms of extracting info
            for line in stock:
                line = line.strip()
                line_split = line.split(",")
                retailer_info = line_split[0:5]
                car_info = line_split[5:len(line_split)]
                retailer_id = retailer_info[0]
                string_retailer_info = ','.join(retailer_info)
                string_car_info = ','.join(car_info)
                clean_string_car_info = string_car_info.strip(" '[]")

                #Going tru the lines, if the retailer_id matches, then create append the string in the below format to the placeholder list
                if self.retailer_id == retailer_id:
                    updated_line = f"{string_retailer_info},{string_new_list}"
                    updated_list_to_write.append(updated_line)

                else:
                    no_change_line = f"{string_retailer_info},[{clean_string_car_info}]"
                    updated_list_to_write.append(no_change_line)

            stock.close()

            #Re-writes everything in the txt file with information in the placeholder list
            stock = open(path, 'w')

            for line in updated_list_to_write:
                stock.write(''.join(line) + '\n')

            stock.close()

        return True


    def add_to_stock(self, car):

        # Add a car to the current stock. The car stock should be consistent with the
        # stock.txt file. A boolean value should be returned to indicate whether the
        # adding is successful

        #Similar approach to the remove_from stock. This code passes a car object

        cars_from_retailer = self.get_all_stock()

        #To get the list of car_codes per car_retailer to use as condition
        car_code_retailer = self.load_current_stock(path)

        #Check if the car_object that is passed tru matches any in the car_code list. If not, then append it into the list
        if car.car_code not in car_code_retailer:
            cars_from_retailer.append(car)

        else:
            print("Car already exist")
            return False

        #Change the list of car_objects into string
        to_update = str(cars_from_retailer)

        #Extract info and update information
        stock = open(path, 'r')

        #Placeholder
        updated_list = []

        for line in stock:
            line = line.strip()
            line_split = line.split(",")
            retailer_info = line_split[0:5]
            string_retailer_info = ",".join(retailer_info)
            # car_info = line_split[5:len(line_split)]
            # string_car_info = ','.join(car_info)
            retailer_id = retailer_info[0]

            if retailer_id == self.retailer_id:
                updated_line = f"{string_retailer_info},{to_update}"
                updated_list.append(updated_line)

            else:
                updated_list.append(line)

        stock.close()

        #re-writes everything into the file
        stock = open(path, 'w')

        for line in updated_list:
            stock.write(''.join(line) + '\n')
        stock.close()

        return True


    def get_stock_by_car_type(self, car_types):

        #Return the list of cars in the current stock by specific car_type values

        cars_from_retailer = self.get_all_stock()

        #ensure the arguement pass tru is in lower font
        car_types = car_types.lower()

        #Placeholder to store car_type
        awd_type_car = []
        rwd_type_car = []
        fwd_type_car = []

        #for each car in the cars_from_retailer, we want to pass each attribute to a variable so I can certain tpye(str to int)
        #and then create a car object.

        for car in cars_from_retailer:

            car_code = car.car_code
            car_name = car.car_name
            car_capacity = car.car_capacity
            car_horsepower = int(car.car_horsepower)
            car_weight = int(car.car_weight)
            car_type = car.car_type

            ind_car_obj = Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)

            #the below will ensure that the each car_type will be stored in their respective list
            if ind_car_obj.get_car_type() == "AWD":
                awd_type_car.append(ind_car_obj)

            elif ind_car_obj.get_car_type() == "FWD":
                fwd_type_car.append(ind_car_obj)

            elif ind_car_obj.get_car_type() == "RWD":
                rwd_type_car.append(ind_car_obj)

        #Below will return the relevant list of cars according to the arguement passed tru
        if car_types == "awd":
            return awd_type_car

        elif car_types == "fwd":
            return fwd_type_car

        elif car_types == "rwd":
            return rwd_type_car


    def get_stock_by_license_type(self, license_types):

        #Return the list of cars in the current stock that are not forbidden by the
        #driver’s licence type.

        cars_from_retailer = self.get_all_stock()

        #ensure the arguement passed tru is in lower format
        license_types = license_types.lower()

        #placeholder list to store probationary and non-probationary cars
        probationary_cars = []
        non_probationary_cars = []

        #same approach to get_stock_by_car_type method
        # for each car in the cars_from_retailer, we want to pass each attribute to a variable so I can certain tpye(str to int)
        # and then create a car object.

        for car in cars_from_retailer:
            car_code = car.car_code
            car_name = car.car_name
            car_capacity = car.car_capacity
            car_horsepower = int(car.car_horsepower)
            car_weight = int(car.car_weight)
            car_type = car.car_type

            ind_car_obj = Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)

            if ind_car_obj.probationary_licence_prohibited_vehicle() == True:
                probationary_cars.append(ind_car_obj)

            elif ind_car_obj.probationary_licence_prohibited_vehicle() == False:
                non_probationary_cars.append((ind_car_obj))

        # Below will return the relevant list of cars according to the arguement passed tru
        if license_types == "l" or license_types == "full":
            return non_probationary_cars

        elif license_types == "p":
            return probationary_cars


    def car_recommendation(self):

        # Return a car that is randomly selected from the cars in stock at the current
        # car retailer

        cars_from_retailer = self.get_all_stock()
        random_car = random.choice(cars_from_retailer)
        return random_car

    def create_order(self, car_code):

        # Return an order object of a created order. When an order is created, the
        # car needs to be removed from the current stock of the car retailer. Such
        # updates need to be reflected in “stock.txt”. The created order needs to be
        # appended to “order.txt

        cars_from_retailer = self.get_all_stock()

        # for each car in the cars_from_retailer, we want to pass each attribute to a variable so I can certain tpye(str to int)
        # and then create a car object.
        for car in cars_from_retailer:
            zcar_code = car.car_code
            zcar_name = car.car_name
            zcar_capacity = car.car_capacity
            zcar_horsepower = int(car.car_horsepower)
            zcar_weight = int(car.car_weight)
            zcar_type = car.car_type

            ind_car_obj = Car(zcar_code, zcar_name, zcar_capacity, zcar_horsepower, zcar_weight, zcar_type)

            #as it iterates tru all the car objects, if the car objects matches the car_code being passed tru then an order will be made
            if ind_car_obj.car_code == car_code:

                #The below will be used to create an order object
                order_car = ind_car_obj.car_code
                order_retailer = self.retailer_id

                #Will give current UNIX time
                order_creation_time = int(time.time())

                #Will create the order object with the information that we have and turn it into a string
                new_order = Order(order_car = order_car, order_retailer = order_retailer,
                                  order_creation_time = order_creation_time)
                new_order_string = str(new_order)

                #Appends the information into the order txt
                order = open('data/order.txt', 'a')
                order.write(new_order_string + '\n')

                order.close()

                return new_order_string




#Test (I'm using the ready stock file for below)

# path = 'data/stock.txt'

# 2.3.2
# car_retailer1 = CarRetailer(retailer_id="3398595", retailer_name="Jerry", carretailer_business_hours= "(11.0, 20.0)",
#                             carretailer_address="shah alam 20394")
# print(car_retailer1)
# Outpur:6195882, Jerry, shah alam 20394, (11.0, 20.0),[]

# 2.3.3
# print(car_retailer1.load_current_stock(path))
# Output: ['2H2ESDKI', 'MJ20K6SI', 'CRD19Y1V', '4C90VTC7']

# 2.3.4
# print(car_retailer1.is_operating(4.5))
# Output: False

# 2.3.5
# print(car_retailer1.get_all_stock())
# Output: ['2H2ESDKI,Perodua Bezza,5,70, 940, FWD', 'MJ20K6SI,Ford Fiesta,5,92, 1217, FWD', 'CRD19Y1V,Mazda MX-5,2,135, 1030, RWD', '4C90VTC7,Subaru Forester,5,155, 1532, AWD']

# 2.3.6
# print(car_retailer1.get_postcode_distance(40150))
# Outtput: 19756

# 2.3.7
# print(car_retailer1.remove_from_stock("MJ20K6SI"))
#car with the matching car_code was removed
#Output: 3398595, Albert Camus, Shah Alam 40150, (11.0, 20.0),['2H2ESDKI,Perodua Bezza,5,70, 940, FWD', 'CRD19Y1V,Mazda MX-5,2,135, 1030, RWD', '4C90VTC7,Subaru Forester,5,155, 1532, AWD']

# 2.3.9
# print(car_retailer1.get_stock_by_car_type("rwd"))
# Output: ['CRD19Y1V,Mazda MX-5,2,135, 1030, RWD']

# 2.3.10
# print(car_retailer1.get_stock_by_license_type("l"))
# Output: ['2H2ESDKI,Perodua Bezza,5,70, 940, FWD', '4C90VTC7,Subaru Forester,5,155, 1532, AWD']
# print(car_retailer1.get_stock_by_license_type("p"))
# Output: ['CRD19Y1V,Mazda MX-5,2,135, 1030, RWD']

# 2.3.11
# print(car_retailer1.car_recommendation())
# Output : 2H2ESDKI,Perodua Bezza,5,70, 940, FWD

# 2.3.12
# print(car_retailer1.create_order("4C90VTC7"))
# Output: This line will be appended to the ordertxt file: ~!!~~~~~~~$$$$$4C90VTC71695374111,4C90VTC7,3398595 1695374111