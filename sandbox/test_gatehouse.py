import bridge
import time

curr = bridge.get_coordinates()
print(f"Current position: {curr}")

# Try to move Left
print("Trying to move Left...")
bridge.press_buttons(["Left", "sleep 350"])
curr = bridge.get_coordinates()
print(f"Now at: {curr}")

# Try to move Up from (4, 5) or current
print("Trying to move Up...")
bridge.press_buttons(["Up", "sleep 350"])
curr = bridge.get_coordinates()
print(f"Now at: {curr}")

# Try to move Left from current
print("Trying to move Left...")
bridge.press_buttons(["Left", "sleep 350"])
curr = bridge.get_coordinates()
print(f"Now at: {curr}")

# Try to move Up
print("Trying to move Up...")
bridge.press_buttons(["Up", "sleep 350"])
curr = bridge.get_coordinates()
print(f"Now at: {curr}")

# Let's see what is walkable and try to talk to the clerk!
print("Test complete.")
