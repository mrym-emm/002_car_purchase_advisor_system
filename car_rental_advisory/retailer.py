import random

class Retailer:

    def __init__(self, retailer_id = -1 , retailer_name = None):

        #Retailer Attributes

        if retailer_id == -1:
            retailer_id = self.generate_retailer_id()
        #The above code will automatically generate the retailer ID when value is -1

        self.retailer_id = retailer_id
        self.retailer_name = retailer_name


    def __str__(self):

        # Return the retailer information as a formatted string.
        return f"{self.retailer_id}, {self.retailer_name}"


    def __repr__(self):

        # Not part of task, but used it so objects appear in list (if needed)
        return f"{self.retailer_id}, {self.retailer_name}"


    def generate_retailer_id(self):

        # Generate a randomly generated unique retailer ID that is different from
        # the existing retailer IDs and set it as the retailer_id (8 digits number)
        retailer_id = str(random.randint(1000000, 9999999))
        return retailer_id


# Test

# retailer1 = Retailer(-1,"Bob")
# print(retailer1)
# Output: 2719642, Bob (Random ID)















