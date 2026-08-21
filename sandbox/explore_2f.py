import mgba
import time

# We are at (5, 10) on 2F West.
# Let's test walking in different directions to find out where the walls and stairs are.
print("Current position:", mgba.get_coordinates())

directions = ["Left", "Right", "Down", "Up"]
for direction in directions:
    pos_before = mgba.get_coordinates()
    print(f"Testing {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Moved to {pos_after}")
    # Move back if we successfully moved
    if pos_before != pos_after:
        # Check if we transitioned maps
        if abs(pos_before['x'] - pos_after['x']) > 2 or abs(pos_before['y'] - pos_after['y']) > 2:
            print(f"WARPED! New map coordinates: {pos_after}")
            # Warp back if possible
            if direction == "Left":
                mgba.press_buttons(["Right"])
            elif direction == "Right":
                mgba.press_buttons(["Left"])
            elif direction == "Down":
                mgba.press_buttons(["Up"])
            elif direction == "Up":
                mgba.press_buttons(["Down"])
            time.sleep(0.5)
        else:
            # Walk back
            if direction == "Left":
                mgba.press_buttons(["Right"])
            elif direction == "Right":
                mgba.press_buttons(["Left"])
            elif direction == "Down":
                mgba.press_buttons(["Up"])
            elif direction == "Up":
                mgba.press_buttons(["Down"])
            time.sleep(0.3)

print("Finished test!")
