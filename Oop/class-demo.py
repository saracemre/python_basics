class Comment():
    def __init__(self, username, text, likes, dislikes):
        self._username = username
        self._text = text
        self._likes = likes
        self._dislikes = dislikes

comment1 = Comment('EmreSarac', 'Abi adamsin', 27, 3)
comment2 = Comment('BeyzaSarac', 'Disciyim', 36, 6)
comment3 = Comment('ElifSarac', 'Sacma video', 9, 32)
comment4 = Comment('MustafaSarac', 'Etkileyici!', 123, 12)

comments = [comment1, comment2, comment3, comment4]

for a in comments:
    print(a._username, a._text, a._likes, a._dislikes)