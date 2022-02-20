class Car:
    """Represents a car object."""
 
    def __init__(self, color, make, model, miles=0):
        """Set initial details of car."""
        self.color = color
        self.make = make
        self.model = model
        self.miles = miles

    def add_miles(self, miles):
        """Increase miles by given number."""
        self.miles += miles
    
    def display_miles(self):
        """Print the current miles value."""
        print(
            f"{self.make} {self.model} ({self.color}) "
            f"has driven {self.miles} miles."
        )


astra = Car("Red", "Vauxhall", "Astra")

astra.display_miles()
astra.add_miles(100)
astra.display_miles()
print(astra.model)


prius = Car("Blue", "Toyota", "Prius", 1000)

prius.display_miles()
prius.add_miles(5000)
prius.display_miles()