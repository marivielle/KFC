from inv import *
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

    def death(self):
        if self.health <= 0:
            self.alive = False
            print("Bit of an issue.. you are dead") #Place holder for a more interesting death message
            return self.alive
    

    def attack(self, weapon, attacker):
        weak_weapons = ["id card", "toilet brush", "bandage", "toothpaste", "newspaper"]
        medium_weapons = ["rock", "mop", "sunflower"]
        strong_weapons = ["large log", "drain unblocker"]
        
        if weapon == "fists":
            fists_dmg = random.randrange(0.5, 4)
            
            print("You hit " + attacker.name + " with " + weapon +
                  " for " + str(firsts_dmg) + " damage!")
            return fists_dmg
        
        elif weapon in weak_weapons:
            weak_dmg = random.randrange(0, 2)
            print("You hit " + attacker.name + " with " + weapon +
                  " for " + str(weak_dmg) + " damage!")
            return weak_dmg
            
        elif weapon in medium_weapons:
            med_dmg = random.randrange(3, 6)
            print("You hit " + attacker.name + " with " + weapon +
                  " for " + str(med_dmg) + " damage!")
            return med_dmg

        elif weapon in strong_weapons:
            strong_dmg = random.randrange(7, 10)
            
            print("You hit " + attacker.name + " with " + weapon +
                  " for " + str(strong_dmg) + " damage!")
            
            return strong_dmg
        
