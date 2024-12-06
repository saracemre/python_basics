# import pdb

# one = 'one'
# two = 'two'
# pdb.set_trace()

# sonuc = one+two

# three = 'three'

# sonuc += three

# print(sonuc)

from pdb import set_trace


def add_numbers(a,b,c):
    import pdb; pdb.set_trace()
    return a+b+c

add_numbers(1,2,3)

# l => list
# n => next line
# p => print
# c => continue