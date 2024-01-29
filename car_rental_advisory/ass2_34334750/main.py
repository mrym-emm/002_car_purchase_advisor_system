import random
import time
from car import Car
from car_retailer import CarRetailer


def main_menu():
	print("""\n +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
 |C|a|r| |P|u|r|c|h|a|s|e| |A|d|v|i|s|o|r|y| |S|y|s|t|e|m| 
 +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+""")

	print(" 🍃 🚗 🚜 🛻 🚐 🚗 🚜 🛻 🚐 🚗 🚜 🛻 🚐 🚗 🚜 🛻 🚐 🍃 \n")
	print("1. Find nearest car retailer")
	print("2. Get car purchase advice")
	print("3. Place a car order")
	print("4. Exit\n")


#Created additional function for the sub-menu
def sub_menu():
	print("1. Get a car recommendation")
	print("2. Get all cars in stock ")
	print("3. Get car by type")
	print("4. Get probationary license permitted cars")
	print("5. Exit to Main Menu")


#Created additional function to get current time
def current_time():

	#Gets current time structure but not in human readeable format
	cur_time = time.localtime()

	#Turns the above in format like : 17:35
	formatted_time = time.strftime("%H:%M", cur_time)

	#Parse the above formatted_time
	for_cur_hour = int(formatted_time[0:2])
	for_cur_min = formatted_time[3:5]

	#turn it into decimal
	for_cur_min = (int(for_cur_min) / 60)

	#Adds them both up and get it to 2 decimal figure
	cur_hr_min = for_cur_hour + for_cur_min
	cur_hour = round(cur_hr_min, 2)

	return cur_hour


#Created additional function to generate car_code
def car_code_generator():

	car_code_pool_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
							 "S", "T", "U", "V", "W", "X", "Y", "Z"]


	for i in range(0,2):
		letters = random.sample(car_code_pool_letters,2)
		letters = "".join(letters)


	for i in range(0,6):
		numbers = str(random.randint(100000, 999999))

	return f"{letters}{numbers}"


def generate_test_data():

	car_code_final_pool = []

	for i in range(0,20):
		random_car_code = car_code_generator()
		car_code_final_pool.append(random_car_code)


	ran_car_code1, ran_car_code2, ran_car_code3 = random.choice(car_code_final_pool),random.choice(car_code_final_pool),random.choice(car_code_final_pool)
	ran_car_code4, ran_car_code5, ran_car_code6 = random.choice(car_code_final_pool), random.choice(car_code_final_pool), random.choice(car_code_final_pool)
	ran_car_code7, ran_car_code8, ran_car_code9 = random.choice(car_code_final_pool), random.choice(car_code_final_pool), random.choice(car_code_final_pool)
	ran_car_code10, ran_car_code11, ran_car_code12 = random.choice(car_code_final_pool), random.choice(car_code_final_pool), random.choice(car_code_final_pool)

	car_pool_list = [
	str(Car(ran_car_code1,"Perodua Bezza",5,70,940,"FWD")),
	str(Car(ran_car_code2,"Proton Saga",5,69,1035,"FWD")),
	str(Car(ran_car_code3,"Kia Picanto",5,50,860,"FWD")),
	str(Car(ran_car_code4,"Ford Fiesta",5,92,1217,"FWD")),
	str(Car(ran_car_code5,"Toyota Avanza",7,80,1155,"RWD")),
	str(Car(ran_car_code6,"Ford Mustang GT",4,343,1300,"RWD")),
	str(Car(ran_car_code7,"Mazda MX-5",2,135,1030,"RWD")),
	str(Car(ran_car_code8,"Mercedes-Benz SLC",2,140,1075,"RWD")),
	str(Car(ran_car_code9,"Proton X70",5,130,1635,"AWD")),
	str(Car(ran_car_code10,"Subaru Forester",5,155,1532,"AWD")),
	str(Car(ran_car_code11,"Toyota Hilux",5,150,1860,"AWD")),
	str(Car(ran_car_code12,"Hyundai Kona",5,150,1259,"AWD"))
		]

	random.shuffle(car_pool_list)
	list_of_cars_to_write_1 = random.sample(car_pool_list, 4)
	list_of_cars_to_write_2 = random.sample(car_pool_list, 4)
	list_of_cars_to_write_3 = random.sample(car_pool_list, 4)




	car_retailer1 = (str(CarRetailer(-1, "Albert Camus", "Shah Alam 40150", (11.00, 20.00), list_of_cars_to_write_1)))
	car_retailer2 = (str(CarRetailer(-1, "Haruki Murakami", "Petaling Jaya 46050", (9.00, 15.50), list_of_cars_to_write_2)))
	car_retailer3 = (str(CarRetailer(-1, "Leo Tolstoy", "Bamboo Hills 51200", (14.0, 18.00), list_of_cars_to_write_3)))


	with open('data/stock.txt', 'w') as test_writer:
		test_writer.write(car_retailer1 + "\n")
		test_writer.write(car_retailer2 + "\n")
		test_writer.write(car_retailer3 + "\n")


