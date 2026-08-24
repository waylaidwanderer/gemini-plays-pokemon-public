import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Starting at (6, 12) on 1F West
print("Starting on 1F West:", get_pos())

# Walk UP 2 steps to (6, 10)
pos = mgba.get_coordinates()
if pos['y'] == 12:
    mgba.press_buttons(["Up", "sleep 200"])
    pos = mgba.get_coordinates()
    print("Position after 1st Up:", pos)

if pos['y'] == 11:
    mgba.press_buttons(["Up", "sleep 200"])
    pos = mgba.get_coordinates()
    print("Position after 2nd Up:", pos)

# Now at (6, 10). Let's step Left to warp UP to 2F West!
if pos['x'] == 6 and pos['y'] == 10:
    print("Stepping Left onto stairs at (5, 10)...")
    mgba.press_buttons(["Left", "sleep 600"])
    time.sleep(1.5)
    
print("New position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
