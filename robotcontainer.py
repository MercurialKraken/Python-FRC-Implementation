import wpilib
import commands2.button
import math
import navx
from Commands.DriveCommand import DriveCommand
from Subsystems.DriveSubsystem import DriveSubsystem
import constants

class RobotContainer():
    def __init__(self) -> None:
        self.joy1 = wpilib.Joystick(constants.joy1_port)
        self.encR = wpilib.Encoder(0, 1, False, 'k4X')
        self.encL = wpilib.Encoder(2, 3, True, 'k4X')
        self.navx = navx.AHRS.create_spi(wpilib.SPI.Port.kMXP)
        self.driveSubsystem = DriveSubsystem()
        self.driveCommand = DriveCommand(self.driveSubsystem)
        self.configureButtonBindings()
        self.driveSubsystem.setDefaultCommand(self.driveCommand(self.driveSubsystem))


    def configureButtonBindings(self) -> None:
        commands2.button.JoystickButton(self.joy1, 1).whenPressed(wpilib.SmartDashboard.putData('Button Pressed: ', 1))

    def getAutonomousCommand(self) -> None:
        pass

    def getY(self, joystick: wpilib.Joystick, deadband) -> float:
        value = -1*joystick.getY()
        return (0 if math.fabs(value) < deadband else value)

    def getZ(self, joystick: wpilib.Joystick, deadband) -> float:
        value = -1*joystick.getZ()
        return (0 if math.fabs(value) < deadband else value)
        
