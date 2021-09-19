import wpilib
import commands2
import math
import navx
from Commands.DriveCommand import DriveCommand
from Subsystems.DriveSubsystem import DriveSubsystem

class RobotContainer():
    def __init__(self) -> None:
        self.joy1 = wpilib.Joystick(0)
        self.encR = wpilib.Encoder(0, 1, False)
        self.encL = wpilib.Encoder(2, 3, True)
        self.navx = navx.AHRS.createSPI()
        self.driveSubsystem = DriveSubsystem()
        self.driveCommand = DriveCommand(self.driveSubsystem)
        self.configureButtonBindings()
        self.driveSubsystem.setDefaultCommand(self.driveCommand(self.driveSubsystem))


    def configureButtonBindings(self) -> None:
        pass

    def getAutonomousCommand(self) -> None:
        pass

    def getY(self, joystick, deadband) -> float:
        value = -1*self.joy1.getY()
        return (0 if math.abs(value) < deadband else value)

    def getZ(self, joystick, deadband) -> float:
        value = -1*self.joy1.getZ()
        return (0 if math.abs(value) < deadband else value)
        
