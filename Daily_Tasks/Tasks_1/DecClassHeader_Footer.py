class HeaderDecorator:
    def __init__(self, header_msg):
        self.header_msg = header_msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(self.header_msg)
            return func(*args, **kwargs)
        return wrapper

class FooterDecorator:
    def __init__(self, footer_msg):
        self.footer_msg = footer_msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(self.footer_msg)
            return result
        return wrapper

@HeaderDecorator("This is the Header")
@FooterDecorator("This is the Footer")
class PrintMessage:
    def __init__(self, message):
        self.message = message

    def __call__(self):
        print(self.message)

print_message = PrintMessage("This is the message.")
print_message()
