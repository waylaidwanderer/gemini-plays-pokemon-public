import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_dialog():
    print("Dialogue box open, progressing text...")
    for _ in range(5):
        bridge.press_buttons(["A", "sleep 500"])
    # If yes/no prompt appears, press A to select YES (which is the default)
    bridge.press_buttons(["A", "sleep 1200"])
    for _ in range(5):
        bridge.press_buttons(["A", "sleep 500"])

def main():
    print("Entering Gatehouse and buying Safari Zone ticket...")
    # Stand at Fuchsia City (18, 4) facing UP.
    # Walk UP 1 step to enter Gatehouse
    bridge.press_buttons(["Up", "sleep 1000"])
    time.sleep(1.0)
    
    pos = get_pos()
    print(f"Position inside Gatehouse: {pos}")
    
    # We should stand at (3, 5) or (4, 5)
    # Walk UP to stand in front of the clerk (typically at Row 2 or 3)
    bridge.press_buttons(["Up", "sleep 450"])
    bridge.press_buttons(["Up", "sleep 450"])
    bridge.press_buttons(["Up", "sleep 450"])
    
    # Face UP towards clerk
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Interact with clerk
    print("Talking to clerk...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Progress dialogue and buy ticket
    handle_textbox_or_dialog()
    
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
