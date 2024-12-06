def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def hello():
    print('hello')

hello()

@do_twice
def greet(msg):
    print('hello ' + msg)

greet('Emre')
