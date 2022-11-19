import random

class question:
    def __init__(self, anser, looks,):
        self.anser = anser
        self.looks = looks

    def looks(self):
        useagetype = random.randint(1, 4)

        if useagetype = 


    def questionlooks(self):
        n = random.randint(1, 4)

        if n == 1:
            print("what  is the anser to ", self.looks, " :")
            print("a, ", self.anser)
            print("b, ", self.anser + random.randint(-100, 100))
            print("c, ", self.anser + random.randint(-100, 100))
            print("d, ", self.anser + random.randint(-100, 100))
            ans = int(input("anser:"))
            if ans == self.anser:
                print("CORRECT!")
            else:
                print("WRONGE!")

        if n == 2:
            print("what  is the anser to ", self.looks, " :")
            print("a, ", self.anser + random.randint(-100, 100))
            print("b, ", self.anser)
            print("c, ", self.anser + random.randint(-100, 100))
            print("d, ", self.anser + random.randint(-100, 100))
            ans = int(input("anser:"))
            if ans == self.anser:
                print("CORRECT!")
            else:
                print("WRONGE!")

        if n == 3:
            print("what  is the anser to ", self.looks, " :")
            print("a, ", self.anser + random.randint(-100, 100))
            print("b, ", self.anser + random.randint(-100, 100))
            print("c, ", self.anser)
            print("d, ", self.anser + random.randint(-100, 100))
            ans = int(input("anser:"))
            if ans == self.anser:
                print("CORRECT!")
            else:
                print("WRONGE!")

        if n == 4:
            print("what  is the anser to ", self.looks, " :")
            print("a, ", self.anser + random.randint(-100, 100))
            print("b, ", self.anser + random.randint(-100, 100))
            print("c, ", self.anser + random.randint(-100, 100))
            print("d, ", self.anser)
            ans = int(input("anser:"))
            if ans == self.anser:
                print("CORRECT!")
            else:
                print("WRONGE!")
