class Student:
    """Represents a student."""

    def __init__(self, name):
        """Initialise data."""
        self._name = name
        self._results = {}
    
    def _calc_predicted_result(self):
        """Calculate the students predicted results."""
        results = self._results.values()
        return sum(results) / len(results)
    
    def add_result(self, year, result):
        """Add result for student."""
        self._results[year] = result
    
    def dispay_predicted_result(self):
        """Display predicted result."""
        result = round(self._calc_predicted_result(), 1)
        print(f"Student {self._name} is predicted: {result}.")


s = Student("One")

s.add_result(2020, 91)
s.add_result(2019, 78)
s.add_result(2018, 82)

s.dispay_predicted_result()