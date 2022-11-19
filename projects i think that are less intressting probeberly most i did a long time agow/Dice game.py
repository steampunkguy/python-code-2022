import random

class player():
    def __init__(self, name, score):
        self.score = score
        self.name = name

user = ""
p1 = player("", 0)
p2 = player("", 0)

print("this is a 2 player dice game you have 5 rouneds player with highest score winns")

def join(user):
    login = int(input("login(1) or sine up(2): "))
    if login == 2:
       
        username = input("username: ")
        f = open(username, "x")
        password = input("password: ")
        f.write(password)
        user = username + user
    elif login == 1:
   
        username = input("username: ")
        try:
            f = open(username)
            name = username
            pw = f.readline()
            password = input("password: ")
            if pw == password:
                print("in")
                user = username  + user
        except:
            print("thats not a username!")
            quit()
    
def roll(player):
    c = 0
    a = random.randint(1, 6)
    print("you rolled:", a)
    b = random.randint(1, 6)
    print("you rolled:", b)
    if a == b:
        print("DOBBLE ROLL")
        c = random.randint(1, 6)
        print("you rolled:", c)
    r = a + b + c
    print("current score:",r)
    if r % 2 == 0:
        r = r + 10
        print("+10 becouse odd:", r)
    elif r % 2 == 1:
        r = r - 5
        print("-5 becouse odd:", r)
   
    if r <= 0:
        r = 0
   
    player = player + r
    print("your score:",player)

join(p1.name)
join(p2.name)

print(p1.name)
print(p2.name)

for i in range(0,5):
    print(p1.name,"'s go")
    print("")
    roll(p1.score)
    input("press Y for next round: ")
    print(p2.name,"'s go")
    print("")
    roll(p2.score)
    input("press Y for next round: ")
