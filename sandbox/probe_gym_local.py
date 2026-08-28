import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting local probe from (4, 13)...")

# 1. Walk to (4, 12)
mgba.press_buttons(["Up"])
time.sleep(0.55)
pos = get_pos()
if pos == (4, 12):
    print("At (4, 12), testing Up to (4, 11)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    pos2 = get_pos()
    print("Tried Up from (4, 12). Landed at:", pos2)
    if pos2 == (4, 11):
        mgba.press_buttons(["Down"])
        time.sleep(0.55)
    elif pos2 != (4, 12):
        # We got spun!
        # Walk back to (4, 12) if possible, or just let us know
        print(f"Spun from (4, 12) Up to {pos2}")
        exit(0)
        
    # Walk back Down to (4, 13)
    mgba.press_buttons(["Down"])
    time.sleep(0.55)

# 2. Walk to (5, 13)
pos = get_pos()
if pos == (4, 13):
    mgba.press_buttons(["Right"])
    time.sleep(0.55)
    pos = get_pos()
    if pos == (5, 13):
        print("At (5, 13), testing Right to (6, 13)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.55)
        pos2 = get_pos()
        print("Tried Right from (5, 13). Landed at:", pos2)
        if pos2 == (6, 13):
            mgba.press_buttons(["Left"])
            time.sleep(0.55)
        elif pos2 != (5, 13):
            print(f"Spun from (5, 13) Right to {pos2}")
            exit(0)
            
        print("At (5, 13), testing Up to (5, 12)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        pos3 = get_pos()
        print("Tried Up from (5, 13). Landed at:", pos3)
        if pos3 == (5, 12):
            mgba.press_buttons(["Down"])
            time.sleep(0.55)
        elif pos3 != (5, 13):
            print(f"Spun from (5, 13) Up to {pos3}")
            exit(0)
            
        # Walk back Left to (4, 13)
        mgba.press_buttons(["Left"])
        time.sleep(0.55)

print("Final position:", get_pos())
