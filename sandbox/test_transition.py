import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 350"])

def navigate():
    print("Navigating from current (13, 15) to (21, 18) via plateau...")
    
    # 1. Walk Left to (6, 15)
    for _ in range(7):
        walk_step("Left")
    print(f"At: {get_pos()}")
    
    # 2. Walk Down to (6, 20)
    for _ in range(5):
        walk_step("Down")
    print(f"At: {get_pos()}")
    
    # 3. Climb West Stairs
    for _ in range(4):
        walk_step("Up")
    print(f"At: {get_pos()}")
    
    # 4. Walk east to (21, 16)
    for _ in range(15):
        walk_step("Right")
    print(f"At: {get_pos()}")
    
    # 5. Descend East Stairs to (21, 18)
    for _ in range(2):
        walk_step("Down")
    print(f"At: {get_pos()}")
    
    # 6. Walk to (23, 18)
    walk_step("Right")
    walk_step("Right")
    pos = get_pos()
    print(f"At: {pos}")
    
    if pos == (23, 18):
        print("Successfully reached (23, 18). Probing Column 23 UP...")
        for y in range(17, 7, -1):
            print(f"Trying UP to (23, {y})...")
            walk_step("Up")
            npos = get_pos()
            print(f"Result: {npos}")
            if npos is None or npos[1] != y:
                print(f"Blocked at Row {y}! Current pos: {npos}")
                break

if __name__ == "__main__":
    navigate()
