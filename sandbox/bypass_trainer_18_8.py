import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.18)

# Log Dan's defeat and reward in Progression_And_Party_Stats.md
path_stats = "notepads/Progression_And_Party_Stats.md"
with open(path_stats, 'r', encoding='utf-8') as f:
    stats_content = f.read()

dan_milestone = "- **Defeated Youngster Dan:** Defeated Youngster Dan at (18, 5) on Turn 4675, earning ¥255.\n"
if "Defeated Youngster Dan" not in stats_content:
    lines = stats_content.splitlines(keepends=True)
    # Insert it near other Route 25/24 defeated trainers
    insert_idx = -1
    for i, line in enumerate(lines):
        if "Defeated Rocket Grunt" in line and "Route 24" in line:
            insert_idx = i + 1
    if insert_idx != -1:
        lines.insert(insert_idx, dan_milestone)
    else:
        lines.append(dan_milestone)
    
    with open(path_stats, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Logged Youngster Dan's defeat in Progression_And_Party_Stats.md!")

# Update Route25.md to show Dan is defeated and has reward ¥255
path_r25 = "notepads/Locations/Route25.md"
with open(path_r25, 'r', encoding='utf-8') as f:
    r25_content = f.read()

r25_content_updated = r25_content.replace("- **Status:** Engaged on Turn 4673.", "- **Status:** Defeated on Turn 4675.")
r25_content_updated = r25_content_updated.replace("- **Reward:** ¥??", "- **Reward:** ¥255")

with open(path_r25, 'w', encoding='utf-8') as f:
    f.write(r25_content_updated)
print("Updated Route25.md!")

# Execute precise bypass movement:
# Starting at (18, 4)
print("Moving Left to (17, 4)...")
move("Left", 1)

print("Moving Down 5 steps to (17, 9)...")
move("Down", 5)

print("Moving Right 6 steps to (23, 9)...")
move("Right", 6)

time.sleep(0.5)
screenshot = mgba.take_screenshot()
print(f"Bypass movement completed. Screenshot: {screenshot}")
