from room import *
from item import Item as item
from player import *
from parser import *

class game():

    def  __init__(self):
        self.win = False
        self.current_room = None
        self.rooms = []
        self.player = player()
        self.parser = parser()


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

    def sense_route_one(self,strings):
        found = False

        for n in range(0,len(strings)-1):
            if strings[n] in current_room.travel:
                found = True
                    
        if not found:
            for i in range(0,len(strings)-1):
                current = strings[i]+" "+strings[i+1]
                if current in current_room.travel:
                    found = True

        return found

        

    def sense_route_two(self):
        pass

    def sense_item(self, user_input):
        room_items = self.current_room.items

        found = False

        for n in range(0,len(user_input)-1):
            for m in range(0, len(room_items)):
                if user_input[n] == room_items[m].name:
                    found = True
                    
        if not found:
            for i in range(0,len(user_input)-1):
                current = user_input[i]+" " + user_input[i+1]
                for j in range(0, len(room_items)):
                    if current == room_items[j]:
                        found = True

        return found


    def check_availability(self,string):
        check_one = self.parser.sense_travel(string)
        check_two = False
        if check_one:
            pass
            
            
            
        else:
            check_two = self.parser.sense_action(string)

        if not check_one and not check_two:
            print("Command cannot be excecuted due to lack of options: ")


        

    def main(self):
        pass


