import mgba
import time

pos = mgba.get_coordinates()
print("Starting position for warp test:", pos)

# Walk right from (2, 11) to (7, 11)
steps = []
for x in range(3, 8):
    steps.append(("Right", {"x": x, "y": 11}))

for d, c in steps:
    mgba.press_buttons([d])
    time.sleep(0.45)

pos = mgba.get_coordinates()
print("Position before stairs:", pos)

if pos == {"x": 7, "y": 11}:
    print("Stepping UP onto stairs at (7, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    
    pos = mgba.get_coordinates()
    print("Position after warping UP:", pos)
