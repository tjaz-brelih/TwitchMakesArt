import win32api, win32con
from BoundingBox import *
from functools import reduce


def main():

    boxes = []
    boxes.append( BoundingBox( 2, 1156, 140, 791  ))    # Canvas
    boxes.append( BoundingBox( 310, 1020, 50, 139 ))    # Toolbar

    prevBox = 0

    while True:
        mousePos = win32api.GetCursorPos()
        mousePosNew = mousePos

        isMouseInBox = False
        for box in boxes:
            isMouseInBox = isMouseInBox or box.isMouseIn( mousePos )
        
        if not isMouseInBox:
            mousePosNew = boxes[ prevBox ].closestInside( mousePos )

        for i in range( len( boxes ) ):
            if boxes[i].isMouseIn( mousePos ):
                prevBox = i
        
        win32api.SetCursorPos( mousePosNew )
        print( mousePos, mousePosNew )


if __name__ == "__main__":
    main()