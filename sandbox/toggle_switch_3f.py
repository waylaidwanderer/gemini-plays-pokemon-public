import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Dynamic bypass to northwest switch on 3F...")

stuck_cycles = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # If we reached our destination (2, 12), break and interact!
    if pos['x'] == 2 and pos['y'] == 12:
        print("Reached (2, 12)!")
        break
        
    # If we are stuck at same position for too many cycles, NPC might be blocking us permanently.
    # Let's wait a bit or try to turn to let her move.
    
    # Decide next step based on position
    btn = None
    if pos['x'] == 6 and pos['y'] == 11:
        btn = 'Left' # Try to step onto (5, 11)
    elif pos['x'] == 5 and pos['y'] == 11:
        btn = 'Down' # Step to (5, 12)
    elif pos['y'] == 12:
        if pos['x'] > 2:
            btn = 'Left' # Walk left along row 12
        else:
            print("Already at column 2 row 12.")
            break
    else:
        # Fallback if we get pushed off our path
        print("Pushed off path, trying to return...")
        if pos['x'] < 6:
            btn = 'Right'
        else:
            btn = 'Left'

    if not btn:
        break
        
    print(f"Decided button: {btn}")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Position did not change, might be NPC block or battle
        print("Blocked. Checking for battle or waiting for NPC...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # We are still at same position.
            # Let's press B to check if we are in a battle menu
            print("Still blocked. Testing if battle...")
            mgba.press_buttons(["B"])
            time.sleep(0.2)
            pos_battle_check = mgba.get_coordinates()
            if pos_battle_check == new_pos:
                # Still blocked, probably NPC. Let's wait!
                print("NPC is blocking. Waiting 1 turn...")
                time.sleep(1.0)
                # Press B to turn in place or wait
                mgba.press_buttons(["B"])
                time.sleep(0.3)
            else:
                # Position changed, battle or menu closed
                print("Position changed after B press.")
        else:
            print("Position changed after delay.")

# Now we should be at (2, 12). Face UP and interact
print("Facing UP and interacting with Mewtwo statue at (2, 11) on 3F...")
mgba.press_buttons(["Up", "sleep 200", "A", "sleep 1000"])

print("Confirming 'Yes' and clearing text...")
mgba.press_buttons(["A", "sleep 1000", "A", "sleep 500"])

# Verify final position
print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
