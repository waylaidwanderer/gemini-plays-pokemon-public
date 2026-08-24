
import mgba

def get_pos():
    return mgba.get_coordinates()

# Current position is (6, 11) facing Left in dialogue
print("Dismissing dialogue...")
mgba.press_buttons(["B", "sleep 500"])

# Walk UP to Row 9
print("Walking UP to Row 9...")
mgba.press_buttons(["Up", "sleep 450", "Up", "sleep 450"])
print("Position:", get_pos())

# Walk LEFT to Column 3
print("Walking LEFT to Column 3...")
mgba.press_buttons(["Left", "sleep 450", "Left", "sleep 450", "Left", "sleep 450"])
print("Position:", get_pos())

# Walk DOWN to Row 11
print("Walking DOWN to Row 11...")
mgba.press_buttons(["Down", "sleep 450", "Down", "sleep 450"])
print("Position:", get_pos())

# Face LEFT and toggle switch
print("Toggling Mewtwo switch at (2, 11)...")
mgba.press_buttons(["Left", "sleep 300"])
mgba.press_buttons(["A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "B", "sleep 400"])

# Verify position
print("Final Position:", get_pos())
mgba.take_screenshot()
