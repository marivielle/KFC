class room(name,items,actions):

    def __init__(self):
        self.room_name = name
        self.items = items
        self.actions = actions
        self.player_inside = False

    def is_item(item_id):
        for item in self.items:
            if item.item_id == item_id:
                return True
            else:
                return False

    def add_item(item):
        self.items.append(item)

    def remove_item(item):
        self.items.remove(item)

    def check_action(action,item=None):
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
            
            

    
        
