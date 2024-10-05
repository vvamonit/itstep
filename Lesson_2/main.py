#from Lesson_2.character import Character
from Lesson_3.ninja import Ninja
#from Lesson_3.paladin import Paladin
from Lesson_3.berserk import Berserk


player1 = Berserk("Vasya", 100, 15, 0)
print(player1)

#player2 = Paladin("Petya", 100, 20, 4)
#print(player2)

player3 = Ninja("Orest", 100, 18, 0)
print(player3)
#player1.attack(player2)
#print(f"\n{player1}\n{player2}\n")

#while player1.is_alive() and player2.is_alive():
#    player1.attack(player2)
#    print(f"\n{player1}\n{player2}\n")
#    if player2.is_alive():
#       player2.attack(player1)
#       print(f"\n{player1}\n{player2}\n")

#print(f"\n{player1}\n{player2}\n")

while player1.is_alive() and player3.is_alive():
    player1.attack(player3)
#    print(f"\n{player1}\n{player2}\n")
    if player3.is_alive():
       player3.attack(player1)
#       print(f"\n{player1}\n{player2}\n")

print(f"\n{player1}\n{player3}\n")