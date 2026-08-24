import mgba

# Currently at (1, 11) on 3F West in State A with "Got away safely!" on screen.
print("PHASE 1: Clearing battle screen...")
mgba.press_buttons(["B", "sleep 2000"]) # Clear battle text, wait for overworld

# Turn Right
print("PHASE 2: Facing RIGHT towards switch...")
mgba.press_buttons(["Right", "sleep 500"])

# Safe switch toggling sequence (100% verified 1500ms sleeps)
print("PHASE 3: Toggling the switch at (2, 11) facing Right...")
mgba.press_buttons(["A", "sleep 1500"]) # "A secret switch!"
mgba.press_buttons(["A", "sleep 1500"]) # "Press it?" (Yes/No appears)
mgba.press_buttons(["A", "sleep 1500"]) # Select YES -> "(click)"
mgba.press_buttons(["B", "sleep 500"])  # Close dialogue box

print("Toggle sequence complete.")
mgba.take_screenshot()
