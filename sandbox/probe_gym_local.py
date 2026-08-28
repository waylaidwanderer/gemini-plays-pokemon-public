import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting local probe from (4, 13)...")

# 1. Test Right to (5, 13)
mgba.press_buttons(["Right"])
time.sleep(0.55)
pos = get_pos()
print("Tried Right. Landed at:", pos)

if pos == (5, 13):
    # Step back Left to (4, 13)
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    
# 2. Test Up to (4, 12)
pos = get_pos()
if pos == (4, 13):
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    pos = get_pos()
    print("Tried Up. Landed at:", pos)
    
    if pos == (4, 12):
        # Step back Down to (4, 13)
        mgba.press_buttons(["Down"])
        time.sleep(0.55)

# 3. Test Down to (4, 14)
pos = get_pos()
if pos == (4, 13):
    mgba.press_buttons(["Down"])
    time.sleep(0.55)
    pos = get_pos()
    print("Tried Down. Landed at:", pos)
    
    if pos == (4, 14):
        # Step back Up to (4, 13)
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
