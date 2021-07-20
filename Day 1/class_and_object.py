# defining class
class Pen:
    def __init__(self,color,cost):
        self.color = color
        self.cost = cost

    def getColor(self):
        print(self.color)
        
    

pen1 = Pen("Blue",20)
pen1.getColor()
