class room:

    def __init__(self,room_name,items,travel,travel_options,entrances = {},actions = []):
        self.name = room_name
        self.items = items
        self.actions = actions
        self.travel = travel
        self.travel_options = travel_options
        self.player_inside = False
        self.entrances = entrances

    def return_item_id(self,name):
        print(self.items,name)
        for item in self.items:
            print(item.name,name)
            if item.name.lower() == name.lower():
                m = item.id
                return m
           
        
        

    def is_item(self,item_id):
        for item in self.items:
            if item.item_id == item_id:
                return True
            else:
                return False

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)


    def check_action(self,action,item=None):
        if item != None:
            
            for item_unit in self.items:
                if item_unit.item_id == item_id:
                    if action in self.actions:
                        return True
                    
                    else:
                        return False
                    
                else:
                    return False
                
        else:
            if action in self.actions:
                return True
            else:
                return False
            
            

    
        
