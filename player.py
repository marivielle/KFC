from inventory import *

class player(room):
    
    def __init__(self):
        self._current_room = None
        self.inv = inventory.items
        self.health = 0
        
    def initialise(self,game_class):
        self.current_room = game_class.rooms[0].name

    def change_room(self):



        
