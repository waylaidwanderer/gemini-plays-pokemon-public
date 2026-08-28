import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting local probe from (9, 11)...")

# 1. Step Right to (10, 11)
mgba.press_buttons(["Right"])
time.sleep(0.55)
pos = get_pos()
print("Tried Right from (9, 11). Landed at:", pos)

if pos == (10, 11):
    # 2. Test Right to (11, 11)
    mgba.press_buttons(["Right"])
    time.sleep(0.55)
    pos2 = get_pos()
    print("Tried Right from (10, 11). Landed at:", pos2)
    if pos2 == (11, 11):
        mgba.press_buttons(["Left"])
        time.sleep(0.55)
    elif pos2 != (10, 11):
        print(f"SPUN from (10, 11) Right to {pos2}")
        exit(0)
        
    # 3. Test Up to (10, 10)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    pos3 = get_pos()
    print("Tried Up from (10, 11). Landed at:", pos3)
    if pos3 == (10, 10):
        # 4. Test Up to (10, 9)
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        pos4 = get_pos()
        print("Tried Up from (10, 10). Landed at:", pos4)
        if pos4 == (10, 9):
            mgba.press_buttons(["Down"])
            time.sleep(0.55)
        elif pos4 != (10, 10):
            print(f"SPUN from (10, 10) Up to {pos4}")
            exit(0)
            
        # 5. Test Right to (11, 10)
        pos_current = get_pos()
        if pos_current == (10, 10):
            mgba.press_buttons(["Right"])
            time.sleep(0.55)
            pos5 = get_pos()
            print("Tried Right from (10, 10). Landed at:", pos5)
            if pos5 == (11, 10):
                mgba.press_buttons(["Left"])
                time.sleep(0.55)
            elif pos5 != (10, 10):
                print(f"SPUN from (10, 10) Right to {pos5}")
                exit(0)
                
        # Walk back Down to (10, 11)
        mgba.press_buttons(["Down"])
        time.sleep(0.55)
        
    # Walk back Left to (9, 11)
    mgba.press_buttons(["Left"])
    time.sleep(0.55)

print("Final position:", get_pos())
