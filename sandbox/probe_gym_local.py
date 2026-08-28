import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting local probe from (4, 13)...")

# 1. Walk to (5, 12) via (5, 13)
mgba.press_buttons(["Right"])
time.sleep(0.55)
pos = get_pos()
if pos == (5, 13):
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    pos = get_pos()
    if pos == (5, 12):
        print("At (5, 12), testing Right to (6, 12) (possible LEFT spinner)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.55)
        pos2 = get_pos()
        print("Tried Right from (5, 12). Landed at:", pos2)
        
        # If we didn't spin, step back Left to (5, 12)
        if pos2 == (6, 12):
            mgba.press_buttons(["Left"])
            time.sleep(0.55)
        elif pos2 != (5, 12):
            # We got spun! The player was pushed by the spinner!
            print(f"SPINNER ENCOUNTERED at (6, 12)! We got spun to {pos2}!")
            exit(0)
            
        # Test UP to (5, 11)
        print("At (5, 12), testing Up to (5, 11)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        pos3 = get_pos()
        print("Tried Up from (5, 12). Landed at:", pos3)
        if pos3 == (5, 11):
            mgba.press_buttons(["Down"])
            time.sleep(0.55)
            
        # Walk back Down to (5, 13)
        mgba.press_buttons(["Down"])
        time.sleep(0.55)
        
    # Walk back Left to (4, 13)
    mgba.press_buttons(["Left"])
    time.sleep(0.55)

print("Final position:", get_pos())
