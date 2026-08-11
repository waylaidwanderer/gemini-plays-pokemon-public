import bridge
import time

print("Running go_to_center.py...")

# Path from Safari Zone Gatehouse (18, 4) to Fuchsia City Pokemon Center (19, 27):
# 1. Right 4 to (22, 4)
# 2. Down 10 to (22, 14)
# 3. Right 4 to (26, 14)
# 4. Down 7 to (26, 21)
# 5. Left 2 to (24, 21)
# 6. Down 7 to (24, 28)
# 7. Left 5 to (19, 28)
# 8. Up 1 to (19, 27) (enters Pokemon Center)

path = (
    ["Right"] * 4 +
    ["Down"] * 10 +
    ["Right"] * 4 +
    ["Down"] * 7 +
    ["Left"] * 2 +
    ["Down"] * 7 +
    ["Left"] * 5 +
    ["Up"] * 1
)

print(f"Sending path of {len(path)} buttons...")
res = bridge.press_buttons(path)
print("Response:", res)
