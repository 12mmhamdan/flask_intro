def my_decorator(func):
    def wrapper():
        print('This is happening before the function is called')
        func()
        print('this is happening after the function is called')
    return wrapper

def say_hello():
    print('Hello how are you today')

say_hello = my_decorator(say_hello)

say_hello()
say_hello()

print('-' * 100)

@my_decorator
def say_goodbye():
    print('Goodbye, see you later!')

say_goodbye()