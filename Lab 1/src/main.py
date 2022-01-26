# Import the required modules to run the motor and encoder 
import motor_Agena_Chiu
import encoder_Agena_Chiu
import pyb

if __name__ == '__main__':
    # Create a encoder driver for both encoders.
    encoder_drv1 = encoder_Agena_Chiu.EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    encoder_drv2 = encoder_Agena_Chiu.EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, 8)
    # Create a motor driver for both motors.
    motor_drv1 = motor_Agena_Chiu.MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    motor_drv2 = motor_Agena_Chiu.MotorDriver(pyb.Pin.cpu.C1, pyb.Pin.cpu.A0, pyb.Pin.cpu.A1, 5)
    # Enable both motors.
    motor_drv1.enable()
    motor_drv2.enable()
    # Set the duty cycle for both motors.
    motor_drv1.set_duty_cycle(50)
    motor_drv2.set_duty_cycle(50)
    # While loop to continuously print the position of both encoders.
    while True:
        print('Encoder 1 position: ' + str(encoder_drv1.read()))
        print('Encoder 2 position: ' + str(encoder_drv2.read()))