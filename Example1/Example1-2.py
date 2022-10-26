from random import randint

def input_dat(name):
    x = int(input(f"{name}, enter the number of sweets you will take from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, enter rhe correct amount of sweets: "))
    return x


def p_print(name, k, counter, value):
    print(f"Went {name}, he took {k}, now he has {counter}. There are {value} sweets left on the table.")


def bot_calc(value):
    k = randint(1,28)
    while value-k <= 28 and value > 28:
        k = randint(1,28)
    return k

player1 = input("Enter the name of the first player: ")
player2 = "Bot"
value = int(input("Enter the number of sweets on the table: "))
flag = randint(0,2) # priority flag
if flag:
    print(f"First walks {player1}")
else:
    print(f"First walks {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Won {player1}")
else:
    print(f"Won {player2}")