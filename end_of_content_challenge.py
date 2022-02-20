class SmartJug:
    """Jug that tracks the percentage of its contents."""
    
    def __init__(self):
        """Initialises the jug object and contents."""
        self.contents = 100
        
    
    def fill(self):
        """Refills the jug to 100%."""
        self.contents = 100
    
    def pour(self):
        """Pours out 25% of jug."""
        if self.contents == 0:
            print("Sorry, this jug is empty!")
        else:
            self.contents -= 25
            print("Pouring...")
            if self.contents == 0:
                print("You emptied the jug, please refill me.")
    
    def display_contents(self):
        print(f"The jug is {self.contents}% full.")

jug = SmartJug()

for _ in range(5):
    jug.pour()

jug.fill()

jug.display_contents()

for _ in range(3):
    jug.pour()
    jug.display_contents()
    
