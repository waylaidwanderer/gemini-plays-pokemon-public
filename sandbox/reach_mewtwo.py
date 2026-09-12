import mgba
import time

def flee_battle():
    # Down, Right, A to run, then B to clear
    mgba.press_buttons(["Down", "Right", "A", "sleep 200", "B", "sleep 100", "B", "sleep 100", "B"])

def execute_surf_from_shoreline():
    # From (4, 31) facing Down:
    # Start -> move to POKéMON -> A -> move to HYDROS -> A -> SURF
    mgba.press_buttons([
        "Start", "sleep 100",
        "Up", "Up", "Up", "Down", "A", "sleep 150",
        "Up", "Up", "Up", "Up", "A", "sleep 150",
        "A", "sleep 300"
    ])

# Step 1: Flee battle
print("Fleeing battle...")
flee_battle()
pos = mgba.get_coordinates()
print(f"Pos after flee: {pos}")

# Step 2: Ensure at (4, 31) facing Down
if pos.get('y') == 30:
    mgba.press_buttons(["Down", "sleep 50"])
    pos = mgba.get_coordinates()
    print(f"Stepped to shoreline: {pos}")

# Step 3: Board Surf
print("Boarding Surf...")
execute_surf_from_shoreline()
pos = mgba.get_coordinates()
print(f"Pos after Surf: {pos}")
