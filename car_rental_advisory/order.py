import time
import random

class Order:

    #to use in my generate_order_id method
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                       "t", "u", "v", "w", "x", "y", "z"]

    #class variable to be used in generate order_id
    str_1 = "~!@#$%^&*"

    def __init__(self, order_id=None,order_retailer =None, order_car = None, order_creation_time = None):

        #Order Attributes
        self.order_id = self.generate_order_id(order_car)
        self.order_car = order_car
        self.order_retailer = order_retailer
        self.order_creation_time = order_creation_time


    def __str__(self):
        return f"{self.order_id},{self.order_car},{self.order_retailer} {self.order_creation_time}"


    def generate_order_id(self, car_code):

        # Step 1: You first need to generate a random string of 6 lowercase alphabetic characters;

        letter_order_id = []

        for i in range(0, 6):
            random_letter_order_id = random.choice(Order.list_of_letters)
            letter_order_id += random_letter_order_id

        # Step 2: For every second character in the string (i.e., the 2nd, 4th, 6th, etc. character), convert it into uppercase letter;

        uppercase_letter_order_id = []
        for letter in range(6):
            if letter == 1 or letter == 3 or letter == 5:
                uppercase_letter_order_id.append(letter_order_id[letter].upper())
            else:
                uppercase_letter_order_id.append(letter_order_id[letter])

        string_order_id = "".join(uppercase_letter_order_id)

        # Step 3: For each character in the string from Step 2, get the ASCII code of the letter using ord();
        # Step 4: Step 4: Calculate the ASCII code to the power of 2 for each character and get the remainder of \
        # the powered ASCII code divided by the length of str_1;

        remainder_value = []
        for letter in string_order_id:
            ascii = ord(letter) ** 2
            remainder_ascii = ascii % len(Order.str_1)
            remainder_value.append(remainder_ascii)

        # Step 5: Use the remainder from Step 4 as the index to obtain the corresponding \
        # character from str_1 for each character in Step 2;

        corresponding_char = []
        for i in range(len(remainder_value)):
            char = Order.str_1[remainder_value[i]]
            corresponding_char.append(char)

        test_string = "".join(corresponding_char)

        # Step 6: Append each of the characters from Step 5 n times to the string
        # updated in Step 2. (n is the index of the character in the string
        # from Step 2).

        final_string = ""

        #i needed a number to increment
        position = 0

        for char in test_string:
            final_string = final_string + (char * (position))
            position += 1

        unix_time = int(time.time())

        return f"{final_string}{car_code}{unix_time}"


# Test

# 2.4.3
# order = Order()
# print(order.generate_order_id("JEPVIX1C"))
# Output:~&&!!!$$$$$$$$$JEPVIX1C1695375044



