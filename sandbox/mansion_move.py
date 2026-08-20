import mgba
import time
import os

# Cleanup obsolete files as requested by overwatch
obsolete_files = ['check_party_robust.py', 'walk_down_column_25.py', 'use_dig.py']
for f in obsolete_files:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted obsolete file: {f}")
        except Exception as e:
            print(f"Failed to delete {f}: {e}")

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    # Gen 1 escape sequence
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Navigating to 3F stairs at (18, 2) on 2F in State B...")
# Target: (18, 2)
# We start at (2, 12).
# Path:
# 1. Down to (2, 13)
# 2. Right to (12, 13)
# 3. Up to (12, 5)
# 4. Right to (18, 5)
# 5. Up to (18, 2) and warp!

buttons_pressed = 0
while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Check if we warped to 3F (or if we are at (18, 2) or on 3F map)
    # On 3F, our position might be near (18, 2) or on 3F map layout.
    # To be safe, if we reach y <= 2 on column 18, we warp.
    if pos['x'] == 18 and pos['y'] <= 2:
        print("At stairs warp! Stepping Up...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        print("Final Position on 3F:", mgba.get_coordinates())
        break
        
    btn = None
    if pos['x'] == 2 and pos['y'] < 13:
        btn = 'Down'
    elif pos['y'] == 13 and pos['x'] < 12:
        btn = 'Right'
    elif pos['x'] == 12 and pos['y'] > 5:
        btn = 'Up'
    elif pos['y'] == 5 and pos['x'] < 18:
        btn = 'Right'
    elif pos['x'] == 18 and pos['y'] > 2:
        btn = 'Up'
    else:
        # Recovery/fallback pathing
        if pos['y'] > 13:
            btn = 'Up'
        elif pos['x'] < 2:
            btn = 'Right'
        elif pos['x'] > 18:
            btn = 'Left'
        else:
            # We are between columns 2 and 18, and rows 5 and 13
            if pos['x'] < 12:
                if pos['y'] < 13:
                    btn = 'Down'
                else:
                    btn = 'Right'
            else:
                if pos['y'] > 5:
                    btn = 'Up'
                else:
                    btn = 'Right'

    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        run_from_battle()
        buttons_pressed += 6
        time.sleep(0.5)
        
    if buttons_pressed >= 80:
        print("Button budget limit approached.")
        break

mgba.take_screenshot()
print("Script completed. Current Position:", mgba.get_coordinates())
