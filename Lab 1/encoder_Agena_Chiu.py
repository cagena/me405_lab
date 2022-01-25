import pyb

class EncoderDriver:  
    '''! 
    This class implements a encoder driver for an ME405 kit. 
    '''
    def __init__(self, in1pin, in2pin, timer):
        '''! 
        Creates a encoder driver by initializing encoder
        pins. 
        @param in1pin pin 1 to read the encoder.
        @param in2pin pin 2 to read the encoder.
        @param timer timer to use for encoder channels.
        '''
        
        # Defines the timer variable for the motor.
        self.tim = pyb.Timer(timer, prescaler = 0, period = 65535)
        
        # Defines the pin variables to recieve the duty cycles.
        self.pin1 = pyb.Pin(in1pin, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(in2pin, pyb.Pin.OUT_PP)
        
        # Define two channel variables.
        self.ch1 = self.tim.channel(1, pyb.Timer.ENC_AB,
                                    pin = self.pin1)
        self.ch2 = self.tim.channel(2, pyb.Timer.ENC_AB,
                                    pin = self.pin2)
        
        # Set the initial position to zero.
        self.pos = 0
        
        # Set the initial past time to zero.
        self.past = 0
    
    def read(self):
        '''!
        Reads the encoder position and returns the values.
        @return The position of the encoder.
        '''
        self.current = self.tim.counter()
        self.delta = self.current - self.past
        if self.delta < -32768:
            self.delta += 65536
        elif self.delta > 32768:
            self.delta -= 65536
        self.pos += self.delta
        self.past = self.current
        return self.pos

    def zero(self):
        '''!
        Sets the encoder reading to zero.
        '''
        self.pos = 0   