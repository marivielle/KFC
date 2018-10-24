from room import *
from game_item import *
from player import *
from game_parser import parser

class game:

    def  __init__(self):
        self.win = False
        self.current_room = None
        self.rooms = []
        self.player = player()
        self.parser = parser()
        self.item_key_unlocks = {"id1":[("Courtytard",["Front door"]),
                                        ("Reception",["Waiting door","Storage door"])],
                                 "rk1":[("Courtyard",["Window"])],
                                 "lg1":[("Courtyard",["Window"])],
                                 "sr1":[("Storage closet",["Door"])]}


    def generate_rooms_items(self):

        
        self.rooms.append(room("Courtyard",
                               [item("Rock","rk1"),
                                item("ID Card","id1"),
                                item("Large Log","lg1")],
                                ["Reception"],
                                {"Reception":["Front door","Window"]},
                                {"Front door": True,"Window": True},
                                {"Front door":"id1","Window":["rk1","lg1"]}))
        
        self.rooms.append(room("Reception",
                               [item("Screwdriver","sr1"),
                                item("Flashlight","ft1")],
                                ["Waiting room","Storage closet"],
                                {"Waiting room":["Door"],"Storage closet":["Door"]},
                                {"Waiting door": True,"Storage door":True},
                                {"Waiting door":"id1","Storage door":["id1","sr1"]}))
        
        self.rooms.append(room("Toilet",
                               [item("Toilet Brush","th1"),
                                item("Bandage","be1"),
                                item("Toothpaste","te1")],
                                ["Reception"],
                                {"Reception":["Door"]},
                                {"Door":False},
                                {}))
        
        self.rooms.append(room("Storage Closet",
                               [item("Mop","mp1"),
                                item("Drain Unblocker","dr1"),
                                item("Newspaper","nr1")],
                                ["Waiting room"],
                                {"Waiting room":["Door"]},
                                {"Door":True},
                                {"Door":"sr1"}))
        
        
        self.rooms.append(room("Hallway",
                               [item("Sunflower Kirill","sl1")],
                               [None],
                               {None:[None]}))

        
        
        self.current_room = self.rooms[0]


    def return_room_object(self,room_name):
        val = False
        for n in self.rooms:
            if self.cap_string(room_name) == n.name:
                val = n

        return val


    def move_player(self,room_temp):
        room_obj = self.return_room_object(room_temp)
        if type(room_obj) is bool:
            print("You are already in the " + self.current_room.name + ".")
        else:
            self.current_room = room_obj
        

        
    def sense_route_one(self,strings):
        
        found = False
        room = ""

        for n in range(0,len(strings)):
            #print(strings[n],self.current_room.travel)
            for m in self.current_room.travel:
                if strings[n] == m.lower():
                    found = True
                    room = strings[n]
                    
        if not found:
            for i in range(0,len(strings)-1):
                try:
                    current = strings[i]+" "+strings[i+1]
                    if current in self.current_room.travel:
                        found = True
                        room = strings[i]+" "+strings[i+1]
                except IndexError:
                    continue

        
        return found,room

    def cap_string(self,string):

        n = string[1:len(string)]
        p = string[0:1]
        p = p.upper()
        string = p+n

        return string

        

    def sense_route_two(self,strings,direction):

        found = False
        direction_travel  = ""
        direction = self.cap_string(direction)
        for n in range(0,len(strings)):
            if strings[n] in self.current_room.travel_options[direction]:
                found = True
                direction_travel = strings[n]
        
        if not found:
            for i in range(0,len(strings)-1):
                try:
                    current = self.cap_string(strings[i])+" "+strings[i+1]
                    if current in self.current_room.travel_options[direction]:
                        found = self.cap_string(strings[i])+" "+strings[i+1]
                        direction_travel = current
                except IndexError:
                    continue

        return found,direction_travel

    def sense_key(self, string,direction):
        found = False
        key = ""
        sem_list = self.player.inv_obj.create_semantic_list()
        for n in string:
            if n in sem_list:
                for m in range(0,len(inventory)-1):
                    if inventory[m].name == n:
                        try:
                            key = inventory[m].id

                            unlocks = self.item_key_unlocks[key]
                            
                            for i in unlocks:
                                if i[0] == self.current_room.name:
                                    if direction in i[1]:
                                        found = True
                                    
                        except KeyError:
                            pass


        return key
        

    def is_item(self, user_input):
        room_items = self.current_room.items
        item = ""
        found = False
        for n in range(0,len(user_input)):
            for m in range(0, len(room_items)):
                if user_input[n] == room_items[m].name.lower():
                    found = True
                    item = user_input[n]
                    
        if not found:
            for i in range(0,len(user_input)-1):
                current = user_input[i]+" " + user_input[i+1]
                for j in range(0, len(room_items)):
                    if current == room_items[j].name.lower():
                        found = True
                        item = user_input[i]+" " + user_input[i+1]

        return found,item



    def check_availability(self,string):
        key_found = False
        key_index = 0
        travel_check,string = self.parser.sense_travel(string)
        
        if travel_check:
            #print("Travel Check")
            direction_check,room = self.sense_route_one(string)
            
            if direction_check:
                #print("direction Check")
                #print(room)
                travel_option_check,direction = self.sense_route_two(string,room)
                
                if travel_option_check:
                    #print("travel option check")
                    #print(self.current_room.entrances)
                    if self.current_room.entrances[self.cap_string(direction)]:
                        #print("door locked check")
                        
                        key = self.sense_key(string,self.cap_string(direction))
                        
                        
                        if key in self.current_room.actions[direction]:
                            self.move_player(room)
                      
                            
                        
                    else:
                        print("Enter room!")
                        self.move_player(room)

            
        else:
            action_check = self.parser.sense_actions(string)
            if action_check:
                
                item_check,current_item = self.is_item(string)
                if item_check:
                    self.player.inv_obj.add_item(current_item,self.current_room)
                    
                    

        if not travel_check and not action_check:
            print("Command cannot be excecuted due to lack of options: ")


        

    def main(self):
        self.generate_rooms_items()
        while True:
            print()
            print()
            print("You are currently in the " + self.current_room.name + ".")
            print()
            print()
            user_inp = str(input("Please enter string: "))
            self.check_availability(user_inp)

game_class = game()

game_class.main()