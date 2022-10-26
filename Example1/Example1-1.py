from random import randint

def input_dat(name):
    x = int(input(f"{name}, enter the number of sweets you will take from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, enter the correct amount of sweets: "))
    return x


def p_print(name, k, counter, value):
    print(f"Walked {name}, he took {k}, now he has {counter}. There are {value} sweets lef on the table.")

player1 = input("Enter the name of the first player: ")
player2 = input("Enter the name of the second player: ")
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
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Won {player1}")
else:
    print(f"Won {player2}")