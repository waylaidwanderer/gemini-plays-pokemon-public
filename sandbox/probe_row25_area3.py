import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    return get_pos()

def main():
    print("Probing row 25 passage...")
    pos = get_pos()
    print(f"Starting position: {pos}")
    
    # We are at (21, 24). Let's walk to (18, 24).
    # Since we know the horizontal path is clear, we can just walk Left.
    for i in range(3):
        print(f"Walking Left from {get_pos()}")
        bridge.press_buttons(["Left", "sleep 500"])
        
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
    print(f"Arrived at: {pos}")
    
    # Now try to step Down
    print("Attempting to walk Down from (18, 24)...")
    bridge.press_buttons(["Down", "sleep 500"])
    
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
        
    print(f"Position after Down attempt: {pos}")
    
    if pos is not None and pos[1] == 25:
        print("SUCCESS! (18, 25) is WALKABLE!")
    else:
        print("FAILED! (18, 25) is BLOCKED!")

if __name__ == "__main__":
    main()
