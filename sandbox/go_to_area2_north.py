import mgba
import time

print("--- DIAGNOSING CURRENT LOCATION ---")

def get_pos():
    return mgba.get_coordinates()

start_pos = get_pos()
print("Starting Position:", start_pos)

# Try moving Up
mgba.press_buttons(["Up"])
time.sleep(0.4)
up_pos = get_pos()
print("After Up:", up_pos)
if up_pos != start_pos:
    # Go back Down
    mgba.press_buttons(["Down"])
    time.sleep(0.4)

# Try moving Left
mgba.press_buttons(["Left"])
time.sleep(0.4)
left_pos = get_pos()
print("After Left:", left_pos)
if left_pos != start_pos:
    # Go back Right
    mgba.press_buttons(["Right"])
    time.sleep(0.4)

# Try moving Right
mgba.press_buttons(["Right"])
time.sleep(0.4)
right_pos = get_pos()
print("After Right:", right_pos)
if right_pos != start_pos:
    # Go back Left
    mgba.press_buttons(["Left"])
    time.sleep(0.4)

# Try moving Down
mgba.press_buttons(["Down"])
time.sleep(0.4)
down_pos = get_pos()
print("After Down:", down_pos)
if down_pos != start_pos:
    # Go back Up
    mgba.press_buttons(["Up"])
    time.sleep(0.4)

print("Diagnostic complete!")
