import win32api, win32con
import logging

from threading import Thread

from BoundingBox import *
from AnarchyQueue import *


def main():

    #
    # BOUNDING BOXES
    #
    boxes = []
    boxes.append( BoundingBox( 2, 1156, 140, 791  ))    # Canvas
    boxes.append( BoundingBox( 310, 1020, 50, 139 ))    # Toolbar

    prevBox = 0


    #
    # COMMANDS
    #
    mouseMovement = 10

    commands = { "left":    lambda x: ( x[0] - mouseMovement, x[1] ), \
                 "right":   lambda x: ( x[0] + mouseMovement, x[1] ), \
                 "up":      lambda x: ( x[0], x[1] - mouseMovement ), \
                 "down":    lambda x: ( x[0], x[1] + mouseMovement ), \
                 "click":   lambda x: win32api.mouse_event( win32con.MOUSEEVENTF_LEFTDOWN, x[0], x[1], 0, 0 ), \
                 "release": lambda x: win32api.mouse_event( win32con.MOUSEEVENTF_LEFTUP,   x[0], x[1], 0, 0 ) }

    #
    # OTHER
    #
    queue = AnarchyQueue( 0.9 )


    #
    # LOGGING
    #
    logging.basicConfig( filename = "logs\\twitchmakesart.log", filemode = "w", level = logging.INFO, format = "%(asctime)s %(levelname)s: %(message)s" )
    logging.info( "Application started." )

    
    #
    # THREADING
    #
    # We create a new thread dedicated to reading the Twitch chat and adding commands to the queue.
    threadCommand = Thread( target = commandGetter, args=(queue,) )
    threadCommand.daemon = True
    threadCommand.start()


    #
    # MAIN LOOP
    #
    while True:
        mousePos = win32api.GetCursorPos()

        nextCommand = queue.get()

        # In this case the queue is empty
        if nextCommand is None:
            continue

        func = commands.get( nextCommand )
        if func is not None:
            ret = func( mousePos )

            # Click and Release commands return None, therefore we have to check
            if ret is not None:
                mousePos = ret


        #
        # MOUSE CONTROL
        #
        isMouseInBox = False
        for box in boxes:
            isMouseInBox = isMouseInBox or box.isMouseIn( mousePos )
        
        if not isMouseInBox:
            mousePos = boxes[ prevBox ].closestInside( mousePos )

        # We need to know which bounding box to use when returning the mouse from out-of-bounds
        for i in range( len( boxes ) ):
            if boxes[i].isMouseIn( mousePos ):
                prevBox = i
        

        win32api.SetCursorPos( mousePos )



def commandGetter( q ):
    logging.info( "Command getter thread started." )

    # Get next input
    c = input( "" )

    # Filtering input
    c.lower()
    c = "".join( filter( str.isalpha, c ) )

    q.add( c )


if __name__ == "__main__":
    main()