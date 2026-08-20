import mgba
import time

def flee_battle():
    # Execute the verified 1-turn battle flee sequence
    mgba.press_buttons(["B", "B", "B", "Down", "Right", "A", "B", "sleep 300", "B"])

def step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    pos_after = mgba.get_coordinates()
    # Check if we didn't move
    if pos_before == pos_after:
        # Might be in a battle or hit a wall
        # Try fleeing just in case
        flee_battle()
        pos_after = mgba.get_coordinates()
    return pos_after

pos = mgba.get_coordinates()
print(f"Starting position: {pos}")
