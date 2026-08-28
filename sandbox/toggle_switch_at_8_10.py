import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print(f"Starting switch toggle at {get_pos()} facing Up...")

# Step 1: Open dialogue
print("Pressing A to open dialogue...")
mgba.press_buttons(["A"])
time.sleep(0.6)

# Step 2: Advance "A secret switch!"
print("Pressing A to advance first dialogue...")
mgba.press_buttons(["A"])
time.sleep(0.6)

# Step 3: Select YES on "Press it?"
print("Pressing A to select YES...")
mgba.press_buttons(["A"])
time.sleep(0.6)

# Step 4: Advance "Who wouldn't?"
print("Pressing A to complete dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print(f"Dialogue finished. Position now: {get_pos()}")
mgba.take_screenshot()
