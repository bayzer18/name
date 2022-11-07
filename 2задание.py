class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
        print('I am climbing the tree')

mk1 = Monkey()
print(mk1.max_age)
print(mk1.loves_bananas)
mk1.climb()

mk2 = Monkey()
print(mk2.max_age)
print(mk2.loves_bananas)
mk2.climb()