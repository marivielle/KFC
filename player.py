from inventory import *
from NPC import *
import random
class player():
    
    def __init__(self):
        
        self.inv = inventory.items
        self.health = 100
        self.alive = True

    def heal(self):
        
        if self.health < 100:
            if "bandage" in self.inv:
                self.health + random.randrange(8, 36)
    
    def print_health(self):
        
        print("Player Health: " + self.health)

    

    def attack(self, weapon):
        weak_weapons = ["id card", "toilet brush", "bandage", "toothpaste", "newspaper"]
        medium_weapons = ["rock", "mop", "sunflower"]
        strong_weapons = ["large log", "drain unblocker"]
        
        if weapon == "fists":
            fists_dmg = random.randrange(0.5, 4)
            
            print("You hit " + NPC.name + " with " + weapon +
                  " for " + firsts_dmg + "damage!")
        
        elif weapon in weak_weapons:
            weak_dmg = random.randrange(0, 2)
            print("You hit " + NPC.name + " with " + weapon +
                  " for " + weak_dmg + "damage!")
            return weak_dmg
            
        elif weapon in medium_weapons:
            med_dmg = random.randrange(3, 6)
            print("You hit " + NPC.name + " with " + weapon +
                  " for " + med_dmg + "damage!")
            return med_dmg

        elif weapon in strong_weapons:
            strong_dmg = random.randrange(7, 10)
            
            print("You hit " + NPC.name + " with " + weapon +
                  " for " + strong_dmg + "damage!")
            
            return strong_dmg
        
