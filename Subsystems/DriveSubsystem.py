import commands2
import wpilib
import constants

class DriveSubsystem(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        #commands2.SubsystemBase.__init__()

        self.fl = wpilib.Talon(0)
        self.fr = wpilib.Talon(1)
        self.bl = wpilib.Talon(2)
        self.br = wpilib.Talon(3)

        self.left = wpilib.SpeedControllerGroup(self.fl, self.bl)
        self.right = wpilib.SpeedControllerGroup(self.fr, self.br)

        self.drivetrain = wpilib.drive.DifferentialDrive(self.left, self.right)

    def periodic(self):
        pass

    def arcadeInbuilt(self, y, z):
        self.fr.setInverted = False
        self.br.setInverted = False
        self.drivetrain.arcadeDrive(y*constants.max_speed, z*constants.max_speed)
