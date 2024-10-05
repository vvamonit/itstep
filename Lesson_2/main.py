from character import Character

player1 = Character("Vasya", 100, 5, 0)
player1.show_stats()

player2 = Character("Petya", 100, 3, 2)
player2.show_stats()

#player1.attack(player2)
#print(f"\n{player1}\n{player2}\n")

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
#    print(f"\n{player1}\n{player2}\n")
    if player2.is_alive():
       player2.attack(player1)
#       print(f"\n{player1}\n{player2}\n")

print(f"\n{player1}\n{player2}\n")