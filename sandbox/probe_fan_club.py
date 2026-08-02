import mgba
import time

print("Starting Fan Club NPC Probe...")

# Current position: (3, 5) facing Up
pos = mgba.get_coordinates()
print(f"Start position: {pos}")

# 1. Test A press at (3, 5)
mgba.press_buttons(["A", "sleep 300"])
s1 = mgba.take_screenshot()
print(f"Screen at (3,5) after A: {s1}")

# 2. Walk to Guy NPC at (6, 3)
# From (3, 5): Right 4 to (7, 5), Up 2 to (7, 3), Left 1 facing (6, 3)
mgba.press_buttons(["Right", "Right", "Right", "Right", "Up", "Up", "Left", "sleep 300"])
p_guy = mgba.get_coordinates()
print(f"Position facing Guy NPC: {p_guy}")
mgba.press_buttons(["A", "sleep 500"])
s_guy = mgba.take_screenshot()
print(f"Guy NPC screen: {s_guy}")

# Dismiss text
mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])

# 3. Walk to Green-Bearded NPC at (5, 1)
# From (6, 3): Right 1 to (7, 3), Up 2 to (7, 1), Left 1 to (6, 1) facing (5, 1)
mgba.press_buttons(["Right", "Up", "Up", "Left", "sleep 300"])
p_gb = mgba.get_coordinates()
print(f"Position facing Green-Bearded NPC: {p_gb}")
mgba.press_buttons(["A", "sleep 500"])
s_gb = mgba.take_screenshot()
print(f"Green-bearded screen: {s_gb}")

# Dismiss text
mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])

# 4. Walk to Girl NPC at (1, 3)
# From (6, 1): Right 1 to (7, 1), Down 4 to (7, 5), Left 6 to (1, 5), Up 1 facing (1, 4)/(1, 3)
mgba.press_buttons(["Right", "Down", "Down", "Down", "Down", "Left", "Left", "Left", "Left", "Left", "Left", "Up", "sleep 300"])
p_girl = mgba.get_coordinates()
print(f"Position facing Girl NPC: {p_girl}")
mgba.press_buttons(["A", "sleep 500"])
s_girl = mgba.take_screenshot()
print(f"Girl NPC screen: {s_girl}")

print("Probe complete!")
