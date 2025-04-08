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