from room import *
from game_item import *
from player import *
from game_parser import parser
from logo import show_logo, fancy_output
import os
import time

class game:

    def  __init__(self):
        self.win = False
        self.current_room = None
        self.rooms = []
        self.player = player()
        self.parser = parser()
        self.item_key_unlocks = {"id1":[("Courtyard",["Front door"]),
                                        ("Reception",["Door"]),
                                        ("Waiting room",["Door","Door"]),
                                        ("Hallway",["Door"]),
                                        ("Toilet",["Door"]),
                                        ("Storage closet",["Door"])],
                                 "rk1":[("Courtyard",["Window"])],
                                 "lg1":[("Courtyard",["Window"])],
                                 "sr1":[("Storage closet",["Door"]),
                                        ("Hallway",["Door"]),
                                        ("Toilet",["Door"])]}

        self.item_keys = {"id card":"id1","rock":"rk1","screwdriver":"sr1"}
        self.final_items = ["mop","sunflower kirill","birth certificate","tonail clippings","bucket"]
        
        


    def generate_rooms_items(self):
 
        
        self.rooms.append(room("Courtyard",
                               [item("Rock","rk1", "A large and jagged rock, you might hurt yourself with it if you’re not careful"),
                                item("ID Card","id1", "An ID card, its a bit bent and the picture is faded, but you can see the words “Researcher” and “Access” on it"),
                                item("Large Log","lg1", "A big, mossy log. You can barely carry it"),
                                item("Birth certificate","be1","A tattered old birth certificate for someone called Kirril, with two r's and one l. ")],
                                ["Reception"],
                                {"Reception":["Front door","Window"]},
                                {"Front door": True,"Window": True},
                                {"Front door":"id1","Window":["rk1","lg1"]},
                               """                                    You scope out your location. Seeing the signs of decay all around, you gather that the asylum has been abandoned,
                                    or maybe severly neglected,for quite some time. Prepared to run if necessary.
                                    you start to look around for potential threats and items that may be useful. You see a group of old decaying cars,
                                    which have broken windows and open doors. You can spot an open waste bin further alongdoors.
                                    \n                                    The door appears to be locked and requires some sort of card,
                                    and besides it a window can be reached but is fully intact. You spot some sort of white card
                                    under one of the cars next to some sort of document that seems very official except for the picture of a baby attached to it,
                                    a pile of large logs off to the side, and a massive pile of palm-sized rocks. Maybe something will help you get in?"""))
 
 
        self.rooms.append(room("Waiting room",
                               [item("Flashlight","ft1", "A heavy black flashlight that constantly flickers on and off, maybe it needs new batteries? ")],
                                ["Reception","Storage closet"],
                                {"Reception":["Door"],"Storage closet":["Door"]},
                                {"Door": True,"Door":True},
                                {"Door":["id1","sr1"]},
                               """Upon entering this room you get a cold shiver all over your body, every single chair in the room has been torn apart and thrown around
                                the room, it’s a complete mess.The sun is peeking through the blinds that are withering away.
                                \nThere is only one other exit at the opposite side of the room which appears locked,
                                and a light flickers on and off underneath one of the torn chairs."""
                        ))
        
        
        self.rooms.append(room("Reception",
                               [item("Screwdriver","sr1", "You find an old rusty screwdriver, with a blunt end like it’s been used to puncture something.")],
                                ["Waiting room","Toilet","Hallway"],
                                {"Waiting room":["Door"],"Toilet":["Door"],"Hallway":["Door"]},
                                {"Door": True,"Door":True,"Door":True},
                                {"Door":["id1","sr1"]},
                                """Entering the room, you are greeted with dizzyingly awful stench and a feeling of dread.
                                You barely make out the words “Welcome to Ainsworth Asylum" on a worn out sign located above a dusty wooden counter covered in old
                                leaflets and ripped paper. Time has made sure the writing is illegible.
                                The sound of dripping distracts emanating from there making you gag.
                                You stay away from it. You spot all the open drawers behind the desk, as if someone had left in a hurry.
                                Looking around, you see an old backpack hanging from the coat hook.\nYou can spot a sink behind one of the doors,
                                another door seems to lead to a bigger room
                                with a lot of chairs while the third door leads deeper into the building. There seems to be some
                                kind of tool-box with a couple of items in the backpack, maybe something will help you get in somewhere.
                                Or maybe something will help you light the way."""
			    ))
        
        self.rooms.append(room("Toilet",
                               [item("Toilet Brush","th1", "A dirty yellow toilet brush propped up against the toilet in a cracked holder."),
                                item("Bandage","be1", "An unused bandage is found in an open first aid box that is spilled onto the floor."),
                                item("Toothpaste","te1", "An old and half-filled tube of toothpaste. Minty."),
                                item("Tonail clippings","ts1", "A baggie of small, razor sharp tonail clippings covered in dirt and possibly mold."),
                                ],
                                ["Reception"],
                                {"Reception":["Door"]},
                                {"Door":True},
                                {"Door":["sr1","id1"]},
                               """Going from one awfully smelling room to another, the smell of old, unflushed excrement assault your nostrils.
                                The damp, moldy walls make you cover your nose and mouth to prevent ingesting anything permeating from them.
                                You look down to see a cracked toilet
                                fading into the vegetation growing through the walls. A shine catches your eye, you spot that there is a broken mirror above the sink.\nThe cleaning tools for the toilet are clearly still there, there seems to be some kind of personal hygienekit on one of the broken sinks and a first aid kit lying on the floor, most of the contents unusable, and what seems to be tonails in a bag?"""
			    ))
        
        self.rooms.append(room("Storage closet",
                               [item("Mop","mp1", "A mop. A very wet and stinky mop."),
                                item("Drain Unblocker","dr1", "On the top shelf you find a sealed bottle of drain unblocker."),
                                item("Newspaper","nr1", "A faded yellow newspaper, with water stains ruining the text"),
                                item("Bucket","bt1","A large stainless steel bucket, perfect for any spills you need cleaning up, works well with a mop. ")],
                                ["Waiting room"],
                                {"Waiting room":["Door"]},
                                {"Door":True},
                                {"Door":["sr1","id1"]},
                               """Entering this room is problematic by itself, the cramped room with lots of stuff left to decay over time. Spiders and cockroaches
                        rush out and you try to ignore them as they crawl all over your shoes and hair to get out of the closet.
                        There are no windows, so you can barely make out anything.\nYou can feel some rustling under your foot, as if there were some paper under it.There seems to be some unopened drain unblocker here, along with some cleaning tools. Some of them are wet, not sure you want to know with what. A bucket and mop"""
                            ))


        self.rooms.append(room("Morgue",
                       [item("Lock of hair","lr1","A lock of blonde, straw-like hair, bundled together with a hairband tied up half a dozen times. ")],
                        ["Hallway"],
                        {"Hallway":["Door"]},
                        {"Door":True},
                        {},
                        """Corpses litter the room, some laying on tables while others are simply pilled on top of each other in the corners of the room. If you thought the smell at the reception and the bathroom were bad, the smeel of rotting corpses was quickly changing your mind. They seem almost alive by the movement coming from the exaggerated amount of maggots inside the bodies.\nSome of these seem to have been used for research, or maybe experimentation. There is a surgical table with only a scalp, some hair hanging loosely off of it, and at the other end of the table some small, white crescent shaped objects"""
                    ))

        
        self.rooms.append(room("Hallway",
                               [item("Sunflower Kirill","sl1", "What looks like a normal sundeprived sunflower, you actually discover to be a flower made of tiny Kirill faces.")],
                               ["Reception","Morgue"],
                               {"Reception":["Door"],"Morgue":["Door"]},
                                {"Door":True},
                                {"Door":["sr1","id1"]},
                               """You see a long cold corridor with hard oak floor and dark wallpapered walls. As you step forwards the floor begins to creek.\nBesides the unkept sunflower and the ominous door with the letter "M" on it, there doesn't seem to be much here"""
                                
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
                #print(strings[n],m.lower())
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

                key = self.item_keys[sem_list[m].name.lower()]
                print()
                print()
                #print(sem_list[m].name.lower())
                unlocks = self.item_key_unlocks[key]
                
                for i in unlocks:
                    #print(i[0],self.cap_string(self.current_room.name))
                    if i[0] == self.cap_string(self.current_room.name):
                        #print(self.cap_string(direction),i[1])
                        if self.cap_string(direction) in i[1]:
                            found = True
                            return key,found
                    
                            
            except KeyError:
                print("You cannot use that to open this door! ")

        return key,found
                                
                        


            

    def sense_item(self,string,item_name):
        name = ""
        found = False
        #print(item_name.lower(),string)
        if item_name.lower() in string:
            found = True
        return found
                
        

    def is_item_room(self, user_input):
        room_items = self.current_room.items
        item = ""
        found = False
        
        for item in room_items:
            item_found = self.sense_item(user_input,item.name)
            if item_found:
                found = True
                break
                    
        if not found:
            for i in range(0,len(user_input)-1):
                current = user_input[i]+" " + user_input[i+1]
                for j in range(0, len(room_items)):
                    if current == room_items[j].name.lower():
                        found = True
                        item = room_items[j]
                        break

        return found,item


    def is_item_inventory(self, user_input):

        inv_items = self.player.inv_obj.inv_list
        item = ""
        found = False
        for n in range(0,len(user_input)):
            for m in range(0, len(inv_items)):
                
                if user_input[n] == inv_items[m].name.lower():
                    found = True
                    item = inv_items[m]
                        
        if not found:
            for i in range(0,len(user_input)-1):
                current = user_input[i]+" " + user_input[i+1]
                for j in range(0, len(inv_items)):
                    if current == inv_items[j].name.lower():
                        found = True
                        item = inv_items[j]

        return found,item

    def contains_for_obj(self,item,lis):
        tr = False
        for i in lis:
            
            if i.name.lower() == item:
                tr = True

        return tr
        

    def is_inventory_final(self):
        n = True
        for i in self.final_items:
            
            if self.contains_for_obj(i,self.player.inv_obj.inv_list):
                continue
            else:
                n = False
            
        return n


    #def final_sense():

        
        
            


    def convey_ending(self,room):
        if self.current_room.name == "Hallway" and self.is_inventory_final():
            print("Take a look at the morgue, i think something must've shifted, its no longer wedged shut.")
            if room  == "morgue":
                self.move_player(room)

        if self.current_room.name == "Morgue" and self.is_inventory_final():

            combo = ["tonail clippings","sunflower kirril","birth certificate"]
            print("You stumble into the morgue, there are strange noises coming from the vents, you brush them past you, there is a bucket on the floor. ")
            print("There is a peice of paper on the floor, it says in bold writing, (m+b)/(sk*bc*tc) = SERUM, maybe this is a hint? ")
            print("What do you do? ")
            user_input = self.parser.sentence_to_list(self.parser.remove_punct(str(input(">> "))))
            while not "bucket" in user_input:
                print("That cant be the first part of the formula, try something different? ")
                user_input = self.parser.sentence_to_list(self.parser.remove_punct(str(input(">> "))))
                
            if "bucket" in user_input:
                print("Yes, this seems right... but now what?? ")
                user_input = self.parser.sentence_to_list(self.parser.remove_punct(str(input(">> "))))
                while not "mop" in user_input:
                    print("In the bucket like that?? are you sure??? ")
                    user_input = self.parser.sentence_to_list(self.parser.remove_punct(str(input(">> "))))

                if "mop" in user_input:
                    print("The mop! genius!!, seems like theres only one viable option left... ")
                    user_input = self.parser.sentence_to_list(self.parser.remove_punct(str(input(">> "))))
                    while len(combo) != 0:
                        
                        if len(combo) == 3:
                            print("In the bucket like that?? are you sure??? ")
                        elif len(combo) == 2:
                            
                            print("Yes, getting closer! ")
                        elif len(combo) == 1:
                            print("So close i you can taste it!! ")

                        for i in range(0,len(user_input)-1):
                            print(user_input[i]+" "+user_input[i+1])
                            if (user_input[i]+" "+user_input[i+1]) in combo:
                                combo.remove(user_input[i]+" "+user_input[i+1])
                            
                        user_input = self.parser.sentence_to_list(self.parser.remove_punct(str(input(">> "))))
                        
                                

                    if len(combo) == 0:
                        print("The SERUM IS COMPLETE... CONGRATULATIONS")
                        sys.exit()
                        
                    
                
                

                
                
            
            
            
        



    def check_availability(self,string):
        key_found = False
        key_index = 0
        action_check = False
        drop_action_check = False
        inv_Check = False
 
        travel_check,string = self.parser.sense_travel(string)
        if "inventory" in string:
            inv_Check = True
            self.player.inv_obj.print_inv()
        else:
            
            if travel_check:
     
                direction_check,room = self.sense_route_one(string)
                #print(self.cap_string(self.current_room.name),self.is_inventory_final()),self.cap_string(self.current_room.name),self.is_inventory_final()
                if (self.cap_string(self.current_room.name) == "Hallway" and self.is_inventory_final()) or (self.cap_string(self.current_room.name) == "Morgue" and self.is_inventory_final()):
                    self.convey_ending(room)

                else:
                
                    #print("getting here")
                    if direction_check:
         
                        travel_option_check,direction = self.sense_route_two(string,room)
                        direction = self.cap_string(direction)
                        if travel_option_check:
                            
                            try:
                                if self.current_room.entrances[self.cap_string(direction)]:
                                    
                                    key,found = self.sense_key(string,self.cap_string(direction))
                                    if found:
                                        #print(key,self.current_room.actions,direction)
                                        if key in self.current_room.actions[direction]:
                                            
                                            self.move_player(room)
                                            
                                    else:
                                        print()
                                        print("*** You do not have the required items to open this passway ***")
                                        print()

                                
                                  
                                        
                                    
                                elif not self.current_room.entrances[self.cap_string(direction)]:
                                    print("*** Enter room ***")
                                    self.move_player(room)
                                    
                            except KeyError:
                                print("Such a key either does not exist or cannot be used for this passage")
                        else:
                            print()
                            print("*** Please specify route ***")
                            togo = room.capitalize()
                            options = ""
                            if len(self.current_room.travel_options[togo]) > 1:
                                for t in self.current_room.travel_options[togo]:
                                    options = options + t + ", "
                                options = options[:-2]
                            else:
                                 for t in self.current_room.travel_options[togo]:
                                    options = t
                                    
                            print("*** Your available routes are: " + options + " ***")    
                            print()


                        

                
            else:
                action_check = self.parser.sense_actions(string)
                if action_check:
                    
                    item_check,current_item = self.is_item_room(string)
                    if item_check:
                        check, b, = self.is_item_inventory(string)
                        if check == False:
                            self.player.inv_obj.add_item(current_item,self.current_room)
                            print()
                            print("*** You have now acquired " + str(current_item.name) + " ***")
                            print()
                        else:
                            print()
                            print("*** Your already have that item in your inventory ***")
                            print() 

            
                drop_action_check = self.parser.sense_drop(string)
                if drop_action_check:
                    drop_item_check,current_item = self.is_item_inventory(string)
                    if drop_item_check:
                        print()
                        print()
                        print("You no longer have the item " + str(current_item.name) + "")
                        self.player.inv_obj.remove_item(current_item)
                        self.current_room.items.append(current_item)

                else:
                    investigate_check = self.parser.sense_investigate(string)
                    if investigate_check:
                        self.inspect_item(string)

                    
        if not inv_Check:
            if not travel_check and not action_check and not drop_action_check and not investigate_check:
                print("Command cannot be executed due to lack of options: ")

        inv_Check = False

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
                    if item.name.lower() in current:
                        found = True
                        print(item.description)
                        break
                
        if not found:
            print("Item cannot be inspected")

    def check_endgame(self):
        endgame_item_id = ["Screwdriver", "Mop"]
        number_in_inv = 0
        
        for item in endgame_item_id:
           
            if item.lower() in self.player.inv_obj.inv_list:
                number_in_inv += 1
                
        if number_in_inv == len(endgame_item_id):
            print("endgame title here")
        

    def test(self):
        self.generate_rooms_items()
        
        print()
        print("--------------------------------------")
        print("You are currently in the " + self.current_room.name.upper() + ". --")
        print("--------------------------------------")
        print()
        print(self.current_room.description)
        print()
        
        x = "take id card"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "take birth certificate"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "enter reception through front door"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "take screwdriver"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "enter toilet through door"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "take tonail clippings"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "enter reception through door"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "enter waiting room through door"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "enter storage closet through door"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "take mop"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "take bucket"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "enter waiting room through door"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "enter reception through door"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "enter hallway through door"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        x = "take sunflower kirill"
        self.check_availability(x)
        print(">> "+ x)
        time.sleep(0.08)
        print()
        print()
        
        while True:
            print()
            print("--------------------------------------")
            print("You are currently in the " + self.current_room.name.upper() + ". --")
            print("--------------------------------------")
            print()
            print(self.current_room.description)
            print()
            user_inp = str(input(">> "))
            self.check_availability(user_inp)

           

    def main(self):
        show_logo(), os.system('cls')
        self.generate_rooms_items()
        print("""\nYou direct the car left to join the windy dirt track that will take you to the isolated hills of ##.
The silence and stillness becomes disturbed by the rattling and banging of your beaten car.
Despite the painful noise of your car dying you put your foot down, racing up the track.
Seconds later you arrive at the ##. You speed into the car park and skid to a halt, causing the car to finally cut out.\n\n""")
        #winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        while True:
            print()
            print("--------------------------------------")
            print("You are currently in the " + self.current_room.name.upper() + ". --")
            print("--------------------------------------")
            print()
            print(self.current_room.description)
            print()
            user_inp = str(input(">> "))
            self.check_availability(user_inp)
            self.check_endgame()

game_class = game()

game_class.main()
#game_class.test()
