import mgba
import time

def get_pos():
    return mgba.get_coordinates()

print("Testing switch hypothesis...")
print("Initial pos:", get_pos())

# Step Down to (1, 11)
mgba.press_buttons(["Down", "sleep 250"])
print("After Down:", get_pos())

# Try stepping Right to (2, 11) (the switch tile)
mgba.press_buttons(["Right", "sleep 250"])
print("After Right (Mewtwo statue):", get_pos())

sc = mgba.take_screenshot()
print("Screenshot:", sc)