def main():
	path = 'data/stock.txt'


	#writes the data into stock.txt file
	generate_test_data()

	list_of_car_retailers = []

	stock = open(path, 'r')

	for line in stock:
		line = line.strip()
		line_split = line.split(",")
		retailer_info = line_split[0:5]
		car_info = line_split[5:len(line_split)]

		retailer_id = str(retailer_info[0])
		retailer_name = retailer_info[1].strip()
		carretailer_address = retailer_info[2].strip()
		carretailer_business_hours_start = float(retailer_info[3].replace("(", "").strip())
		carretailer_business_hours_end = float(retailer_info[4].replace(")", "").strip())
		carretailer_business_hours = f"({carretailer_business_hours_start},{carretailer_business_hours_end})"

		car_codes = []

		car_code_index = list(range(0, len(car_info), 6))
		for index in car_code_index:
			car_code = car_info[index].strip(" '[]")
			car_codes.append(car_code)

		car_retailer = CarRetailer(retailer_id,retailer_name,carretailer_address,carretailer_business_hours,car_codes)

		list_of_car_retailers.append(car_retailer)

	stock.close()

	car_retailer1 = list_of_car_retailers[0]
	car_retailer2 = list_of_car_retailers[1]
	car_retailer3 = list_of_car_retailers[2]

	while True:

		main_menu()

		try:

			user_input = int(input("Which service would you like?\n"))


			if user_input == 1:

				#The approach I took based on {Get key from value in Dictionary : https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/}

				while True:

					try:

						postcode = int(input("Please input your postcode\n"))

						distance_postcode_dict = {f"Retailer 1(ID): {car_retailer1.retailer_id}":car_retailer1.get_postcode_distance(postcode),f"Retailer 2(ID):{car_retailer2.retailer_id}":car_retailer2.get_postcode_distance(postcode), f"Retailer 3(ID):{car_retailer3.retailer_id}":car_retailer3.get_postcode_distance(postcode) }


						min_postcode_distance = min(distance_postcode_dict.values())

						distance_postcode_key = list(distance_postcode_dict.keys())
						distance_postcode_values = list(distance_postcode_dict.values())

						retailer_position = distance_postcode_values.index(min_postcode_distance)
						retailer_to_print = distance_postcode_key[retailer_position]

						print(f"Closest retailer to you is {retailer_to_print}. If you wish to purchase from them, please take not of the Retailer's ID for your reference!")

						break

					except (TypeError, ValueError):
						print("Invalid input! Please put in your postcode (5-digit)")


			if user_input == 2:

				print("Here is the list of all retailers available! Please select on one for further information.\n")

				print(f"1. Car Retailer 🠮 |Retailer Name| {car_retailer1.retailer_name} ☆ |Retailer ID| {car_retailer1.retailer_id} ☆ |Shop Address| {car_retailer1.carretailer_address} \n")

				print(f"2. Car Retailer 🠮 |Retailer Name| {car_retailer2.retailer_name} ☆ |Retailer ID| {car_retailer2.retailer_id} ☆ |Shop Address| {car_retailer2.carretailer_address}\n")

				print(f"3. Car Retailer 🠮 |Retailer Name| {car_retailer3.retailer_name} ☆ |Retailer ID| {car_retailer3.retailer_id} ☆ |Shop Address| {car_retailer3.carretailer_address}\n")


				user_retailer_choice = int(input("Which car retailer would you like to go with? Please input the corresponding number:\n"))


				while True:

					sub_menu()

					user_action = int(input("Which action would you like to perform? Please input the corresponding number:\n"))

					if user_action == 1:

						if user_retailer_choice == 1:

							rec_car = car_retailer1.car_recommendation()

							print(f"From {car_retailer1.retailer_name}'s shop\nRetailer ID: {car_retailer1.retailer_id}")
							print(f"\nWe recommend: \nCar Name: {rec_car.car_name}\nCar Code: {rec_car.car_code}\nNum Seat: {rec_car.car_capacity} seats\nCar Type: {rec_car.car_type}\n")

						elif user_retailer_choice == 2:

							rec_car = car_retailer2.car_recommendation()

							print(f"From {car_retailer2.retailer_name}'s shop\nRetailer ID: {car_retailer2.retailer_id}")
							print(f"\nWe recommend: \nCar Name: {rec_car.car_name}\nCar Code: {rec_car.car_code}\nNum Seat: {rec_car.car_capacity} seats\nCar Type: {rec_car.car_type}\n")

						elif user_retailer_choice == 3:

							rec_car = car_retailer3.car_recommendation()

							print(f"From {car_retailer3.retailer_name}'s shop\nRetailer ID: {car_retailer3.retailer_id}")
							print(f"\nWe recommend: \nCar Name: {rec_car.car_name}\nCar Code: {rec_car.car_code}\nNum Seat: {rec_car.car_capacity} seats\nCar Type: {rec_car.car_type}\n")



					if user_action == 2:

						if user_retailer_choice == 1:

							all_cars = car_retailer1.get_all_stock()

							print(f"From {car_retailer1.retailer_name}'s shop\nRetailer ID: {car_retailer1.retailer_id}\n")
							print(f"Here are all available cars from {car_retailer1.retailer_name}'s shop!\n")

							for car in all_cars:

								print(f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight} ☆ |CarType| 🠮 {car.car_type}\n")

						elif user_retailer_choice == 2:

							all_cars = car_retailer2.get_all_stock()

							print(f"From {car_retailer2.retailer_name}'s shop\nRetailer ID: {car_retailer2.retailer_id}\n")
							print(f"Here are all available cars from {car_retailer2.retailer_name}'s shop!\n")

							for car in all_cars:

								print(f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight} ☆ |CarType| 🠮 {car.car_type}\n")

						elif user_retailer_choice == 3:

							all_cars = car_retailer3.get_all_stock()

							print(f"From {car_retailer3.retailer_name}'s shop\nRetailer ID: {car_retailer3.retailer_id}\n")
							print(f"Here are all available cars from {car_retailer3.retailer_name}'s shop!\n")

							for car in all_cars:

								print(f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight} ☆ |CarType| 🠮 {car.car_type}\n")



					if user_action == 3:

						if user_retailer_choice == 1:

							user_car_type = input("Please enter the car type (FWD,RWD,AWD):\n")
							filtered_car_type = car_retailer1.get_stock_by_car_type(user_car_type)

							print(f"From {car_retailer1.retailer_name}'s shop\nRetailer ID: {car_retailer1.retailer_id}\n")
							print(f"There are {len(filtered_car_type)} cars in stock:\n")

							for car in filtered_car_type:
								print(f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |CarType| 🠮 {car.car_type} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight}\n")

						elif user_retailer_choice == 2:

							user_car_type = input("Please enter the car type (FWD,RWD,AWD):\n")
							filtered_car_type = car_retailer2.get_stock_by_car_type(user_car_type)

							print(f"From {car_retailer2.retailer_name}'s shop\nRetailer ID: {car_retailer2.retailer_id}\n")
							print(f"There are {len(filtered_car_type)} cars in stock:\n")

							for car in filtered_car_type:
								print(
									f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |CarType| 🠮 {car.car_type} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight}\n")

						elif user_retailer_choice == 3:

							user_car_type = input("Please enter the car type (FWD or RWD or AWD):\n")
							filtered_car_type = car_retailer3.get_stock_by_car_type(user_car_type)

							print(f"From {car_retailer3.retailer_name}'s shop\nRetailer ID: {car_retailer3.retailer_id}\n")
							print(f"There are {len(filtered_car_type)} cars in stock:\n")

							for car in filtered_car_type:
								print(
									f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |CarType| 🠮 {car.car_type} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight}\n")


					if user_action == 4:

						if user_retailer_choice == 1:

							filtered_car_type = car_retailer1.get_stock_by_license_type('p')

							print(f"From {car_retailer1.retailer_name}'s shop\nRetailer ID: {car_retailer1.retailer_id}\n")
							print(f"There are {len(filtered_car_type)} Probationary license car/s in stock at {car_retailer1.retailer_name}'s shop:\n")

							for car in filtered_car_type:
								print(f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |CarType| 🠮 {car.car_type} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight}\n")

						elif user_retailer_choice == 2:

							filtered_car_type = car_retailer2.get_stock_by_license_type('p')

							print(f"From {car_retailer2.retailer_name}'s shop\nRetailer ID: {car_retailer2.retailer_id}\n")
							print(f"There are {len(filtered_car_type)} Probationary license car/s in stock at {car_retailer2.retailer_name}'s shop:\n")

							for car in filtered_car_type:
								print(f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |CarType| 🠮 {car.car_type} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight}\n")

						elif user_retailer_choice == 3:

							filtered_car_type = car_retailer3.get_stock_by_license_type('p')

							print(f"From {car_retailer3.retailer_name}'s shop\nRetailer ID: {car_retailer3.retailer_id}\n")
							print(f"There are {len(filtered_car_type)} Probationary license car/s in stock at {car_retailer3.retailer_name}'s shop:\n")

							for car in filtered_car_type:
								print(f"|CarCode| 🠮 {car.car_code} ☆ |CarName| 🠮 {car.car_name} ☆ |CarType| 🠮 {car.car_type} ☆ |NumSeats| 🠮 {car.car_capacity} ☆ |Car🐎Power| 🠮 {car.car_horsepower} kW ☆ |CarWeight| 🠮 {car.car_weight}\n")

					elif user_action == 5:

						break


			if user_input == 3:

				user_order = input("Please input the relevant Retailer ID followed by the Car Code you would like to order in the following format\n({Retailer ID}_space_{Car Code}):\n")

				user_retailer_id = user_order[0:7]
				user_car_code = user_order[8:16]

				cur_time = time.localtime()
				formatted_time = time.strftime("%H:%M", cur_time)

				cur_hour = current_time()

				if user_retailer_id == car_retailer1.retailer_id:

					if car_retailer1.is_operating(cur_hour) == True:

						order = car_retailer1.create_order(user_car_code)
						order_id = order[0:33]

						car_retailer1.remove_from_stock(user_car_code)

						print(f"Order created! Thank you! You have created an order for CarCode: {user_car_code} from {car_retailer1.retailer_name}'s shop at {formatted_time}.")
						print(f"OrderID: {order_id}")

					else:
						print(f"Sorry, {car_retailer1.retailer_name}'s shop is close! Their business hours are {car_retailer1.carretailer_business_hours} - 24hr format ")


				elif user_retailer_id == car_retailer2.retailer_id:

					if car_retailer2.is_operating(cur_hour) == True:

						order = car_retailer2.create_order(user_car_code)
						order_id = order[0:33]

						car_retailer2.remove_from_stock(user_car_code)

						print(f"OrderID: {order_id}")
						print(f"Order created! Thank you! You have created an order for CarCode: {user_car_code} from {car_retailer2.retailer_name}'s shop at {formatted_time}.")

					else:
						print(f"Sorry, {car_retailer2.retailer_name}'s shop is close! Their business hours are {car_retailer2.carretailer_business_hours} - 24hr format ")


				elif user_retailer_id == car_retailer3.retailer_id:

					if car_retailer3.is_operating(cur_hour) == True:

						order = car_retailer3.create_order(user_car_code)
						order_id = order[0:33]

						car_retailer3.remove_from_stock(user_car_code)

						print(f"OrderID: {order_id}")
						print(f"Order created! Thank you! You have created an order for CarCode: {user_car_code} from {car_retailer3.retailer_name}'s shop at {formatted_time}.")


					else:
						print(f"Sorry, {car_retailer3.retailer_name}'s shop is close! Their business hours are {car_retailer3.carretailer_business_hours} - 24hr format ")


			if user_input == 4:
				print("ฅ^•ﻌ•^ฅ See you again! ฅ^•ﻌ•^ฅ")
				break

		except (TypeError, ValueError):
			print("Invalid choice. Please try again!")


if __name__ == "__main__":
	main()


