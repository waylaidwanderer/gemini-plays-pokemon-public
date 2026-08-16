import mgba
import time

def press_and_wait(btn, delay=0.8):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(delay)

print("--- PAYING AND ENTERING SAFARI ZONE PERFECT ---")

# We are currently in the dialogue. Let's press A multiple times with delay to clear all pages of dialogue.
# We will press A 12 times to be absolutely sure we clear all possible pages, select YES, and return to the overworld.
for i in range(12):
    press_and_wait("A", 1.2)

print("Dialogue should be fully complete. Now walking UP to warp into Safari Zone Center!")

# Walk UP 4 steps to be absolutely sure we trigger the warp
for i in range(4):
    mgba.press_buttons(["Up"])
    time.sleep(0.5)

time.sleep(1.5) # Wait for map transition

pos = mgba.get_coordinates()
print("Position after warp attempt:", pos)
mgba.take_screenshot()
