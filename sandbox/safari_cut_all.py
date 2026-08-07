import mgba
import time

def try_cut_slot(slot_idx):
    print(f"Trying to use CUT with Pokémon in Slot {slot_idx}...")
    
    # 1. Open Start menu
    mgba.press_buttons(["Start", "sleep 500"])
    
    # 2. Go to POKÉMON and select
    mgba.press_buttons(["Down", "sleep 300", "A", "sleep 800"])
    
    # 3. Move to target slot (slot_idx is 1-based, cursor starts at slot 1)
    moves = ["Down"] * (slot_idx - 1)
    for m in moves:
        mgba.press_buttons([m, "sleep 200"])
        
    # Select the Pokémon
    mgba.press_buttons(["A", "sleep 500"])
    
    # 4. Select the first option (CUT or STATS)
    mgba.press_buttons(["A", "sleep 2000"])
    
    # 5. Dismiss any screens/text and exit menus completely
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400", "B", "sleep 400", "B", "sleep 400"])
    time.sleep(0.5)

if __name__ == "__main__":
    # We are at (15, 22) facing Left.
    # To face Down (towards the bush at 15, 23), let's tap Down once
    mgba.press_buttons(["Down", "sleep 300"])
    
    # Try all 5 slots
    for i in range(1, 6):
        try_cut_slot(i)
