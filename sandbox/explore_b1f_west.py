import mgba
import time

print("Starting battle escape sequence...")
# Clear "Wild VULPIX appeared!"
mgba.press_buttons(["B"])
time.sleep(1.5) # Wait for "Go! SHELLBY!" to print

# Clear "Go! SHELLBY!" and wait for battle menu
mgba.press_buttons(["B"])
time.sleep(1.5)

# Move cursor to RUN and select it
mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A"])
time.sleep(1.5) # Wait for escape message "Got away safely!"

# Clear escape message and return to overworld
mgba.press_buttons(["B"])
time.sleep(1.0)

# Verify we are back in overworld
pos_overworld = mgba.get_coordinates()
print("Overworld Position:", pos_overworld)

# Walk Left 3 steps to (14, 6)
print("Resuming movement to the west...")
mgba.press_buttons(["Left", "Left", "Left"])
time.sleep(1.5) # Wait for movement

pos_final = mgba.get_coordinates()
print("Final Position on B1F:", pos_final)
img_path = mgba.take_screenshot()
print("Saved screenshot on B1F:", img_path)
