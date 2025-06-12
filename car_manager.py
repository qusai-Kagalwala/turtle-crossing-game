# =============================================================================
# Turtle Crossing Game - Car Manager Class
# Controls creation, movement, and speed of car obstacles
# =============================================================================

from turtle import Turtle
import random

# =============================================================================
# CAR CONFIGURATION CONSTANTS
# =============================================================================
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# =============================================================================
# CAR MANAGER CLASS DEFINITION
# =============================================================================
class CarManager:
    """
    Manages car creation, movement, and speed progression.
    """

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Creates a new car with random color and y-position.
        Chance of creation is 1 in 6 to control frequency.
        """
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Move all cars leftwards based on current speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """
        Increase the speed of cars.
        Called when player levels up.
        """
        self.car_speed += MOVE_INCREMENT

    def reset(self):
        """
        Clear all cars and reset speed to starting value.
        Used when restarting the game.
        """
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE

# =============================================================================
# CHANGES MADE TO ORIGINAL CODE:
#
# ORIGINAL ISSUES:
# 1. No reset mechanism for restart
# 2. No named constants for move distance or increment
#
# ENHANCEMENTS:
# 1. ✅ Introduced reset() method
# 2. ✅ Added STARTING_MOVE_DISTANCE as a global constant
# 3. ✅ Updated main.py to use .reset() instead of direct variable change
# =============================================================================
