def add_wrapping(func):
    def wrapper(*args, **kwargs):
        print("Starting the print_numbers method:")
        result = func(*args, **kwargs)
        print("Finished the print_numbers method.")
        return result
    return wrapper

class PrintNumbers:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @add_wrapping
    def print_numbers(self):
        print("Positional arguments:")
        for arg in self.args:
            print(arg)

        print("Keyword arguments:")
        for key, value in self.kwargs.items():
            print(f"{key}: {value}")

numbers = PrintNumbers(1, 2, 3, a=10, b=20, c=30)

numbers.print_numbers()
