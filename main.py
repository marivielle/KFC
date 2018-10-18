from room import *
from item import item

class game():

    def  __init__(self):
        self.win = False
        self.current_room = None
        self.rooms = []
        self.player = Player()


    def generate_rooms_items(self):
        self.rooms.append(room("Courtyard",
                               [item("Rock","rk1"),
                                item("ID Card","id1"),
                                item("Large Log","lg1")],
                               ["Reception"],
                               {"Reception":["Front door","Window"]}))
        
        self.rooms.append(room("Reception",
                               [item("Screwdriver","sr1"),
                                item("Flashlight","ft1")],
                                ["Waiting Room","Storage Closet"],
                                {"Waiting Room":["Door"],"Storage Closet":["Door"]}))
        
        self.rooms.append(room("Toilet",
                               [item("Toilet Brush","th1"),
                                item("Bandage","be1"),
                                item("Toothpaste","te1")],
                                ["Reception"],
                                {"Reception":["Door"]}))
        
        self.rooms.append(room("Storage Closet",
                               [item("Mop","mp1"),
                                item("Drain Unblocker","dr1"),
                                item("Newspaper","nr1")],
                                ["Waiting Room"],
                                {"Waiting Room":["Door"]}))
        
        self.rooms.append(room("Hallway",
                               [item("Sunflower Kirill","sl1")],
                               [None],
                               {None:[None]}))

        
        
        self.current_room = self.rooms[0]


    def move_player(self,room):
        for n in self.rooms:
            if room.name == n.name:
                self.current_room = room
            else:
                print("Such a room does not exist. ")



    def check_availability(self,string):


        

    def main(self):
