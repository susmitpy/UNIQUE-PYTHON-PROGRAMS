import random

class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def prepare(self):
        a = "{} of {}".format(self.value, self.suite)
        return a
    
class Deck:
    def build(self):
        cards = []
        self.cards = cards
        for s in ["SPADE", "CLUB", "HEART", "DIAMOND"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v).prepare())

    def show(self):
        print(self.cards)

    def shuffle(self):
        for i in range(1, random.randint(3, 5) + 1):
            random.shuffle(self.cards)
            
    def create_pack(self):
        c =  self.cards
        return c
                 
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        
    def show(self):
        print("{} has {} point(s)".format(self.name, self.points))
    
    def uppoint(self):
        self.points += 1

    def pick(self):
        card_index = int(input("Enter The Card Position You Want To Pick: ")) - 1
        print("Now Guess: ")
        sr = input("Enter The Suites(any 2) Separated By a Space: ").split(" ")
        vr = input("Enter The Value Range separated by a Space (difference should be 6): ").split(" ")
        
        s1, s2  = sr[0].upper(), sr[1].upper()
        v1, v2 = int(vr[0]), int(vr[1])
        pickedS = c[card_index].split(" ")[-1]
        pickedV = int(c[card_index].split(" ")[0])
        print("Picked By You:")
        print(pickedS, pickedV)
        if pickedS == s1 or pickedS == s2:
            for i in range(min(v1, v2), max(v1, v2) + 1):
                if i == pickedV:
                    self.uppoint()
        self.show()




    



