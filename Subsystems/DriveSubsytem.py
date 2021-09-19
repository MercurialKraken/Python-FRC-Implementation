import commands2
import wpilib
import constants

class DriveSubsytem(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        #commands2.SubsystemBase.__init__()

        self.fl = wpilib.Talon(0)
        self.fr = wpilib.Talon(1)
        self.bl = wpilib.Talon(2)
        self.br = wpilib.Talon(3)

        self.left = wpilib.SpeedControllerGroup(fl, bl)
        self.right = wpilib.SpeedControllerGroup(fr, br)

        self.drivetrain = wpilib.drive.DifferentialDrive(left, right)

    def periodic(self):
        pass

    def arcadeInbuilt(y, z):
        fr.setInverted = False
        br.setInverted = False
        drivetrain.arcadeDrive(y*constants.max_speed, z*constants.max_speed)
