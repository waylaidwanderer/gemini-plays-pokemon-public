import mgba
import time

def check_and_escape():
    # Let's check if we are in a battle.
    # We can detect if we are in battle by reading screen state or taking a screenshot and analyzing.
    # For simplicity, if we get into a battle, the player's coordinate doesn't change or we can press Run (Right, Down, A).
    # Let's write a small helper to run away if a battle is detected.
    # In Gen 1 battle, the coordinates don't update or the screen changes drastically.
    # A safe way is to check the current coordinates. If get_coordinates() is None or doesn't change after movement,
    # or we can proactively try to escape by pressing: B, Right, Down, A.
    # Let's press "B" first to clear any text/menus, then try the escape sequence:
    # "Right" (move to RUN), "Down" (ensure we are on RUN), "A" (select RUN).
    # Let's do this if we suspect we are in battle.
    pass

def walk_step(direction):
    # Press the direction button
    mgba.press_buttons([direction, "sleep 300"])
    # Wait a bit
    time.sleep(0.1)

def run_to_destination(path):
    # path is a list of directions
    for i, direction in enumerate(path):
        pos_before = mgba.get_coordinates()
        walk_step(direction)
        pos_after = mgba.get_coordinates()
        
        # If position didn't change, we might have run into a wild battle!
        if pos_before == pos_after:
            print(f"Bump or Battle detected at step {i} ({direction}) from {pos_before}")
            # Try to handle battle / text boxes
            for escape_attempt in range(5):
                # Press B to clear any level up/text
                mgba.press_buttons(["B", "sleep 200"])
                # Try to run: Right, Down, A
                mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
                pos_check = mgba.get_coordinates()
                if pos_check != pos_after:
                    print("Successfully fled battle or cleared block! New pos:", pos_check)
                    break
            else:
                print("Failed to move, still stuck at:", mgba.get_coordinates())

# Our starting position is (6, 10) on 2F West.
# We want to go to (12, 11).
# Path:
# 1. UP to Row 3: (6, 10) -> (6, 3) (7 steps UP)
path_1 = ["Up"] * 7

# 2. RIGHT to Column 23: (6, 3) -> (23, 3) (17 steps RIGHT)
path_2 = ["Right"] * 17

# 3. DOWN to Row 11: (23, 3) -> (23, 11) (8 steps DOWN)
path_3 = ["Down"] * 8

# 4. LEFT to Column 12: (23, 11) -> (12, 11) (11 steps LEFT)
path_4 = ["Left"] * 11

print("Starting walk to 2F East switch...")
run_to_destination(path_1)
print("Reached Row 3. Moving to Column 23...")
run_to_destination(path_2)
print("Reached Column 23. Moving to Row 11...")
run_to_destination(path_3)
print("Reached Row 11. Moving to Column 12...")
run_to_destination(path_4)

print("Arrived at target! Current pos:", mgba.get_coordinates())

# Now stand at (12, 11) facing RIGHT (towards (13, 11)) and press A to toggle switch
# To face RIGHT, we can press Right, but wait! Pressing Right might step onto (13, 11) if it is open!
# Wait! Is (13, 11) a solid statue?
# Yes, the Mewtwo statue at (13, 11) is 100% solid, so pressing Right will turn us to face Right and bump into it without stepping!
# This is safe and perfect.
mgba.press_buttons(["Right", "sleep 300", "A", "sleep 1000"])

# We expect the dialogue: "Whoops! A secret switch! Press it?"
# Select YES (press A)
mgba.press_buttons(["A", "sleep 1000"])

# It says "Opened/closed the shutter doors!"
# Close dialogue (press A)
mgba.press_buttons(["A", "sleep 500"])

screentype = mgba.take_screenshot()
print("Final screen coordinate after toggle:", mgba.get_coordinates())
print("Saved screenshot:", screentype)
