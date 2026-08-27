import mgba
import time

# We are at (15, 7).
# Walk left to (12, 7) and step down to (12, 8).

def get_current_pos():
    return mgba.get_coordinates()

pos = get_current_pos()
print("Starting pos:", pos)

# Walk left 3 steps to (12, 7)
steps = [
    "Left", "Left", "Left"
]
for d in steps:
    mgba.press_buttons([d])
    time.sleep(0.4)
    
pos = get_current_pos()
print("Pos after moving left:", pos)

if pos == {"x": 12, "y": 7}:
    print("At (12, 7). Trying to walk DOWN to (12, 8)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    pos = get_current_pos()
    print("Pos after walking down:", pos)
