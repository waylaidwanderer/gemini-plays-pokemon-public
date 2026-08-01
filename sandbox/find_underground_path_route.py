import mgba
import time

print("Starting Master Underground Path Route Finder Script...")

# Step 1: Open Start menu and use Teleport
pos = mgba.get_coordinates()
print(f"Current Position before Teleport: {pos}")

mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300", "Down", "A", "sleep 300", "A", "sleep 1500"])

pos = mgba.get_coordinates()
print(f"Position after Teleport: {pos}")

# Step 2: Exit Pokemon Center and walk to Route 8 Upper Highway
# Lavender Town PC is at (11, 20) or inside at (3, 8)
if pos['x'] == 3 and pos['y'] == 8:
    # Inside PC
    mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "sleep 1000"])
    pos = mgba.get_coordinates()
    print(f"Position after exiting PC: {pos}")

if pos['x'] == 11 and pos['y'] == 20:
    # Outside PC in Lavender Town
    print("Outside PC at (11, 20). Walking to Route 8 entrance (0, 9)...")
    # Path: Right 3 to (14, 20) -> Up 8 to (14, 12) -> Left 1 to (13, 12) -> Up 3 to (13, 9) -> Left 13 to (0, 9)
    seq = ["Right", "Right", "Right", 
           "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", 
           "Left", 
           "Up", "Up", "Up", 
           "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "sleep 1000"]
    mgba.press_buttons(seq)
    pos = mgba.get_coordinates()
    print(f"Position after entering Route 8: {pos}")

# Step 3: Now on Route 8 Upper Highway at (59, 8) or (59, 9)
print(f"Current Route 8 position: {pos}")

# Let's test walking West on Row 8/9
west_seq = []
for i in range(15):
    west_seq.append("Left")

mgba.press_buttons(west_seq)
pos = mgba.get_coordinates()
print(f"Position after walking 15 Left: {pos}")

screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
