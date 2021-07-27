class Cloth:
    def __init__(self, size, height):
     self.size = size
     self.height = height

     def coat_square(self):
         return self.size / 6.5 + 0.5

     def suit_square(self):
         return self.height * 2 + 0.3

     @property
     def general_square(self):
         print(f'Общая площадь ткани - {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Cloth):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.coat_sq = (self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани, требующейся на пальто - {self.coat_sq}'

class Suit(Cloth):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.suit_sq = (self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани, требующейся на костюм - {self.suit_sq}'

coat = Coat(3, 5)
suit = Suit(1, 8)
print(coat)
print(suit)
coat.general_square()
suit.general_square()
