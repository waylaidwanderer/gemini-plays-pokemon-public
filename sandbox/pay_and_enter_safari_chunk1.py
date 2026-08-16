import mgba
import time

def press_and_wait(btn, delay=0.8):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(delay)

print("--- PAYING AND ENTERING SAFARI ZONE ---")

# Step 1: Press A to speak to the clerk across the counter
press_and_wait("A", 1.5) # "Would you like to join the hunt?"

# Step 2: Clear first line of text
press_and_wait("A", 1.5) # Prompts Yes/No (Yes is default)

# Step 3: Select YES (Press A)
press_and_wait("A", 1.5) # "That'll be 500. We only use special Pokeballs."

# Step 4: Clear price text
press_and_wait("A", 1.5) # "ACE received 30 SAFARI BALLS!"

# Step 5: Clear received item text
press_and_wait("A", 1.5) # "We'll call you when you run out of time..."

# Step 6: Clear time warning text
press_and_wait("A", 1.5) # "Good luck!"

# Step 7: Clear final text and return to overworld
press_and_wait("A", 1.5)

print("Dialogue complete. Now walking into the warp door to enter the Safari Zone!")

# Step 8: Walk UP to (3, 1) to trigger the warp
mgba.press_buttons(["Up"])
time.sleep(0.5)
mgba.press_buttons(["Up"])
time.sleep(0.5)
mgba.press_buttons(["Up"])
time.sleep(1.5) # Wait for map transition

pos = mgba.get_coordinates()
print("Position after warp:", pos)
mgba.take_screenshot()
