import time

class NPC():
    def __init__(self, trigger_item, speech):
        self.trigger_item = trigger_item
        self.speech = speech

    def deliver_speech(self):
        print("\nThe patient runs towards you intent on attacking you")
        time.sleep(2)
        print("but when they get closer, they recognise an item you have.")
        time.sleep(2)
        print("\nIt used to belong to them. Remembering themselves, they tell you:")
        print(self.speech)

    def attack(self):
        print("\nThe patient runs towards you intent on attacking you")


    def decide_action(self, player_inv):
        if trigger_item in player_inv:
            self.deliver_speech()
        else:
            self.attack()

