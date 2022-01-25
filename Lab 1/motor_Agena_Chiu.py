import pyb
    
class MotorDriver:  
    '''! 
    This class implements a motor driver for an ME405 kit. 
    '''
    def __init__(self, en_pin, in1pin, in2pin, timer):
        '''! 
        Creates a motor driver by initializing GPIO
        pins and turning the motor off for safety. 
        @param en_pin pin for enabling the motor.
        @param in1pin pin 1 to control the motor.
        @param in2pin pin 2 to control the motor.
        @param timer timer to use for motor channels.
        '''
        # Defines pin variables for the enable pin on the Nucleo
        self.EN = pyb.Pin(en_pin, mode = pyb.Pin.OUT_OD,
                          pull = pyb.Pin.PULL_UP)
        
        # Defines the timer variable for the motor.
        self.tim = pyb.Timer(timer, freq = 20000)
        
        # Defines the pin variables to recieve the duty cycles.
        self.pin1 = pyb.Pin(in1pin, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(in2pin, pyb.Pin.OUT_PP)
        
        # Define two channel variables.
        self.ch1 = self.tim.channel(1, mode = pyb.Timer.PWM,
                                    pin = self.pin1)
        self.ch2 = self.tim.channel(2, mode = pyb.Timer.PWM,
                                    pin = self.pin2)
        
        # Turn the motor off for safety.
        self.pin1.low()
        self.pin2.low()
        
        print ('Creating a motor driver')
        
    def enable(self):
        '''!
        Enables the motor, allowing power to it.
        '''
        self.EN.high()
        
    def disable(self):
        '''!
        Disables the motor, preventing power to it.
        '''
        self.EN.low()
        
    def set_duty_cycle(self, duty):
        '''!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param duty A signed integer holding the duty
               cycle of the voltage sent to the motor 
        '''
        if duty > 0:
            self.ch1.pulse_width_percent(duty)
            self.ch2.pulse_width_percent(0)
        elif duty < 0:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(-duty)  
        else:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(0) 
            
        print ('Setting duty cycle to ' + str (duty))   