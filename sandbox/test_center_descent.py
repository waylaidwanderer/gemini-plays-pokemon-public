import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def test_area2_walkability():
    print("=== PROBING AREA 2 NORTH GROUND WALKABILITY ===")
    
    # 1. Walk UP to transition into Area 2 North
    print("Transitioning into Area 2 North...")
    bridge.press_buttons(["Up", "sleep 1000"])
    
    pos = get_pos()
    print("Coordinates after transition:", pos)
    if pos is None or pos[1] != 35:
        print("Error: Not at expected Row 35 of Area 2!")
        return
        
    # We are at pos (x, 35)
    # Let's try to walk Right up to 4 times and see if we get blocked
    stuck = False
    for i in range(4):
        curr_pos = get_pos()
        print(f"Standing at {curr_pos}. Trying to walk Right...")
        bridge.press_buttons(["Right", "sleep 400"])
        new_pos = get_pos()
        if new_pos == curr_pos:
            print(f"BLOCKED! Cannot walk Right from {curr_pos}!")
            stuck = True
            break
        else:
            print(f"Successfully walked Right to {new_pos}!")
            
    if stuck:
        # If Right is blocked, let's try walking UP
        curr_pos = get_pos()
        print(f"Trying to walk Up from blocked position {curr_pos}...")
        bridge.press_buttons(["Up", "sleep 400"])
        new_pos = get_pos()
        if new_pos == curr_pos:
            print(f"BLOCKED! Cannot walk Up from {curr_pos}!")
        else:
            print(f"Successfully walked Up to {new_pos}!")
            # Try walking Right from the new Up position
            curr_pos = new_pos
            print(f"Trying to walk Right from {curr_pos}...")
            bridge.press_buttons(["Right", "sleep 400"])
            new_pos = get_pos()
            if new_pos == curr_pos:
                print(f"BLOCKED! Cannot walk Right from {curr_pos}!")
            else:
                print(f"Successfully walked Right to {new_pos}!")

if __name__ == "__main__":
    test_area2_walkability()
