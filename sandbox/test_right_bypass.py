import mgba
import time

# We are currently at (4, 5)
# Walk Right to (10, 5)
# Walk Up to (10, 2)
# Walk Right to (22, 2)

path = [
    ('Right', 5, 5), ('Right', 6, 5), ('Right', 7, 5), ('Right', 8, 5),
    ('Right', 9, 5), ('Right', 10, 5),
    ('Up', 10, 4), ('Up', 10, 3), ('Up', 10, 2),
    ('Right', 11, 2), ('Right', 12, 2), ('Right', 13, 2), ('Right', 14, 2),
    ('Right', 15, 2), ('Right', 16, 2), ('Right', 17, 2), ('Right', 18, 2),
    ('Right', 19, 2), ('Right', 20, 2), ('Right', 21, 2), ('Right', 22, 2)
]

print("Walking to (22, 2)...")
for btn, tx, ty in path:
    mgba.press_buttons([btn])
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {btn}, now at: {pos}")
