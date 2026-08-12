import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Interaction/Battle detected. Clearing with B...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    # Press Right, Down, A to run
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def probe_up():
    print("Starting probe UP on column 28...")
    stuck_count = 0
    
    # We are currently at (28, 24)
    # We want to walk UP as far as possible
    for step in range(15):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
            if pos is None:
                print("Failed to get position after running away.")
                return
        
        cx, cy = pos
        print(f"Before step {step}: ({cx}, {cy})")
        
        # Press UP
        bridge.press_buttons(["Up", "sleep 400"])
        
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            new_pos = get_pos()
            if new_pos is None:
                print("Failed to get position after battle.")
                return
                
        ncx, ncy = new_pos
        print(f"After step {step}: ({ncx}, {ncy})")
        
        if ncx == cx and ncy == cy:
            print(f"BLOCKED! Could not move UP from ({cx}, {cy}).")
            break

if __name__ == "__main__":
    probe_up()
