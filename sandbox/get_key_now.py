import mgba
import time

def run_from_battle():
    print("Stuck! Attempting to run from battle...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    max_steps = 100
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            walk_step("Right")
        elif x > target_x:
            walk_step("Left")
        elif y < target_y:
            walk_step("Down")
        elif y > target_y:
            walk_step("Up")
        steps += 1
    return False

# Starting on Cinnabar Island at (11, 12)
print("0. Entering the Mansion...")
walk_to(18, 12)
walk_to(18, 5)
walk_to(6, 5)
walk_to(6, 3)
mgba.press_buttons(["Up", "sleep 400"]) # Step UP to warp into Mansion
time.sleep(1.5)
print("Inside Mansion 1F:", mgba.get_coordinates())

# 1. Walk from (5, 27) to (5, 10) and warp UP to 2F West
print("1. Warp UP to 2F West...")
walk_to(5, 11)
walk_to(8, 11)
walk_to(8, 10)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # Step LEFT onto (5, 10) to warp
time.sleep(1.5)
print("Position on 2F West:", mgba.get_coordinates())

# 2. Warp UP to 3F West
print("2. Warp UP to 3F West...")
walk_to(7, 11)
mgba.press_buttons(["Up", "sleep 400"]) # Step UP onto stairs at (7, 10) to warp
time.sleep(1.5)
print("Position on 3F West:", mgba.get_coordinates())

# 3. Walk to 3F East Balcony (Row 18) in State A
print("3. Walking to the Balcony (19, 18) in State A...")
walk_to(7, 6)
walk_to(19, 6)
walk_to(19, 18)

# 4. Drop over the Balcony to B1F East
print("4. Dropping over the balcony...")
mgba.press_buttons(["Down", "sleep 500"])
time.sleep(2.0)
print("Position on B1F East:", mgba.get_coordinates())

# 5. Walk to B1F East switch at (15, 6)
print("5. Walking to switch at (15, 6)...")
walk_to(22, 6)
walk_to(15, 7)
# Face UP towards switch at (15, 6) and toggle to State B!
print("Toggling B1F switch to State B...")
mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500", "B", "sleep 200"])

# 6. Walk horizontally along B1F Row 5 across open gate (9, 5) to B1F West North (1, 5)
print("6. Walking along Row 5 to (1, 5) in State B...")
walk_to(15, 5)
walk_to(1, 5)

# 7. Retrieve the Secret Key at (1, 4)
print("7. Picking up the Secret Key...")
mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
print("Secret Key pick-up executed! Current position:", mgba.get_coordinates())

# 8. Escape via DIG
print("8. Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
time.sleep(2.0)

print("Escaped! Final position on Cinnabar Island:", mgba.get_coordinates())
