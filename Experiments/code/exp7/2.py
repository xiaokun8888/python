class Block:
    # Good Luck!
    def __init__(self, a):
        self.width=a[0]
        self.length=a[1]
        self.height=a[2]
        
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.width*self.height*self.length
    
    def get_surface_area(self):
        return 2*(self.width*self.height+self.width*self.length+self.length*self.height)