# =============================================================================
# Turtle Crossing Game - Player Class
# Represents the user-controlled turtle that moves forward (up only)
# =============================================================================

from turtle import Turtle

# =============================================================================
# PLAYER CONFIGURATION CONSTANTS (ADDED: Grouped and documented)
# =============================================================================
STARTING_POSITION = (0, -280)     # Player's starting coordinates
MOVE_DISTANCE = 10                # Distance moved per key press
FINISH_LINE_Y = 280               # Y-position to trigger level up

# =============================================================================
# PLAYER CLASS DEFINITION
# =============================================================================
class Player(Turtle):
    """
    ENHANCED Player class that allows upward movement and level checks.
    Inherits from Turtle for drawing and movement capabilities.

    ORIGINAL VERSION: Only had a placeholder pass statement.
    ENHANCED VERSION: Implements movement, reset, and level detection.
    """

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)  # Face the turtle upward

    def move_up(self):
        """
        Move the turtle upward by a fixed distance.
        ORIGINAL: Not implemented
        ENHANCED: Added upward movement using Turtle's forward()
        """
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        """
        Check if the player has reached the top of the screen.

        Returns:
            bool: True if y-coordinate is above finish line
        """
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        """
        Reset the player to the starting position.
        ENHANCED: Used in level-up and game restart
        """
        self.goto(STARTING_POSITION)

# =============================================================================
# CHANGES MADE TO ORIGINAL CODE:
#
# ORIGINAL CODE ISSUES:
# 1. ❌ Empty class with no functionality
#
# ENHANCED VERSION IMPROVEMENTS:
# 1. ✅ Added position constants for maintainability
# 2. ✅ Implemented move_up, reset, and finish detection
# 3. ✅ Improved structure with class-level docstring
#
# CORE FUNCTIONALITY PRESERVED:
# - Turtle still moves up only
#
# NEW FUNCTIONALITY ADDED:
# - Movement logic
# - Finish line check
# - Restart support through go_to_start()
# =============================================================================