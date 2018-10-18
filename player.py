from inventory import *

class player(room):
    
    def __init__(self):
        self._current_room = None
        self.inv = inventory.items
        self.health = 0
        

    def change_room(self):



        
