import mgba
import time

def clear_dialog():
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 200"])

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

# 1. Walk right from (17, 23) to transition to Center
# We are currently at (17, 23)
print("Moving right to transition...")
for i in range(13):
    mgba.press_buttons(["Right", "sleep 300"])
    
cx, cy = get_pos()
print(f"Position after walking right: ({cx}, {cy})")

# If we are in a battle, run away
# (Let's check if coordinates didn't change and we got stuck, meaning battle or dialog)
# Actually, the python script can check and run if needed.
