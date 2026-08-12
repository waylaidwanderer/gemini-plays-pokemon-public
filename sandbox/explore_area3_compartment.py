import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_all():
    print("=== EXPLORING AREA 3 NORTH CORRIDOR ===")
    
    # We are currently at (23, 8). Let's walk UP to (23, 2)
    path_up = ["Up"] * 6
    for step in path_up:
        bridge.press_buttons([step, "sleep 400"])
        
    pos = get_pos()
    print(f"Reached: {pos}")
    
    # Try to walk RIGHT along Row 2 from (23, 2) to Column 30
    path_right = ["Right"] * 10
    for idx, step in enumerate(path_right):
        pos_before = get_pos()
        bridge.press_buttons([step, "sleep 400"])
        pos_after = get_pos()
        print(f"Step {idx}: Tried {step} from {pos_before} -> {pos_after}")
        if pos_after == pos_before:
            # We got blocked! Let's try to face Right and press again just in case of turn-in-place
            bridge.press_buttons([step, "sleep 400"])
            pos_after2 = get_pos()
            print(f"Retry Step {idx}: Tried {step} again -> {pos_after2}")
            if pos_after2 == pos_before:
                print(f"Blocked at {pos_before} going {step}!")
                break
                
    print(f"Final coordinates: {get_pos()}")

if __name__ == "__main__":
    run_all()
