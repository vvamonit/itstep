import random

from Lesson_2 import character
from Lesson_2.character import Character

class Ninja(Character):
    def __init__(self, name, health, damage, defence, evasion_chance =0.25, type='human'):
        Character.__init__(self, name, health, damage, defence, type)
        self.evasion_chance = evasion_chance

    def take_damage(self, damage):
        if random.random() < self.evasion_chance:
            print(f"{self.name} уникнув атаки")
            return
        damage -= self.defence
        if damage < 0:
            damage = 0
        super().take_damage(damage)
    def __str__(self):
        return super().__str__() + f"\nЙмовірне уникнення {self.evasion_chance * 100:.1f}%"
    def attack(self, target):
        target.take_damage(self.damage)