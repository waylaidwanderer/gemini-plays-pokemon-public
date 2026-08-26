import mgba
import time
from PIL import Image

pos = mgba.get_coordinates()
print("Current position:", pos)

# Walk to (1, 13)
# We are currently at (1, 11). Walk Down to (1, 13)
steps = [
    ("Down", {"x": 1, "y": 12}),
    ("Down", {"x": 1, "y": 13}),
]
for d, c in steps:
    mgba.press_buttons([d])
    time.sleep(0.45)
    
pos = mgba.get_coordinates()
print("Position before switch check:", pos)

if pos == {"x": 1, "y": 13}:
    # Turn UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Step 1: Press A to open dialogue
    print("Pressing A (1)...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    scr1 = mgba.take_screenshot()
    Image.open(scr1).resize((160, 144), Image.Resampling.NEAREST).save("switch_step_1.png")
    
    # Step 2: Press A to advance to YES/NO
    print("Pressing A (2)...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    scr2 = mgba.take_screenshot()
    Image.open(scr2).resize((160, 144), Image.Resampling.NEAREST).save("switch_step_2.png")
    
    # Step 3: Press A to select YES
    print("Pressing A (3)...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    scr3 = mgba.take_screenshot()
    Image.open(scr3).resize((160, 144), Image.Resampling.NEAREST).save("switch_step_3.png")
    
    # Step 4: Press A to dismiss 'Pressed it!'
    print("Pressing A (4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    scr4 = mgba.take_screenshot()
    Image.open(scr4).resize((160, 144), Image.Resampling.NEAREST).save("switch_step_4.png")
    
    print("Switch verification sequence completed!")
else:
    print("Failed to reach (1, 13)")
