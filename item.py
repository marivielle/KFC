class Item():
    def __init__(self, name, description, identification, strength):
        self.name = name
        self.reduce_inv = False #whether the item is large enough to reduce inventory space
        self.description = description #item description
        self.id = identification  #id of item
        self.item_strength = strength #determines the amount of damage left when hitting with this item
