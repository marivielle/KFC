import time
import random


class NPC():
    def __init__(self, trigger_item, speech = "", name = ""):
        self.name = name
        self.trigger_item = trigger_item
        self.speech = speech
        self.health = 20

    def deliver_speech(self):
        print("\nThe patient runs towards you intent on attacking you")
        time.sleep(2)
        print("but when they get closer, they recognise an item you have.")
        time.sleep(2)
        print("\nIt used to belong to them. Remembering themselves, they tell you:")
        print(self.speech)

    def attack(self):
        print("\nThe patient runs towards you intent on attacking you")
        #10% of the time 40-60 damage
        #20% of the time 30 - 40
        #30 % of the time 20 - 30
        #40 % of the time 10 - 20
        if self.health <= 5:
            print("but they're too injured")
            return 0
        else:
            damage_dealt = random.randint(10,50)

            return damage_dealt

    def decide_action(self, player_inv):
        if self.trigger_item in player_inv:
            self.deliver_speech()
            return 0
        else:
            damage = self.attack()
            return damage
