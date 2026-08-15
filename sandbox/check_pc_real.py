import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    # If in text box, clear it
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 200"])
    return get_pos()

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
    bridge.press_buttons([direction, "sleep 450"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    return new_pos

def main():
    print("Starting automatic Safari step exhaustion...")
    
    # Loop walking back and forth between (19, 24) and (21, 24)
    # until warped to Gatehouse at (4, 3)
    step_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            
        # Check if we are inside the Gatehouse
        # Gatehouse coordinates: x=4, y=3
        if pos is not None and pos[0] < 10 and pos[1] < 10:
            print(f"Successfully arrived in Safari Gatehouse! Position: {pos}")
            break
            
        # Walk back and forth on Row 24
        # Walk Left to (19, 24)
        while pos is not None and pos[0] > 19:
            pos = walk_step_robust("Left")
            if pos is None:
                pos = handle_textbox_or_battle()
                
        # Walk Right to (21, 24)
        while pos is not None and pos[0] < 21:
            pos = walk_step_robust("Right")
            if pos is None:
                pos = handle_textbox_or_battle()
                
        step_count += 1
        if step_count % 10 == 0:
            print(f"Exhausted {step_count * 2} steps...")
            
    # We are in the Gatehouse! Let's exit to Fuchsia City
    pos = get_pos()
    print(f"Current Position inside Gatehouse: {pos}")
    
    # Walk DOWN to exit mat at (4, 7) or (4, 5)
    # Inside the Gatehouse, we warp at (4, 3).
    # To exit, walk DOWN to (4, 7) or (3, 7) or (4, 5).
    # Let's walk Down 4 steps:
    print("Exiting Gatehouse to Fuchsia City...")
    for _ in range(5):
        bridge.press_buttons(["Down", "sleep 500"])
        
    # Wait for map transition to Fuchsia City
    time.sleep(2.0)
    pos = get_pos()
    print(f"Position outside in Fuchsia City: {pos}")
    
    # We should be at (18, 4) in Fuchsia City.
    # Walk to the Pokémon Center door at (19, 27) and enter it.
    if pos == (18, 4):
        print("Navigating to Pokémon Center...")
        # Walk DOWN to (18, 8)
        for _ in range(4):
            bridge.press_buttons(["Down", "sleep 500"])
        # Walk RIGHT to Column 19 on Row 8
        bridge.press_buttons(["Right", "sleep 500"])
        # Walk DOWN to Row 27
        for _ in range(19):
            bridge.press_buttons(["Down", "sleep 450"])
        # We should be standing directly below Pokémon Center at (19, 27). Enter it.
        bridge.press_buttons(["Up", "sleep 1500"])
        
    pos = get_pos()
    print(f"Inside Pokémon Center: {pos}")
    
    # Walk to PC at (13, 4)
    # Inside Pokemon Center, we start at (3, 7) or (4, 7) on the doormat.
    if pos is not None and pos[1] >= 6:
        print("Navigating to PC...")
        # Walk up to Row 5
        bridge.press_buttons(["Up", "sleep 400", "Up", "sleep 400", "Up", "sleep 400"]) # to (3, 5) or (4, 5)
        # Walk to Column 13
        for _ in range(9):
            bridge.press_buttons(["Right", "sleep 400"])
        # Walk UP to stand in front of PC at (13, 4)
        bridge.press_buttons(["Up", "sleep 400"])
        # Face UP
        bridge.press_buttons(["Up", "sleep 500"])
        
    pos = get_pos()
    print(f"Standing in front of PC: {pos}")
    
    # 4. Turn on PC and open Withdraw menu
    print("Opening ACE's PC Withdraw menu...")
    bridge.press_buttons(["A", "sleep 1200"]) # Turn on PC
    bridge.press_buttons(["A", "sleep 1200"]) # Progress boot text "ACE turned on the PC!"
    bridge.press_buttons(["A", "sleep 1200"]) # Progress "Access whose PC?"
    bridge.press_buttons(["A", "sleep 1500"]) # Select ACE's PC
    bridge.press_buttons(["A", "sleep 1500"]) # Select WITHDRAW ITEM
    
    # Take screenshot of page 1 of PC Withdraw
    p1 = mgba.take_screenshot()
    print(f"PC Withdraw Page 1: {p1}")
    
    # Scroll down 10 times to see every single item in the PC, taking screenshots
    for i in range(5):
        bridge.press_buttons(["Down", "sleep 400"])
        p = mgba.take_screenshot()
        print(f"PC Scroll {i+1}: {p}")
        
    # Close PC menu safely by pressing B multiple times
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 400"])
        
    pos = get_pos()
    print(f"Final overworld position: {pos}")

if __name__ == "__main__":
    main()
