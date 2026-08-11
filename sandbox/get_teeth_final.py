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

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def navigate():
    print("Starting Gold Teeth retrieval from (13, 15)...")
    
    # 1. Walk Left to (3, 15)
    for _ in range(10):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        walk_step("Left")
        
    print(f"At Column 3: {get_pos()}")
    
    # 2. Walk Down to (3, 20)
    for _ in range(5):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        walk_step("Down")
        
    print(f"At Row 20: {get_pos()}")
    
    # 3. Walk Right to (6, 20)
    for _ in range(3):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        walk_step("Right")
        
    print(f"At West Stairs base: {get_pos()}")
    
    # 4. Climb West Stairs to (6, 16)
    for _ in range(4):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        walk_step("Up")
        
    print(f"On plateau: {get_pos()}")
    
    # 5. Walk East to (21, 16)
    for _ in range(15):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        walk_step("Right")
        
    print(f"At East Stairs top: {get_pos()}")
    
    # 6. Descend East Stairs to (21, 18)
    for _ in range(2):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        walk_step("Down")
        
    print(f"At East Stairs base: {get_pos()}")
    
    # 7. Walk Down to (21, 24)
    for _ in range(6):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        walk_step("Down")
        
    print(f"At southern Row 24: {get_pos()}")
    
    # 8. Walk Left to (19, 24)
    for _ in range(2):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        walk_step("Left")
        
    pos = get_pos()
    print(f"Standing below Gold Teeth at: {pos}")
    if pos == (19, 24):
        print("Picking up Gold Teeth...")
        bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
        print("Retrieval Complete!")

if __name__ == "__main__":
    navigate()
