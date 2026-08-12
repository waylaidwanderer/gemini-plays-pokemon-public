import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def test_col26():
    pos = get_pos()
    print(f"Starting position: {pos}")
    
    print("Walking UP to (26, 12)...")
    walk_step("Up")
    pos1 = get_pos()
    print(f"Pos after step 1: {pos1}")
    
    if pos1 == (26, 12):
        print("Walking UP to (26, 11)...")
        walk_step("Up")
        pos2 = get_pos()
        print(f"Pos after step 2: {pos2}")
        if pos2 == (26, 11):
            print("SUCCESS! Column 26 is OPEN!")
            return
            
    print("Column 26 blocked.")

if __name__ == "__main__":
    test_col26()
