import mgba
import time

print("--- EXECUTING SAFARI ENTRY DIALOGUE ---")

def get_pos():
    return mgba.get_coordinates()

# We are at (4, 2) with the text "Welcome to the SAFARI ZONE!" open.
# We will press A 9 times to advance and select YES.

for i in range(12):
    print(f"Press {i+1} of A...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    pos = get_pos()
    print(f"Position: {pos}")
    if pos and pos['x'] != 4:
        print("Successfully warped out of the Gatehouse!")
        break

time.sleep(1.5)
mgba.take_screenshot()
print("Final Position:", get_pos())
