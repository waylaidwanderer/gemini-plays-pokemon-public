import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    mgba.press_buttons([
        "B", "sleep 150", "B", "sleep 150", "B", "sleep 150", 
        "Right", "sleep 150", "Down", "sleep 150", "A", "sleep 2000"
    ])

def try_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 3:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Currently at (1, 10)
print("Starting switch interaction test...")

# Spot 1: Standing at (1, 10) facing RIGHT towards (2, 10)
print("Testing Spot 1: Standing at (1, 10) facing RIGHT...")
try_step("Down") # Align to (1, 11) first to face right? Wait, let's just go to (1, 11) first.
# Wait, let's walk back to (1, 11)
try_step("Down") # To (1, 11)
print("Position:", get_pos())

# Face RIGHT
mgba.press_buttons(["Right", "sleep 250"])
print("Pressed Right, checking for switch text...")
mgba.press_buttons(["A", "sleep 400"])
# Let's see if a textbox is open. We take a screenshot
sc = mgba.take_screenshot()
print("Screenshot after A on Spot 1:", sc)

# Spot 2: Standing at (1, 12) facing RIGHT towards (2, 12)
print("Testing Spot 2: Standing at (1, 12) facing RIGHT...")
try_step("Down") # To (1, 12)
mgba.press_buttons(["Right", "sleep 250"])
mgba.press_buttons(["A", "sleep 400"])
sc = mgba.take_screenshot()
print("Screenshot after A on Spot 2:", sc)

# Spot 3: Standing at (2, 13) facing UP towards (2, 12)
print("Testing Spot 3: Standing at (2, 13) facing UP...")
try_step("Down") # To (1, 13)
try_step("Right") # To (2, 13)
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 400"])
sc = mgba.take_screenshot()
print("Screenshot after A on Spot 3:", sc)

# Spot 4: Standing at (3, 13) facing UP towards (3, 12)
print("Testing Spot 4: Standing at (3, 13) facing UP...")
try_step("Right") # To (3, 13)
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 400"])
sc = mgba.take_screenshot()
print("Screenshot after A on Spot 4:", sc)

# Spot 5: Standing at (4, 11) facing LEFT towards (3, 11)
print("Testing Spot 5: Standing at (4, 11) facing LEFT...")
try_step("Right") # To (4, 13)
try_step("Up") # To (4, 12)
try_step("Up") # To (4, 11)
mgba.press_buttons(["Left", "sleep 250"])
mgba.press_buttons(["A", "sleep 400"])
sc = mgba.take_screenshot()
print("Screenshot after A on Spot 5:", sc)
