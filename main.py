from room import *
from game_item import *
from player import *
from game_parser import parser
from logo import show_logo, fancy_output
import os

class game:

    def  __init__(self):
        self.win = False
        self.current_room = None
        self.rooms = []
        self.player = player()
        self.parser = parser()
        self.item_key_unlocks = {"id1":[("Courtyard",["Front door"]),
                                        ("Reception",["Door"]),
                                        ("Waiting room",["Door","Door"])],
                                 "rk1":[("Courtyard",["Window"])],
                                 "lg1":[("Courtyard",["Window"])],
                                 "sr1":[("Storage closet",["Door"])]}

        self.item_keys = {"id card":"id1","rock":"rk1","screwdriver":"sr1"}

        
        


    def generate_rooms_items(self):
 
        
        self.rooms.append(room("Courtyard",
                               [item("Rock","rk1"),
                                item("ID Card","id1"),
                                item("Large Log","lg1")],
                                ["Reception"],
                                {"Reception":["Front door","Window"]},
                                {"Front door": True,"Window": True},
                                {"Front door":"id1","Window":["rk1","lg1"]},
                               """You scope out your location. Seeing the signs of decay all around, you gather that ## has been abandoned, or maybe severly neglected, for quite some time.
                                Prepared to run if necessary. you start to look around for potential threats and items that may be useful. You see a group of old decaying cars, which have broken windows and open doors. You can spot an open waste bin further along"""))
 
 
        self.rooms.append(room("Waiting room",
                               [item("Flashlight","ft1")],
                                ["Reception","Storage closet"],
                                {"Reception":["Door"],"Storage closet":["Door"]},
                                {"Door": True,"Door":True},
                                {"Door":["id1","sr1"]}
                        ))
        
        
        self.rooms.append(room("Reception",
                               [item("Screwdriver","sr1")],
                                ["Waiting room","Toilet"],
                                {"Waiting room":["Door"],"Toilet":["Door"]},
                                {"Door": True,"Door":True},
                                {"Door":["id1","sr1"]},
                """Entering the room, you are greeted with dizzyingly awful stench and a feeling of dread. You barely make out the words “Welcome to ##" on a worn out sign located above a dusty wooden counter covered in old leaflets and ripped paper. Time has made sure the writing is illegible. The sound of dripping distracts emanating from there making you gag. You stay away from it.
                                You spot all the open drawers behind the desk, as if someone had left in a hurry. Looking around, you see an old backpack hanging from the coat hook."""
                ))
        
        self.rooms.append(room("Toilet",
                               [item("Toilet Brush","th1"),
                                item("Bandage","be1"),
                                item("Toothpaste","te1")],
                                ["Reception"],
                                {"Reception":["Door"]},
                                {"Door":False},
                                {},
                """Going from one awfully smelling room to another, the smell of old, unflushed excrement assault your nostrils. The damp, moldy walls make you cover your nose and mouth to prevent ingesting anything permeating from them. You look down to see a cracked toilet fading into the vegetation growing through the walls. A shine catches your eye, you spot that there is a broken mirror above the sink. 
                                """
                ))
        
        self.rooms.append(room("Storage closet",
                               [item("Mop","mp1"),
                                item("Drain Unblocker","dr1"),
                                item("Newspaper","nr1")],
                                ["Waiting room"],
                                {"Waiting room":["Door"]},
                                {"Door":True},
                                {"Door":"sr1"}
                            ))
        
        
        self.rooms.append(room("Hallway",
                               [item("Sunflower Kirill","sl1")],
                               [None],
                               {None:[None]},
                                {},
                [],
                """You see a long cold corridor with hard oak floor and dark wallpapered walls. You step forwards  the floor begins to creek.
                                """
                ))
 
        
        
        self.current_room = self.rooms[0]


    def return_room_object(self,room_name):
        val = False
        for n in self.rooms:
            if room_name == n.name.lower():
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
            
            for m in self.current_room.travel:
                if strings[n] == m.lower():
                    found = True
                    room = strings[n]
                    
        if not found:
            for i in range(0,len(strings)-1):

                
                current = self.cap_string(strings[i])+" "+strings[i+1]
                #print(current,self.current_room.travel)
                if current in self.current_room.travel:
                    found = True
                    room = strings[i]+" "+strings[i+1]

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
            #print(self.cap_string(strings[n]) + "   "  +str(self.current_room.travel_options[direction]))
            if self.cap_string(strings[n]) in self.current_room.travel_options[direction]:
                found = True
                direction_travel = strings[n]
        
        if not found:
            for i in range(0,len(strings)-1):
                
                current = self.cap_string(strings[i])+" "+strings[i+1]
                #print(current,self.current_room.travel_options[direction])
                if current in self.current_room.travel_options[direction]:
                    found = True
                    direction_travel = current
            

        return found,direction_travel

    def sense_key(self, string,direction):
        found = False
        key = ""
        sem_list = self.player.inv_obj.inv_list
        
        for m in range(0,len(sem_list)):
            try:
                key = self.item_keys[sem_list[m]]
                print(key)
                unlocks = self.item_key_unlocks[key]
                
                for i in unlocks:
                    print(i[0],self.cap_string(self.current_room.name))
                    if i[0] == self.cap_string(self.current_room.name):
                        print(self.cap_string(direction),i[1])
                        if self.cap_string(direction) in i[1]:
                            found = True
                            
            except KeyError:
                print("You cannot use that to open this door! ")
                                
                        


        return key,found
        

    def is_item_room(self, user_input):
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


    def is_item_inventory(self, user_input):

        inv_items = self.player.inv_obj.inv_list
        item = ""
        found = False
        for n in range(0,len(user_input)):
            if user_input[n] in inv_items:
                found = True
                item = user_input[n]
                    
        if not found:
            for i in range(0,len(user_input)-1):
                current = user_input[i]+" " + user_input[i+1]
                if current in inv_items:
                    found = True
                    item = current

        return found,item



    def check_availability(self,string):
        key_found = False
        key_index = 0
 
        travel_check,string = self.parser.sense_travel(string)
 
        if travel_check:
 
            direction_check,room = self.sense_route_one(string)
            print(room)
            if direction_check:
 
                travel_option_check,direction = self.sense_route_two(string,room)
                direction = self.cap_string(direction)
                if travel_option_check:
                    
                    
                    if self.current_room.entrances[self.cap_string(direction)]:
                        
                        key,found = self.sense_key(string,self.cap_string(direction))
                        if found:
                            if key in self.current_room.actions[direction]:
                                
                                self.move_player(room)
                                
                        else:
                            print()
                            print("You do not have the required items to open this passway -- ")
                            print()
                      
                            
                        
                    elif not self.current_room.entrances[self.cap_string(direction)]:
                        print("Enter room!")
                        self.move_player(room)

                    

            
        else:
            action_check = self.parser.sense_actions(string)
            if action_check:
                
                item_check,current_item = self.is_item_room(string)
                if item_check:
                    self.player.inv_obj.add_item(current_item,self.current_room)
                    print()
                    print()
                    print("You have now aqcuired " + str(current_item))

        
            drop_action_check = self.parser.sense_drop(string)
            if drop_action_check:
                drop_item_check,current_item = self.is_item_inventory(string)
                if drop_item_check:
                    print()
                    print()
                    print("You no longer have the item " + str(current_item) + "")

            else:
                investigate_check = self.parser.sense_investigate(string)
                if investigate_check:
                    self.inspect_item(string)

                    

        if not travel_check and not action_check and not drop_action_check and not investigate_check:
            print("Command cannot be excecuted due to lack of options: ")

    def inspect_item(self, user_input):
        found = False
        item = ""
        

        for item in self.current_room.items:
            for pos in range(0,len(user_input)-1):
                current = user_input[pos] + " " + user_input[pos+1]
                if item.name.lower() in current:
                    found = True
                    print(item.description)
                    break
            
            
        if not found:
            for room in self.current_room.travel:
                for entrance in self.current_room.travel_options[room]:
                    if entrance.lower() in user_input:
                        print("I don't know where the entryway descriptions are stored soz")
                        found = True
                        break
        if not found:
            for item in self.player.inv_obj.inv_list:
                for pos in range(0,len(user_input)-1):
                    current = user_input[pos] + " " + user_input[pos+1]
                    if item.lower() in current:
                        found = True
                        print(item.description)
                        break
                
        if not found:
            print("Item cannot be inspected")

    def check_endgame(self):
        endgame_item_id = ["sl1", "mp1"]
        for item in endgame_item_id:
            #for inv_item in self.player.inv
            pass

        

    def main(self):
        show_logo(), os.system('cls')
        self.generate_rooms_items()
        fancy_output("""\nYou direct the car left to join the windy dirt track that will take you to the isolated hills of ##.\nThe silence and stillness becomes disturbed by the rattling and banging of your beaten car.\nDespite the painful noise of your car dying you put your foot down, racing up the track.\nSeconds later you arrive at the ##. You speed into the car park and skid to a halt, causing the car to finally cut out.""")
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
