import mgba
import time

def get_pos():
    return mgba.get_coordinates()

print("Initial Position:", get_pos())

# Let's try walking around on Row 10 to find the warp!
# We are currently at (7, 10). Let's step Left to (6, 10) and then (5, 10).
print("Stepping Left to (6, 10)...")
mgba.press_buttons(["Left", "sleep 500"])
print("Position:", get_pos())

print("Stepping Left to (5, 10)...")
mgba.press_buttons(["Left", "sleep 500"])
print("Position:", get_pos())

# If we are at (5, 10) and it has stairs, let's try going Up or Left to see if it warps us!
print("Trying Up from (5, 10)...")
mgba.press_buttons(["Up", "sleep 1200"])
print("Position after Up:", get_pos())

print("Trying Left from (5, 10)...")
mgba.press_buttons(["Left", "sleep 1200"])
print("Position after Left:", get_pos())
