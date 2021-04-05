# concepts

# class.
# self === this

# initialization.

# class Entity() {
#     constructor(x, y) {
#         this.x = x; 
#         this.y = y;
#     }
# }

class Entity:
    def __init__(self, x, y):
        """
            all data members are presumed private
        """
        self.x = x
        self.y = y



e = Entity(10, 1) # e is an instance of the Entity() class

e.x = 23