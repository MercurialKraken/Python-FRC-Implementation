import wpilib
import commands2
import typing
#import Timer

from robotcontainer import RobotContainer


class Robot (wpilib.TimedRobot):

    autonomousCommand: typing.Optional[commands2.Command] = None

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.container = RobotContainer()
        #self.timer = Timer()
    
    def disabledInit(self):
        """This function is run once each time the robot enters disabled mode."""
        pass

    def disabledPeriodic(self):
        """This function is called periodic during disabled."""
        pass

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        #self.timer.reset()
        #self.timer.start()
        self.autonomousCommand = self.container.getAutonomousCommand()

        if self.autonomousCommand:
            self.autonomousCommand.schedule()

     def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopInit(self):
        """This function is run once each time the robot enters teleop mode."""
        if self.autonomousCommand:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self):
        """This function is called periodically during teleop."""
        pass

    def testInit(self):
        """This function is run once each time the robot enters test mode."""
        commands2.CommandScheduler.getInstance().cancelAll()
    
    def testPeriodic(self):
        """This function is called periodically during test."""
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)