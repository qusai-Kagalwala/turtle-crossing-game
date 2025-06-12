# =============================================================================
# Turtle Crossing Game - Scoreboard Class
# Displays current level and handles Game Over messages
# =============================================================================

from turtle import Turtle

# =============================================================================
# SCOREBOARD DISPLAY CONSTANTS (Grouped for visibility)
# =============================================================================
FONT = ("Courier", 24, "normal")        # Default display font
ALIGN = "center"                         # Text alignment
STARTING_LEVEL = 1                       # Initial level

# =============================================================================
# SCOREBOARD CLASS
# =============================================================================
class Scoreboard(Turtle):
    """
    ENHANCED Scoreboard class that manages the level display and game-over text.
    Inherits from Turtle to draw text on screen.
    """

    def __init__(self):
        super().__init__()
        self.level = STARTING_LEVEL
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears and redraws the level text.
        Ensures text is always at top after reset.
        """
        self.clear()
        self.goto(0, 260)  # Ensure position at top
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def increase_level(self):
        """
        Increment level by one and update display.
        Triggered when player reaches top edge.
        """
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        """
        Reset level to starting level and update display.
        Used when restarting the game.
        """
        self.level = STARTING_LEVEL
        self.update_scoreboard()

    def game_over(self):
        """
        Display a 'Game Over' message in the center of the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
        self.goto(0, -40)
        self.write("Press 'R' to Restart", align=ALIGN, font=("Courier", 18, "normal"))


# =============================================================================
# CHANGES MADE TO ORIGINAL CODE:
#
# ORIGINAL CODE ISSUES:
# 1. ❌ Empty class with no functionality
#
# ENHANCED VERSION IMPROVEMENTS:
# 1. ✅ Displays level and updates on progress
# 2. ✅ Added reset() for restart support
# 3. ✅ Displays Game Over with restart prompt
# 4. ✅ Separated constants for formatting and alignment
#
# CORE FUNCTIONALITY PRESERVED:
# - Text-based level display
# - Game Over handling
#
# NEW FUNCTIONALITY ADDED:
# - Reset functionality
# - Restart instructions
# =============================================================================
