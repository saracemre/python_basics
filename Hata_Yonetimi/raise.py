# x = 10

# if x > 5:
#     raise ValueError("x 5'ten buyuk olamaz.")


def colorize(text, color):
    colors = ("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalidir.")

    if type(color) is not str:
        raise TypeError("Renk str tipinde olmalidir.")

    if color not in colors:
        raise ValueError("Gecersiz bir renk ismi.")
    print(f"{text}, {color} renk olarak yazdirildi.")

# colorize('merhaba',10)
colorize('merhaba','blue')
colorize('merhaba','yellow')