# =============================================================================
# Turtle Crossing Game - Main Entry Point
# Handles game loop, collision detection, level progression, and restart
# =============================================================================

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# =============================================================================
# SETUP SCREEN
# =============================================================================
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("background.gif")  # Optional background graphic
screen.tracer(0)
screen.title("Turtle Crossing Game")

# =============================================================================
# INSTANTIATE GAME OBJECTS
# =============================================================================
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# =============================================================================
# RESTART FUNCTION
# =============================================================================
def restart_game():
    """
    Resets game state: player, cars, and scoreboard
    ENHANCEMENT: Full game restart without quitting
    """
    global game_is_on
    car_manager.reset()
    player.go_to_start()
    scoreboard.reset()
    screen.update()
    screen.onkey(player.move_up, "Up")  # Rebind movement
    game_loop()

# =============================================================================
# MAIN GAME LOOP
# =============================================================================
def game_loop():
    """
    Core game loop that runs each frame: update, collision, level check
    """
    global game_is_on
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with any car
        for car in car_manager.all_cars:
            if player.distance(car) < 20:
                scoreboard.game_over()
                screen.onkey(None, "Up")  # Disable movement
                game_is_on = False
                break

        # Check if player reached the finish line
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.increase_speed()
            scoreboard.increase_level()

# =============================================================================
# KEYBINDINGS (MOVEMENT + RESTART + EXIT)
# =============================================================================
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(restart_game, "r")  # Press 'r' to restart
screen.onkey(screen.bye, "q")    # Press 'q' to quit

# =============================================================================
# START GAME
# =============================================================================
game_loop()
screen.mainloop()