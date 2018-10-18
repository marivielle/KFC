from room import *

class inventory_obj():

    def __init__(self):
        self.full = False 
        self.inv_list = [] 
        self.capacity = 10
    def check_full(self):

        """Checks if inventory contains more than 10 items, if it does
        it will set the full boolean to true"""
    
        if len(self.inv_list) >= self.capacity: 
            self.full = True


    def add_item(self, item):
        """Adds an item to the inv list IF the inventory is NOT full"""
        #Need to remove items from room when adding to player inventory
        #Large items take up more than one space?
        #Could possibly achieve this by making big items reduce the capacity variable
        self.check_full()
        
        if self.full == False:
            self.inv_list.append(item)
            room.remove(item)
        elif self.full == True:
            print("Your inventory is full!")

    def remove_item(self, item):
        """Removes an item from the inventory list"""
        
        for i in self.inv_list:
            if i == item:
                self.inv_list.remove(i)
                self.check_full()
                

    def print_inv(self):
        """Prints out a list of items for the player"""
        print("\nYou are currently carrying: \n")
        for i in self.inv_list:
            print(i)






        
    
            
            
            
