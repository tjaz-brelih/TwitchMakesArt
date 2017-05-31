import logging

from queue import Queue, Empty
from random import Random
from builtins import Exception

class AnarchyQueue:
    
    def __init__( self, p ):
        """ p (float : (0,1)): Probability of an adding command to be actualy put in the queue. """

        if p < 0:
            p = 0
        elif p > 1:
            p = 1

        self.p = p
        self.random = Random()
        self.queue = Queue()
        
    def add( self, command ):
        if self.random.uniform( 0, 1 ) <= self.p:
            try:
                self.queue.put_nowait( command )
                return True
            except Exception:
                logging.exception( "AnarchyQueue.add()" )

        return False
            

    def get( self ):
        ret = None
        try:
            ret = self.queue.get()
        except Empty:
            logging.info( "AnarchyQueue is empty." )
        except Exception:
            logging.exception( "AnarchyQueue.get()" )
        return ret