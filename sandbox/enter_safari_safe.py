import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def clear_remaining_dialogue():
    print("Completing remaining dialogue with 1.5s delays...")
    for step in range(5):
        print(f"Pressing A for step {step}...")
        bridge.press_buttons(["A", "sleep 1500"])
        
    print("Done! Checking position...")
    pos = get_pos()
    print(f"Position: {pos}")
    return pos

if __name__ == "__main__":
    clear_remaining_dialogue()
