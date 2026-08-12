import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def test_walk_up():
    print("Testing walk UP through the Gatehouse corridor...")
    
    # Starting at (4, 3)
    for step in range(5):
        pos = get_pos()
        print(f"Step {step}: pos before UP = {pos}")
        walk_step("Up")
        pos_after = get_pos()
        print(f"Step {step}: pos after UP = {pos_after}")
        if pos_after == pos:
            print("BLOCKED!")
            break
            
if __name__ == "__main__":
    test_walk_up()
