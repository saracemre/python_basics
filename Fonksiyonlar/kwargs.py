# def displayUser(*args):
#     print(type(args))
#     print(args)
# displayUser()

# def displayUser(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# displayUser()

# def displayUser(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#     print('\n')

# displayUser(username = 'Saro', email = 'saro@gmail.com')
# displayUser(username = 'Saro', email = 'saro@gmail.com', country = 'Turkey')


def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1='Value1',key2='Value2')