import wpilib
import commands2
from robotcontainer import RobotContainer
from Subsystems.DriveSubsystem import DriveSubsystem

class DriveCommand(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem):
        super().__init__()
        self.drive = drive
        self.addRequirements([self.drive])
    
    def execute(self):
        DriveSubsystem.arcadeInbuilt(RobotContainer.getY, RobotContainer.getZ)
        