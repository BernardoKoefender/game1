import Tkinter
import threading
import time

G_WIDTH             = 800
G_HEIGHT            = 800
PLAYER_SIZE         = 20
PLAYER_START_WIDTH  = 50
PLAYER_START_HEIGHT = 50
DISPLACEMENT_SPEED  = 1
G_THEME_COLOR       = 'goldenrod' # http://wiki.tcl.tk/37701

class playWindow( Tkinter.Tk ):

    def __init__( self ):
        Tkinter.Tk.__init__( self )

        self.geometry( "800x800" )
        self.resizable( 0, 0 )
        self.protocol( 'WM_DELETE_WINDOW', self.killProgram2 )

        self.closeAll = False

        self.mainFrame = Tkinter.Frame( self, bg = 'white', height = G_HEIGHT, width = G_WIDTH )
        self.mainFrame.pack_propagate( False )
        self.mainFrame.pack()

        self.canvasMain = Tkinter.Canvas( self.mainFrame, height = G_HEIGHT, width = G_WIDTH, bg = 'black' )
        self.canvasMain.pack()

        self.borderRectangle = self.canvasMain.create_rectangle( 10, 10, G_HEIGHT-10, G_WIDTH -10, tags = ( "border" ), outline = 'white' )

        S_C1X = PLAYER_START_WIDTH
        S_C1Y = PLAYER_START_HEIGHT
        S_C2X = PLAYER_START_WIDTH  + PLAYER_SIZE
        S_C2Y = PLAYER_START_HEIGHT + PLAYER_SIZE


        self.playerRectangle = self.canvasMain.create_rectangle( S_C1X, S_C1Y, S_C2X, S_C2Y , tags = ( "player" ), outline = 'white', fill = G_THEME_COLOR )


        self.playerIsMoving               = False
        self.playerPresentMovingDirection = 'still'
        self.playerFutureMovingDirection  = 'still'
        self.playerDisplcementX           = 0
        self.playerDisplcementY           = 0

        self.bind( "<Up>",     self.pressUpEvent    )
        self.bind( "<Right>",  self.pressRightEvent )
        self.bind( "<Down>",   self.pressDownEvent  )
        self.bind( "<Left>",   self.pressLeftEvent  )
        self.bind( "<Escape>", self.killProgram     )

        self.playerThread = playerThread( self )
        self.playerThread.start()


    def killProgram( self, event ):
        self.closeAll = True
        self.destroy()
    def killProgram2( self ):
        self.closeAll = True
        self.destroy()


    def pressUpEvent( self, event ):
        if self.playerIsMoving:
            self.playerFutureMovingDirection  = 'up'
        else:
            self.playerPresentMovingDirection = 'up'
            self.playerIsMoving = True


    def pressRightEvent( self, event ):
        if self.playerIsMoving:
            self.playerFutureMovingDirection  = 'right'
        else:
            self.playerPresentMovingDirection = 'right'
            self.playerIsMoving = True


    def pressDownEvent( self, event ):
        if self.playerIsMoving:
            self.playerFutureMovingDirection  = 'down'
        else:
            self.playerPresentMovingDirection = 'down'
            self.playerIsMoving = True


    def pressLeftEvent( self, event ):
        if self.playerIsMoving:
            self.playerFutureMovingDirection  = 'left'
        else:
            self.playerPresentMovingDirection = 'left'
            self.playerIsMoving = True


class playerThread( threading.Thread ):
    
    def __init__( self, playWindow ):
        self.playWindow = playWindow
        threading.Thread.__init__( self )


    def run( self ):

        A_PD_X = self.playWindow.playerDisplcementX
        A_PD_Y = self.playWindow.playerDisplcementY

        while not self.playWindow.closeAll:

            time.sleep( 0.003 )

            if self.playWindow.playerPresentMovingDirection == 'still':
                self.playWindow.playerPresentMovingDirection = self.playWindow.playerFutureMovingDirection
                self.playWindow.playerFutureMovingDirection  = 'still'
    
            if self.playWindow.playerIsMoving:
    
                A_PD_X = self.playWindow.playerDisplcementX
                A_PD_Y = self.playWindow.playerDisplcementY

                if   self.playWindow.playerPresentMovingDirection == 'up':
                    self.playWindow.playerDisplcementY -= DISPLACEMENT_SPEED
    
                elif self.playWindow.playerPresentMovingDirection == 'right':
                    self.playWindow.playerDisplcementX += DISPLACEMENT_SPEED
    
                elif self.playWindow.playerPresentMovingDirection == 'down':
                    self.playWindow.playerDisplcementY += DISPLACEMENT_SPEED
    
                elif self.playWindow.playerPresentMovingDirection == 'left':
                    self.playWindow.playerDisplcementX -= DISPLACEMENT_SPEED

                PP_C1X   = PLAYER_START_WIDTH  +               self.playWindow.playerDisplcementX
                PP_C1Y   = PLAYER_START_HEIGHT +               self.playWindow.playerDisplcementY
                PP_C2X   = PLAYER_START_WIDTH  + PLAYER_SIZE + self.playWindow.playerDisplcementX
                PP_C2Y   = PLAYER_START_HEIGHT + PLAYER_SIZE + self.playWindow.playerDisplcementY
    
                if ( ( PP_C1X < 14 ) or ( PP_C1Y < 14 ) or ( PP_C2X > G_WIDTH - 14 ) or ( PP_C2Y > G_HEIGHT - 14 ) ):
                    print "a"
                    self.playWindow.playerPresentMovingDirection = 'still'
                    self.playWindow.playerDisplcementX = A_PD_X
                    self.playWindow.playerDisplcementY = A_PD_Y
                    PP_C1X   = PLAYER_START_WIDTH  +               self.playWindow.playerDisplcementX
                    PP_C1Y   = PLAYER_START_HEIGHT +               self.playWindow.playerDisplcementY
                    PP_C2X   = PLAYER_START_WIDTH  + PLAYER_SIZE + self.playWindow.playerDisplcementX
                    PP_C2Y   = PLAYER_START_HEIGHT + PLAYER_SIZE + self.playWindow.playerDisplcementY
    
                self.playWindow.canvasMain.coords( "player", PP_C1X, PP_C1Y, PP_C2X, PP_C2Y )


main = playWindow()
main.mainloop()