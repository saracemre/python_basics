def dec_kacKere(count):
    def kacKere(fn):
        def wrapper_kacKere(*args, **kwargs):
            for _ in range(count):
                fn(*args, **kwargs)
        return wrapper_kacKere
    return kacKere

@dec_kacKere(count=2)
def hello():
    print('hello')

@dec_kacKere(count=5)
def greet(name):
    print('hello ' + name)

hello()
greet('Emre')
