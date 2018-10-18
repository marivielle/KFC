class item():
    def __init__(self, name, description = "", identification):
        self.name = name
        self.reduce_inv = False #whether the item is large enough to reduce inventory space
        self.description = description #item description
        self.id = identification  #id of item
