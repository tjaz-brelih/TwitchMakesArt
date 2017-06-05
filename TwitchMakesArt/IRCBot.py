import irc.client
import logging

class IRCBot( irc.client.SimpleIRCClient ):

    def __init__( self, channel, queue, commands, db, password ):
        irc.client.SimpleIRCClient.__init__( self )

        self.channel = channel
        self.queue = queue
        self.commands = commands
        self.db = db
        self.password = password


    def on_welcome( self, connection, event ):
        logging.info( "Connected to IRC server" )
        connection.join( self.channel )


    def on_join( self, connection, event ):
        logging.info( "Connected to IRC channel." )

    def on_disconnect( self, connection, event ):
        self.connect( "irc.chat.twitch.tv", 6667, "twitchmakesart_channel", password = self.password )
        self.start()


    def on_pubmsg( self, connection, event ):
        user = event.source.nick
        message = event.arguments[0]
        
        logging.debug( user + ": " + message )

        # Filtering input
        message = message.lower()
        message = "".join( filter( str.isalpha, message ) )

        if self.commands.get( message ) is not None:
            if self.queue.add( message ):
                logging.debug( "Added to queue: " + message )

                cur = self.db.cursor()
                cur.execute( "INSERT INTO users VALUES (?,?)", (user, message) )
                self.db.commit()