class User:
    """A user of the store."""

    def __init__(self, name, password):
        """Initialise data for user."""
        self._name = name
        self._password = password
        self._logged_in = False

    def login(self, password):
        """Check password and log user in."""
        if password == self._password:
            self._logged_in = True
            print("Login successful.")
        else:
            print("Incorrect password.")

    def show_status(self):
        """Print the status of the user."""
        if self._logged_in:
            print(f"{self._name} is logged in.")
        else:
            print(f"{self._name} is NOT logged in.")


customer = User(
    name = "Lewis",
    password = "Reading2012"
)

customer.login("Reading2012")
customer.show_status()


class Admin(User):
    """Administrator of the store."""

    def __init__(self, name, password, staff_id):
        """Initialise data for a store admin."""
        super().__init__(name, password)
        self._staff_id = staff_id
    

    def add_product(self, name):
        """Add a new product to the inventory."""
        if self._logged_in:
            print(f"{self._name} ({self._staff_id}) added product: {name}.")
        else:
            print("Login to add product.")


staff1 = Admin(
    name = "Lewis",
    password = "Yes Sir",
    staff_id= 1234
)

staff1.add_product("Coffee")
staff1.login("Yes Sir")
staff1.add_product("Tea")
