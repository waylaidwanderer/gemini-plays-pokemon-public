import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Current position:", get_pos())

# 1. Try to step Down to (1, 11)
old_pos = get_pos()
mgba.press_buttons(["Down"])
time.sleep(0.55)
pos = get_pos()
print("Position after Down:", pos)

if pos == (1, 11):
    # Try to step Down to (1, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.55)
    pos = get_pos()
    print("Position after second Down:", pos)
    
    if pos == (1, 12):
        # Try to step Right to (2, 12)
        mgba.press_buttons(["Right"])
        time.sleep(0.55)
        pos = get_pos()
        print("Position after Right to (2, 12):", pos)
        
        # If successfully reached (2, 12), step back Left
        if pos == (2, 12):
            print("Gate at (2, 12) is OPEN!")
            mgba.press_buttons(["Left"])
            time.sleep(0.55)
        else:
            print("Gate at (2, 12) is CLOSED!")
        
        # Step back Up
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
    else:
        # Step back Up
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
