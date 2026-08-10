import bridge
import time

curr = bridge.get_coordinates()
print(f"Current position: {curr}")

# Try to walk LEFT to column 6, then test walking DOWN
route = [
    (12, 10), (11, 10), (10, 10), (9, 10), (8, 10), (7, 10), (6, 10)
]

for target in route[1:]:
    curr = bridge.get_coordinates()
    direction = "Left"
    print(f"Moving Left from {curr} towards {target}")
    bridge.press_buttons([direction, "sleep 350"])
    new_curr = bridge.get_coordinates()
    if new_curr == curr:
        print(f"Blocked at {curr}!")
        break

# Test walking DOWN from column 6
curr = bridge.get_coordinates()
print(f"Now testing walking DOWN from {curr}")
for y in range(curr[1]+1, 15):
    print(f"Trying to move DOWN from {curr} to ({curr[0]}, {y})...")
    bridge.press_buttons(["Down", "sleep 350"])
    new_curr = bridge.get_coordinates()
    print(f"Now at {new_curr}")
    if new_curr == curr:
        print(f"Blocked walking DOWN at {curr}!")
        break
    curr = new_curr

print(f"Test complete. Final position: {bridge.get_coordinates()}")
