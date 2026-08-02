import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B1F elevator activation path from:", pos)

if pos['x'] == 20 and pos['y'] == 11:
    # 1. Walk to B3F stairs at (25, 6)
    print("Walking Up to Row 7 on B3F...")
    pos = move(["Up"])
    pos = move(["Up"])
    pos = move(["Up"])
    pos = move(["Up"])
    
    print("Walking Right to Column 25...")
    for _ in range(5):
        pos = move(["Right"])
        
    print("Stepping onto B2F stairs at (25, 6)...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on B2F:", pos)

# Now we should be on B2F. Spawning at (21, 8) or (21, 9)
if pos['x'] == 21:
    print("Successfully on B2F!")
    # On B2F, walk to B1F stairs at (27, 8)
    print("Walking Right to Column 27 on B2F...")
    for _ in range(6):
        pos = move(["Right"])
        
    # Wait to see if we warp
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on B1F:", pos)

# Now we should be on B1F. Spawning at (23, 2)
if pos['x'] == 23 and pos['y'] == 2:
    print("Successfully on B1F!")
    # We are at (23, 2) facing DOWN (towards the elevator door at (23, 3))
    print("Facing DOWN at (23, 3) elevator door. Pressing A to open...")
    mgba.press_buttons(["Down"]) # Face Down
    time.sleep(0.3)
    mgba.press_buttons(["A"]) # Press A
    time.sleep(1.0)
    
    # Try to walk Down into the elevator
    print("Walking DOWN into the elevator...")
    pos = move(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after elevator entry attempt:", pos)

mgba.take_screenshot()
