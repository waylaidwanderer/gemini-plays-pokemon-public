import mgba
import time

def escape_battle():
    # Turn 1: Dismiss intro text
    mgba.press_buttons(["A", "sleep 200", "B", "sleep 300"])
    # Turn 2: Select RUN
    mgba.press_buttons(["Down", "Right", "A", "sleep 400"])
    # Turn 3: Dismiss 'Got away safely!'
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])
    return mgba.get_coordinates()

def safe_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    return pos_before, pos_after
