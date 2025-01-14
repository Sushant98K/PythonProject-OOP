class NumberAnalyzer:
    def __init__(self):
        """Initialize with an empty list of numbers."""
        self.__numbers = [] 

    def add_number(self, number):
        """Add a number to the list after validation."""
        if not isinstance(number, (int, float)):
            raise ValueError("Only numbers are allowed.")
        self.__numbers.append(number)

    def remove_number(self, number):
        """Remove a number from the list."""
        if number not in self.__numbers:
            raise ValueError("The number is not in the list.")
        self.__numbers.remove(number)

    def get_numbers(self):
        """Return the current list of numbers."""
        return self.__numbers

    def display_numbers(self):
        """Display the list of numbers."""
        if not self.__numbers:
            return "The list is empty."
        return ", ".join(map(str, self.__numbers))

    def sort_numbers(self, reverse=False):
        """Sort the numbers in ascending (default) or descending order."""
        self.__numbers.sort(reverse=reverse)
        return self.__numbers

    def sum_numbers(self):
        """Calculate and return the sum of all numbers in the list."""
        return sum(self.__numbers)

    def clear_numbers(self):
        """Clear all numbers from the list."""
        self.__numbers.clear()