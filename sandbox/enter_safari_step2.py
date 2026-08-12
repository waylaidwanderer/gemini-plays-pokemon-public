import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def enter_from_counter():
    print("Executing safe A presses to complete entry dialogue...")
    
    # We are at (4, 2) with "Welcome to the SAFARI ZONE!" active.
    # We need 7 A presses to clear dialogue and warp in.
    for step in range(7):
        print(f"Pressing A for step {step}...")
        bridge.press_buttons(["A", "sleep 850"])
        
    print("Done! Checking position...")
    pos = get_pos()
    print(f"Position: {pos}")
    return pos

if __name__ == "__main__":
    enter_from_counter()
