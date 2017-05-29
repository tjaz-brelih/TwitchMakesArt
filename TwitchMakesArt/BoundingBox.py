class BoundingBox:

    def __init__( self, left, right, top, bottom ):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


    def isMouseIn( self, mouse ):
        return mouse[0] >= self.left and mouse[0] <= self.right and mouse[1] >= self.top and mouse[1] <= self.bottom


    def closestInside( self, mousePos ):
        """ Returns the closest position that is still in the box. """

        x = mousePos[0]
        y = mousePos[1]

        if x < self.left:
            x = self.left
        elif x > self.right:
            x = self.right

        if y < self.top:
            y = self.top
        elif y > self.bottom:
            y = self.bottom

        return (x, y)
            