import mgba
import time
import os

# Update the notepad directly on disk to document our discoveries before context summarization
notepad_path = "notepads/Scratchpad/Switch_Matrix.md"
if os.path.exists(notepad_path):
    try:
        with open(notepad_path, 'r') as f:
            content = f.read()
            
        old_str = "## Verified 3F Layout Constraints\n- **Northeast Columns:** On 3F, columns 18 and 19 on row 8 are blocked by solid columns/machines (empirically verified on Turn 48596)."
        new_str = "## Verified 3F Layout Constraints\n- **Northeast Columns:** On 3F, columns 18 and 19 on row 8 are blocked by solid columns/machines (empirically verified on Turn 48596).\n- **Row 7 Open Corridor:** On 3F, row 7 is completely open horizontally across columns 5 to 22 in both State A and State B, allowing free horizontal traversal across the entire map."
        
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(notepad_path, 'w') as f:
                f.write(content)
            print("Successfully updated notepad on disk!")
        else:
            print("Old string not found in notepad. Checking if already updated...")
    except Exception as e:
        print(f"Error updating notepad: {e}")

def walk_to_2f_from_3f():
    print("Walking from (22, 7) on 3F back to the 2F stairs at (7, 10)...")
    # Current position: (22, 7) on 3F.
    
    # 1. Walk Left to column 7 (15 steps Left)
    for i in range(15):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Left {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle or battle going Left!")
            break
            
    # 2. Walk Down to (7, 10) (3 steps Down)
    pos = mgba.get_coordinates()
    if pos['x'] == 7:
        for i in range(3):
            pos = mgba.get_coordinates()
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Down {i+1}: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Hit obstacle going Down!")
                break
                
    # 3. Step onto stairs warp to go to 2F
    pos = mgba.get_coordinates()
    if pos['x'] == 7 and pos['y'] == 10:
        print("At stairs warp! Stepping Down to trigger warp...")
        mgba.press_buttons(["Down"])
        time.sleep(1.2)
        print("Warp complete! New Position:", mgba.get_coordinates())
        
    mgba.take_screenshot()

walk_to_2f_from_3f()
