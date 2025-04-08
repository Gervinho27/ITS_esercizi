#Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
class Restaurant:
    def __init__(self, name, cuisineType):
        self.name = name
        self.cuisineType = cuisineType

    def describe_Restaurant(self):
        print(f"Name: {self.name}\nCuisineType: {self.cuisineType}")

    def open_Restaurant(self):
        print("The restaurant is open!")

restaurant = Restaurant("Pizzeria", "Italiana")
restaurant.describe_Restaurant()
restaurant.open_Restaurant()

print("-------------------")

restaurant2 = Restaurant("Ristorante", "Mexican")
restaurant2.describe_Restaurant()

print("-------------------")

restaurant3 = Restaurant("FastFood", "American")
restaurant3.describe_Restaurant()