import irc.client
import logging

class IRCBot( irc.client.SimpleIRCClient ):

    def __init__( self, channel, queue, commands ):
        irc.client.SimpleIRCClient.__init__( self )

        self.channel = channel
        self.queue = queue
        self.commands = commands


    def on_welcome( self, connection, event ):
        logging.info( "Connected to IRC server" )
        connection.join( self.channel )


    def on_join( self, connection, event ):
        logging.info( "Connected to IRC channel." )


    def on_pubmsg( self, connection, event ):
        user = event.source.nick
        message = event.arguments[0]
        
        #print( user, message )

        # Filtering input
        message.lower()
        message = "".join( filter( str.isalpha, message ) )

        if self.commands.get( message ) is not None:
            self.queue.add( message )

        #TODO write user in database