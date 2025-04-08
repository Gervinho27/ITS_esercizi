class Restaurant:
    def __init__(self, name, cuisineType, number_served = 0):
        self.name = name
        self.cuisineType = cuisineType

    def describe_Restaurant(self):
        print(f"Name: {self.name}\nCuisineType: {self.cuisineType}")

    def open_Restaurant(self):
        print("The restaurant is open!")

    def number_served(self, number_served):
        self.number_served = number_served
        print(f"Number of customers served: {self.number_served}")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"Number of customers served: {self.number_served}")

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print(f"Number of customers served: {self.number_served}")
    

restaurant = Restaurant("Pizzeria", "Italiana")
restaurant.describe_Restaurant()
restaurant.open_Restaurant()
restaurant.number_served(0)
restaurant.set_number_served(10)
restaurant.set_number_served(20)
restaurant.increment_number_served(10)
restaurant.increment_number_served(15)